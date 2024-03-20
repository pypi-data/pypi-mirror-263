# -*- encoding: utf-8 -*-

'''
Author     :Phailin
Datetime   :2024-03-18 10:25:51
E-Mail     :phailin791@hotmail.com
'''

import json
import time
import uuid
import requests
from loguru import logger
from datetime import datetime
from typing import Dict, List, Text


from httprunner_lite.client import HttpSession
from httprunner_lite.response import Response
from httprunner_lite.utils.parse import Parser,build_url
from httprunner_lite.utils.uploader import prepare_upload_step
from httprunner_lite.utils.helpers import merge_variables, pretty_format
from httprunner_lite.utils.exceptions import ParamsError, ValidationFailure
from httprunner_lite.model import (ProjectMeta, TestConfig, VariablesMapping,
    Hooks, TestStep, TestCase, TestCaseTime, StepResult, 
    TestCaseInOut, TestCaseSummary)

class HttpRunner:

    teststeps: List # list of step

    parser: Parser = None
    session: HttpSession = None
    case_id: Text = ""
    worker_id: Text = "worker_master"

    __config: TestConfig
    __export: List[Text] = []
    __step_results: List[StepResult] = []
    __session_variables: VariablesMapping = {}
    
    # time
    __start_at: float = 0
    __duration: float = 0

    def run(self, testcase: TestCase, project_meta : ProjectMeta = None):
        logger.info(f"project_meta: {project_meta}")
        self.__project_meta =  project_meta
        self._init_env(testcase, project_meta.functions)
        
        logger.info(
            f"Start to run testcase: {self.__config.name}, TestCase ID: {self.case_id}"
        )

        ### start time
        self.__start_at = time.time()
        try:
            # run step in sequential order
            for teststep in testcase.teststeps:
                self._run_teststep(teststep)
        except Exception as e:
            logger.error(e)
        finally:
            logger.info(f"generate testcase log: {self.__step_results}")
        return self.__step_results

    def _init_env(self, testcase: TestCase, function_mapping) -> None:
        self.__config = testcase.config
        self.__session_variables = self.__session_variables or {}
        self.__start_at = 0
        self.__duration = 0
        self.__project_meta = self.__project_meta or ProjectMeta(id=1)
        self.case_id = self.case_id or str(uuid.uuid4())
        self.worker_id = self.worker_id or "worker on pc"
        self.__step_results = self.__step_results or []
        self.session = self.session or HttpSession()
        self.parser = self.parser or Parser(function_mapping)
    
    def get_export_variabels(self)->Dict:
        # override testcase export vars with step export
        export_var_names = self.__export or self.__config.export
        export_var_mapping = {}
        for var_name in export_var_names:
            if var_name not in self.__session_variables:
                raise ParamsError(
                    f"failed to export variable {var_name} from session variables {self.__session_variables}"
                )
            
            export_var_mapping[var_name] = self.__session_variables[var_name]

        return export_var_mapping
    
    def get_summary(self) -> TestCaseSummary:
        """get testcase result summary"""
        start_at_timestamp = self.__start_at
        start_at_iso_format = datetime.fromtimestamp(start_at_timestamp).isoformat()

        summary_success = True
        for step_result in self.__step_results:
            if not step_result.success:
                summary_success = False
                break
        
        return TestCaseSummary(
            name=self.__config.name,
            success=summary_success,
            case_id=self.case_id,
            time=TestCaseTime(
                start_at=self.__start_at,
                start_at_iso_format=start_at_iso_format,
                duration=self.__duration,
            ),
            in_out=TestCaseInOut(
                config_vars=self.__config.variables,
                export_vars=self.get_export_variables(),
            ),
            log=self.__log_path,
            step_results=self.__step_results,
        )

    def merge_step_variables(self, variables: VariablesMapping) -> VariablesMapping:
        # override variables
        # step variables > extracted variables from previous steps
        variables = merge_variables(variables, self.__session_variables)
        # step variables > testcase config variables
        variables = merge_variables(variables, self.__config.variables)

        # parse variables
        return self.parser.parse_variables(variables)

    def get_config(self)->TestConfig:
        return self.__config
    
    def call_hooks(self, hooks: Hooks,  step_variables: VariablesMapping, hook_msg: str) -> None:
        """call hook actions.

        Args:
            hooks (list): each hook in hooks list maybe in two format.

                format1 (str): only call hook functions.
                    ${func()}
                format2 (dict): assignment, the value returned by hook function will be assigned to variable.
                    {"var": "${func()}"}

            step_variable: current step variables to call hook, include two special variables

                request: parsed request dict
                response: ResponseObject for current response

            hook_msg: setup/teardown request/testcase

        """

        logger.info(f"call hook actions: {hook_msg}")

        if not isinstance(hooks, list):
            logger.error(f"Invalid hooks format: {hooks}")
            return
        
        for hook in hooks:
            if isinstance(hook, Text):
                # format 1: ["${func()}"]
                logger.debug(f"call hook function: {hook}")
                self.parser.parse_data(hook, step_variables)
            elif isinstance(hook, dict) and len(hook) == 1:
                # format 2: {"var": "${func()}"}
                var_name, hook_content = list(hook.items())[0]
                hook_content_eval = self.parser.parse_data(
                    hook_content, step_variables
                )
                logger.debug(
                    f"call hook function: {hook_content}, got value: {hook_content_eval}"
                )
                logger.debug(f"assign variable: {var_name} = {hook_content_eval}")
                step_variables[var_name] = hook_content_eval
            else:
                logger.error(f"Invalid hook format: {hook}")

    def step_run(self, teststep: TestStep)->StepResult:
        """run teststep: request"""
        step_result = StepResult(
            name = teststep.name,
            step_type= "request",
            success= False
        )

        ### TODO 1.start time
        start_time = time.time()
        ### TODO 2.parse
        functions = self.parser.functions_mapping
        step_variables = self.merge_step_variables(teststep.variables)
        prepare_upload_step(teststep, step_variables, functions)

        ### TODO 3.initialation: request's data
        request_dict = teststep.request.dict()

        request_dict.pop("upload", None)
        request_dict.pop("id")
        parsed_request_dict = self.parser.parse_data(
            request_dict, step_variables
        )

        ### TODO 4.request headers
        request_headers = parsed_request_dict.pop("headers", {})
        # omit pseudo header names for HTTP/1, e.g. :authority, :method, :path, :scheme
        request_headers = {
        key: request_headers[key] for key in request_headers.keys() if not key.startswith(":")
        }
        # add request-id
        request_headers["HRUN-Request-ID"] = f"HRUN-{self.worker_id}" \
            + f"-{self.case_id}-{str(int(time.time() * 1000))[-6:]}"
        
        parsed_request_dict["headers"] = request_headers

        ### setup hooks
        if teststep.setup_hooks:
            self.call_hooks(teststep.setup_hooks, step_variables, "setup request")
        
        ### prepare request arguments
        config = self.get_config()
        method = parsed_request_dict.pop("method")
        url_path = parsed_request_dict.pop("url")
        url = build_url(config.base_url, url_path)
        parsed_request_dict["verify"] = config.verify
        parsed_request_dict["json"] = parsed_request_dict.pop("request_json", {})

        ### log request
        request_print = "====== request details ======\n"
        request_print += f"url: {url}\n"
        request_print += f"method: {method}\n"
        for k, v in parsed_request_dict.items():
            request_print += f"{k}: {pretty_format(v)}\n"
        logger.debug(request_print)

        ### request and get response
        response = self.session.request(
            method=method,
            url=url,
            **parsed_request_dict
        )

        ### log response
        response_print = "====== response details ======\n"
        response_print += f"status_code: {response.status_code}\n"
        response_print += f"headers: {pretty_format(response.headers)}\n"

        try:
            response_body = response.json()
        except (requests.exceptions.JSONDecodeError, json.decoder.JSONDecodeError):
            response_body = response.content

        response_print += f"body: {pretty_format(response_body)}\n"

        ### formation: Response
        response_obj = Response(response, self.parser)

        step_variables["response"] = response_obj

        ### teardown hooks
        if teststep.teardown_hooks:
            self.call_hooks(teststep.teardown_hooks, step_variables, "teardown request")
            
        ### extract
        extractors = teststep.extract
        extract_mapping = response_obj.extract(
            extractors, step_variables)
        step_result.export_vars = extract_mapping

        # merge extract mapping to step variables
        variables_mapping = step_variables
        variables_mapping.update(extract_mapping)

        ### validate & set step result
        validators = teststep.validators

        try:
            response_obj.validate(validators, variables_mapping)
            step_result.success = True
        except ValidationFailure:
            raise
        finally:
            session_data = self.session.data
            session_data.success = step_result.success
            session_data.validators = response_obj.validation_results

            # save step data
            step_result.data = session_data
            session_data.stat.elapsed_time_ms = time.time() - start_time
        
        return step_result

    def _run_teststep(self, teststep: TestStep):
        """run teststep, step maybe any kind that implements IStep interface

        Args:
            step (Step): teststep

        """
        logger.info(f"run step begin: {teststep.name} >>>>>>")
        for i in range(teststep.retry_times + 1):
            try:
                step_result: StepResult = self.step_run(teststep)
                break
            except ValidationFailure as ex:
                if i == teststep.retry_times:
                    raise
                else:
                    logger.warning(
                        f"run step {teststep.name()} validation failed,wait {teststep.retry_interval} sec and try again"
                    )
                    time.sleep(teststep.retry_interval)
                    logger.info(
                        f"run step retry ({i + 1}/{teststep.retry_times} time): {teststep.name()} >>>>>>"
                    )

        # save extracted variables to session variables
        self.__session_variables.update(step_result.export_vars)
        # update testcase summary
        self.__step_results.append(step_result)
        logger.info(f"run step end: {teststep.name} <<<<<<\n")
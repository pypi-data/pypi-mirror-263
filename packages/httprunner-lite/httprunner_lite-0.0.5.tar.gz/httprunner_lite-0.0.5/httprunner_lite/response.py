# -*- encoding: utf-8 -*-

'''
Author     :Phailin
Datetime   :2024-03-18 09:07:18
E-Mail     :phailin791@hotmail.com
'''

import requests
import jmespath
from loguru import logger
from typing import Dict, Text, Any
from jmespath.exceptions import JMESPathError

from httprunner_lite.model import VariablesMapping, Validators
from httprunner_lite.utils.unform_data import uniform_validator
from httprunner_lite.utils.parse import parse_string_value, Parser
from httprunner_lite.utils.exceptions import ValidationFailure, ParamsError

class ResponseBase:
    def __init__(self, response_obj: requests.Response, parser: Parser):
        """initialize with a response object

        Args:
            response_obj (instance): requests.Response instance

        """
        self.response_obj = response_obj
        self.parser = parser
        self.validation_results: Dict = {}

    def extract(
            self, extractors: Dict[Text, Text],
            variables_mapping: VariablesMapping = None
        ) -> Dict:
        if not extractors:
            return {}
        
        extract_mapping = {}

        for key, field in extractors.items():
            if "$" in field:
                # field contains variable or function
                field = self.parser.parse_data(field, variables_mapping)
            field_value = self._search_jmespath(field)
            extract_mapping[key] = field_value
        logger.info(f"extract mapping: {extract_mapping}")
        return extract_mapping
    
    def _search_jmespath(self, jmespath_str: str) -> Any:
        try:
            check_value = jmespath.search(jmespath_str, self.response_obj)
        except JMESPathError as ex:
            logger.error(
                f"failed to search with jmespath\n"
                f"expression: {jmespath_str}\n"
                f"data: {self.response_obj}\n"
                f"exception: {ex}"
            )
            raise
        return check_value
    
    def validate(self,
        validators: Validators,
        variables_mapping: VariablesMapping = {}
    )->Any:
        self.validation_results = {}

        if not validators:
            return 
        
        validate_pass = True
        failures = []

        for v in validators:
            if "validate_extractor" not in self.validation_results:
                self.validation_results["validate_extractor"] = []
            
            u_validator = uniform_validator(v)

            ### check item
            check_item = u_validator["check"]
            if "$" in check_item:
                # check_item is variable or function
                check_item = self.parser.parse_data(check_item, variables_mapping)
                check_item = parse_string_value(check_item)
            
            if check_item and isinstance(check_item, Text):
                check_value = self._search_jmespath(check_item)
            else:
                # variable or function evaluation result is "" or not text
                check_value = check_item
            
            ### comparator
            assert_method = u_validator["assert"]
            assert_func = self.parser.get_mapping_function(assert_method)

            ### expect item
            expect_item = u_validator["expect"]
            # parse expected value with config/teststep/extracted variables
            expect_value = self.parser.parse_data(expect_item, variables_mapping)

            ### message
            message = u_validator["message"]
            # parse message with config/teststep/extracted variables
            message = self.parser.parse_data(message, variables_mapping)

            validate_msg = f"assert {check_item} {assert_method} {expect_value}({type(expect_value).__name__})"

            validator_dict = {
                "comparator": assert_method,
                "check": check_item,
                "check_value": check_value,
                "expect": expect_item,
                "expect_value": expect_value,
                "message": message,
            }

            try:
                assert_func(check_value, expect_value, message)
                validate_msg += "\t==> pass"
                logger.info(validate_msg)
                validator_dict["check_result"] = "pass"
            except AssertionError as ex:
                validate_pass = False
                validator_dict["check_result"] = "fail"
                validate_msg += "\t==> fail"
                validate_msg += (
                    f"\n"
                    f"check_item: {check_item}\n"
                    f"check_value: {check_value}({type(check_value).__name__})\n"
                    f"assert_method: {assert_method}\n"
                    f"expect_value: {expect_value}({type(expect_value).__name__})"
                )
                message = str(ex)
                if message:
                    validate_msg += f"\nmessage: {message}"

                logger.error(validate_msg)
                failures.append(validate_msg)

            self.validation_results["validate_extractor"].append(validator_dict)

        if not validate_pass:
            failures_string = "\n".join([failure for failure in failures])
            raise ValidationFailure(failures_string)

class Response(ResponseBase):
    def __getattr__(self, key):
        if key in ["json", "content", "body"]:
            try:
                value = self.response_obj.json()
            except ValueError:
                value = self.response_obj.content
        elif key == "cookies":
            value = self.response_obj.cookies.get_dict()
        else:
            try:
                value = getattr(self.response_obj, key)
            except AttributeError:
                err_msg = "ResponseObject does not have attribute: {}".format(key)
                logger.error(err_msg)
                raise ParamsError(err_msg)

        self.__dict__[key] = value
        return value

    def _search_jmespath(self, jmespath_str: str) -> Any:
        
        response_mata = {
            "status_code": self.status_code,
            "headers": self.headers,
            "cookies": self.cookies,
            "body": self.body,
        }
        if not jmespath_str.startswith(tuple(response_mata.keys())):
            if hasattr(self.response_obj, jmespath_str):
                return getattr(self.response_obj, jmespath_str)
            else:
                return jmespath_str

        try:
            check_value = jmespath.search(jmespath_str, response_mata)
        except JMESPathError as ex:
            logger.error(
                f"failed to search with jmespath\n"
                f"expression: {jmespath_str}\n"
                f"data: {response_mata}\n"
                f"exception: {ex}"
            )
            raise

        return check_value
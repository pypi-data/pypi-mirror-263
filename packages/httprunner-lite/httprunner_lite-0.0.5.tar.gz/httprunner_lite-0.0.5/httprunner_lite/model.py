# -*- encoding: utf-8 -*-

'''
Author     :Phailin
Datetime   :2024-03-12 09:00:00
E-Mail     :phailin791@hotmail.com
'''

from enum import Enum
from typing import List, Dict, Union, Text, Any, Callable
from pydantic import BaseModel, Field, HttpUrl, AnyUrl

Validators = List[Dict]
Hooks = List[Union[Text, Dict[Text, Text]]]
VariablesMapping = Dict[Text, Any]
FunctionsMapping = Dict[Text, Callable]

class MethodEnum(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    PATCH = "PATCH"

################################################
####################REQUEST_DATA################
################################################
class HttpRequest(BaseModel):
    id: int = Field(..., title="ID", description="ID of the request")
    url: str = Field(..., title="URL", description="URL to send the request to")
    method: MethodEnum = Field(..., title="Method", description="HTTP method to use")
    headers: Dict[Text, Text] = Field({}, title="Headers", description="Headers to send with the request")
    request_json: Union[Dict, List, Text] = Field({}, title="Request JSON", description="JSON data to send with the request")
    data: Union[Text, Dict[Text, Any]] = Field(None, title="Data", description="Data to send with the request")
    params: Dict[Text, Text] = Field({}, title="Params", description="URL parameters to send with the request")
    cookies:  Dict[Text, Text] = Field({}, title="Cookies", description="Cookies to send with the request")
    timeout: float = Field(120, title="Timeout", description="Timeout in seconds")
    allow_redirects: bool = Field(True, title="Allow Redirects", description="Whether to follow redirects")
    verify: bool = Field(False, title="Verify SSL", description="Whether to verify SSL certificates")
    upload: Dict[Text, Any] = Field({}, title="Upload", description="Files to upload with the request")

class TestConfig(BaseModel):
    id: int = Field(..., title="ID", description="ID of the test")
    name: str = Field(..., title="Name", description="Name of the test")
    verify: bool = Field(False, title="Verify SSL", description="Whether to verify SSL certificates")
    base_url: Union[HttpUrl, Text] = Field("", title="Base URL", description="Base URL for the API")
    variables: Union[VariablesMapping, Text] = Field({}, title="Variables", description="Variables to use in the test")
    parameters: Union[VariablesMapping, Text] = Field({}, title="Parameters", description="Parameters to use in the test")
    export: List = Field([], title="Export", description="Variables to export from the test")
    path: Text = Field(None, title="Path", description="Path to the test file")

class TestStep(BaseModel):
    id: int = Field(..., title="ID", description="ID of the test step")
    name : str = Field(..., title="Name", description="Name of the test step")
    request: Union[HttpRequest, None] = Field(None, title="Request", description="Request to send")
    testcase: Union[Text, Callable, None] = Field(None, title="Testcase", description="Testcase to run")
    variables: VariablesMapping = Field({}, title="Variables", description="Variables to use in the test step")
    setup_hooks: List = Field([], title="Setup Hooks", description="Setup hooks to run before the test step")
    teardown_hooks: List = Field([], title="Teardown Hooks", description="Teardown hooks to run after the test step")
    extract: VariablesMapping = Field({}, title="Extract", description="Variables to extract from the response")
    export: List = Field([], title="Export", description="Variables to export from the test step")
    validators: Validators = Field([], title="Validators", description="Validators to run against the response")
    validate_script: List = Field([], title="Validate Script", description="Validate script to run against the response")
    retry_times: int = Field(0, title="Retry Times", description="Number of times to retry the test step")
    retry_interval: int = Field(0, title="Retry Interval", description="Interval between retries in seconds")

class TestCase(BaseModel):
    id: int = Field(..., title="ID", description="Unique identifier for the test case")
    config: TestConfig
    teststeps: List[TestStep] = Field([], title="Test Steps", description="Test steps to run")

class ProjectMeta(BaseModel):
    id: int = Field(..., title="ID", description="Unique identifier for the project")
    driver_path: str = Field("", title="Driver Path", description="Path to the driver.py file")
    functions: FunctionsMapping = Field({}, title="Functions", description="Custom functions to use in the test steps")

################################################
####################RESPONSE_REQUEST############
################################################
class RequestStat(BaseModel):
    content_size: int = Field(0, title="Content Size", description="Size of the response content")
    response_time_ms: float = Field(0, title="Response Time (ms)", description="Response time in milliseconds")
    elapsed_time_ms: float = Field(0, title="Elapsed Time (ms)", description="Elapsed time in milliseconds")

class RequestData(BaseModel):
    url: AnyUrl = Field(..., title="URL", description="Request URL")
    method: MethodEnum = Field(MethodEnum.GET, title="Method", description="Request method")
    headers: Dict[str, str] = Field({}, title="Headers", description="Request headers")
    cookie: Dict[str, str] = Field({}, title="Cookie", description="Request cookie")
    body: Union[Text, bytes, List, Dict, None] = Field({}, title="Body", description="Request body")

class ResponseData(BaseModel):
    status_code: int = Field(0, title="Status Code", description="Response status code")
    headers: Dict[str, str] = Field({}, title="Headers", description="Response headers")
    cookie: Dict[str, str] = Field({}, title="Cookie", description="Response cookie")
    content_type: str = Field("", title="Content Type", description="Response content type")
    body: Union[Text, bytes, List, Dict, None] = Field({}, title="Body", description="Response body")

class AddressData(BaseModel):
    client_ip: str = Field("N/A", title="Client IP", description="Client IP address")
    client_port: int = Field(0, title="Client Port", description="Client port number")
    server_ip: str = Field("N/A", title="Server IP", description="Server IP address")
    server_port: int = Field(0, title="Server Port", description="Server port number")

class RequestEvent(BaseModel):
    request: RequestData = Field(..., title="Request", description="Request data")
    response: ResponseData = Field(..., title="Response", description="Response data")

class SessionData(BaseModel):
    """request session data, including request, response, validators and stat data"""
    success: bool = Field(False, title="Success", description="Whether the request was successful")
    # in most cases, req_resps only contains one request & response
    # while when 30X redirect occurs, req_resps will contain multiple request & response
    request_events: List[RequestEvent] = Field([], title="Request Events", description="Request events")
    stat: RequestStat = Field(RequestStat(), title="Stat", description="Request stat data")
    address: AddressData = Field(AddressData(), title="Address", description="Request address data")
    validators: Dict = Field({}, title="Validators", description="Request validators data")

class PlatformInfo(BaseModel):
    httprunner_version: str = Field(..., title="HttpRunner Version", description="HttpRunner version")
    python_version: str = Field(..., title="Python Version", description="Python version")
    platform: str = Field(..., title="Platform", description="Platform")

class RunningStatistics(BaseModel):
    total: int = Field(..., title="Total", description="Total number of testcases")
    success: int = Field(..., title="Success", description="Number of successful testcases")
    fail: int = Field(..., title="Fail", description="Number of failed testcases")

class TestCaseTime(BaseModel):
    start_at: float = Field(0, title="Start At", description="Start time of the test case")
    start_at_iso_format: str = Field("", title="Start At ISO Format", description="Start time of the test case in ISO format")
    duration: float = Field(0, title="Duration", description="Duration of the test case in seconds")

class StepResult(BaseModel):
    """teststep data, each step maybe corresponding to one request or one testcase"""

    name: str = Field(..., title="Name", description="Teststep name")
    step_type: str = Field(..., title="Step Type", description="Teststep type: request, testcase")
    success: bool = Field(False, title="Success", description="Whether the teststep was successful")
    data: Union[SessionData, List["StepResult"]] = Field(None, title="Data", description="Teststep data")
    elapsed: float = Field(0.0, title="Elapsed", description="Teststep elapsed time")
    content_size: float = Field(0.0, title="Content Size", description="Teststep content size")
    export_vars: VariablesMapping = Field({}, title="Export Vars", description="Teststep export variables")
    attachment: str = Field("", title="Attachment", description="Teststep attachment")

class TestCaseInOut(BaseModel):
    config_vars: VariablesMapping = Field({}, title="Config Vars", description="Configuration variables for the test case")
    export_vars: Dict[str, Any] = Field({}, title="Export Vars", description="Exported variables for the test case")

class TestCaseSummary(BaseModel):
    name: str = Field(..., title="Name", description="Testcase name")
    success: bool = Field(False, title="Success", description="Whether the testcase was successful")
    case_id: str = Field(..., title="Case ID", description="Testcase ID")
    time: TestCaseTime
    in_out: TestCaseInOut = {}
    log: Text = Field("", title="Log", description="Testcase log")
    step_results: List[StepResult] = Field([], title="Step Results", description="Testcase step results")

class TestSuiteSummary(BaseModel):
    success: bool = Field(False, title="Success", description="Whether the test suite was successful")
    running_statistics: RunningStatistics = Field(..., title="Running Statistics", description="Running statistics of the test suite")
    time: TestCaseTime = Field(..., title="Time", description="Test suite time")
    testcases: List[TestCaseSummary] = Field([], title="Testcases", description="Testcase summaries")
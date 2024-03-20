# -*- encoding: utf-8 -*-

'''
Author     :Phailin
Datetime   :2024-03-12 09:00:00
E-Mail     :phailin791@hotmail.com
'''

import json
import time
from loguru import logger
import urllib3
import requests
from requests import Request, Response, Session
from requests.exceptions import (
    InvalidSchema,
    InvalidURL,
    MissingSchema,
    RequestException
)

from httprunner_lite.model import RequestData, ResponseData, SessionData, RequestEvent

from httprunner_lite.utils.helpers import (lower_dict_keys, omit_long_data)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_request_response_record(response_obj: Response)-> RequestEvent:
    """get request and response info from Response() object."""
    def log_print(http_meta, http_meta_type):
        msg = f"\n================== {http_meta_type} details ==================\n"
        for key, value in http_meta.dict().items():
            if isinstance(value, dict) or isinstance(value, list):
                value = json.dumps(value, indent=4, ensure_ascii=False)

            msg += "{:<8} : {}\n".format(key, value)
        logger.debug(msg)
    
    # record actual request info
    request_headers = dict(response_obj.request.headers)
    request_cookies = response_obj.request._cookies.get_dict()

    request_body = response_obj.request.body
    if request_body is not None:
        try:
            request_body = json.loads(request_body)
        except json.JSONDecodeError:
            # str: a=1&b=2
            pass
        except UnicodeDecodeError:
            # bytes/bytearray: request body in protobuf
            pass
        except TypeError:
            # neither str nor bytes/bytearray, e.g. <MultipartEncoder>
            pass

        request_content_type = lower_dict_keys(request_headers).get("content-type")
        if request_content_type and "multipart/form-data" in request_content_type:
            # upload file type
            request_body = "upload file stream (OMITTED)"
    
    request_data = RequestData(
        method=response_obj.request.method,
        url=response_obj.request.url,
        headers=request_headers,
        cookies=request_cookies,
        body=request_body,
    )

    # log request details in debug mode
    log_print(request_data, "request")

    # record response info
    response_headers = dict(response_obj.headers)
    lower_response_headers = lower_dict_keys(response_headers)
    content_type = lower_response_headers.get("content-type", "")

    if "image" in content_type:
        # response is image type, record bytes content only
        response_body = response_obj.content
    else:
        try:
            # try to record json data
            response_body = response_obj.json()
        except ValueError:
            # only record at most 512 text charactors
            response_text = response_obj.text
            response_body = omit_long_data(response_text)
    
    response_data = ResponseData(
        status_code=response_obj.status_code,
        cookies=response_obj.cookies or {},
        encoding=response_obj.encoding,
        headers=response_headers,
        content_type=content_type,
        body=response_body,
    )
    # log response details in debug mode
    log_print(response_data, "response")

    request_event = RequestEvent(request=request_data, response=response_data)

    return request_event

class ApiResponse(Response):
    def raise_for_status(self):
        if hasattr(self, "error") and self.error:
            raise self.error
        Response.raise_for_status(self)

class HttpSession(Session):
    """
    Class for performing HTTP requests and holding (session-) cookies between requests (in order
    to be able to log in and out of websites). Each request is logged so that HttpRunner can
    display statistics.

    This is a slightly extended version of `python-request <http://python-requests.org>`_'s
    :py:class:`requests.Session` class and mostly this class works exactly the same.
    """

    def __init__(self) -> None:
        super(HttpSession, self).__init__()
        self.data = SessionData()

    def update_last_request_response_record(self, response_obj: Response):
        """
        update request and response info from Response() object.
        """
        self.data.request_events.pop()
        self.data.request_events.append(
            get_request_response_record(response_obj)
        )

    def request(self, method, url, name=None, **kwargs):
        """
        Constructs and sends a :py:class:`requests.Request`.
        Returns :py:class:`requests.Response` object.

        :param method:
            method for the new :class:`Request` object.
        :param url:
            URL for the new :class:`Request` object.
        :param name: (optional)
            Placeholder, make compatible with Locust's HttpSession
        :param params: (optional)
            Dictionary or bytes to be sent in the query string for the :class:`Request`.
        :param data: (optional)
            Dictionary or bytes to send in the body of the :class:`Request`.
        :param headers: (optional)
            Dictionary of HTTP Headers to send with the :class:`Request`.
        :param cookies: (optional)
            Dict or CookieJar object to send with the :class:`Request`.
        :param files: (optional)
            Dictionary of ``'filename': file-like-objects`` for multipart encoding upload.
        :param auth: (optional)
            Auth tuple or callable to enable Basic/Digest/Custom HTTP Auth.
        :param timeout: (optional)
            How long to wait for the server to send data before giving up, as a float, or \
            a (`connect timeout, read timeout <user/advanced.html#timeouts>`_) tuple.
            :type timeout: float or tuple
        :param allow_redirects: (optional)
            Set to True by default.
        :type allow_redirects: bool
        :param proxies: (optional)
            Dictionary mapping protocol to the URL of the proxy.
        :param stream: (optional)
            whether to immediately download the response content. Defaults to ``False``.
        :param verify: (optional)
            if ``True``, the SSL cert will be verified. A CA_BUNDLE path can also be provided.
        :param cert: (optional)
            if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
        """
        self.data = SessionData()

        # timeout default to 120 seconds
        kwargs.setdefault("timeout", 120)

        # set stream to True, in order to get client/server IP/Port
        kwargs["stream"] = True

        # start time
        start_timestamp = time.time()
        # request and get response
        response = self._send_request_safe_mode(method, url, **kwargs)
        # duration
        response_time_ms = round((time.time() - start_timestamp) * 1000, 2)

        # request client address info
        try:
            client_ip, client_port = response.raw._connection.sock.getsockname()
            self.data.address.client_ip = client_ip
            self.data.address.client_port = client_port
            logger.debug(f"client IP: {client_ip}, Port: {client_port}")
        except Exception:
            pass

        # response server address info
        try:
            server_ip, server_port = response.raw._connection.sock.getpeername()
            self.data.address.server_ip = server_ip
            self.data.address.server_port = server_port
            logger.debug(f"server IP: {server_ip}, Port: {server_port}")
        except Exception:
            pass

        # get length of the response content
        content_size = int(dict(response.headers).get("content-length") or 0)

        # record the consumed time
        self.data.stat.response_time_ms = response_time_ms
        self.data.stat.elapsed_time_ms = response.elapsed.microseconds / 1000.0
        self.data.stat.content_size = content_size

        # record request and response histories, include 30X redirection
        response_list = response.history + [response]
        self.data.request_events = [
            get_request_response_record(response_obj) for response_obj in response_list
        ]

        try:
            response.raise_for_status()
        except RequestException as ex:
            logger.error(f"{str(ex)}")
        else:
            logger.info(
                f"status_code: {response.status_code}, "
                f"response_time(ms): {response_time_ms} ms, "
                f"response_length: {content_size} bytes"
            )
        return response

    def _send_request_safe_mode(self, method, url, **kwargs):
        """
        Send a HTTP request, and catch any exception that might occur due to connection problems.
        Safe mode has been removed from requests 1.x.
        """
        try:
            return requests.Session.request(self, method, url, **kwargs)
        except (MissingSchema, InvalidSchema, InvalidURL):
            raise
        except RequestException as ex:
            response = ApiResponse()
            response.error = ex
            response.status_code = 0  # with this status_code, content returns None
            response.request = Request(method, url).prepare()
            return response
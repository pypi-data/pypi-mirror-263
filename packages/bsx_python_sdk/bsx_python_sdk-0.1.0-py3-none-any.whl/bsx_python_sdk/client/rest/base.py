import functools
import json
from http import HTTPStatus

import requests

from bsx_python_sdk.common.exception import BSXRequestException, UnknownException, UnauthenticatedException
from bsx_python_sdk.common.utils import AccountStorage


class RestClient(object):
    domain: str

    def __init__(self, domain: str):
        self.domain = domain

    def post(self, endpoint: str, body: dict, headers: dict = None):
        if headers is None:
            headers = {}

        headers["accept"] = "application/json"
        headers["Content-Type"] = "application/json"

        response = requests.post(f"{self.domain}{endpoint}", json=body, headers=headers)
        return self._handle_response(response)

    def delete(self, endpoint: str, body: dict, headers: dict = None):
        if headers is None:
            headers = {}

        headers["accept"] = "application/json"
        headers["Content-Type"] = "application/json"

        response = requests.delete(f"{self.domain}{endpoint}", json=body, headers=headers)
        return self._handle_response(response)

    def get(self, endpoint: str, params: dict = None, headers: dict = None):
        response = requests.get(f"{self.domain}{endpoint}", params=params, headers=headers)
        return self._handle_response(response)

    def _handle_response(self, response: requests.Response):
        resp_body = response.text
        if response.status_code != HTTPStatus.OK.value:
            try:
                json_body = json.loads(resp_body)
                if "code" in json_body:
                    err_code = json_body["code"]
                    if err_code == 16:
                        raise UnauthenticatedException()
                    else:
                        raise BSXRequestException(
                            err_code, json_body.get("message", "Unknown error"), json_body.get("detail")
                        )
            except Exception:
                pass

            raise UnknownException(resp_body)

        return json.loads(resp_body)


class AuthRequiredClient(RestClient):
    def post(self, endpoint: str, body: dict, headers: dict = None):
        if headers is None:
            headers = {}

        api_key = AccountStorage().get_api_key()
        headers['bsx-key'] = api_key.api_key
        headers['bsx-secret'] = api_key.api_secret

        return super().post(endpoint, body, headers)

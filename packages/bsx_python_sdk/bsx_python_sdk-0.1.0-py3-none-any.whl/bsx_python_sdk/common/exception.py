class BSXRequestException(Exception):
    _code: int
    _message: str
    _detail: str

    def __init__(self, code: int, message: str, detail: str):
        super().__init__(f'Request failed with code: {code}, message: {message}, detail: {detail}')

    def get_code(self) -> int:
        return self._code

    def get_message(self) -> str:
        return self._message

    def get_detail(self) -> str:
        return self._detail


class UnknownException(BSXRequestException):
    _response_body: str

    def __init__(self, response_body: str):
        super().__init__(500, "Unknown error", detail=f"Response: {response_body}")
        self._response_body = response_body


class UnauthenticatedException(BSXRequestException):
    def __init__(self):
        super().__init__(code=16, message="Unauthenticated", detail="")

from processout.errors.authenticationerror import AuthenticationError
from processout.errors.genericerror import GenericError
from processout.errors.internalerror import InternalError
from processout.errors.notfounderror import NotFoundError
from processout.errors.validationerror import ValidationError


class Response:
    def __init__(self, resp):
        """Create a new Response instance from the raw requests response

        Keyword argument:
        resp -- requests response"""
        self._raw = resp
        self._status_code = resp.status_code
        self._headers = resp.headers
        self._raw_body = resp.text

        try:
            self._body = resp.json()
        except BaseException:
            self._body = {}

        self._check()

    @property
    def raw(self):
        """Get the raw response"""
        return self._raw

    @property
    def status_code(self):
        """Get the status code"""
        return self._status_code

    @property
    def headers(self):
        """Get the headers array"""
        return self._headers

    @property
    def body(self):
        """Get the json decoded body"""
        return self._body

    @property
    def raw_body(self):
        """Get the raw body"""
        return self._raw_body

    @property
    def success(self):
        """Get the response status"""
        if self.body.get("success") is None or not self.body["success"]:
            return False

        return True

    @property
    def code(self):
        """Get the response code message"""
        code = ""
        if self.body.get("error_type") is not None:
            code = code + self.body["error_type"]

        return code

    @property
    def message(self):
        """Get the response error message"""
        message = ""
        if self.body.get("message") is not None:
            message = message + self.body["message"]

        return message

    def _check(self):
        """Check if response was successful, or raise an error"""
        if not self.success:
            if self.status_code == 404:
                raise NotFoundError(self.code, self.message)
            if self.status_code == 401:
                raise AuthenticationError(self.code, self.message)
            if self.status_code == 400:
                raise ValidationError(self.code, self.message)
            if self.status_code >= 500:
                raise InternalError(self.code, self.message)

            raise GenericError(self.code, self.message)

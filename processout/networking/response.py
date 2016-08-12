try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from ..exceptions.apiexception               import ApiException
from ..exceptions.notfoundexception          import NotFoundException
from ..exceptions.apiauthenticationexception import ApiAuthenticationException

class Response:
    def __init__(self, resp, checkStatusCode = True):
        """Create a new Response instance from the raw requests response

        Keyword argument:
        resp -- requests response
        checkStatusCode -- whether or not to make sure the request succeeded"""
        self._raw        = resp
        self._statusCode = resp.status_code
        self._headers    = resp.headers
        self._rawBody    = resp.text

        self._body = resp.json()

        self._check()

    @property
    def raw(self):
        """Get the raw response"""
        return self._raw

    @property
    def statusCode(self):
        """Get the status code"""
        return self._statusCode

    @property
    def headers(self):
        """Get the headers array"""
        return self._headers

    @property
    def body(self):
        """Get the json decoded body"""
        return self._body

    @property
    def rawBody(self):
        """Get the raw body"""
        return self._rawBody

    @property
    def success(self):
        """Get the response status"""
        if (self.body["success"] == None or not self.body["success"]):
            return False

        return True

    @property
    def message(self):
        """Get the response error message"""
        message = ""
        if self.body["message"] != None:
            message = message + self.body["message"]

        return message

    def _check(self):
        """Check if response was successful, or raise an exception"""
        if (not self.success):
            if self.statusCode == 404:
                raise ApiException(
                    'The resource could not be found (404): ' + self.message)
            if self.statusCode == 401:
                raise ApiException(
                    'Your ProcessOut credentials could not be verified (401): ' +
                        self.message)

            raise ApiException(
                'ProcessOut returned an error (' +
                    str(self.statusCode) + '): ' + self.message)

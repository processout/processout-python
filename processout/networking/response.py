# processout.networking.response

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
        self._body       = resp.json()
        self._rawBody    = resp.text

        if checkStatusCode:
            self._checkStatusCode()

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
        if self.body['success'] == None:
            return False

        return self.body['success']

    @property
    def message(self):
        """Get the response error message"""
        return self.body['message']

    def _checkStatusCode(self):
        """Check if response was successful, or raise an exception"""
        if self.statusCode == 400:
            raise ApiException(self.message)
        elif self.statusCode == 404:
            raise NotFoundException(self.message)
        elif (self.statusCode == 401) or (self.statusCode == 402):
            raise ApiAuthenticationException(self.message)

        if ((self.statusCode < 200) or (self.statusCode > 206)
        		or (self.success != True)):
            raise ApiException(
                'ProcessOut returned an error which couldn\'t be identified. Status code: ' +
                    self.statusCode);
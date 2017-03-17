import requests
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from processout.client import ProcessOut

class Request:
    def __init__(self, client):
        """Create a new Request instance

        Keyword argument:
        client -- ProcessOut client instance
        """
        self._client = client

    def _authenticate(self):
        """Return the correct needed authentication"""
        username = self._client.project_id
        password = self._client.project_secret
        return (username, password)

    def _get_headers(self, options):
        """Return the headers sent with the request"""
        headers = {}
        headers["API-Version"] = "1.4.0.0"

        if options is None:
            return headers

        if "idempotency_key" in options:
            headers["Idempotency-Key"] = options["idempotency_key"]
        if "disable_logging" in options:
            headers["Disable-Logging"] = options["disable_logging"]

        return headers

    def _get_data(self, data, options):
        """Return the data processed with the given options"""
        if options is None:
            return data

        if "expand" in options:
            data["expand"] = options["expand"]
        if "filter" in options:
            data["filter"] = options["filter"]
        if "limit" in options:
            data["limit"] = options["limit"]
        if "end_before" in options:
            data["end_before"] = options["end_before"]
        if "start_after" in options:
            data["start_after"] = options["start_after"]

        return data

    def get(self, path, data, options):
        """Perform a GET request

        Keyword argument:
        path -- Path of the request
        data -- Data to be passed along with the request
        options -- Options sent with the request
        """
        return requests.get(self._client.host + path + '?' +
            urlencode(self._get_data(data, options)),
            auth = self._authenticate(),
            verify = True,
            headers = self._get_headers(options))

    def post(self, path, data, options):
        """Perform a POST request

        Keyword argument:
        path -- Path of the request
        data -- Data to be passed along with the request
        options -- Options sent with the request
        """
        return requests.post(self._client.host + path,
            auth = self._authenticate(),
            json = self._get_data(data, options),
            verify = True,
            headers = self._get_headers(options))

    def put(self, path, data, options):
        """Perform a PUT request

        Keyword argument:
        path -- Path of the request
        data -- Data to be passed along with the request
        options -- Options sent with the request
        """
        return requests.put(self._client.host + path,
            auth = self._authenticate(),
            json = self._get_data(data, options),
            verify = True,
            headers = self._get_headers(options))

    def delete(self, path, data, options):
        """Perform a DELETE request

        Keyword argument:
        path -- Path of the request
        data -- Data to be passed along with the request
        options -- Options sent with the request
        """
        return requests.delete(self._client.host + path + '?' +
                urlencode(self._get_data(data, options)),
            auth = self._authenticate(),
            verify = True,
            headers = self._get_headers(options))
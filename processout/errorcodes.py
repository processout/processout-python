try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class ErrorCodes(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._gateway = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def gateway(self):
        """Get gateway"""
        return self._gateway

    @gateway.setter
    def gateway(self, val):
        """Set gateway
        Keyword argument:
        val -- New gateway value"""
        if val is None:
            self._gateway = val
            return self

        if isinstance(val, dict):
            obj = processout.CategoryErrorCodes(self._client)
            obj.fill_with_data(val)
            self._gateway = obj
        else:
            self._gateway = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "gateway" in data.keys():
            self.gateway = data["gateway"]

        return self

    def to_json(self):
        return {
            "gateway": self.gateway,
        }

    def all(self, options={}):
        """Get all error codes.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/error-codes"
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        body = response.body

        obj = processout.ErrorCodes(self._client)
        return_values.append(obj.fill_with_data(body))

        return return_values[0]

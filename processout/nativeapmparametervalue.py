try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class NativeAPMParameterValue(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._key = None
        self._value = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def key(self):
        """Get key"""
        return self._key

    @key.setter
    def key(self, val):
        """Set key
        Keyword argument:
        val -- New key value"""
        self._key = val
        return self

    @property
    def value(self):
        """Get value"""
        return self._value

    @value.setter
    def value(self, val):
        """Set value
        Keyword argument:
        val -- New value value"""
        self._value = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "key" in data.keys():
            self.key = data["key"]
        if "value" in data.keys():
            self.value = data["value"]

        return self

    def to_json(self):
        return {
            "key": self.key,
            "value": self.value,
        }

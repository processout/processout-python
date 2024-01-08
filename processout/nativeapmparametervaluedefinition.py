try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class NativeAPMParameterValueDefinition(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._value = None
        self._default = None
        self._display_name = None
        if prefill is not None:
            self.fill_with_data(prefill)

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

    @property
    def default(self):
        """Get default"""
        return self._default

    @default.setter
    def default(self, val):
        """Set default
        Keyword argument:
        val -- New default value"""
        self._default = val
        return self

    @property
    def display_name(self):
        """Get display_name"""
        return self._display_name

    @display_name.setter
    def display_name(self, val):
        """Set display_name
        Keyword argument:
        val -- New display_name value"""
        self._display_name = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "value" in data.keys():
            self.value = data["value"]
        if "default" in data.keys():
            self.default = data["default"]
        if "display_name" in data.keys():
            self.display_name = data["display_name"]

        return self

    def to_json(self):
        return {
            "value": self.value,
            "default": self.default,
            "display_name": self.display_name,
        }

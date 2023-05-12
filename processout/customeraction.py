try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class CustomerAction(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._type = None
        self._value = None
        self._metadata = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def type(self):
        """Get type"""
        return self._type

    @type.setter
    def type(self, val):
        """Set type
        Keyword argument:
        val -- New type value"""
        self._type = val
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

    @property
    def metadata(self):
        """Get metadata"""
        return self._metadata

    @metadata.setter
    def metadata(self, val):
        """Set metadata
        Keyword argument:
        val -- New metadata value"""
        self._metadata = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "type" in data.keys():
            self.type = data["type"]
        if "value" in data.keys():
            self.value = data["value"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]

        return self

    def to_json(self):
        return {
            "type": self.type,
            "value": self.value,
            "metadata": self.metadata,
        }

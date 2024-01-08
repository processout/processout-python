try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class NativeAPMParameterDefinition(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._key = None
        self._type = None
        self._required = None
        self._length = None
        self._display_name = None
        self._available_values = None
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
    def required(self):
        """Get required"""
        return self._required

    @required.setter
    def required(self, val):
        """Set required
        Keyword argument:
        val -- New required value"""
        self._required = val
        return self

    @property
    def length(self):
        """Get length"""
        return self._length

    @length.setter
    def length(self, val):
        """Set length
        Keyword argument:
        val -- New length value"""
        self._length = val
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

    @property
    def available_values(self):
        """Get available_values"""
        return self._available_values

    @available_values.setter
    def available_values(self, val):
        """Set available_values
        Keyword argument:
        val -- New available_values value"""
        if val is None:
            self._available_values = []
            return self

        if len(val) > 0 and isinstance(
                val[0], processout.NativeAPMParameterValueDefinition):
            self._available_values = val
        else:
            l = []
            for v in val:
                obj = processout.NativeAPMParameterValueDefinition(
                    self._client)
                obj.fill_with_data(v)
                l.append(obj)
            self._available_values = l
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "key" in data.keys():
            self.key = data["key"]
        if "type" in data.keys():
            self.type = data["type"]
        if "required" in data.keys():
            self.required = data["required"]
        if "length" in data.keys():
            self.length = data["length"]
        if "display_name" in data.keys():
            self.display_name = data["display_name"]
        if "available_values" in data.keys():
            self.available_values = data["available_values"]

        return self

    def to_json(self):
        return {
            "key": self.key,
            "type": self.type,
            "required": self.required,
            "length": self.length,
            "display_name": self.display_name,
            "available_values": self.available_values,
        }

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class NativeAPMResponse(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._state = None
        self._parameter_definitions = None
        self._parameter_values = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def state(self):
        """Get state"""
        return self._state

    @state.setter
    def state(self, val):
        """Set state
        Keyword argument:
        val -- New state value"""
        self._state = val
        return self

    @property
    def parameter_definitions(self):
        """Get parameter_definitions"""
        return self._parameter_definitions

    @parameter_definitions.setter
    def parameter_definitions(self, val):
        """Set parameter_definitions
        Keyword argument:
        val -- New parameter_definitions value"""
        if val is None:
            self._parameter_definitions = []
            return self

        if len(val) > 0 and isinstance(
                val[0], processout.NativeAPMParameterDefinition):
            self._parameter_definitions = val
        else:
            l = []
            for v in val:
                obj = processout.NativeAPMParameterDefinition(self._client)
                obj.fill_with_data(v)
                l.append(obj)
            self._parameter_definitions = l
        return self

    @property
    def parameter_values(self):
        """Get parameter_values"""
        return self._parameter_values

    @parameter_values.setter
    def parameter_values(self, val):
        """Set parameter_values
        Keyword argument:
        val -- New parameter_values value"""
        if val is None:
            self._parameter_values = []
            return self

        if len(val) > 0 and isinstance(
                val[0], processout.NativeAPMParameterValue):
            self._parameter_values = val
        else:
            l = []
            for v in val:
                obj = processout.NativeAPMParameterValue(self._client)
                obj.fill_with_data(v)
                l.append(obj)
            self._parameter_values = l
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "state" in data.keys():
            self.state = data["state"]
        if "parameter_definitions" in data.keys():
            self.parameter_definitions = data["parameter_definitions"]
        if "parameter_values" in data.keys():
            self.parameter_values = data["parameter_values"]

        return self

    def to_json(self):
        return {
            "state": self.state,
            "parameter_definitions": self.parameter_definitions,
            "parameter_values": self.parameter_values,
        }

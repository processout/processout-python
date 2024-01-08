try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class NativeAPMRequest(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._parameter_values = None
        if prefill is not None:
            self.fill_with_data(prefill)

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
        if "parameter_values" in data.keys():
            self.parameter_values = data["parameter_values"]

        return self

    def to_json(self):
        return {
            "parameter_values": self.parameter_values,
        }

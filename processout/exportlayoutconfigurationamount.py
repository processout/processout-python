try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class ExportLayoutConfigurationAmount(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._precision = None
        self._separator = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def precision(self):
        """Get precision"""
        return self._precision

    @precision.setter
    def precision(self, val):
        """Set precision
        Keyword argument:
        val -- New precision value"""
        self._precision = val
        return self

    @property
    def separator(self):
        """Get separator"""
        return self._separator

    @separator.setter
    def separator(self, val):
        """Set separator
        Keyword argument:
        val -- New separator value"""
        self._separator = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "precision" in data.keys():
            self.precision = data["precision"]
        if "separator" in data.keys():
            self.separator = data["separator"]

        return self

    def to_json(self):
        return {
            "precision": self.precision,
            "separator": self.separator,
        }

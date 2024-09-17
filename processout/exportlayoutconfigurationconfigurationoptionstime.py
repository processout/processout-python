try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class ExportLayoutConfigurationConfigurationOptionsTime(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._format = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def format(self):
        """Get format"""
        return self._format

    @format.setter
    def format(self, val):
        """Set format
        Keyword argument:
        val -- New format value"""
        self._format = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "format" in data.keys():
            self.format = data["format"]

        return self

    def to_json(self):
        return {
            "format": self.format,
        }

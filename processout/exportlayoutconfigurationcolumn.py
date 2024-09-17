try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class ExportLayoutConfigurationColumn(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._name = None
        self._rename = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def name(self):
        """Get name"""
        return self._name

    @name.setter
    def name(self, val):
        """Set name
        Keyword argument:
        val -- New name value"""
        self._name = val
        return self

    @property
    def rename(self):
        """Get rename"""
        return self._rename

    @rename.setter
    def rename(self, val):
        """Set rename
        Keyword argument:
        val -- New rename value"""
        self._rename = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "name" in data.keys():
            self.name = data["name"]
        if "rename" in data.keys():
            self.rename = data["rename"]

        return self

    def to_json(self):
        return {
            "name": self.name,
            "rename": self.rename,
        }

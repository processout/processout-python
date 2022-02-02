try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class InvoiceExternalFraudTools(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._forter = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def forter(self):
        """Get forter"""
        return self._forter

    @forter.setter
    def forter(self, val):
        """Set forter
        Keyword argument:
        val -- New forter value"""
        self._forter = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "forter" in data.keys():
            self.forter = data["forter"]

        return self

    def to_json(self):
        return {
            "forter": self.forter,
        }

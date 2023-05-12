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
        self._signifyd = None
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

    @property
    def signifyd(self):
        """Get signifyd"""
        return self._signifyd

    @signifyd.setter
    def signifyd(self, val):
        """Set signifyd
        Keyword argument:
        val -- New signifyd value"""
        self._signifyd = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "forter" in data.keys():
            self.forter = data["forter"]
        if "signifyd" in data.keys():
            self.signifyd = data["signifyd"]

        return self

    def to_json(self):
        return {
            "forter": self.forter,
            "signifyd": self.signifyd,
        }

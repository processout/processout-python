try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class PaymentDataNetworkAuthentication(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._cavv = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def cavv(self):
        """Get cavv"""
        return self._cavv

    @cavv.setter
    def cavv(self, val):
        """Set cavv
        Keyword argument:
        val -- New cavv value"""
        self._cavv = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "cavv" in data.keys():
            self.cavv = data["cavv"]

        return self

    def to_json(self):
        return {
            "cavv": self.cavv,
        }

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class InvoiceTax(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._amount = None
        self._rate = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def amount(self):
        """Get amount"""
        return self._amount

    @amount.setter
    def amount(self, val):
        """Set amount
        Keyword argument:
        val -- New amount value"""
        self._amount = val
        return self

    @property
    def rate(self):
        """Get rate"""
        return self._rate

    @rate.setter
    def rate(self, val):
        """Set rate
        Keyword argument:
        val -- New rate value"""
        self._rate = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "rate" in data.keys():
            self.rate = data["rate"]

        return self

    def to_json(self):
        return {
            "amount": self.amount,
            "rate": self.rate,
        }

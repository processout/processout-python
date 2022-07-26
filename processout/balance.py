try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class Balance(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._amount = None
        self._currency = None
        self._expiry = None
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
    def currency(self):
        """Get currency"""
        return self._currency

    @currency.setter
    def currency(self, val):
        """Set currency
        Keyword argument:
        val -- New currency value"""
        self._currency = val
        return self

    @property
    def expiry(self):
        """Get expiry"""
        return self._expiry

    @expiry.setter
    def expiry(self, val):
        """Set expiry
        Keyword argument:
        val -- New expiry value"""
        self._expiry = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "currency" in data.keys():
            self.currency = data["currency"]
        if "expiry" in data.keys():
            self.expiry = data["expiry"]

        return self

    def to_json(self):
        return {
            "amount": self.amount,
            "currency": self.currency,
            "expiry": self.expiry,
        }

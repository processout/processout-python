try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class NativeAPMTransactionDetailsInvoice(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._amount = None
        self._currency_code = None
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
    def currency_code(self):
        """Get currency_code"""
        return self._currency_code

    @currency_code.setter
    def currency_code(self, val):
        """Set currency_code
        Keyword argument:
        val -- New currency_code value"""
        self._currency_code = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "currency_code" in data.keys():
            self.currency_code = data["currency_code"]

        return self

    def to_json(self):
        return {
            "amount": self.amount,
            "currency_code": self.currency_code,
        }

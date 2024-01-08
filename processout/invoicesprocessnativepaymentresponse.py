try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class InvoicesProcessNativePaymentResponse(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._transaction = None
        self._native_apm = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def transaction(self):
        """Get transaction"""
        return self._transaction

    @transaction.setter
    def transaction(self, val):
        """Set transaction
        Keyword argument:
        val -- New transaction value"""
        if val is None:
            self._transaction = val
            return self

        if isinstance(val, dict):
            obj = processout.Transaction(self._client)
            obj.fill_with_data(val)
            self._transaction = obj
        else:
            self._transaction = val
        return self

    @property
    def native_apm(self):
        """Get native_apm"""
        return self._native_apm

    @native_apm.setter
    def native_apm(self, val):
        """Set native_apm
        Keyword argument:
        val -- New native_apm value"""
        if val is None:
            self._native_apm = val
            return self

        if isinstance(val, dict):
            obj = processout.NativeAPMResponse(self._client)
            obj.fill_with_data(val)
            self._native_apm = obj
        else:
            self._native_apm = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "transaction" in data.keys():
            self.transaction = data["transaction"]
        if "native_apm" in data.keys():
            self.native_apm = data["native_apm"]

        return self

    def to_json(self):
        return {
            "transaction": self.transaction,
            "native_apm": self.native_apm,
        }

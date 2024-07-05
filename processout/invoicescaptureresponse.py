try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class InvoicesCaptureResponse(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._transaction = None
        self._customer_action = None
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
    def customer_action(self):
        """Get customer_action"""
        return self._customer_action

    @customer_action.setter
    def customer_action(self, val):
        """Set customer_action
        Keyword argument:
        val -- New customer_action value"""
        if val is None:
            self._customer_action = val
            return self

        if isinstance(val, dict):
            obj = processout.CustomerAction(self._client)
            obj.fill_with_data(val)
            self._customer_action = obj
        else:
            self._customer_action = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "transaction" in data.keys():
            self.transaction = data["transaction"]
        if "customer_action" in data.keys():
            self.customer_action = data["customer_action"]

        return self

    def to_json(self):
        return {
            "transaction": self.transaction,
            "customer_action": self.customer_action,
        }

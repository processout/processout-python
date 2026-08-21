try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class CardSchemeDetails(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._transaction_id = None
        self._transaction_link_id = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def transaction_id(self):
        """Get transaction_id"""
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, val):
        """Set transaction_id
        Keyword argument:
        val -- New transaction_id value"""
        self._transaction_id = val
        return self

    @property
    def transaction_link_id(self):
        """Get transaction_link_id"""
        return self._transaction_link_id

    @transaction_link_id.setter
    def transaction_link_id(self, val):
        """Set transaction_link_id
        Keyword argument:
        val -- New transaction_link_id value"""
        self._transaction_link_id = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "transaction_id" in data.keys():
            self.transaction_id = data["transaction_id"]
        if "transaction_link_id" in data.keys():
            self.transaction_link_id = data["transaction_link_id"]

        return self

    def to_json(self):
        return {
            "transaction_id": self.transaction_id,
            "transaction_link_id": self.transaction_link_id,
        }

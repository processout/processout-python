try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class PayoutItemAmountBreakdowns(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._scheme_fee = None
        self._interchange_fee = None
        self._gateway_fee = None
        self._markup_fee = None
        self._acquirer_fee = None
        self._other_fee = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def scheme_fee(self):
        """Get scheme_fee"""
        return self._scheme_fee

    @scheme_fee.setter
    def scheme_fee(self, val):
        """Set scheme_fee
        Keyword argument:
        val -- New scheme_fee value"""
        self._scheme_fee = val
        return self

    @property
    def interchange_fee(self):
        """Get interchange_fee"""
        return self._interchange_fee

    @interchange_fee.setter
    def interchange_fee(self, val):
        """Set interchange_fee
        Keyword argument:
        val -- New interchange_fee value"""
        self._interchange_fee = val
        return self

    @property
    def gateway_fee(self):
        """Get gateway_fee"""
        return self._gateway_fee

    @gateway_fee.setter
    def gateway_fee(self, val):
        """Set gateway_fee
        Keyword argument:
        val -- New gateway_fee value"""
        self._gateway_fee = val
        return self

    @property
    def markup_fee(self):
        """Get markup_fee"""
        return self._markup_fee

    @markup_fee.setter
    def markup_fee(self, val):
        """Set markup_fee
        Keyword argument:
        val -- New markup_fee value"""
        self._markup_fee = val
        return self

    @property
    def acquirer_fee(self):
        """Get acquirer_fee"""
        return self._acquirer_fee

    @acquirer_fee.setter
    def acquirer_fee(self, val):
        """Set acquirer_fee
        Keyword argument:
        val -- New acquirer_fee value"""
        self._acquirer_fee = val
        return self

    @property
    def other_fee(self):
        """Get other_fee"""
        return self._other_fee

    @other_fee.setter
    def other_fee(self, val):
        """Set other_fee
        Keyword argument:
        val -- New other_fee value"""
        self._other_fee = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "scheme_fee" in data.keys():
            self.scheme_fee = data["scheme_fee"]
        if "interchange_fee" in data.keys():
            self.interchange_fee = data["interchange_fee"]
        if "gateway_fee" in data.keys():
            self.gateway_fee = data["gateway_fee"]
        if "markup_fee" in data.keys():
            self.markup_fee = data["markup_fee"]
        if "acquirer_fee" in data.keys():
            self.acquirer_fee = data["acquirer_fee"]
        if "other_fee" in data.keys():
            self.other_fee = data["other_fee"]

        return self

    def to_json(self):
        return {
            "scheme_fee": self.scheme_fee,
            "interchange_fee": self.interchange_fee,
            "gateway_fee": self.gateway_fee,
            "markup_fee": self.markup_fee,
            "acquirer_fee": self.acquirer_fee,
            "other_fee": self.other_fee,
        }

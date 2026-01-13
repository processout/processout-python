try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class UnsupportedFeatureBypass(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._incremental_authorization = None
        self._split_payments = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def incremental_authorization(self):
        """Get incremental_authorization"""
        return self._incremental_authorization

    @incremental_authorization.setter
    def incremental_authorization(self, val):
        """Set incremental_authorization
        Keyword argument:
        val -- New incremental_authorization value"""
        self._incremental_authorization = val
        return self

    @property
    def split_payments(self):
        """Get split_payments"""
        return self._split_payments

    @split_payments.setter
    def split_payments(self, val):
        """Set split_payments
        Keyword argument:
        val -- New split_payments value"""
        self._split_payments = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "incremental_authorization" in data.keys():
            self.incremental_authorization = data["incremental_authorization"]
        if "split_payments" in data.keys():
            self.split_payments = data["split_payments"]

        return self

    def to_json(self):
        return {
            "incremental_authorization": self.incremental_authorization,
            "split_payments": self.split_payments,
        }

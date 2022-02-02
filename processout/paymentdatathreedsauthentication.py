try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class PaymentDataThreeDSAuthentication(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._xid = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def xid(self):
        """Get xid"""
        return self._xid

    @xid.setter
    def xid(self, val):
        """Set xid
        Keyword argument:
        val -- New xid value"""
        self._xid = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "XID" in data.keys():
            self.xid = data["XID"]

        return self

    def to_json(self):
        return {
            "XID": self.xid,
        }

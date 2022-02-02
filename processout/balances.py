try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class Balances(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._vouchers = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def vouchers(self):
        """Get vouchers"""
        return self._vouchers

    @vouchers.setter
    def vouchers(self, val):
        """Set vouchers
        Keyword argument:
        val -- New vouchers value"""
        if val is None:
            self._vouchers = []
            return self

        if len(val) > 0 and isinstance(val[0], processout.Balance):
            self._vouchers = val
        else:
            l = []
            for v in val:
                obj = processout.Balance(self._client)
                obj.fill_with_data(v)
                l.append(obj)
            self._vouchers = l
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "vouchers" in data.keys():
            self.vouchers = data["vouchers"]

        return self

    def to_json(self):
        return {
            "vouchers": self.vouchers,
        }

    def find(self, token_id, options={}):
        """Fetch a customer token's balance
        Keyword argument:
        token_id -- ID of the customer's token
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/balances/tokens/" + quote_plus(token_id) + ""
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        body = response.body
        body = body["balances"]
        balances = processout.Balances(self._client)
        return_values.append(balances.fill_with_data(body))

        return return_values[0]

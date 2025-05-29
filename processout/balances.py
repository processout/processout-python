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
        self._available_balance = None
        self._customer_action = None
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

    @property
    def available_balance(self):
        """Get available_balance"""
        return self._available_balance

    @available_balance.setter
    def available_balance(self, val):
        """Set available_balance
        Keyword argument:
        val -- New available_balance value"""
        if val is None:
            self._available_balance = val
            return self

        if isinstance(val, dict):
            obj = processout.Balance(self._client)
            obj.fill_with_data(val)
            self._available_balance = obj
        else:
            self._available_balance = val
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
            obj = processout.BalancesCustomerAction(self._client)
            obj.fill_with_data(val)
            self._customer_action = obj
        else:
            self._customer_action = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "vouchers" in data.keys():
            self.vouchers = data["vouchers"]
        if "available_balance" in data.keys():
            self.available_balance = data["available_balance"]
        if "customer_action" in data.keys():
            self.customer_action = data["customer_action"]

        return self

    def to_json(self):
        return {
            "vouchers": self.vouchers,
            "available_balance": self.available_balance,
            "customer_action": self.customer_action,
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

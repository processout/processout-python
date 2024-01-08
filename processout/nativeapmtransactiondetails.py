try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class NativeAPMTransactionDetails(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._gateway = None
        self._invoice = None
        self._parameters = None
        self._state = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def gateway(self):
        """Get gateway"""
        return self._gateway

    @gateway.setter
    def gateway(self, val):
        """Set gateway
        Keyword argument:
        val -- New gateway value"""
        if val is None:
            self._gateway = val
            return self

        if isinstance(val, dict):
            obj = processout.NativeAPMTransactionDetailsGateway(self._client)
            obj.fill_with_data(val)
            self._gateway = obj
        else:
            self._gateway = val
        return self

    @property
    def invoice(self):
        """Get invoice"""
        return self._invoice

    @invoice.setter
    def invoice(self, val):
        """Set invoice
        Keyword argument:
        val -- New invoice value"""
        if val is None:
            self._invoice = val
            return self

        if isinstance(val, dict):
            obj = processout.NativeAPMTransactionDetailsInvoice(self._client)
            obj.fill_with_data(val)
            self._invoice = obj
        else:
            self._invoice = val
        return self

    @property
    def parameters(self):
        """Get parameters"""
        return self._parameters

    @parameters.setter
    def parameters(self, val):
        """Set parameters
        Keyword argument:
        val -- New parameters value"""
        if val is None:
            self._parameters = []
            return self

        if len(val) > 0 and isinstance(
                val[0], processout.NativeAPMParameterDefinition):
            self._parameters = val
        else:
            l = []
            for v in val:
                obj = processout.NativeAPMParameterDefinition(self._client)
                obj.fill_with_data(v)
                l.append(obj)
            self._parameters = l
        return self

    @property
    def state(self):
        """Get state"""
        return self._state

    @state.setter
    def state(self, val):
        """Set state
        Keyword argument:
        val -- New state value"""
        self._state = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "gateway" in data.keys():
            self.gateway = data["gateway"]
        if "invoice" in data.keys():
            self.invoice = data["invoice"]
        if "parameters" in data.keys():
            self.parameters = data["parameters"]
        if "state" in data.keys():
            self.state = data["state"]

        return self

    def to_json(self):
        return {
            "gateway": self.gateway,
            "invoice": self.invoice,
            "parameters": self.parameters,
            "state": self.state,
        }

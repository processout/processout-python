try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class PaymentProcessingConfiguration(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._bypass_unsupported_split_payments = None
        self._apm_payment_config = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def bypass_unsupported_split_payments(self):
        """Get bypass_unsupported_split_payments"""
        return self._bypass_unsupported_split_payments

    @bypass_unsupported_split_payments.setter
    def bypass_unsupported_split_payments(self, val):
        """Set bypass_unsupported_split_payments
        Keyword argument:
        val -- New bypass_unsupported_split_payments value"""
        self._bypass_unsupported_split_payments = val
        return self

    @property
    def apm_payment_config(self):
        """Get apm_payment_config"""
        return self._apm_payment_config

    @apm_payment_config.setter
    def apm_payment_config(self, val):
        """Set apm_payment_config
        Keyword argument:
        val -- New apm_payment_config value"""
        if val is None:
            self._apm_payment_config = val
            return self

        if isinstance(val, dict):
            obj = processout.APMPaymentProcessingConfiguration(self._client)
            obj.fill_with_data(val)
            self._apm_payment_config = obj
        else:
            self._apm_payment_config = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "bypass_unsupported_split_payments" in data.keys():
            self.bypass_unsupported_split_payments = data["bypass_unsupported_split_payments"]
        if "apm_payment_config" in data.keys():
            self.apm_payment_config = data["apm_payment_config"]

        return self

    def to_json(self):
        return {
            "bypass_unsupported_split_payments": self.bypass_unsupported_split_payments,
            "apm_payment_config": self.apm_payment_config,
        }

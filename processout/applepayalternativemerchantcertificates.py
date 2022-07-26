try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class ApplePayAlternativeMerchantCertificates(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._count = None
        self._alternative_merchant_certificates = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def count(self):
        """Get count"""
        return self._count

    @count.setter
    def count(self, val):
        """Set count
        Keyword argument:
        val -- New count value"""
        self._count = val
        return self

    @property
    def alternative_merchant_certificates(self):
        """Get alternative_merchant_certificates"""
        return self._alternative_merchant_certificates

    @alternative_merchant_certificates.setter
    def alternative_merchant_certificates(self, val):
        """Set alternative_merchant_certificates
        Keyword argument:
        val -- New alternative_merchant_certificates value"""
        if val is None:
            self._alternative_merchant_certificates = []
            return self

        if len(val) > 0 and isinstance(
                val[0], processout.AlternativeMerchantCertificate):
            self._alternative_merchant_certificates = val
        else:
            l = []
            for v in val:
                obj = processout.AlternativeMerchantCertificate(self._client)
                obj.fill_with_data(v)
                l.append(obj)
            self._alternative_merchant_certificates = l
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "count" in data.keys():
            self.count = data["count"]
        if "alternative_merchant_certificates" in data.keys():
            self.alternative_merchant_certificates = data["alternative_merchant_certificates"]

        return self

    def to_json(self):
        return {
            "count": self.count,
            "alternative_merchant_certificates": self.alternative_merchant_certificates,
        }

    def fetch(self, options={}):
        """Fetch the project's alternative certificates by ID
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/projects/applepay/alternative-merchant-certificates"
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        body = response.body
        body = body["applepay_certificates"]
        applePayAlternativeMerchantCertificates = processout.ApplePayAlternativeMerchantCertificates(
            self._client)
        return_values.append(
            applePayAlternativeMerchantCertificates.fill_with_data(body))

        return return_values[0]

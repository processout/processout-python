try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class AlternativeMerchantCertificate(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._id = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def id(self):
        """Get id"""
        return self._id

    @id.setter
    def id(self, val):
        """Set id
        Keyword argument:
        val -- New id value"""
        self._id = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "id" in data.keys():
            self.id = data["id"]

        return self

    def to_json(self):
        return {
            "id": self.id,
        }

    def save(self, options={}):
        """Save new alternative apple pay certificates
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/projects/applepay/alternative-merchant-certificates"
        data = {

        }

        response = Response(request.post(path, data, options))
        return_values = []

        body = response.body
        body = body["alternative_merchant_certificate"]
        alternativeMerchantCertificate = processout.AlternativeMerchantCertificate(
            self._client)
        return_values.append(
            alternativeMerchantCertificate.fill_with_data(body))

        return return_values[0]

    def delete(self, options={}):
        """Delete a given alternative merchant certificate
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/projects/applepay/alternative-merchant-certificates/" + \
            quote_plus(self.id) + ""
        data = {

        }

        response = Response(request.delete(path, data, options))
        return_values = []

        return_values.append(response.success)

        return return_values[0]

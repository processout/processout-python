try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class CardUpdateRequest(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._preferred_scheme = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def preferred_scheme(self):
        """Get preferred_scheme"""
        return self._preferred_scheme

    @preferred_scheme.setter
    def preferred_scheme(self, val):
        """Set preferred_scheme
        Keyword argument:
        val -- New preferred_scheme value"""
        self._preferred_scheme = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "preferred_scheme" in data.keys():
            self.preferred_scheme = data["preferred_scheme"]

        return self

    def to_json(self):
        return {
            "preferred_scheme": self.preferred_scheme,
        }

    def update(self, card_id, options={}):
        """Update a card by its ID.
        Keyword argument:
        card_id -- ID of the card
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/cards/" + quote_plus(card_id) + ""
        data = {
            'preferred_scheme': self.preferred_scheme
        }

        response = Response(request.put(path, data, options))
        return_values = []

        body = response.body
        body = body["card"]

        return_values.append(self.fill_with_data(body))

        return return_values[0]

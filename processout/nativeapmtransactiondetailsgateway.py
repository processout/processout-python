try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class NativeAPMTransactionDetailsGateway(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._display_name = None
        self._logo_url = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def display_name(self):
        """Get display_name"""
        return self._display_name

    @display_name.setter
    def display_name(self, val):
        """Set display_name
        Keyword argument:
        val -- New display_name value"""
        self._display_name = val
        return self

    @property
    def logo_url(self):
        """Get logo_url"""
        return self._logo_url

    @logo_url.setter
    def logo_url(self, val):
        """Set logo_url
        Keyword argument:
        val -- New logo_url value"""
        self._logo_url = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "display_name" in data.keys():
            self.display_name = data["display_name"]
        if "logo_url" in data.keys():
            self.logo_url = data["logo_url"]

        return self

    def to_json(self):
        return {
            "display_name": self.display_name,
            "logo_url": self.logo_url,
        }

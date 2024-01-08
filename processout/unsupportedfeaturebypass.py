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

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "incremental_authorization" in data.keys():
            self.incremental_authorization = data["incremental_authorization"]

        return self

    def to_json(self):
        return {
            "incremental_authorization": self.incremental_authorization,
        }

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class APMPaymentProcessingConfiguration(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._return_redirect_type = None
        self._preferred_finalization_mode = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def return_redirect_type(self):
        """Get return_redirect_type"""
        return self._return_redirect_type

    @return_redirect_type.setter
    def return_redirect_type(self, val):
        """Set return_redirect_type
        Keyword argument:
        val -- New return_redirect_type value"""
        self._return_redirect_type = val
        return self

    @property
    def preferred_finalization_mode(self):
        """Get preferred_finalization_mode"""
        return self._preferred_finalization_mode

    @preferred_finalization_mode.setter
    def preferred_finalization_mode(self, val):
        """Set preferred_finalization_mode
        Keyword argument:
        val -- New preferred_finalization_mode value"""
        self._preferred_finalization_mode = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "return_redirect_type" in data.keys():
            self.return_redirect_type = data["return_redirect_type"]
        if "preferred_finalization_mode" in data.keys():
            self.preferred_finalization_mode = data["preferred_finalization_mode"]

        return self

    def to_json(self):
        return {
            "return_redirect_type": self.return_redirect_type,
            "preferred_finalization_mode": self.preferred_finalization_mode,
        }

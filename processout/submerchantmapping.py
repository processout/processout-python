try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class SubmerchantMapping(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._submerchant_id = None
        self._gateway_configuration_id = None
        self._psp_submerchant_id = None
        self._created_at = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def submerchant_id(self):
        """Get submerchant_id"""
        return self._submerchant_id

    @submerchant_id.setter
    def submerchant_id(self, val):
        """Set submerchant_id
        Keyword argument:
        val -- New submerchant_id value"""
        self._submerchant_id = val
        return self

    @property
    def gateway_configuration_id(self):
        """Get gateway_configuration_id"""
        return self._gateway_configuration_id

    @gateway_configuration_id.setter
    def gateway_configuration_id(self, val):
        """Set gateway_configuration_id
        Keyword argument:
        val -- New gateway_configuration_id value"""
        self._gateway_configuration_id = val
        return self

    @property
    def psp_submerchant_id(self):
        """Get psp_submerchant_id"""
        return self._psp_submerchant_id

    @psp_submerchant_id.setter
    def psp_submerchant_id(self, val):
        """Set psp_submerchant_id
        Keyword argument:
        val -- New psp_submerchant_id value"""
        self._psp_submerchant_id = val
        return self

    @property
    def created_at(self):
        """Get created_at"""
        return self._created_at

    @created_at.setter
    def created_at(self, val):
        """Set created_at
        Keyword argument:
        val -- New created_at value"""
        self._created_at = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "submerchant_id" in data.keys():
            self.submerchant_id = data["submerchant_id"]
        if "gateway_configuration_id" in data.keys():
            self.gateway_configuration_id = data["gateway_configuration_id"]
        if "psp_submerchant_id" in data.keys():
            self.psp_submerchant_id = data["psp_submerchant_id"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]

        return self

    def to_json(self):
        return {
            "submerchant_id": self.submerchant_id,
            "gateway_configuration_id": self.gateway_configuration_id,
            "psp_submerchant_id": self.psp_submerchant_id,
            "created_at": self.created_at,
        }

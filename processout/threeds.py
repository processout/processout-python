try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class ThreeDS(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._version = None
        self._status = None
        self._fingerprinted = None
        self._challenged = None
        self._ares_trans_status = None
        self._cres_trans_status = None
        self._ds_trans_id = None
        self._fingerprint_completion_indicator = None
        self._server_trans_id = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def version(self):
        """Get version"""
        return self._version

    @version.setter
    def version(self, val):
        """Set version
        Keyword argument:
        val -- New version value"""
        self._version = val
        return self

    @property
    def status(self):
        """Get status"""
        return self._status

    @status.setter
    def status(self, val):
        """Set status
        Keyword argument:
        val -- New status value"""
        self._status = val
        return self

    @property
    def fingerprinted(self):
        """Get fingerprinted"""
        return self._fingerprinted

    @fingerprinted.setter
    def fingerprinted(self, val):
        """Set fingerprinted
        Keyword argument:
        val -- New fingerprinted value"""
        self._fingerprinted = val
        return self

    @property
    def challenged(self):
        """Get challenged"""
        return self._challenged

    @challenged.setter
    def challenged(self, val):
        """Set challenged
        Keyword argument:
        val -- New challenged value"""
        self._challenged = val
        return self

    @property
    def ares_trans_status(self):
        """Get ares_trans_status"""
        return self._ares_trans_status

    @ares_trans_status.setter
    def ares_trans_status(self, val):
        """Set ares_trans_status
        Keyword argument:
        val -- New ares_trans_status value"""
        self._ares_trans_status = val
        return self

    @property
    def cres_trans_status(self):
        """Get cres_trans_status"""
        return self._cres_trans_status

    @cres_trans_status.setter
    def cres_trans_status(self, val):
        """Set cres_trans_status
        Keyword argument:
        val -- New cres_trans_status value"""
        self._cres_trans_status = val
        return self

    @property
    def ds_trans_id(self):
        """Get ds_trans_id"""
        return self._ds_trans_id

    @ds_trans_id.setter
    def ds_trans_id(self, val):
        """Set ds_trans_id
        Keyword argument:
        val -- New ds_trans_id value"""
        self._ds_trans_id = val
        return self

    @property
    def fingerprint_completion_indicator(self):
        """Get fingerprint_completion_indicator"""
        return self._fingerprint_completion_indicator

    @fingerprint_completion_indicator.setter
    def fingerprint_completion_indicator(self, val):
        """Set fingerprint_completion_indicator
        Keyword argument:
        val -- New fingerprint_completion_indicator value"""
        self._fingerprint_completion_indicator = val
        return self

    @property
    def server_trans_id(self):
        """Get server_trans_id"""
        return self._server_trans_id

    @server_trans_id.setter
    def server_trans_id(self, val):
        """Set server_trans_id
        Keyword argument:
        val -- New server_trans_id value"""
        self._server_trans_id = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "version" in data.keys():
            self.version = data["version"]
        if "status" in data.keys():
            self.status = data["status"]
        if "fingerprinted" in data.keys():
            self.fingerprinted = data["fingerprinted"]
        if "challenged" in data.keys():
            self.challenged = data["challenged"]
        if "ares_trans_status" in data.keys():
            self.ares_trans_status = data["ares_trans_status"]
        if "cres_trans_status" in data.keys():
            self.cres_trans_status = data["cres_trans_status"]
        if "ds_trans_id" in data.keys():
            self.ds_trans_id = data["ds_trans_id"]
        if "fingerprint_completion_indicator" in data.keys():
            self.fingerprint_completion_indicator = data["fingerprint_completion_indicator"]
        if "server_trans_id" in data.keys():
            self.server_trans_id = data["server_trans_id"]

        return self

    def to_json(self):
        return {
            "version": self.version,
            "status": self.status,
            "fingerprinted": self.fingerprinted,
            "challenged": self.challenged,
            "ares_trans_status": self.ares_trans_status,
            "cres_trans_status": self.cres_trans_status,
            "ds_trans_id": self.ds_trans_id,
            "fingerprint_completion_indicator": self.fingerprint_completion_indicator,
            "server_trans_id": self.server_trans_id,
        }

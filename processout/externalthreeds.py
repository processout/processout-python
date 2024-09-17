try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class ExternalThreeDS(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._xid = None
        self._trans_status = None
        self._eci = None
        self._cavv = None
        self._ds_trans_id = None
        self._version = None
        self._authentication_flow = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def xid(self):
        """Get xid"""
        return self._xid

    @xid.setter
    def xid(self, val):
        """Set xid
        Keyword argument:
        val -- New xid value"""
        self._xid = val
        return self

    @property
    def trans_status(self):
        """Get trans_status"""
        return self._trans_status

    @trans_status.setter
    def trans_status(self, val):
        """Set trans_status
        Keyword argument:
        val -- New trans_status value"""
        self._trans_status = val
        return self

    @property
    def eci(self):
        """Get eci"""
        return self._eci

    @eci.setter
    def eci(self, val):
        """Set eci
        Keyword argument:
        val -- New eci value"""
        self._eci = val
        return self

    @property
    def cavv(self):
        """Get cavv"""
        return self._cavv

    @cavv.setter
    def cavv(self, val):
        """Set cavv
        Keyword argument:
        val -- New cavv value"""
        self._cavv = val
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
    def authentication_flow(self):
        """Get authentication_flow"""
        return self._authentication_flow

    @authentication_flow.setter
    def authentication_flow(self, val):
        """Set authentication_flow
        Keyword argument:
        val -- New authentication_flow value"""
        self._authentication_flow = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "xid" in data.keys():
            self.xid = data["xid"]
        if "trans_status" in data.keys():
            self.trans_status = data["trans_status"]
        if "eci" in data.keys():
            self.eci = data["eci"]
        if "cavv" in data.keys():
            self.cavv = data["cavv"]
        if "ds_trans_id" in data.keys():
            self.ds_trans_id = data["ds_trans_id"]
        if "version" in data.keys():
            self.version = data["version"]
        if "authentication_flow" in data.keys():
            self.authentication_flow = data["authentication_flow"]

        return self

    def to_json(self):
        return {
            "xid": self.xid,
            "trans_status": self.trans_status,
            "eci": self.eci,
            "cavv": self.cavv,
            "ds_trans_id": self.ds_trans_id,
            "version": self.version,
            "authentication_flow": self.authentication_flow,
        }

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class ThreeDS(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._version = None
        self._status = None
        self._fingerprinted = None
        self._challenged = None
        if prefill != None:
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
    

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "Version" in data.keys():
            self.version = data["Version"]
        if "Status" in data.keys():
            self.status = data["Status"]
        if "fingerprinted" in data.keys():
            self.fingerprinted = data["fingerprinted"]
        if "challenged" in data.keys():
            self.challenged = data["challenged"]
        
        return self

    def to_json(self):
        return {
            "Version": self.version,
            "Status": self.status,
            "fingerprinted": self.fingerprinted,
            "challenged": self.challenged,
        }

    

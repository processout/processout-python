try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class InvoiceDevice(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._channel = None
        self._ip_address = None
        if prefill != None:
            self.fill_with_data(prefill)

    
    @property
    def channel(self):
        """Get channel"""
        return self._channel

    @channel.setter
    def channel(self, val):
        """Set channel
        Keyword argument:
        val -- New channel value"""
        self._channel = val
        return self
    
    @property
    def ip_address(self):
        """Get ip_address"""
        return self._ip_address

    @ip_address.setter
    def ip_address(self, val):
        """Set ip_address
        Keyword argument:
        val -- New ip_address value"""
        self._ip_address = val
        return self
    

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "channel" in data.keys():
            self.channel = data["channel"]
        if "ip_address" in data.keys():
            self.ip_address = data["ip_address"]
        
        return self

    

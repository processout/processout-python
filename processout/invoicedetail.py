try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class InvoiceDetail(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._name = None
        self._type = None
        self._amount = None
        self._quantity = None
        self._metadata = None
        if prefill != None:
            self.fill_with_data(prefill)

    
    @property
    def name(self):
        """Get name"""
        return self._name

    @name.setter
    def name(self, val):
        """Set name
        Keyword argument:
        val -- New name value"""
        self._name = val
        return self
    
    @property
    def type(self):
        """Get type"""
        return self._type

    @type.setter
    def type(self, val):
        """Set type
        Keyword argument:
        val -- New type value"""
        self._type = val
        return self
    
    @property
    def amount(self):
        """Get amount"""
        return self._amount

    @amount.setter
    def amount(self, val):
        """Set amount
        Keyword argument:
        val -- New amount value"""
        self._amount = val
        return self
    
    @property
    def quantity(self):
        """Get quantity"""
        return self._quantity

    @quantity.setter
    def quantity(self, val):
        """Set quantity
        Keyword argument:
        val -- New quantity value"""
        self._quantity = val
        return self
    
    @property
    def metadata(self):
        """Get metadata"""
        return self._metadata

    @metadata.setter
    def metadata(self, val):
        """Set metadata
        Keyword argument:
        val -- New metadata value"""
        self._metadata = val
        return self
    

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "name" in data.keys():
            self.name = data["name"]
        if "type" in data.keys():
            self.type = data["type"]
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "quantity" in data.keys():
            self.quantity = data["quantity"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        
        return self

    

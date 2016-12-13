try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Token(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = None
        self._customer = None
        self._customer_id = None
        self._card = None
        self._type = None
        self._metadata = None
        self._is_subscription_only = None
        self._created_at = None
        if prefill != None:
            self.fill_with_data(prefill)

    
    @property
    def id(self):
        """Get id"""
        return self._id

    @id.setter
    def id(self, val):
        """Set id
        Keyword argument:
        val -- New id value"""
        self._id = val
        return self
    
    @property
    def customer(self):
        """Get customer"""
        return self._customer

    @customer.setter
    def customer(self, val):
        """Set customer
        Keyword argument:
        val -- New customer value"""
        if isinstance(val, dict):
            obj = processout.Customer(self._client)
            obj.fill_with_data(val)
            self._customer = obj
        else:
            self._customer = val
        return self
    
    @property
    def customer_id(self):
        """Get customer_id"""
        return self._customer_id

    @customer_id.setter
    def customer_id(self, val):
        """Set customer_id
        Keyword argument:
        val -- New customer_id value"""
        self._customer_id = val
        return self
    
    @property
    def card(self):
        """Get card"""
        return self._card

    @card.setter
    def card(self, val):
        """Set card
        Keyword argument:
        val -- New card value"""
        if isinstance(val, dict):
            obj = processout.Card(self._client)
            obj.fill_with_data(val)
            self._card = obj
        else:
            self._card = val
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
    
    @property
    def is_subscription_only(self):
        """Get is_subscription_only"""
        return self._is_subscription_only

    @is_subscription_only.setter
    def is_subscription_only(self, val):
        """Set is_subscription_only
        Keyword argument:
        val -- New is_subscription_only value"""
        self._is_subscription_only = val
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
        if "id" in data.keys():
            self.id = data["id"]
        if "customer" in data.keys():
            self.customer = data["customer"]
        if "customer_id" in data.keys():
            self.customer_id = data["customer_id"]
        if "card" in data.keys():
            self.card = data["card"]
        if "type" in data.keys():
            self.type = data["type"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "is_subscription_only" in data.keys():
            self.is_subscription_only = data["is_subscription_only"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        
        return self

    def find(self, customer_id, token_id, options = {}):
        """Find a customer's token by its ID.
        Keyword argument:
        customer_id -- ID of the customer
        token_id -- ID of the token
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/customers/" + quote_plus(customer_id) + "/tokens/" + quote_plus(token_id) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        body = response.body
        body = body["token"]
                
                
        obj = processout.Token(self._client)
        return_values.append(obj.fill_with_data(body))
                

        
        return return_values[0]

    def create(self, customer_id, source, options = {}):
        """Create a new token for the given customer ID.
        Keyword argument:
        customer_id -- ID of the customer
        source -- Source used to create the token (most likely a card token generated by ProcessOut.js)
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/customers/" + quote_plus(customer_id) + "/tokens"
        data    = {
            'metadata': self.metadata, 
            'settings': options.get("settings"), 
            'target': options.get("target"), 
            'replace': options.get("replace"), 
            'source': source
        }

        response = Response(request.post(path, data, options))
        return_values = []
        
        body = response.body
        body = body["token"]
                
                
        return_values.append(self.fill_with_data(body))
                

        
        return return_values[0]

    def create_from_request(self, customer_id, source, target, options = {}):
        """Create a new token for the given customer ID from an authorization request
        Keyword argument:
        customer_id -- ID of the customer
        source -- Source used to create the token (most likely a card token generated by ProcessOut.js)
        target -- Authorization request ID
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/customers/" + quote_plus(customer_id) + "/tokens"
        data    = {
            'metadata': self.metadata, 
            'settings': options.get("settings"), 
            'replace': options.get("replace"), 
            'source': source, 
            'target': target
        }

        response = Response(request.post(path, data, options))
        return_values = []
        
        body = response.body
        body = body["token"]
                
                
        return_values.append(self.fill_with_data(body))
                

        
        return return_values[0]

    def delete(self, options = {}):
        """Delete a customer token
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/customers/" + quote_plus(self.customer_id) + "/tokens/" + quote_plus(self.id) + ""
        data    = {

        }

        response = Response(request.delete(path, data, options))
        return_values = []
        
        return_values.append(response.success)

        
        return return_values[0]

    

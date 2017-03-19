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
        self._gateway_configuration = None
        self._gateway_configuration_id = None
        self._card = None
        self._card_id = None
        self._type = None
        self._metadata = None
        self._is_subscription_only = None
        self._is_default = None
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
        if val is None:
            self._customer = val
            return self

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
    def gateway_configuration(self):
        """Get gateway_configuration"""
        return self._gateway_configuration

    @gateway_configuration.setter
    def gateway_configuration(self, val):
        """Set gateway_configuration
        Keyword argument:
        val -- New gateway_configuration value"""
        if val is None:
            self._gateway_configuration = val
            return self

        if isinstance(val, dict):
            obj = processout.GatewayConfiguration(self._client)
            obj.fill_with_data(val)
            self._gateway_configuration = obj
        else:
            self._gateway_configuration = val
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
    def card(self):
        """Get card"""
        return self._card

    @card.setter
    def card(self, val):
        """Set card
        Keyword argument:
        val -- New card value"""
        if val is None:
            self._card = val
            return self

        if isinstance(val, dict):
            obj = processout.Card(self._client)
            obj.fill_with_data(val)
            self._card = obj
        else:
            self._card = val
        return self
    
    @property
    def card_id(self):
        """Get card_id"""
        return self._card_id

    @card_id.setter
    def card_id(self, val):
        """Set card_id
        Keyword argument:
        val -- New card_id value"""
        self._card_id = val
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
    def is_default(self):
        """Get is_default"""
        return self._is_default

    @is_default.setter
    def is_default(self, val):
        """Set is_default
        Keyword argument:
        val -- New is_default value"""
        self._is_default = val
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
        if "gateway_configuration" in data.keys():
            self.gateway_configuration = data["gateway_configuration"]
        if "gateway_configuration_id" in data.keys():
            self.gateway_configuration_id = data["gateway_configuration_id"]
        if "card" in data.keys():
            self.card = data["card"]
        if "card_id" in data.keys():
            self.card_id = data["card_id"]
        if "type" in data.keys():
            self.type = data["type"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "is_subscription_only" in data.keys():
            self.is_subscription_only = data["is_subscription_only"]
        if "is_default" in data.keys():
            self.is_default = data["is_default"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        
        return self

    def fetch_customer_tokens(self, customer_id, options = {}):
        """Get the customer's tokens.
        Keyword argument:
        customer_id -- ID of the customer
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/customers/" + quote_plus(customer_id) + "/tokens"
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        a    = []
        body = response.body
        for v in body['tokens']:
            tmp = processout.Token(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)
            

        
        return return_values[0]

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

    def create(self, options = {}):
        """Create a new token for the given customer ID.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/customers/" + quote_plus(self.customer_id) + "/tokens"
        data    = {
            'metadata': self.metadata, 
            'source': options.get("source"), 
            'settings': options.get("settings"), 
            'target': options.get("target"), 
            'set_default': options.get("set_default")
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

    

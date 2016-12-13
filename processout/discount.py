try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Discount(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = None
        self._project = None
        self._subscription = None
        self._coupon = None
        self._amount = None
        self._expires_at = None
        self._metadata = None
        self._sandbox = None
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
    def project(self):
        """Get project"""
        return self._project

    @project.setter
    def project(self, val):
        """Set project
        Keyword argument:
        val -- New project value"""
        if isinstance(val, dict):
            obj = processout.Project(self._client)
            obj.fill_with_data(val)
            self._project = obj
        else:
            self._project = val
        return self
    
    @property
    def subscription(self):
        """Get subscription"""
        return self._subscription

    @subscription.setter
    def subscription(self, val):
        """Set subscription
        Keyword argument:
        val -- New subscription value"""
        if isinstance(val, dict):
            obj = processout.Subscription(self._client)
            obj.fill_with_data(val)
            self._subscription = obj
        else:
            self._subscription = val
        return self
    
    @property
    def coupon(self):
        """Get coupon"""
        return self._coupon

    @coupon.setter
    def coupon(self, val):
        """Set coupon
        Keyword argument:
        val -- New coupon value"""
        if isinstance(val, dict):
            obj = processout.Coupon(self._client)
            obj.fill_with_data(val)
            self._coupon = obj
        else:
            self._coupon = val
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
    def expires_at(self):
        """Get expires_at"""
        return self._expires_at

    @expires_at.setter
    def expires_at(self, val):
        """Set expires_at
        Keyword argument:
        val -- New expires_at value"""
        self._expires_at = val
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
    def sandbox(self):
        """Get sandbox"""
        return self._sandbox

    @sandbox.setter
    def sandbox(self, val):
        """Set sandbox
        Keyword argument:
        val -- New sandbox value"""
        self._sandbox = val
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
        if "project" in data.keys():
            self.project = data["project"]
        if "subscription" in data.keys():
            self.subscription = data["subscription"]
        if "coupon" in data.keys():
            self.coupon = data["coupon"]
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "expires_at" in data.keys():
            self.expires_at = data["expires_at"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        
        return self

    def apply(self, subscription_id, options = {}):
        """Apply a new discount to the given subscription ID.
        Keyword argument:
        subscription_id -- ID of the subscription
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(subscription_id) + "/discounts"
        data    = {
            'amount': self.amount, 
            'expires_at': self.expires_at, 
            'metadata': self.metadata, 
            'coupon_id': options.get("coupon_id")
        }

        response = Response(request.post(path, data, options))
        return_values = []
        
        body = response.body
        body = body["discount"]
                
                
        return_values.append(self.fill_with_data(body))
                

        
        return return_values[0]

    def apply_coupon(self, subscription_id, coupon_id, options = {}):
        """Apply a new discount on the subscription from a coupon ID.
        Keyword argument:
        subscription_id -- ID of the subscription
        coupon_id -- ID of the coupon
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(subscription_id) + "/discounts"
        data    = {
            'coupon_id': coupon_id
        }

        response = Response(request.post(path, data, options))
        return_values = []
        
        body = response.body
        body = body["discount"]
                
                
        obj = processout.Discount(self._client)
        return_values.append(obj.fill_with_data(body))
                

        
        return return_values[0]

    def find(self, subscription_id, discount_id, options = {}):
        """Find a subscription's discount by its ID.
        Keyword argument:
        subscription_id -- ID of the subscription on which the discount was applied
        discount_id -- ID of the discount
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(subscription_id) + "/discounts/" + quote_plus(discount_id) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        body = response.body
        body = body["discount"]
                
                
        obj = processout.Discount(self._client)
        return_values.append(obj.fill_with_data(body))
                

        
        return return_values[0]

    

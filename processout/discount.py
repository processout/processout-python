try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Discount:
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = ""
        self._project = None
        self._subscription = None
        self._coupon = None
        self._amount = ""
        self._expiresAt = ""
        self._metadata = {}
        self._sandbox = False
        self._createdAt = ""
        if prefill != None:
            self.fillWithData(prefill)

    
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
        if isinstance(val, Project):
            self._project = val
        else:
            obj = processout.Project(self._client)
            obj.fillWithData(val)
            self._project = obj
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
        if isinstance(val, Subscription):
            self._subscription = val
        else:
            obj = processout.Subscription(self._client)
            obj.fillWithData(val)
            self._subscription = obj
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
        if isinstance(val, Coupon):
            self._coupon = val
        else:
            obj = processout.Coupon(self._client)
            obj.fillWithData(val)
            self._coupon = obj
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
    def expiresAt(self):
        """Get expiresAt"""
        return self._expiresAt

    @expiresAt.setter
    def expiresAt(self, val):
        """Set expiresAt
        Keyword argument:
        val -- New expiresAt value"""
        self._expiresAt = val
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
    def createdAt(self):
        """Get createdAt"""
        return self._createdAt

    @createdAt.setter
    def createdAt(self, val):
        """Set createdAt
        Keyword argument:
        val -- New createdAt value"""
        self._createdAt = val
        return self
    

    def fillWithData(self, data):
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
            self.expiresAt = data["expires_at"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.createdAt = data["created_at"]
        
        return self

    def apply(self, subscriptionId, options = None):
        """Apply a new discount to the given subscription ID.
        Keyword argument:
        subscriptionId -- ID of the subscription
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(subscriptionId) + "/discounts"
        data    = {
            'amount': self.amount, 
            'expires_at': self.expiresAt, 
            'metadata': self.metadata
        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["discount"]
                
                
        returnValues.append(self.fillWithData(body))
                

        
        return returnValues[0];

    def applyCoupon(self, subscriptionId, couponId, options = None):
        """Apply a new discount to the given subscription ID from a coupon ID.
        Keyword argument:
        subscriptionId -- ID of the subscription
        couponId -- ID of the coupon
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(subscriptionId) + "/discounts"
        data    = {
            'amount': self.amount, 
            'expires_at': self.expiresAt, 
            'metadata': self.metadata, 
            'coupon_id': couponId
        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["discount"]
                
                
        returnValues.append(self.fillWithData(body))
                

        
        return returnValues[0];

    def find(self, subscriptionId, discountId, options = None):
        """Find a subscription's discount by its ID.
        Keyword argument:
        subscriptionId -- ID of the subscription on which the discount was applied
        discountId -- ID of the discount
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(subscriptionId) + "/discounts/" + quote_plus(discountId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["discount"]
                
                
        obj = processout.Discount(self._client)
        returnValues.append(obj.fillWithData(body))
                

        
        return returnValues[0];

    

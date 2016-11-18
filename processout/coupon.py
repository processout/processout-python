try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Coupon(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = ""
        self._project = None
        self._name = ""
        self._amountOff = ""
        self._percentOff = 0
        self._currency = ""
        self._maxRedemptions = 0
        self._expiresAt = ""
        self._metadata = {}
        self._iterationCount = 0
        self._redeemedNumber = 0
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
        if isinstance(val, dict):
            obj = processout.Project(self._client)
            obj.fillWithData(val)
            self._project = obj
        else:
            self._project = val
        return self
    
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
    def amountOff(self):
        """Get amountOff"""
        return self._amountOff

    @amountOff.setter
    def amountOff(self, val):
        """Set amountOff
        Keyword argument:
        val -- New amountOff value"""
        self._amountOff = val
        return self
    
    @property
    def percentOff(self):
        """Get percentOff"""
        return self._percentOff

    @percentOff.setter
    def percentOff(self, val):
        """Set percentOff
        Keyword argument:
        val -- New percentOff value"""
        self._percentOff = val
        return self
    
    @property
    def currency(self):
        """Get currency"""
        return self._currency

    @currency.setter
    def currency(self, val):
        """Set currency
        Keyword argument:
        val -- New currency value"""
        self._currency = val
        return self
    
    @property
    def maxRedemptions(self):
        """Get maxRedemptions"""
        return self._maxRedemptions

    @maxRedemptions.setter
    def maxRedemptions(self, val):
        """Set maxRedemptions
        Keyword argument:
        val -- New maxRedemptions value"""
        self._maxRedemptions = val
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
    def iterationCount(self):
        """Get iterationCount"""
        return self._iterationCount

    @iterationCount.setter
    def iterationCount(self, val):
        """Set iterationCount
        Keyword argument:
        val -- New iterationCount value"""
        self._iterationCount = val
        return self
    
    @property
    def redeemedNumber(self):
        """Get redeemedNumber"""
        return self._redeemedNumber

    @redeemedNumber.setter
    def redeemedNumber(self, val):
        """Set redeemedNumber
        Keyword argument:
        val -- New redeemedNumber value"""
        self._redeemedNumber = val
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
        if "name" in data.keys():
            self.name = data["name"]
        if "amount_off" in data.keys():
            self.amountOff = data["amount_off"]
        if "percent_off" in data.keys():
            self.percentOff = data["percent_off"]
        if "currency" in data.keys():
            self.currency = data["currency"]
        if "max_redemptions" in data.keys():
            self.maxRedemptions = data["max_redemptions"]
        if "expires_at" in data.keys():
            self.expiresAt = data["expires_at"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "iteration_count" in data.keys():
            self.iterationCount = data["iteration_count"]
        if "redeemed_number" in data.keys():
            self.redeemedNumber = data["redeemed_number"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.createdAt = data["created_at"]
        
        return self

    def all(self, options = None):
        """Get all the coupons.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/coupons"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        a    = []
        body = response.body
        for v in body['coupons']:
            tmp = Coupon(self._client)
            tmp.fillWithData(v)
            a.append(tmp)

        returnValues.append(a)
            

        
        return returnValues[0];

    def create(self, options = None):
        """Create a new coupon.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/coupons"
        data    = {
            'id': self.id, 
            'amount_off': self.amountOff, 
            'percent_off': self.percentOff, 
            'currency': self.currency, 
            'iteration_count': self.iterationCount, 
            'max_redemptions': self.maxRedemptions, 
            'expires_at': self.expiresAt, 
            'metadata': self.metadata
        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["coupon"]
                
                
        returnValues.append(self.fillWithData(body))
                

        
        return returnValues[0];

    def find(self, couponId, options = None):
        """Find a coupon by its ID.
        Keyword argument:
        couponId -- ID of the coupon
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/coupons/" + quote_plus(couponId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["coupon"]
                
                
        obj = processout.Coupon(self._client)
        returnValues.append(obj.fillWithData(body))
                

        
        return returnValues[0];

    def save(self, options = None):
        """Save the updated coupon attributes.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/coupons/" + quote_plus(self.id) + ""
        data    = {
            'metadata': self.metadata
        }

        response = Response(request.put(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["coupon"]
                
                
        returnValues.append(self.fillWithData(body))
                

        
        return returnValues[0];

    def delete(self, options = None):
        """Delete the coupon.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/coupons/" + quote_plus(self.id) + ""
        data    = {

        }

        response = Response(request.delete(path, data, options))
        returnValues = []
        
        returnValues.append(response.success)

        
        return returnValues[0];

    

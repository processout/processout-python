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

        self._id = None
        self._project = None
        self._project_id = None
        self._amount_off = None
        self._percent_off = None
        self._currency = None
        self._iteration_count = None
        self._max_redemptions = None
        self._expires_at = None
        self._metadata = None
        self._redeemed_number = None
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
        if val is None:
            self._project = val
            return self

        if isinstance(val, dict):
            obj = processout.Project(self._client)
            obj.fill_with_data(val)
            self._project = obj
        else:
            self._project = val
        return self
    
    @property
    def project_id(self):
        """Get project_id"""
        return self._project_id

    @project_id.setter
    def project_id(self, val):
        """Set project_id
        Keyword argument:
        val -- New project_id value"""
        self._project_id = val
        return self
    
    @property
    def amount_off(self):
        """Get amount_off"""
        return self._amount_off

    @amount_off.setter
    def amount_off(self, val):
        """Set amount_off
        Keyword argument:
        val -- New amount_off value"""
        self._amount_off = val
        return self
    
    @property
    def percent_off(self):
        """Get percent_off"""
        return self._percent_off

    @percent_off.setter
    def percent_off(self, val):
        """Set percent_off
        Keyword argument:
        val -- New percent_off value"""
        self._percent_off = val
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
    def iteration_count(self):
        """Get iteration_count"""
        return self._iteration_count

    @iteration_count.setter
    def iteration_count(self, val):
        """Set iteration_count
        Keyword argument:
        val -- New iteration_count value"""
        self._iteration_count = val
        return self
    
    @property
    def max_redemptions(self):
        """Get max_redemptions"""
        return self._max_redemptions

    @max_redemptions.setter
    def max_redemptions(self, val):
        """Set max_redemptions
        Keyword argument:
        val -- New max_redemptions value"""
        self._max_redemptions = val
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
    def redeemed_number(self):
        """Get redeemed_number"""
        return self._redeemed_number

    @redeemed_number.setter
    def redeemed_number(self, val):
        """Set redeemed_number
        Keyword argument:
        val -- New redeemed_number value"""
        self._redeemed_number = val
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
        if "project_id" in data.keys():
            self.project_id = data["project_id"]
        if "amount_off" in data.keys():
            self.amount_off = data["amount_off"]
        if "percent_off" in data.keys():
            self.percent_off = data["percent_off"]
        if "currency" in data.keys():
            self.currency = data["currency"]
        if "iteration_count" in data.keys():
            self.iteration_count = data["iteration_count"]
        if "max_redemptions" in data.keys():
            self.max_redemptions = data["max_redemptions"]
        if "expires_at" in data.keys():
            self.expires_at = data["expires_at"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "redeemed_number" in data.keys():
            self.redeemed_number = data["redeemed_number"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        
        return self

    def all(self, options = {}):
        """Get all the coupons.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/coupons"
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        a    = []
        body = response.body
        for v in body['coupons']:
            tmp = processout.Coupon(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)
            

        
        return return_values[0]

    def create(self, options = {}):
        """Create a new coupon.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/coupons"
        data    = {
            'id': self.id, 
            'amount_off': self.amount_off, 
            'percent_off': self.percent_off, 
            'currency': self.currency, 
            'iteration_count': self.iteration_count, 
            'max_redemptions': self.max_redemptions, 
            'expires_at': self.expires_at, 
            'metadata': self.metadata
        }

        response = Response(request.post(path, data, options))
        return_values = []
        
        body = response.body
        body = body["coupon"]
                
                
        return_values.append(self.fill_with_data(body))
                

        
        return return_values[0]

    def find(self, coupon_id, options = {}):
        """Find a coupon by its ID.
        Keyword argument:
        coupon_id -- ID of the coupon
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/coupons/" + quote_plus(coupon_id) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        body = response.body
        body = body["coupon"]
                
                
        obj = processout.Coupon(self._client)
        return_values.append(obj.fill_with_data(body))
                

        
        return return_values[0]

    def save(self, options = {}):
        """Save the updated coupon attributes.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/coupons/" + quote_plus(self.id) + ""
        data    = {
            'metadata': self.metadata
        }

        response = Response(request.put(path, data, options))
        return_values = []
        
        body = response.body
        body = body["coupon"]
                
                
        return_values.append(self.fill_with_data(body))
                

        
        return return_values[0]

    def delete(self, options = {}):
        """Delete the coupon.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/coupons/" + quote_plus(self.id) + ""
        data    = {

        }

        response = Response(request.delete(path, data, options))
        return_values = []
        
        return_values.append(response.success)

        
        return return_values[0]

    

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Plan:
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = ""
        self._project = None
        self._name = ""
        self._amount = ""
        self._currency = ""
        self._metadata = {}
        self._interval = ""
        self._trialPeriod = "0d"
        self._returnUrl = ""
        self._cancelUrl = ""
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
    def interval(self):
        """Get interval"""
        return self._interval

    @interval.setter
    def interval(self, val):
        """Set interval
        Keyword argument:
        val -- New interval value"""
        self._interval = val
        return self
    
    @property
    def trialPeriod(self):
        """Get trialPeriod"""
        return self._trialPeriod

    @trialPeriod.setter
    def trialPeriod(self, val):
        """Set trialPeriod
        Keyword argument:
        val -- New trialPeriod value"""
        self._trialPeriod = val
        return self
    
    @property
    def returnUrl(self):
        """Get returnUrl"""
        return self._returnUrl

    @returnUrl.setter
    def returnUrl(self, val):
        """Set returnUrl
        Keyword argument:
        val -- New returnUrl value"""
        self._returnUrl = val
        return self
    
    @property
    def cancelUrl(self):
        """Get cancelUrl"""
        return self._cancelUrl

    @cancelUrl.setter
    def cancelUrl(self, val):
        """Set cancelUrl
        Keyword argument:
        val -- New cancelUrl value"""
        self._cancelUrl = val
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
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "currency" in data.keys():
            self.currency = data["currency"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "interval" in data.keys():
            self.interval = data["interval"]
        if "trial_period" in data.keys():
            self.trialPeriod = data["trial_period"]
        if "return_url" in data.keys():
            self.returnUrl = data["return_url"]
        if "cancel_url" in data.keys():
            self.cancelUrl = data["cancel_url"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.createdAt = data["created_at"]
        
        return self

    def all(self, options = None):
        """Get all the plans.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/plans"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        a    = []
        body = response.body
        for v in body['plans']:
            tmp = Plan(self._client)
            tmp.fillWithData(v)
            a.append(tmp)

        returnValues.append(a)
            

        
        return returnValues[0];

    def create(self, options = None):
        """Create a new plan.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/plans"
        data    = {
            'id': self.id, 
            'name': self.name, 
            'amount': self.amount, 
            'currency': self.currency, 
            'interval': self.interval, 
            'trial_period': self.trialPeriod, 
            'metadata': self.metadata, 
            'return_url': self.returnUrl, 
            'cancel_url': self.cancelUrl
        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["plan"]
                
                
        returnValues.append(self.fillWithData(body))
                

        
        return returnValues[0];

    def find(self, planId, options = None):
        """Find a plan by its ID.
        Keyword argument:
        planId -- ID of the plan
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/plans/" + quote_plus(planId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["plan"]
                
                
        obj = processout.Plan(self._client)
        returnValues.append(obj.fillWithData(body))
                

        
        return returnValues[0];

    def update(self, options = None):
        """Update the plan. This action won't affect subscriptions already linked to this plan.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/plans/" + quote_plus(self.id) + ""
        data    = {
            'name': self.name, 
            'trial_period': self.trialPeriod, 
            'metadata': self.metadata, 
            'return_url': self.returnUrl, 
            'cancel_url': self.cancelUrl
        }

        response = Response(request.put(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["plan"]
                
                
        returnValues.append(self.fillWithData(body))
                

        
        return returnValues[0];

    def end(self, options = None):
        """Delete a plan. Subscriptions linked to this plan won't be affected.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/plans/" + quote_plus(self.id) + ""
        data    = {

        }

        response = Response(request.delete(path, data, options))
        returnValues = []
        
        returnValues.append(response.success)

        
        return returnValues[0];

    

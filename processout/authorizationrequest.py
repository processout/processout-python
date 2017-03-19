try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class AuthorizationRequest(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = None
        self._project = None
        self._project_id = None
        self._customer = None
        self._customer_id = None
        self._token = None
        self._token_id = None
        self._name = None
        self._currency = None
        self._return_url = None
        self._cancel_url = None
        self._authorized = None
        self._sandbox = None
        self._url = None
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
    def token(self):
        """Get token"""
        return self._token

    @token.setter
    def token(self, val):
        """Set token
        Keyword argument:
        val -- New token value"""
        if val is None:
            self._token = val
            return self

        if isinstance(val, dict):
            obj = processout.Token(self._client)
            obj.fill_with_data(val)
            self._token = obj
        else:
            self._token = val
        return self
    
    @property
    def token_id(self):
        """Get token_id"""
        return self._token_id

    @token_id.setter
    def token_id(self, val):
        """Set token_id
        Keyword argument:
        val -- New token_id value"""
        self._token_id = val
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
    def return_url(self):
        """Get return_url"""
        return self._return_url

    @return_url.setter
    def return_url(self, val):
        """Set return_url
        Keyword argument:
        val -- New return_url value"""
        self._return_url = val
        return self
    
    @property
    def cancel_url(self):
        """Get cancel_url"""
        return self._cancel_url

    @cancel_url.setter
    def cancel_url(self, val):
        """Set cancel_url
        Keyword argument:
        val -- New cancel_url value"""
        self._cancel_url = val
        return self
    
    @property
    def authorized(self):
        """Get authorized"""
        return self._authorized

    @authorized.setter
    def authorized(self, val):
        """Set authorized
        Keyword argument:
        val -- New authorized value"""
        self._authorized = val
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
    def url(self):
        """Get url"""
        return self._url

    @url.setter
    def url(self, val):
        """Set url
        Keyword argument:
        val -- New url value"""
        self._url = val
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
        if "customer" in data.keys():
            self.customer = data["customer"]
        if "customer_id" in data.keys():
            self.customer_id = data["customer_id"]
        if "token" in data.keys():
            self.token = data["token"]
        if "token_id" in data.keys():
            self.token_id = data["token_id"]
        if "name" in data.keys():
            self.name = data["name"]
        if "currency" in data.keys():
            self.currency = data["currency"]
        if "return_url" in data.keys():
            self.return_url = data["return_url"]
        if "cancel_url" in data.keys():
            self.cancel_url = data["cancel_url"]
        if "authorized" in data.keys():
            self.authorized = data["authorized"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "url" in data.keys():
            self.url = data["url"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        
        return self

    def fetch_customer(self, options = {}):
        """Get the customer linked to the authorization request.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/authorization-requests/" + quote_plus(self.id) + "/customers"
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        body = response.body
        body = body["customer"]
        customer = processout.Customer(self._client)
        return_values.append(customer.fill_with_data(body))

        
        return return_values[0]

    def create(self, options = {}):
        """Create a new authorization request for the given customer ID.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/authorization-requests"
        data    = {
            'customer_id': self.customer_id, 
            'name': self.name, 
            'currency': self.currency, 
            'return_url': self.return_url, 
            'cancel_url': self.cancel_url
        }

        response = Response(request.post(path, data, options))
        return_values = []
        
        body = response.body
        body = body["authorization_request"]
                
                
        return_values.append(self.fill_with_data(body))
                

        
        return return_values[0]

    def find(self, authorization_request_id, options = {}):
        """Find an authorization request by its ID.
        Keyword argument:
        authorization_request_id -- ID of the authorization request
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/authorization-requests/" + quote_plus(authorization_request_id) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        body = response.body
        body = body["authorization_request"]
                
                
        obj = processout.AuthorizationRequest(self._client)
        return_values.append(obj.fill_with_data(body))
                

        
        return return_values[0]

    

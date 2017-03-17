try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class APIRequest(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = None
        self._project = None
        self._api_version = None
        self._idempotency_key = None
        self._url = None
        self._method = None
        self._headers = None
        self._body = None
        self._response_code = None
        self._response_headers = None
        self._response_body = None
        self._response_ms = None
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
    def api_version(self):
        """Get api_version"""
        return self._api_version

    @api_version.setter
    def api_version(self, val):
        """Set api_version
        Keyword argument:
        val -- New api_version value"""
        if val is None:
            self._api_version = val
            return self

        if isinstance(val, dict):
            obj = processout.APIVersion(self._client)
            obj.fill_with_data(val)
            self._api_version = obj
        else:
            self._api_version = val
        return self
    
    @property
    def idempotency_key(self):
        """Get idempotency_key"""
        return self._idempotency_key

    @idempotency_key.setter
    def idempotency_key(self, val):
        """Set idempotency_key
        Keyword argument:
        val -- New idempotency_key value"""
        self._idempotency_key = val
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
    def method(self):
        """Get method"""
        return self._method

    @method.setter
    def method(self, val):
        """Set method
        Keyword argument:
        val -- New method value"""
        self._method = val
        return self
    
    @property
    def headers(self):
        """Get headers"""
        return self._headers

    @headers.setter
    def headers(self, val):
        """Set headers
        Keyword argument:
        val -- New headers value"""
        self._headers = val
        return self
    
    @property
    def body(self):
        """Get body"""
        return self._body

    @body.setter
    def body(self, val):
        """Set body
        Keyword argument:
        val -- New body value"""
        self._body = val
        return self
    
    @property
    def response_code(self):
        """Get response_code"""
        return self._response_code

    @response_code.setter
    def response_code(self, val):
        """Set response_code
        Keyword argument:
        val -- New response_code value"""
        self._response_code = val
        return self
    
    @property
    def response_headers(self):
        """Get response_headers"""
        return self._response_headers

    @response_headers.setter
    def response_headers(self, val):
        """Set response_headers
        Keyword argument:
        val -- New response_headers value"""
        self._response_headers = val
        return self
    
    @property
    def response_body(self):
        """Get response_body"""
        return self._response_body

    @response_body.setter
    def response_body(self, val):
        """Set response_body
        Keyword argument:
        val -- New response_body value"""
        self._response_body = val
        return self
    
    @property
    def response_ms(self):
        """Get response_ms"""
        return self._response_ms

    @response_ms.setter
    def response_ms(self, val):
        """Set response_ms
        Keyword argument:
        val -- New response_ms value"""
        self._response_ms = val
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
        if "api_version" in data.keys():
            self.api_version = data["api_version"]
        if "idempotency_key" in data.keys():
            self.idempotency_key = data["idempotency_key"]
        if "url" in data.keys():
            self.url = data["url"]
        if "method" in data.keys():
            self.method = data["method"]
        if "headers" in data.keys():
            self.headers = data["headers"]
        if "body" in data.keys():
            self.body = data["body"]
        if "response_code" in data.keys():
            self.response_code = data["response_code"]
        if "response_headers" in data.keys():
            self.response_headers = data["response_headers"]
        if "response_body" in data.keys():
            self.response_body = data["response_body"]
        if "response_ms" in data.keys():
            self.response_ms = data["response_ms"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        
        return self

    def all(self, options = {}):
        """Get all the API requests.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/api-requests"
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        a    = []
        body = response.body
        for v in body['api_requests']:
            tmp = processout.APIRequest(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)
            

        
        return return_values[0]

    def find(self, api_request_id, options = {}):
        """Find an API request by its ID.
        Keyword argument:
        api_request_id -- ID of the API request
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/api-requests/{request_id}"
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        body = response.body
        body = body["api_request"]
                
                
        obj = processout.APIRequest(self._client)
        return_values.append(obj.fill_with_data(body))
                

        
        return return_values[0]

    

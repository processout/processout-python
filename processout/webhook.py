try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Webhook(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = None
        self._project = None
        self._project_id = None
        self._event = None
        self._event_id = None
        self._request_url = None
        self._request_method = None
        self._response_body = None
        self._response_code = None
        self._response_headers = None
        self._response_time_ms = None
        self._status = None
        self._created_at = None
        self._release_at = None
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
    def event(self):
        """Get event"""
        return self._event

    @event.setter
    def event(self, val):
        """Set event
        Keyword argument:
        val -- New event value"""
        if val is None:
            self._event = val
            return self

        if isinstance(val, dict):
            obj = processout.Event(self._client)
            obj.fill_with_data(val)
            self._event = obj
        else:
            self._event = val
        return self
    
    @property
    def event_id(self):
        """Get event_id"""
        return self._event_id

    @event_id.setter
    def event_id(self, val):
        """Set event_id
        Keyword argument:
        val -- New event_id value"""
        self._event_id = val
        return self
    
    @property
    def request_url(self):
        """Get request_url"""
        return self._request_url

    @request_url.setter
    def request_url(self, val):
        """Set request_url
        Keyword argument:
        val -- New request_url value"""
        self._request_url = val
        return self
    
    @property
    def request_method(self):
        """Get request_method"""
        return self._request_method

    @request_method.setter
    def request_method(self, val):
        """Set request_method
        Keyword argument:
        val -- New request_method value"""
        self._request_method = val
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
    def response_time_ms(self):
        """Get response_time_ms"""
        return self._response_time_ms

    @response_time_ms.setter
    def response_time_ms(self, val):
        """Set response_time_ms
        Keyword argument:
        val -- New response_time_ms value"""
        self._response_time_ms = val
        return self
    
    @property
    def status(self):
        """Get status"""
        return self._status

    @status.setter
    def status(self, val):
        """Set status
        Keyword argument:
        val -- New status value"""
        self._status = val
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
    
    @property
    def release_at(self):
        """Get release_at"""
        return self._release_at

    @release_at.setter
    def release_at(self, val):
        """Set release_at
        Keyword argument:
        val -- New release_at value"""
        self._release_at = val
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
        if "event" in data.keys():
            self.event = data["event"]
        if "event_id" in data.keys():
            self.event_id = data["event_id"]
        if "request_url" in data.keys():
            self.request_url = data["request_url"]
        if "request_method" in data.keys():
            self.request_method = data["request_method"]
        if "response_body" in data.keys():
            self.response_body = data["response_body"]
        if "response_code" in data.keys():
            self.response_code = data["response_code"]
        if "response_headers" in data.keys():
            self.response_headers = data["response_headers"]
        if "response_time_ms" in data.keys():
            self.response_time_ms = data["response_time_ms"]
        if "status" in data.keys():
            self.status = data["status"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        if "release_at" in data.keys():
            self.release_at = data["release_at"]
        
        return self

    

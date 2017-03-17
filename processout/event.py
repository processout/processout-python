try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Event(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = None
        self._project = None
        self._project_id = None
        self._name = None
        self._data = None
        self._sandbox = None
        self._fired_at = None
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
    def data(self):
        """Get data"""
        return self._data

    @data.setter
    def data(self, val):
        """Set data
        Keyword argument:
        val -- New data value"""
        self._data = val
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
    def fired_at(self):
        """Get fired_at"""
        return self._fired_at

    @fired_at.setter
    def fired_at(self, val):
        """Set fired_at
        Keyword argument:
        val -- New fired_at value"""
        self._fired_at = val
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
        if "name" in data.keys():
            self.name = data["name"]
        if "data" in data.keys():
            self.data = data["data"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "fired_at" in data.keys():
            self.fired_at = data["fired_at"]
        
        return self

    def fetch_webhooks(self, options = {}):
        """Get all the webhooks of the event.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/events/" + quote_plus(self.id) + "/webhooks"
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        a    = []
        body = response.body
        for v in body['webhooks']:
            tmp = processout.Webhook(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)
            

        
        return return_values[0]

    def all(self, options = {}):
        """Get all the events.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/events"
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        a    = []
        body = response.body
        for v in body['events']:
            tmp = processout.Event(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)
            

        
        return return_values[0]

    def find(self, event_id, options = {}):
        """Find an event by its ID.
        Keyword argument:
        event_id -- ID of the event
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/events/" + quote_plus(event_id) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        body = response.body
        body = body["event"]
                
                
        obj = processout.Event(self._client)
        return_values.append(obj.fill_with_data(body))
                

        
        return return_values[0]

    

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Event:
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = ""
        self._project = None
        self._name = ""
        self._data = None
        self._sandbox = False
        self._firedAt = ""
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
    def firedAt(self):
        """Get firedAt"""
        return self._firedAt

    @firedAt.setter
    def firedAt(self, val):
        """Set firedAt
        Keyword argument:
        val -- New firedAt value"""
        self._firedAt = val
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
        if "data" in data.keys():
            self.data = data["data"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "fired_at" in data.keys():
            self.firedAt = data["fired_at"]
        
        return self

    def fetchWebhooks(self, options = None):
        """Get all the webhooks of the event.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/events/" + quote_plus(self.id) + "/webhooks"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        a    = []
        body = response.body
        for v in body['webhooks']:
            tmp = Webhook(self._client)
            tmp.fillWithData(v)
            a.append(tmp)

        returnValues.append(a)
            

        
        return returnValues[0];

    def all(self, options = None):
        """Get all the events.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/events"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        a    = []
        body = response.body
        for v in body['events']:
            tmp = Event(self._client)
            tmp.fillWithData(v)
            a.append(tmp)

        returnValues.append(a)
            

        
        return returnValues[0];

    def find(self, eventId, options = None):
        """Find an event by its ID.
        Keyword argument:
        eventId -- ID of the event
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/events/" + quote_plus(eventId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["event"]
                
                
        obj = processout.Event(self._client)
        returnValues.append(obj.fillWithData(body))
                

        
        return returnValues[0];

    

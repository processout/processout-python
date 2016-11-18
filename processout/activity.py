try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Activity(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = ""
        self._project = None
        self._title = ""
        self._content = ""
        self._level = 0
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
    def title(self):
        """Get title"""
        return self._title

    @title.setter
    def title(self, val):
        """Set title
        Keyword argument:
        val -- New title value"""
        self._title = val
        return self
    
    @property
    def content(self):
        """Get content"""
        return self._content

    @content.setter
    def content(self, val):
        """Set content
        Keyword argument:
        val -- New content value"""
        self._content = val
        return self
    
    @property
    def level(self):
        """Get level"""
        return self._level

    @level.setter
    def level(self, val):
        """Set level
        Keyword argument:
        val -- New level value"""
        self._level = val
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
        if "title" in data.keys():
            self.title = data["title"]
        if "content" in data.keys():
            self.content = data["content"]
        if "level" in data.keys():
            self.level = data["level"]
        if "created_at" in data.keys():
            self.createdAt = data["created_at"]
        
        return self

    def all(self, options = None):
        """Get all the project activities.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/activities"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        a    = []
        body = response.body
        for v in body['activities']:
            tmp = Activity(self._client)
            tmp.fillWithData(v)
            a.append(tmp)

        returnValues.append(a)
            

        
        return returnValues[0];

    def find(self, activityId, options = None):
        """Find a specific activity and fetch its data.
        Keyword argument:
        activityId -- ID of the activity
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/activities/" + quote_plus(activityId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["activity"]
                
                
        obj = processout.Activity(self._client)
        returnValues.append(obj.fillWithData(body))
                

        
        return returnValues[0];

    

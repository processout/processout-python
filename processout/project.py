try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Project:
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = ""
        self._name = ""
        self._logoUrl = ""
        self._email = ""
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
    def logoUrl(self):
        """Get logoUrl"""
        return self._logoUrl

    @logoUrl.setter
    def logoUrl(self, val):
        """Set logoUrl
        Keyword argument:
        val -- New logoUrl value"""
        self._logoUrl = val
        return self
    
    @property
    def email(self):
        """Get email"""
        return self._email

    @email.setter
    def email(self, val):
        """Set email
        Keyword argument:
        val -- New email value"""
        self._email = val
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
        if "name" in data.keys():
            self.name = data["name"]
        if "logo_url" in data.keys():
            self.logoUrl = data["logo_url"]
        if "email" in data.keys():
            self.email = data["email"]
        if "created_at" in data.keys():
            self.createdAt = data["created_at"]
        
        return self

    def fetchGatewayConfigurations(self, options = None):
        """Get all the gateway configurations of the project
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/projects/" + quote_plus(self.id) + "/gateway-configurations"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        a    = []
        body = response.body
        for v in body['gateway_configurations']:
            tmp = GatewayConfiguration(self._client)
            tmp.fillWithData(v)
            a.append(tmp)

        returnValues.append(a)
            

        
        return returnValues[0];

    

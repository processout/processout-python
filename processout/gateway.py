try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Gateway(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = None
        self._name = None
        self._display_name = None
        self._logo_url = None
        self._url = None
        self._flows = None
        self._tags = None
        self._description = None
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
    def display_name(self):
        """Get display_name"""
        return self._display_name

    @display_name.setter
    def display_name(self, val):
        """Set display_name
        Keyword argument:
        val -- New display_name value"""
        self._display_name = val
        return self
    
    @property
    def logo_url(self):
        """Get logo_url"""
        return self._logo_url

    @logo_url.setter
    def logo_url(self, val):
        """Set logo_url
        Keyword argument:
        val -- New logo_url value"""
        self._logo_url = val
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
    def flows(self):
        """Get flows"""
        return self._flows

    @flows.setter
    def flows(self, val):
        """Set flows
        Keyword argument:
        val -- New flows value"""
        self._flows = val
        return self
    
    @property
    def tags(self):
        """Get tags"""
        return self._tags

    @tags.setter
    def tags(self, val):
        """Set tags
        Keyword argument:
        val -- New tags value"""
        self._tags = val
        return self
    
    @property
    def description(self):
        """Get description"""
        return self._description

    @description.setter
    def description(self, val):
        """Set description
        Keyword argument:
        val -- New description value"""
        self._description = val
        return self
    

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "id" in data.keys():
            self.id = data["id"]
        if "name" in data.keys():
            self.name = data["name"]
        if "display_name" in data.keys():
            self.display_name = data["display_name"]
        if "logo_url" in data.keys():
            self.logo_url = data["logo_url"]
        if "url" in data.keys():
            self.url = data["url"]
        if "flows" in data.keys():
            self.flows = data["flows"]
        if "tags" in data.keys():
            self.tags = data["tags"]
        if "description" in data.keys():
            self.description = data["description"]
        
        return self

    

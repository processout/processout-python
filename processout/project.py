try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Project(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = None
        self._supervisor_project = None
        self._supervisor_project_id = None
        self._api_version = None
        self._name = None
        self._logo_url = None
        self._email = None
        self._default_currency = None
        self._private_key = None
        self._dunning_configuration = None
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
    def supervisor_project(self):
        """Get supervisor_project"""
        return self._supervisor_project

    @supervisor_project.setter
    def supervisor_project(self, val):
        """Set supervisor_project
        Keyword argument:
        val -- New supervisor_project value"""
        if val is None:
            self._supervisor_project = val
            return self

        if isinstance(val, dict):
            obj = processout.Project(self._client)
            obj.fill_with_data(val)
            self._supervisor_project = obj
        else:
            self._supervisor_project = val
        return self
    
    @property
    def supervisor_project_id(self):
        """Get supervisor_project_id"""
        return self._supervisor_project_id

    @supervisor_project_id.setter
    def supervisor_project_id(self, val):
        """Set supervisor_project_id
        Keyword argument:
        val -- New supervisor_project_id value"""
        self._supervisor_project_id = val
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
    def default_currency(self):
        """Get default_currency"""
        return self._default_currency

    @default_currency.setter
    def default_currency(self, val):
        """Set default_currency
        Keyword argument:
        val -- New default_currency value"""
        self._default_currency = val
        return self
    
    @property
    def private_key(self):
        """Get private_key"""
        return self._private_key

    @private_key.setter
    def private_key(self, val):
        """Set private_key
        Keyword argument:
        val -- New private_key value"""
        self._private_key = val
        return self
    
    @property
    def dunning_configuration(self):
        """Get dunning_configuration"""
        return self._dunning_configuration

    @dunning_configuration.setter
    def dunning_configuration(self, val):
        """Set dunning_configuration
        Keyword argument:
        val -- New dunning_configuration value"""
        if val is None:
            self._dunning_configuration = []
            return self

        if len(val) > 0 and isinstance(val[0], processout.DunningAction):
            self._dunning_configuration = val
        else:
            l = []
            for v in val:
                obj = processout.DunningAction(self._client)
                obj.fill_with_data(v)
                l.append(obj)
            self._dunning_configuration = l
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
        if "supervisor_project" in data.keys():
            self.supervisor_project = data["supervisor_project"]
        if "supervisor_project_id" in data.keys():
            self.supervisor_project_id = data["supervisor_project_id"]
        if "api_version" in data.keys():
            self.api_version = data["api_version"]
        if "name" in data.keys():
            self.name = data["name"]
        if "logo_url" in data.keys():
            self.logo_url = data["logo_url"]
        if "email" in data.keys():
            self.email = data["email"]
        if "default_currency" in data.keys():
            self.default_currency = data["default_currency"]
        if "private_key" in data.keys():
            self.private_key = data["private_key"]
        if "dunning_configuration" in data.keys():
            self.dunning_configuration = data["dunning_configuration"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        
        return self

    def fetch_gateway_configurations(self, options = {}):
        """Get all the gateway configurations of the project
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/projects/" + quote_plus(self.id) + "/gateway-configurations"
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        a    = []
        body = response.body
        for v in body['gateway_configurations']:
            tmp = processout.GatewayConfiguration(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)
            

        
        return return_values[0]

    

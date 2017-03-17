try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class GatewayConfiguration(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = None
        self._project = None
        self._project_id = None
        self._gateway = None
        self._gateway_id = None
        self._name = None
        self._fee_fixed = None
        self._fee_percentage = None
        self._default_currency = None
        self._enabled = None
        self._public_keys = None
        self._created_at = None
        self._enabled_at = None
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
    def gateway(self):
        """Get gateway"""
        return self._gateway

    @gateway.setter
    def gateway(self, val):
        """Set gateway
        Keyword argument:
        val -- New gateway value"""
        if val is None:
            self._gateway = val
            return self

        if isinstance(val, dict):
            obj = processout.Gateway(self._client)
            obj.fill_with_data(val)
            self._gateway = obj
        else:
            self._gateway = val
        return self
    
    @property
    def gateway_id(self):
        """Get gateway_id"""
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, val):
        """Set gateway_id
        Keyword argument:
        val -- New gateway_id value"""
        self._gateway_id = val
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
    def fee_fixed(self):
        """Get fee_fixed"""
        return self._fee_fixed

    @fee_fixed.setter
    def fee_fixed(self, val):
        """Set fee_fixed
        Keyword argument:
        val -- New fee_fixed value"""
        self._fee_fixed = val
        return self
    
    @property
    def fee_percentage(self):
        """Get fee_percentage"""
        return self._fee_percentage

    @fee_percentage.setter
    def fee_percentage(self, val):
        """Set fee_percentage
        Keyword argument:
        val -- New fee_percentage value"""
        self._fee_percentage = val
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
    def enabled(self):
        """Get enabled"""
        return self._enabled

    @enabled.setter
    def enabled(self, val):
        """Set enabled
        Keyword argument:
        val -- New enabled value"""
        self._enabled = val
        return self
    
    @property
    def public_keys(self):
        """Get public_keys"""
        return self._public_keys

    @public_keys.setter
    def public_keys(self, val):
        """Set public_keys
        Keyword argument:
        val -- New public_keys value"""
        self._public_keys = val
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
    def enabled_at(self):
        """Get enabled_at"""
        return self._enabled_at

    @enabled_at.setter
    def enabled_at(self, val):
        """Set enabled_at
        Keyword argument:
        val -- New enabled_at value"""
        self._enabled_at = val
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
        if "gateway" in data.keys():
            self.gateway = data["gateway"]
        if "gateway_id" in data.keys():
            self.gateway_id = data["gateway_id"]
        if "name" in data.keys():
            self.name = data["name"]
        if "fee_fixed" in data.keys():
            self.fee_fixed = data["fee_fixed"]
        if "fee_percentage" in data.keys():
            self.fee_percentage = data["fee_percentage"]
        if "default_currency" in data.keys():
            self.default_currency = data["default_currency"]
        if "enabled" in data.keys():
            self.enabled = data["enabled"]
        if "public_keys" in data.keys():
            self.public_keys = data["public_keys"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        if "enabled_at" in data.keys():
            self.enabled_at = data["enabled_at"]
        
        return self

    

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class GatewayConfiguration(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._id = None
        self._project = None
        self._project_id = None
        self._gateway = None
        self._gateway_id = None
        self._name = None
        self._default_currency = None
        self._enabled = None
        self._public_keys = None
        self._created_at = None
        self._enabled_at = None
        if prefill is not None:
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

    def to_json(self):
        return {
            "id": self.id,
            "project": self.project,
            "project_id": self.project_id,
            "gateway": self.gateway,
            "gateway_id": self.gateway_id,
            "name": self.name,
            "default_currency": self.default_currency,
            "enabled": self.enabled,
            "public_keys": self.public_keys,
            "created_at": self.created_at,
            "enabled_at": self.enabled_at,
        }

    def all(self, options={}):
        """Get all the gateway configurations.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/gateway-configurations"
        data = {
            'expand_merchant_accounts': options.get("expand_merchant_accounts")
        }

        response = Response(request.get(path, data, options))
        return_values = []

        a = []
        body = response.body
        for v in body['gateway_configurations']:
            tmp = processout.GatewayConfiguration(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)

        return return_values[0]

    def find(self, configuration_id, options={}):
        """Find a gateway configuration by its ID.
        Keyword argument:
        configuration_id -- ID of the gateway configuration
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/gateway-configurations/" + quote_plus(configuration_id) + ""
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        body = response.body
        body = body["gateway_configuration"]

        obj = processout.GatewayConfiguration(self._client)
        return_values.append(obj.fill_with_data(body))

        return return_values[0]

    def save(self, options={}):
        """Save the updated gateway configuration attributes and settings.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/gateway-configurations/" + quote_plus(self.id) + ""
        data = {
            'id': self.id,
            'name': self.name,
            'enabled': self.enabled,
            'default_currency': self.default_currency,
            'settings': options.get("settings"),
            'sub_accounts_enabled': options.get("sub_accounts_enabled")
        }

        response = Response(request.put(path, data, options))
        return_values = []

        body = response.body
        body = body["gateway_configuration"]

        return_values.append(self.fill_with_data(body))

        return return_values[0]

    def delete(self, options={}):
        """Delete the gateway configuration.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/gateway-configurations/" + quote_plus(self.id) + ""
        data = {

        }

        response = Response(request.delete(path, data, options))
        return_values = []

        return_values.append(response.success)

        return return_values[0]

    def create(self, gateway_name, options={}):
        """Create a new gateway configuration.
        Keyword argument:
        gateway_name -- Name of the gateway
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/gateways/" + \
            quote_plus(gateway_name) + "/gateway-configurations"
        data = {
            'id': self.id,
            'name': self.name,
            'enabled': self.enabled,
            'default_currency': self.default_currency,
            'settings': options.get("settings"),
            'sub_accounts_enabled': options.get("sub_accounts_enabled")
        }

        response = Response(request.post(path, data, options))
        return_values = []

        body = response.body
        body = body["gateway_configuration"]

        return_values.append(self.fill_with_data(body))

        return return_values[0]

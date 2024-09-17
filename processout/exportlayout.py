try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class ExportLayout(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._id = None
        self._project = None
        self._project_id = None
        self._created_at = None
        self._name = None
        self._type = None
        self._is_default = None
        self._configuration = None
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
    def type(self):
        """Get type"""
        return self._type

    @type.setter
    def type(self, val):
        """Set type
        Keyword argument:
        val -- New type value"""
        self._type = val
        return self

    @property
    def is_default(self):
        """Get is_default"""
        return self._is_default

    @is_default.setter
    def is_default(self, val):
        """Set is_default
        Keyword argument:
        val -- New is_default value"""
        self._is_default = val
        return self

    @property
    def configuration(self):
        """Get configuration"""
        return self._configuration

    @configuration.setter
    def configuration(self, val):
        """Set configuration
        Keyword argument:
        val -- New configuration value"""
        if val is None:
            self._configuration = val
            return self

        if isinstance(val, dict):
            obj = processout.ExportLayoutConfiguration(self._client)
            obj.fill_with_data(val)
            self._configuration = obj
        else:
            self._configuration = val
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
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        if "name" in data.keys():
            self.name = data["name"]
        if "type" in data.keys():
            self.type = data["type"]
        if "is_default" in data.keys():
            self.is_default = data["is_default"]
        if "configuration" in data.keys():
            self.configuration = data["configuration"]

        return self

    def to_json(self):
        return {
            "id": self.id,
            "project": self.project,
            "project_id": self.project_id,
            "created_at": self.created_at,
            "name": self.name,
            "type": self.type,
            "is_default": self.is_default,
            "configuration": self.configuration,
        }

    def all(self, options={}):
        """Get all the export layouts.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/exports/layouts"
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        a = []
        body = response.body
        for v in body['export_layouts']:
            tmp = processout.ExportLayout(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)

        return return_values[0]

    def find(self, export_layout_id, options={}):
        """Find an export layout by its ID.
        Keyword argument:
        export_layout_id -- ID of the export layout
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/exports/layouts/" + quote_plus(export_layout_id) + ""
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        body = response.body
        body = body["export_layout"]

        obj = processout.ExportLayout(self._client)
        return_values.append(obj.fill_with_data(body))

        return return_values[0]

    def find_default(self, export_type, options={}):
        """Find the default export layout for given export type.
        Keyword argument:
        export_type -- Export type for which the default layout is assigned.
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/exports/layouts/default/" + quote_plus(export_type) + ""
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        body = response.body
        body = body["export_layout"]

        obj = processout.ExportLayout(self._client)
        return_values.append(obj.fill_with_data(body))

        return return_values[0]

    def create(self, options={}):
        """Create a new export layout.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/exports/layouts"
        data = {
            'name': self.name,
            'type': self.type,
            'is_default': self.is_default,
            'configuration': self.configuration
        }

        response = Response(request.post(path, data, options))
        return_values = []

        body = response.body
        body = body["export_layout"]

        return_values.append(self.fill_with_data(body))

        return return_values[0]

    def update(self, export_layout_id, options={}):
        """Update the export layout.
        Keyword argument:
        export_layout_id -- ID of the export layout
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/exports/layouts/" + quote_plus(export_layout_id) + ""
        data = {
            'name': self.name,
            'is_default': self.is_default,
            'configuration': self.configuration
        }

        response = Response(request.put(path, data, options))
        return_values = []

        body = response.body
        body = body["export_layout"]

        return_values.append(self.fill_with_data(body))

        return return_values[0]

    def delete(self, export_layout_id, options={}):
        """Delete the export layout.
        Keyword argument:
        export_layout_id -- ID of the export layout
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/exports/layouts/" + quote_plus(export_layout_id) + ""
        data = {

        }

        response = Response(request.delete(path, data, options))
        return_values = []

        return_values.append(response.success)

        return return_values[0]

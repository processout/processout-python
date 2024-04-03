try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class ProjectSFTPSettingsPublic(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._enabled = None
        self._endpoint = None
        self._username = None
        if prefill is not None:
            self.fill_with_data(prefill)

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
    def endpoint(self):
        """Get endpoint"""
        return self._endpoint

    @endpoint.setter
    def endpoint(self, val):
        """Set endpoint
        Keyword argument:
        val -- New endpoint value"""
        self._endpoint = val
        return self

    @property
    def username(self):
        """Get username"""
        return self._username

    @username.setter
    def username(self, val):
        """Set username
        Keyword argument:
        val -- New username value"""
        self._username = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "enabled" in data.keys():
            self.enabled = data["enabled"]
        if "endpoint" in data.keys():
            self.endpoint = data["endpoint"]
        if "username" in data.keys():
            self.username = data["username"]

        return self

    def to_json(self):
        return {
            "enabled": self.enabled,
            "endpoint": self.endpoint,
            "username": self.username,
        }

    def fetch_sftp_settings(self, id, options={}):
        """Fetch the SFTP settings for the project.
        Keyword argument:
        id -- ID of the project
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/projects/" + quote_plus(id) + "/sftp-settings"
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        body = response.body
        body = body["sftp_settings"]

        obj = processout.ProjectSFTPSettingsPublic(self._client)
        return_values.append(obj.fill_with_data(body))

        return return_values[0]

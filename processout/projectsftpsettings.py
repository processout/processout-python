try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class ProjectSFTPSettings(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._endpoint = None
        self._username = None
        self._password = None
        self._private_key = None
        if prefill is not None:
            self.fill_with_data(prefill)

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

    @property
    def password(self):
        """Get password"""
        return self._password

    @password.setter
    def password(self, val):
        """Set password
        Keyword argument:
        val -- New password value"""
        self._password = val
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

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "endpoint" in data.keys():
            self.endpoint = data["endpoint"]
        if "username" in data.keys():
            self.username = data["username"]
        if "password" in data.keys():
            self.password = data["password"]
        if "private_key" in data.keys():
            self.private_key = data["private_key"]

        return self

    def to_json(self):
        return {
            "endpoint": self.endpoint,
            "username": self.username,
            "password": self.password,
            "private_key": self.private_key,
        }

    def save_sftp_settings(self, id, options={}):
        """Save the SFTP settings for the project.
        Keyword argument:
        id -- ID of the project
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/projects/" + quote_plus(id) + "/sftp-settings"
        data = {
            'endpoint': self.endpoint,
            'username': self.username,
            'password': self.password,
            'private_key': self.private_key
        }

        response = Response(request.put(path, data, options))
        return_values = []

        return_values.append(response.success)

        return return_values[0]

    def delete_sftp_settings(self, id, options={}):
        """Delete the SFTP settings for the project.
        Keyword argument:
        id -- ID of the project
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/projects/" + quote_plus(id) + "/sftp-settings"
        data = {

        }

        response = Response(request.delete(path, data, options))
        return_values = []

        return_values.append(response.success)

        return return_values[0]

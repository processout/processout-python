try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class Activity(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._id = None
        self._project = None
        self._project_id = None
        self._title = None
        self._content = None
        self._level = None
        self._created_at = None
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
        if "project" in data.keys():
            self.project = data["project"]
        if "project_id" in data.keys():
            self.project_id = data["project_id"]
        if "title" in data.keys():
            self.title = data["title"]
        if "content" in data.keys():
            self.content = data["content"]
        if "level" in data.keys():
            self.level = data["level"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]

        return self

    def to_json(self):
        return {
            "id": self.id,
            "project": self.project,
            "project_id": self.project_id,
            "title": self.title,
            "content": self.content,
            "level": self.level,
            "created_at": self.created_at,
        }

    def all(self, options={}):
        """Get all the project activities.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/activities"
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        a = []
        body = response.body
        for v in body['activities']:
            tmp = processout.Activity(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)

        return return_values[0]

    def find(self, activity_id, options={}):
        """Find a specific activity and fetch its data.
        Keyword argument:
        activity_id -- ID of the activity
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/activities/" + quote_plus(activity_id) + ""
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        body = response.body
        body = body["activity"]

        obj = processout.Activity(self._client)
        return_values.append(obj.fill_with_data(body))

        return return_values[0]

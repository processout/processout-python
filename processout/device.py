try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class Device(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._request_origin = None
        self._id = None
        self._channel = None
        self._ip_address = None
        self._user_agent = None
        self._header_accept = None
        self._header_referer = None
        self._app_color_depth = None
        self._app_java_enabled = None
        self._app_language = None
        self._app_screen_height = None
        self._app_screen_width = None
        self._app_timezone_offset = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def request_origin(self):
        """Get request_origin"""
        return self._request_origin

    @request_origin.setter
    def request_origin(self, val):
        """Set request_origin
        Keyword argument:
        val -- New request_origin value"""
        self._request_origin = val
        return self

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
    def channel(self):
        """Get channel"""
        return self._channel

    @channel.setter
    def channel(self, val):
        """Set channel
        Keyword argument:
        val -- New channel value"""
        self._channel = val
        return self

    @property
    def ip_address(self):
        """Get ip_address"""
        return self._ip_address

    @ip_address.setter
    def ip_address(self, val):
        """Set ip_address
        Keyword argument:
        val -- New ip_address value"""
        self._ip_address = val
        return self

    @property
    def user_agent(self):
        """Get user_agent"""
        return self._user_agent

    @user_agent.setter
    def user_agent(self, val):
        """Set user_agent
        Keyword argument:
        val -- New user_agent value"""
        self._user_agent = val
        return self

    @property
    def header_accept(self):
        """Get header_accept"""
        return self._header_accept

    @header_accept.setter
    def header_accept(self, val):
        """Set header_accept
        Keyword argument:
        val -- New header_accept value"""
        self._header_accept = val
        return self

    @property
    def header_referer(self):
        """Get header_referer"""
        return self._header_referer

    @header_referer.setter
    def header_referer(self, val):
        """Set header_referer
        Keyword argument:
        val -- New header_referer value"""
        self._header_referer = val
        return self

    @property
    def app_color_depth(self):
        """Get app_color_depth"""
        return self._app_color_depth

    @app_color_depth.setter
    def app_color_depth(self, val):
        """Set app_color_depth
        Keyword argument:
        val -- New app_color_depth value"""
        self._app_color_depth = val
        return self

    @property
    def app_java_enabled(self):
        """Get app_java_enabled"""
        return self._app_java_enabled

    @app_java_enabled.setter
    def app_java_enabled(self, val):
        """Set app_java_enabled
        Keyword argument:
        val -- New app_java_enabled value"""
        self._app_java_enabled = val
        return self

    @property
    def app_language(self):
        """Get app_language"""
        return self._app_language

    @app_language.setter
    def app_language(self, val):
        """Set app_language
        Keyword argument:
        val -- New app_language value"""
        self._app_language = val
        return self

    @property
    def app_screen_height(self):
        """Get app_screen_height"""
        return self._app_screen_height

    @app_screen_height.setter
    def app_screen_height(self, val):
        """Set app_screen_height
        Keyword argument:
        val -- New app_screen_height value"""
        self._app_screen_height = val
        return self

    @property
    def app_screen_width(self):
        """Get app_screen_width"""
        return self._app_screen_width

    @app_screen_width.setter
    def app_screen_width(self, val):
        """Set app_screen_width
        Keyword argument:
        val -- New app_screen_width value"""
        self._app_screen_width = val
        return self

    @property
    def app_timezone_offset(self):
        """Get app_timezone_offset"""
        return self._app_timezone_offset

    @app_timezone_offset.setter
    def app_timezone_offset(self, val):
        """Set app_timezone_offset
        Keyword argument:
        val -- New app_timezone_offset value"""
        self._app_timezone_offset = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "request_origin" in data.keys():
            self.request_origin = data["request_origin"]
        if "id" in data.keys():
            self.id = data["id"]
        if "channel" in data.keys():
            self.channel = data["channel"]
        if "ip_address" in data.keys():
            self.ip_address = data["ip_address"]
        if "user_agent" in data.keys():
            self.user_agent = data["user_agent"]
        if "header_accept" in data.keys():
            self.header_accept = data["header_accept"]
        if "header_referer" in data.keys():
            self.header_referer = data["header_referer"]
        if "app_color_depth" in data.keys():
            self.app_color_depth = data["app_color_depth"]
        if "app_java_enabled" in data.keys():
            self.app_java_enabled = data["app_java_enabled"]
        if "app_language" in data.keys():
            self.app_language = data["app_language"]
        if "app_screen_height" in data.keys():
            self.app_screen_height = data["app_screen_height"]
        if "app_screen_width" in data.keys():
            self.app_screen_width = data["app_screen_width"]
        if "app_timezone_offset" in data.keys():
            self.app_timezone_offset = data["app_timezone_offset"]

        return self

    def to_json(self):
        return {
            "request_origin": self.request_origin,
            "id": self.id,
            "channel": self.channel,
            "ip_address": self.ip_address,
            "user_agent": self.user_agent,
            "header_accept": self.header_accept,
            "header_referer": self.header_referer,
            "app_color_depth": self.app_color_depth,
            "app_java_enabled": self.app_java_enabled,
            "app_language": self.app_language,
            "app_screen_height": self.app_screen_height,
            "app_screen_width": self.app_screen_width,
            "app_timezone_offset": self.app_timezone_offset,
        }

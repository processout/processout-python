try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class SubmerchantAddress(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._line1 = None
        self._line2 = None
        self._city = None
        self._state = None
        self._country_code = None
        self._zip = None
        self._county = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def line1(self):
        """Get line1"""
        return self._line1

    @line1.setter
    def line1(self, val):
        """Set line1
        Keyword argument:
        val -- New line1 value"""
        self._line1 = val
        return self

    @property
    def line2(self):
        """Get line2"""
        return self._line2

    @line2.setter
    def line2(self, val):
        """Set line2
        Keyword argument:
        val -- New line2 value"""
        self._line2 = val
        return self

    @property
    def city(self):
        """Get city"""
        return self._city

    @city.setter
    def city(self, val):
        """Set city
        Keyword argument:
        val -- New city value"""
        self._city = val
        return self

    @property
    def state(self):
        """Get state"""
        return self._state

    @state.setter
    def state(self, val):
        """Set state
        Keyword argument:
        val -- New state value"""
        self._state = val
        return self

    @property
    def country_code(self):
        """Get country_code"""
        return self._country_code

    @country_code.setter
    def country_code(self, val):
        """Set country_code
        Keyword argument:
        val -- New country_code value"""
        self._country_code = val
        return self

    @property
    def zip(self):
        """Get zip"""
        return self._zip

    @zip.setter
    def zip(self, val):
        """Set zip
        Keyword argument:
        val -- New zip value"""
        self._zip = val
        return self

    @property
    def county(self):
        """Get county"""
        return self._county

    @county.setter
    def county(self, val):
        """Set county
        Keyword argument:
        val -- New county value"""
        self._county = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "line1" in data.keys():
            self.line1 = data["line1"]
        if "line2" in data.keys():
            self.line2 = data["line2"]
        if "city" in data.keys():
            self.city = data["city"]
        if "state" in data.keys():
            self.state = data["state"]
        if "country_code" in data.keys():
            self.country_code = data["country_code"]
        if "zip" in data.keys():
            self.zip = data["zip"]
        if "county" in data.keys():
            self.county = data["county"]

        return self

    def to_json(self):
        return {
            "line1": self.line1,
            "line2": self.line2,
            "city": self.city,
            "state": self.state,
            "country_code": self.country_code,
            "zip": self.zip,
            "county": self.county,
        }

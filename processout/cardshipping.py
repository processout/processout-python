try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class CardShipping(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._address1 = None
        self._address2 = None
        self._city = None
        self._state = None
        self._country_code = None
        self._zip = None
        self._phone = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def address1(self):
        """Get address1"""
        return self._address1

    @address1.setter
    def address1(self, val):
        """Set address1
        Keyword argument:
        val -- New address1 value"""
        self._address1 = val
        return self

    @property
    def address2(self):
        """Get address2"""
        return self._address2

    @address2.setter
    def address2(self, val):
        """Set address2
        Keyword argument:
        val -- New address2 value"""
        self._address2 = val
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
    def phone(self):
        """Get phone"""
        return self._phone

    @phone.setter
    def phone(self, val):
        """Set phone
        Keyword argument:
        val -- New phone value"""
        if val is None:
            self._phone = val
            return self

        if isinstance(val, dict):
            obj = processout.Phone(self._client)
            obj.fill_with_data(val)
            self._phone = obj
        else:
            self._phone = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "address1" in data.keys():
            self.address1 = data["address1"]
        if "address2" in data.keys():
            self.address2 = data["address2"]
        if "city" in data.keys():
            self.city = data["city"]
        if "state" in data.keys():
            self.state = data["state"]
        if "country_code" in data.keys():
            self.country_code = data["country_code"]
        if "zip" in data.keys():
            self.zip = data["zip"]
        if "phone" in data.keys():
            self.phone = data["phone"]

        return self

    def to_json(self):
        return {
            "address1": self.address1,
            "address2": self.address2,
            "city": self.city,
            "state": self.state,
            "country_code": self.country_code,
            "zip": self.zip,
            "phone": self.phone,
        }

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class SubmerchantPhoneNumber(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._dialing_code = None
        self._number = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def dialing_code(self):
        """Get dialing_code"""
        return self._dialing_code

    @dialing_code.setter
    def dialing_code(self, val):
        """Set dialing_code
        Keyword argument:
        val -- New dialing_code value"""
        self._dialing_code = val
        return self

    @property
    def number(self):
        """Get number"""
        return self._number

    @number.setter
    def number(self, val):
        """Set number
        Keyword argument:
        val -- New number value"""
        self._number = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "dialing_code" in data.keys():
            self.dialing_code = data["dialing_code"]
        if "number" in data.keys():
            self.number = data["number"]

        return self

    def to_json(self):
        return {
            "dialing_code": self.dialing_code,
            "number": self.number,
        }

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class CardInformation(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._iin = None
        self._scheme = None
        self._type = None
        self._bank_name = None
        self._brand = None
        self._category = None
        self._country = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def iin(self):
        """Get iin"""
        return self._iin

    @iin.setter
    def iin(self, val):
        """Set iin
        Keyword argument:
        val -- New iin value"""
        self._iin = val
        return self

    @property
    def scheme(self):
        """Get scheme"""
        return self._scheme

    @scheme.setter
    def scheme(self, val):
        """Set scheme
        Keyword argument:
        val -- New scheme value"""
        self._scheme = val
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
    def bank_name(self):
        """Get bank_name"""
        return self._bank_name

    @bank_name.setter
    def bank_name(self, val):
        """Set bank_name
        Keyword argument:
        val -- New bank_name value"""
        self._bank_name = val
        return self

    @property
    def brand(self):
        """Get brand"""
        return self._brand

    @brand.setter
    def brand(self, val):
        """Set brand
        Keyword argument:
        val -- New brand value"""
        self._brand = val
        return self

    @property
    def category(self):
        """Get category"""
        return self._category

    @category.setter
    def category(self, val):
        """Set category
        Keyword argument:
        val -- New category value"""
        self._category = val
        return self

    @property
    def country(self):
        """Get country"""
        return self._country

    @country.setter
    def country(self, val):
        """Set country
        Keyword argument:
        val -- New country value"""
        self._country = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "iin" in data.keys():
            self.iin = data["iin"]
        if "scheme" in data.keys():
            self.scheme = data["scheme"]
        if "type" in data.keys():
            self.type = data["type"]
        if "bank_name" in data.keys():
            self.bank_name = data["bank_name"]
        if "brand" in data.keys():
            self.brand = data["brand"]
        if "category" in data.keys():
            self.category = data["category"]
        if "country" in data.keys():
            self.country = data["country"]

        return self

    def to_json(self):
        return {
            "iin": self.iin,
            "scheme": self.scheme,
            "type": self.type,
            "bank_name": self.bank_name,
            "brand": self.brand,
            "category": self.category,
            "country": self.country,
        }

    def fetch(self, iin, options={}):
        """Fetch card information from the IIN.
        Keyword argument:
        iin -- IIN of the card (first 6 digits)
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/iins/" + quote_plus(iin) + ""
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        body = response.body
        body = body["card_information"]

        obj = processout.CardInformation(self._client)
        return_values.append(obj.fill_with_data(body))

        return return_values[0]

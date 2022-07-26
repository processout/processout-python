try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class InvoiceShipping(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._amount = None
        self._method = None
        self._provider = None
        self._delay = None
        self._address1 = None
        self._address2 = None
        self._city = None
        self._state = None
        self._country_code = None
        self._zip = None
        self._phone_number = None
        self._expects_shipping_at = None
        self._relay_store_name = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def amount(self):
        """Get amount"""
        return self._amount

    @amount.setter
    def amount(self, val):
        """Set amount
        Keyword argument:
        val -- New amount value"""
        self._amount = val
        return self

    @property
    def method(self):
        """Get method"""
        return self._method

    @method.setter
    def method(self, val):
        """Set method
        Keyword argument:
        val -- New method value"""
        self._method = val
        return self

    @property
    def provider(self):
        """Get provider"""
        return self._provider

    @provider.setter
    def provider(self, val):
        """Set provider
        Keyword argument:
        val -- New provider value"""
        self._provider = val
        return self

    @property
    def delay(self):
        """Get delay"""
        return self._delay

    @delay.setter
    def delay(self, val):
        """Set delay
        Keyword argument:
        val -- New delay value"""
        self._delay = val
        return self

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
    def phone_number(self):
        """Get phone_number"""
        return self._phone_number

    @phone_number.setter
    def phone_number(self, val):
        """Set phone_number
        Keyword argument:
        val -- New phone_number value"""
        self._phone_number = val
        return self

    @property
    def expects_shipping_at(self):
        """Get expects_shipping_at"""
        return self._expects_shipping_at

    @expects_shipping_at.setter
    def expects_shipping_at(self, val):
        """Set expects_shipping_at
        Keyword argument:
        val -- New expects_shipping_at value"""
        self._expects_shipping_at = val
        return self

    @property
    def relay_store_name(self):
        """Get relay_store_name"""
        return self._relay_store_name

    @relay_store_name.setter
    def relay_store_name(self, val):
        """Set relay_store_name
        Keyword argument:
        val -- New relay_store_name value"""
        self._relay_store_name = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "method" in data.keys():
            self.method = data["method"]
        if "provider" in data.keys():
            self.provider = data["provider"]
        if "delay" in data.keys():
            self.delay = data["delay"]
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
        if "phone_number" in data.keys():
            self.phone_number = data["phone_number"]
        if "expects_shipping_at" in data.keys():
            self.expects_shipping_at = data["expects_shipping_at"]
        if "relay_store_name" in data.keys():
            self.relay_store_name = data["relay_store_name"]

        return self

    def to_json(self):
        return {
            "amount": self.amount,
            "method": self.method,
            "provider": self.provider,
            "delay": self.delay,
            "address1": self.address1,
            "address2": self.address2,
            "city": self.city,
            "state": self.state,
            "country_code": self.country_code,
            "zip": self.zip,
            "phone_number": self.phone_number,
            "expects_shipping_at": self.expects_shipping_at,
            "relay_store_name": self.relay_store_name,
        }

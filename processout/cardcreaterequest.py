try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class CardCreateRequest(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._device = None
        self._name = None
        self._number = None
        self._exp_day = None
        self._exp_month = None
        self._exp_year = None
        self._cvc2 = None
        self._preferred_scheme = None
        self._metadata = None
        self._token_type = None
        self._eci = None
        self._cryptogram = None
        self._applepay_response = None
        self._applepay_mid = None
        self._payment_token = None
        self._contact = None
        self._shipping = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def device(self):
        """Get device"""
        return self._device

    @device.setter
    def device(self, val):
        """Set device
        Keyword argument:
        val -- New device value"""
        if val is None:
            self._device = val
            return self

        if isinstance(val, dict):
            obj = processout.Device(self._client)
            obj.fill_with_data(val)
            self._device = obj
        else:
            self._device = val
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

    @property
    def exp_day(self):
        """Get exp_day"""
        return self._exp_day

    @exp_day.setter
    def exp_day(self, val):
        """Set exp_day
        Keyword argument:
        val -- New exp_day value"""
        self._exp_day = val
        return self

    @property
    def exp_month(self):
        """Get exp_month"""
        return self._exp_month

    @exp_month.setter
    def exp_month(self, val):
        """Set exp_month
        Keyword argument:
        val -- New exp_month value"""
        self._exp_month = val
        return self

    @property
    def exp_year(self):
        """Get exp_year"""
        return self._exp_year

    @exp_year.setter
    def exp_year(self, val):
        """Set exp_year
        Keyword argument:
        val -- New exp_year value"""
        self._exp_year = val
        return self

    @property
    def cvc2(self):
        """Get cvc2"""
        return self._cvc2

    @cvc2.setter
    def cvc2(self, val):
        """Set cvc2
        Keyword argument:
        val -- New cvc2 value"""
        self._cvc2 = val
        return self

    @property
    def preferred_scheme(self):
        """Get preferred_scheme"""
        return self._preferred_scheme

    @preferred_scheme.setter
    def preferred_scheme(self, val):
        """Set preferred_scheme
        Keyword argument:
        val -- New preferred_scheme value"""
        self._preferred_scheme = val
        return self

    @property
    def metadata(self):
        """Get metadata"""
        return self._metadata

    @metadata.setter
    def metadata(self, val):
        """Set metadata
        Keyword argument:
        val -- New metadata value"""
        self._metadata = val
        return self

    @property
    def token_type(self):
        """Get token_type"""
        return self._token_type

    @token_type.setter
    def token_type(self, val):
        """Set token_type
        Keyword argument:
        val -- New token_type value"""
        self._token_type = val
        return self

    @property
    def eci(self):
        """Get eci"""
        return self._eci

    @eci.setter
    def eci(self, val):
        """Set eci
        Keyword argument:
        val -- New eci value"""
        self._eci = val
        return self

    @property
    def cryptogram(self):
        """Get cryptogram"""
        return self._cryptogram

    @cryptogram.setter
    def cryptogram(self, val):
        """Set cryptogram
        Keyword argument:
        val -- New cryptogram value"""
        self._cryptogram = val
        return self

    @property
    def applepay_response(self):
        """Get applepay_response"""
        return self._applepay_response

    @applepay_response.setter
    def applepay_response(self, val):
        """Set applepay_response
        Keyword argument:
        val -- New applepay_response value"""
        self._applepay_response = val
        return self

    @property
    def applepay_mid(self):
        """Get applepay_mid"""
        return self._applepay_mid

    @applepay_mid.setter
    def applepay_mid(self, val):
        """Set applepay_mid
        Keyword argument:
        val -- New applepay_mid value"""
        self._applepay_mid = val
        return self

    @property
    def payment_token(self):
        """Get payment_token"""
        return self._payment_token

    @payment_token.setter
    def payment_token(self, val):
        """Set payment_token
        Keyword argument:
        val -- New payment_token value"""
        self._payment_token = val
        return self

    @property
    def contact(self):
        """Get contact"""
        return self._contact

    @contact.setter
    def contact(self, val):
        """Set contact
        Keyword argument:
        val -- New contact value"""
        if val is None:
            self._contact = val
            return self

        if isinstance(val, dict):
            obj = processout.CardContact(self._client)
            obj.fill_with_data(val)
            self._contact = obj
        else:
            self._contact = val
        return self

    @property
    def shipping(self):
        """Get shipping"""
        return self._shipping

    @shipping.setter
    def shipping(self, val):
        """Set shipping
        Keyword argument:
        val -- New shipping value"""
        if val is None:
            self._shipping = val
            return self

        if isinstance(val, dict):
            obj = processout.CardShipping(self._client)
            obj.fill_with_data(val)
            self._shipping = obj
        else:
            self._shipping = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "device" in data.keys():
            self.device = data["device"]
        if "name" in data.keys():
            self.name = data["name"]
        if "number" in data.keys():
            self.number = data["number"]
        if "exp_day" in data.keys():
            self.exp_day = data["exp_day"]
        if "exp_month" in data.keys():
            self.exp_month = data["exp_month"]
        if "exp_year" in data.keys():
            self.exp_year = data["exp_year"]
        if "cvc2" in data.keys():
            self.cvc2 = data["cvc2"]
        if "preferred_scheme" in data.keys():
            self.preferred_scheme = data["preferred_scheme"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "token_type" in data.keys():
            self.token_type = data["token_type"]
        if "eci" in data.keys():
            self.eci = data["eci"]
        if "cryptogram" in data.keys():
            self.cryptogram = data["cryptogram"]
        if "applepay_response" in data.keys():
            self.applepay_response = data["applepay_response"]
        if "applepay_mid" in data.keys():
            self.applepay_mid = data["applepay_mid"]
        if "payment_token" in data.keys():
            self.payment_token = data["payment_token"]
        if "contact" in data.keys():
            self.contact = data["contact"]
        if "shipping" in data.keys():
            self.shipping = data["shipping"]

        return self

    def to_json(self):
        return {
            "device": self.device,
            "name": self.name,
            "number": self.number,
            "exp_day": self.exp_day,
            "exp_month": self.exp_month,
            "exp_year": self.exp_year,
            "cvc2": self.cvc2,
            "preferred_scheme": self.preferred_scheme,
            "metadata": self.metadata,
            "token_type": self.token_type,
            "eci": self.eci,
            "cryptogram": self.cryptogram,
            "applepay_response": self.applepay_response,
            "applepay_mid": self.applepay_mid,
            "payment_token": self.payment_token,
            "contact": self.contact,
            "shipping": self.shipping,
        }

    def create(self, options={}):
        """Create a new card.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/cards"
        data = {

        }

        response = Response(request.post(path, data, options))
        return_values = []

        body = response.body
        body = body["card"]

        obj = processout.CardCreateRequest(self._client)
        return_values.append(obj.fill_with_data(body))

        return return_values[0]

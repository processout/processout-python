try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class CategoryErrorCodes(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._generic = None
        self._service = None
        self._gateway = None
        self._card = None
        self._check = None
        self._shipping = None
        self._customer = None
        self._payment = None
        self._refund = None
        self._wallet = None
        self._request = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def generic(self):
        """Get generic"""
        return self._generic

    @generic.setter
    def generic(self, val):
        """Set generic
        Keyword argument:
        val -- New generic value"""
        self._generic = val
        return self

    @property
    def service(self):
        """Get service"""
        return self._service

    @service.setter
    def service(self, val):
        """Set service
        Keyword argument:
        val -- New service value"""
        self._service = val
        return self

    @property
    def gateway(self):
        """Get gateway"""
        return self._gateway

    @gateway.setter
    def gateway(self, val):
        """Set gateway
        Keyword argument:
        val -- New gateway value"""
        self._gateway = val
        return self

    @property
    def card(self):
        """Get card"""
        return self._card

    @card.setter
    def card(self, val):
        """Set card
        Keyword argument:
        val -- New card value"""
        self._card = val
        return self

    @property
    def check(self):
        """Get check"""
        return self._check

    @check.setter
    def check(self, val):
        """Set check
        Keyword argument:
        val -- New check value"""
        self._check = val
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
        self._shipping = val
        return self

    @property
    def customer(self):
        """Get customer"""
        return self._customer

    @customer.setter
    def customer(self, val):
        """Set customer
        Keyword argument:
        val -- New customer value"""
        self._customer = val
        return self

    @property
    def payment(self):
        """Get payment"""
        return self._payment

    @payment.setter
    def payment(self, val):
        """Set payment
        Keyword argument:
        val -- New payment value"""
        self._payment = val
        return self

    @property
    def refund(self):
        """Get refund"""
        return self._refund

    @refund.setter
    def refund(self, val):
        """Set refund
        Keyword argument:
        val -- New refund value"""
        self._refund = val
        return self

    @property
    def wallet(self):
        """Get wallet"""
        return self._wallet

    @wallet.setter
    def wallet(self, val):
        """Set wallet
        Keyword argument:
        val -- New wallet value"""
        self._wallet = val
        return self

    @property
    def request(self):
        """Get request"""
        return self._request

    @request.setter
    def request(self, val):
        """Set request
        Keyword argument:
        val -- New request value"""
        self._request = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "generic" in data.keys():
            self.generic = data["generic"]
        if "service" in data.keys():
            self.service = data["service"]
        if "gateway" in data.keys():
            self.gateway = data["gateway"]
        if "card" in data.keys():
            self.card = data["card"]
        if "check" in data.keys():
            self.check = data["check"]
        if "shipping" in data.keys():
            self.shipping = data["shipping"]
        if "customer" in data.keys():
            self.customer = data["customer"]
        if "payment" in data.keys():
            self.payment = data["payment"]
        if "refund" in data.keys():
            self.refund = data["refund"]
        if "wallet" in data.keys():
            self.wallet = data["wallet"]
        if "request" in data.keys():
            self.request = data["request"]

        return self

    def to_json(self):
        return {
            "generic": self.generic,
            "service": self.service,
            "gateway": self.gateway,
            "card": self.card,
            "check": self.check,
            "shipping": self.shipping,
            "customer": self.customer,
            "payment": self.payment,
            "refund": self.refund,
            "wallet": self.wallet,
            "request": self.request,
        }

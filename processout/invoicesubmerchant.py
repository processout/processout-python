try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class InvoiceSubmerchant(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._id = None
        self._name = None
        self._reference = None
        self._mcc = None
        self._phone_number = None
        self._email = None
        self._address = None
        self._tax_reference = None
        self._service_establishment_number = None
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
    def reference(self):
        """Get reference"""
        return self._reference

    @reference.setter
    def reference(self, val):
        """Set reference
        Keyword argument:
        val -- New reference value"""
        self._reference = val
        return self

    @property
    def mcc(self):
        """Get mcc"""
        return self._mcc

    @mcc.setter
    def mcc(self, val):
        """Set mcc
        Keyword argument:
        val -- New mcc value"""
        self._mcc = val
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
        if val is None:
            self._phone_number = val
            return self

        if isinstance(val, dict):
            obj = processout.SubmerchantPhoneNumber(self._client)
            obj.fill_with_data(val)
            self._phone_number = obj
        else:
            self._phone_number = val
        return self

    @property
    def email(self):
        """Get email"""
        return self._email

    @email.setter
    def email(self, val):
        """Set email
        Keyword argument:
        val -- New email value"""
        self._email = val
        return self

    @property
    def address(self):
        """Get address"""
        return self._address

    @address.setter
    def address(self, val):
        """Set address
        Keyword argument:
        val -- New address value"""
        if val is None:
            self._address = val
            return self

        if isinstance(val, dict):
            obj = processout.SubmerchantAddress(self._client)
            obj.fill_with_data(val)
            self._address = obj
        else:
            self._address = val
        return self

    @property
    def tax_reference(self):
        """Get tax_reference"""
        return self._tax_reference

    @tax_reference.setter
    def tax_reference(self, val):
        """Set tax_reference
        Keyword argument:
        val -- New tax_reference value"""
        self._tax_reference = val
        return self

    @property
    def service_establishment_number(self):
        """Get service_establishment_number"""
        return self._service_establishment_number

    @service_establishment_number.setter
    def service_establishment_number(self, val):
        """Set service_establishment_number
        Keyword argument:
        val -- New service_establishment_number value"""
        self._service_establishment_number = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "id" in data.keys():
            self.id = data["id"]
        if "name" in data.keys():
            self.name = data["name"]
        if "reference" in data.keys():
            self.reference = data["reference"]
        if "mcc" in data.keys():
            self.mcc = data["mcc"]
        if "phone_number" in data.keys():
            self.phone_number = data["phone_number"]
        if "email" in data.keys():
            self.email = data["email"]
        if "address" in data.keys():
            self.address = data["address"]
        if "tax_reference" in data.keys():
            self.tax_reference = data["tax_reference"]
        if "service_establishment_number" in data.keys():
            self.service_establishment_number = data["service_establishment_number"]

        return self

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "reference": self.reference,
            "mcc": self.mcc,
            "phone_number": self.phone_number,
            "email": self.email,
            "address": self.address,
            "tax_reference": self.tax_reference,
            "service_establishment_number": self.service_establishment_number,
        }

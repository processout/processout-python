try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class InvoiceDetail(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._id = None
        self._name = None
        self._type = None
        self._amount = None
        self._quantity = None
        self._metadata = None
        self._reference = None
        self._description = None
        self._brand = None
        self._model = None
        self._discount_amount = None
        self._condition = None
        self._marketplace_merchant = None
        self._marketplace_merchant_is_business = None
        self._marketplace_merchant_created_at = None
        self._category = None
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
    def quantity(self):
        """Get quantity"""
        return self._quantity

    @quantity.setter
    def quantity(self, val):
        """Set quantity
        Keyword argument:
        val -- New quantity value"""
        self._quantity = val
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
    def description(self):
        """Get description"""
        return self._description

    @description.setter
    def description(self, val):
        """Set description
        Keyword argument:
        val -- New description value"""
        self._description = val
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
    def model(self):
        """Get model"""
        return self._model

    @model.setter
    def model(self, val):
        """Set model
        Keyword argument:
        val -- New model value"""
        self._model = val
        return self

    @property
    def discount_amount(self):
        """Get discount_amount"""
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, val):
        """Set discount_amount
        Keyword argument:
        val -- New discount_amount value"""
        self._discount_amount = val
        return self

    @property
    def condition(self):
        """Get condition"""
        return self._condition

    @condition.setter
    def condition(self, val):
        """Set condition
        Keyword argument:
        val -- New condition value"""
        self._condition = val
        return self

    @property
    def marketplace_merchant(self):
        """Get marketplace_merchant"""
        return self._marketplace_merchant

    @marketplace_merchant.setter
    def marketplace_merchant(self, val):
        """Set marketplace_merchant
        Keyword argument:
        val -- New marketplace_merchant value"""
        self._marketplace_merchant = val
        return self

    @property
    def marketplace_merchant_is_business(self):
        """Get marketplace_merchant_is_business"""
        return self._marketplace_merchant_is_business

    @marketplace_merchant_is_business.setter
    def marketplace_merchant_is_business(self, val):
        """Set marketplace_merchant_is_business
        Keyword argument:
        val -- New marketplace_merchant_is_business value"""
        self._marketplace_merchant_is_business = val
        return self

    @property
    def marketplace_merchant_created_at(self):
        """Get marketplace_merchant_created_at"""
        return self._marketplace_merchant_created_at

    @marketplace_merchant_created_at.setter
    def marketplace_merchant_created_at(self, val):
        """Set marketplace_merchant_created_at
        Keyword argument:
        val -- New marketplace_merchant_created_at value"""
        self._marketplace_merchant_created_at = val
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

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "id" in data.keys():
            self.id = data["id"]
        if "name" in data.keys():
            self.name = data["name"]
        if "type" in data.keys():
            self.type = data["type"]
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "quantity" in data.keys():
            self.quantity = data["quantity"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "reference" in data.keys():
            self.reference = data["reference"]
        if "description" in data.keys():
            self.description = data["description"]
        if "brand" in data.keys():
            self.brand = data["brand"]
        if "model" in data.keys():
            self.model = data["model"]
        if "discount_amount" in data.keys():
            self.discount_amount = data["discount_amount"]
        if "condition" in data.keys():
            self.condition = data["condition"]
        if "marketplace_merchant" in data.keys():
            self.marketplace_merchant = data["marketplace_merchant"]
        if "marketplace_merchant_is_business" in data.keys():
            self.marketplace_merchant_is_business = data["marketplace_merchant_is_business"]
        if "marketplace_merchant_created_at" in data.keys():
            self.marketplace_merchant_created_at = data["marketplace_merchant_created_at"]
        if "category" in data.keys():
            self.category = data["category"]

        return self

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "amount": self.amount,
            "quantity": self.quantity,
            "metadata": self.metadata,
            "reference": self.reference,
            "description": self.description,
            "brand": self.brand,
            "model": self.model,
            "discount_amount": self.discount_amount,
            "condition": self.condition,
            "marketplace_merchant": self.marketplace_merchant,
            "marketplace_merchant_is_business": self.marketplace_merchant_is_business,
            "marketplace_merchant_created_at": self.marketplace_merchant_created_at,
            "category": self.category,
        }

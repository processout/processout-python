try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class PayoutItem(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._id = None
        self._project = None
        self._project_id = None
        self._payout = None
        self._payout_id = None
        self._transaction = None
        self._transaction_id = None
        self._type = None
        self._gateway_resource_id = None
        self._amount = None
        self._fees = None
        self._metadata = None
        self._created_at = None
        self._breakdown = None
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
    def project(self):
        """Get project"""
        return self._project

    @project.setter
    def project(self, val):
        """Set project
        Keyword argument:
        val -- New project value"""
        if val is None:
            self._project = val
            return self

        if isinstance(val, dict):
            obj = processout.Project(self._client)
            obj.fill_with_data(val)
            self._project = obj
        else:
            self._project = val
        return self

    @property
    def project_id(self):
        """Get project_id"""
        return self._project_id

    @project_id.setter
    def project_id(self, val):
        """Set project_id
        Keyword argument:
        val -- New project_id value"""
        self._project_id = val
        return self

    @property
    def payout(self):
        """Get payout"""
        return self._payout

    @payout.setter
    def payout(self, val):
        """Set payout
        Keyword argument:
        val -- New payout value"""
        if val is None:
            self._payout = val
            return self

        if isinstance(val, dict):
            obj = processout.Payout(self._client)
            obj.fill_with_data(val)
            self._payout = obj
        else:
            self._payout = val
        return self

    @property
    def payout_id(self):
        """Get payout_id"""
        return self._payout_id

    @payout_id.setter
    def payout_id(self, val):
        """Set payout_id
        Keyword argument:
        val -- New payout_id value"""
        self._payout_id = val
        return self

    @property
    def transaction(self):
        """Get transaction"""
        return self._transaction

    @transaction.setter
    def transaction(self, val):
        """Set transaction
        Keyword argument:
        val -- New transaction value"""
        if val is None:
            self._transaction = val
            return self

        if isinstance(val, dict):
            obj = processout.Transaction(self._client)
            obj.fill_with_data(val)
            self._transaction = obj
        else:
            self._transaction = val
        return self

    @property
    def transaction_id(self):
        """Get transaction_id"""
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, val):
        """Set transaction_id
        Keyword argument:
        val -- New transaction_id value"""
        self._transaction_id = val
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
    def gateway_resource_id(self):
        """Get gateway_resource_id"""
        return self._gateway_resource_id

    @gateway_resource_id.setter
    def gateway_resource_id(self, val):
        """Set gateway_resource_id
        Keyword argument:
        val -- New gateway_resource_id value"""
        self._gateway_resource_id = val
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
    def fees(self):
        """Get fees"""
        return self._fees

    @fees.setter
    def fees(self, val):
        """Set fees
        Keyword argument:
        val -- New fees value"""
        self._fees = val
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
    def created_at(self):
        """Get created_at"""
        return self._created_at

    @created_at.setter
    def created_at(self, val):
        """Set created_at
        Keyword argument:
        val -- New created_at value"""
        self._created_at = val
        return self

    @property
    def breakdown(self):
        """Get breakdown"""
        return self._breakdown

    @breakdown.setter
    def breakdown(self, val):
        """Set breakdown
        Keyword argument:
        val -- New breakdown value"""
        if val is None:
            self._breakdown = val
            return self

        if isinstance(val, dict):
            obj = processout.PayoutItemAmountBreakdowns(self._client)
            obj.fill_with_data(val)
            self._breakdown = obj
        else:
            self._breakdown = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "id" in data.keys():
            self.id = data["id"]
        if "project" in data.keys():
            self.project = data["project"]
        if "project_id" in data.keys():
            self.project_id = data["project_id"]
        if "payout" in data.keys():
            self.payout = data["payout"]
        if "payout_id" in data.keys():
            self.payout_id = data["payout_id"]
        if "transaction" in data.keys():
            self.transaction = data["transaction"]
        if "transaction_id" in data.keys():
            self.transaction_id = data["transaction_id"]
        if "type" in data.keys():
            self.type = data["type"]
        if "gateway_resource_id" in data.keys():
            self.gateway_resource_id = data["gateway_resource_id"]
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "fees" in data.keys():
            self.fees = data["fees"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        if "breakdown" in data.keys():
            self.breakdown = data["breakdown"]

        return self

    def to_json(self):
        return {
            "id": self.id,
            "project": self.project,
            "project_id": self.project_id,
            "payout": self.payout,
            "payout_id": self.payout_id,
            "transaction": self.transaction,
            "transaction_id": self.transaction_id,
            "type": self.type,
            "gateway_resource_id": self.gateway_resource_id,
            "amount": self.amount,
            "fees": self.fees,
            "metadata": self.metadata,
            "created_at": self.created_at,
            "breakdown": self.breakdown,
        }

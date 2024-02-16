try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class Payout(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._id = None
        self._project = None
        self._project_id = None
        self._status = None
        self._amount = None
        self._currency = None
        self._metadata = None
        self._bank_name = None
        self._bank_summary = None
        self._sales_transactions = None
        self._sales_volume = None
        self._refunds_transactions = None
        self._refunds_volume = None
        self._chargebacks_transactions = None
        self._chargebacks_volume = None
        self._fees = None
        self._adjustments = None
        self._reserve = None
        self._settled_at = None
        self._created_at = None
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
    def status(self):
        """Get status"""
        return self._status

    @status.setter
    def status(self, val):
        """Set status
        Keyword argument:
        val -- New status value"""
        self._status = val
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
    def currency(self):
        """Get currency"""
        return self._currency

    @currency.setter
    def currency(self, val):
        """Set currency
        Keyword argument:
        val -- New currency value"""
        self._currency = val
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
    def bank_summary(self):
        """Get bank_summary"""
        return self._bank_summary

    @bank_summary.setter
    def bank_summary(self, val):
        """Set bank_summary
        Keyword argument:
        val -- New bank_summary value"""
        self._bank_summary = val
        return self

    @property
    def sales_transactions(self):
        """Get sales_transactions"""
        return self._sales_transactions

    @sales_transactions.setter
    def sales_transactions(self, val):
        """Set sales_transactions
        Keyword argument:
        val -- New sales_transactions value"""
        self._sales_transactions = val
        return self

    @property
    def sales_volume(self):
        """Get sales_volume"""
        return self._sales_volume

    @sales_volume.setter
    def sales_volume(self, val):
        """Set sales_volume
        Keyword argument:
        val -- New sales_volume value"""
        self._sales_volume = val
        return self

    @property
    def refunds_transactions(self):
        """Get refunds_transactions"""
        return self._refunds_transactions

    @refunds_transactions.setter
    def refunds_transactions(self, val):
        """Set refunds_transactions
        Keyword argument:
        val -- New refunds_transactions value"""
        self._refunds_transactions = val
        return self

    @property
    def refunds_volume(self):
        """Get refunds_volume"""
        return self._refunds_volume

    @refunds_volume.setter
    def refunds_volume(self, val):
        """Set refunds_volume
        Keyword argument:
        val -- New refunds_volume value"""
        self._refunds_volume = val
        return self

    @property
    def chargebacks_transactions(self):
        """Get chargebacks_transactions"""
        return self._chargebacks_transactions

    @chargebacks_transactions.setter
    def chargebacks_transactions(self, val):
        """Set chargebacks_transactions
        Keyword argument:
        val -- New chargebacks_transactions value"""
        self._chargebacks_transactions = val
        return self

    @property
    def chargebacks_volume(self):
        """Get chargebacks_volume"""
        return self._chargebacks_volume

    @chargebacks_volume.setter
    def chargebacks_volume(self, val):
        """Set chargebacks_volume
        Keyword argument:
        val -- New chargebacks_volume value"""
        self._chargebacks_volume = val
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
    def adjustments(self):
        """Get adjustments"""
        return self._adjustments

    @adjustments.setter
    def adjustments(self, val):
        """Set adjustments
        Keyword argument:
        val -- New adjustments value"""
        self._adjustments = val
        return self

    @property
    def reserve(self):
        """Get reserve"""
        return self._reserve

    @reserve.setter
    def reserve(self, val):
        """Set reserve
        Keyword argument:
        val -- New reserve value"""
        self._reserve = val
        return self

    @property
    def settled_at(self):
        """Get settled_at"""
        return self._settled_at

    @settled_at.setter
    def settled_at(self, val):
        """Set settled_at
        Keyword argument:
        val -- New settled_at value"""
        self._settled_at = val
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
        if "status" in data.keys():
            self.status = data["status"]
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "currency" in data.keys():
            self.currency = data["currency"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "bank_name" in data.keys():
            self.bank_name = data["bank_name"]
        if "bank_summary" in data.keys():
            self.bank_summary = data["bank_summary"]
        if "sales_transactions" in data.keys():
            self.sales_transactions = data["sales_transactions"]
        if "sales_volume" in data.keys():
            self.sales_volume = data["sales_volume"]
        if "refunds_transactions" in data.keys():
            self.refunds_transactions = data["refunds_transactions"]
        if "refunds_volume" in data.keys():
            self.refunds_volume = data["refunds_volume"]
        if "chargebacks_transactions" in data.keys():
            self.chargebacks_transactions = data["chargebacks_transactions"]
        if "chargebacks_volume" in data.keys():
            self.chargebacks_volume = data["chargebacks_volume"]
        if "fees" in data.keys():
            self.fees = data["fees"]
        if "adjustments" in data.keys():
            self.adjustments = data["adjustments"]
        if "reserve" in data.keys():
            self.reserve = data["reserve"]
        if "settled_at" in data.keys():
            self.settled_at = data["settled_at"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]

        return self

    def to_json(self):
        return {
            "id": self.id,
            "project": self.project,
            "project_id": self.project_id,
            "status": self.status,
            "amount": self.amount,
            "currency": self.currency,
            "metadata": self.metadata,
            "bank_name": self.bank_name,
            "bank_summary": self.bank_summary,
            "sales_transactions": self.sales_transactions,
            "sales_volume": self.sales_volume,
            "refunds_transactions": self.refunds_transactions,
            "refunds_volume": self.refunds_volume,
            "chargebacks_transactions": self.chargebacks_transactions,
            "chargebacks_volume": self.chargebacks_volume,
            "fees": self.fees,
            "adjustments": self.adjustments,
            "reserve": self.reserve,
            "settled_at": self.settled_at,
            "created_at": self.created_at,
        }

    def fetch_items(self, options={}):
        """Get all the items linked to the payout.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/payouts/" + quote_plus(self.id) + "/items"
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        a = []
        body = response.body
        for v in body['items']:
            tmp = processout.PayoutItem(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)

        return return_values[0]

    def all(self, options={}):
        """Get all the payouts.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/payouts"
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        a = []
        body = response.body
        for v in body['payouts']:
            tmp = processout.Payout(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)

        return return_values[0]

    def find(self, payout_id, options={}):
        """Find a payout by its ID.
        Keyword argument:
        payout_id -- ID of the payout
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/payouts/" + quote_plus(payout_id) + ""
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        body = response.body
        body = body["payout"]

        obj = processout.Payout(self._client)
        return_values.append(obj.fill_with_data(body))

        return return_values[0]

    def delete(self, payout_id, options={}):
        """Delete the payout along with its payout items
        Keyword argument:
        payout_id -- ID of the payout
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/payouts/" + quote_plus(payout_id) + ""
        data = {

        }

        response = Response(request.delete(path, data, options))
        return_values = []

        return_values.append(response.success)

        return return_values[0]

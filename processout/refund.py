try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class Refund(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._id = None
        self._transaction = None
        self._transaction_id = None
        self._amount = None
        self._reason = None
        self._information = None
        self._has_failed = None
        self._metadata = None
        self._sandbox = None
        self._created_at = None
        self._invoice_detail_ids = None
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
    def reason(self):
        """Get reason"""
        return self._reason

    @reason.setter
    def reason(self, val):
        """Set reason
        Keyword argument:
        val -- New reason value"""
        self._reason = val
        return self

    @property
    def information(self):
        """Get information"""
        return self._information

    @information.setter
    def information(self, val):
        """Set information
        Keyword argument:
        val -- New information value"""
        self._information = val
        return self

    @property
    def has_failed(self):
        """Get has_failed"""
        return self._has_failed

    @has_failed.setter
    def has_failed(self, val):
        """Set has_failed
        Keyword argument:
        val -- New has_failed value"""
        self._has_failed = val
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
    def sandbox(self):
        """Get sandbox"""
        return self._sandbox

    @sandbox.setter
    def sandbox(self, val):
        """Set sandbox
        Keyword argument:
        val -- New sandbox value"""
        self._sandbox = val
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
    def invoice_detail_ids(self):
        """Get invoice_detail_ids"""
        return self._invoice_detail_ids

    @invoice_detail_ids.setter
    def invoice_detail_ids(self, val):
        """Set invoice_detail_ids
        Keyword argument:
        val -- New invoice_detail_ids value"""
        self._invoice_detail_ids = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "id" in data.keys():
            self.id = data["id"]
        if "transaction" in data.keys():
            self.transaction = data["transaction"]
        if "transaction_id" in data.keys():
            self.transaction_id = data["transaction_id"]
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "reason" in data.keys():
            self.reason = data["reason"]
        if "information" in data.keys():
            self.information = data["information"]
        if "has_failed" in data.keys():
            self.has_failed = data["has_failed"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        if "invoice_detail_ids" in data.keys():
            self.invoice_detail_ids = data["invoice_detail_ids"]

        return self

    def to_json(self):
        return {
            "id": self.id,
            "transaction": self.transaction,
            "transaction_id": self.transaction_id,
            "amount": self.amount,
            "reason": self.reason,
            "information": self.information,
            "has_failed": self.has_failed,
            "metadata": self.metadata,
            "sandbox": self.sandbox,
            "created_at": self.created_at,
            "invoice_detail_ids": self.invoice_detail_ids,
        }

    def create_for_invoice(self, invoice_id, options={}):
        """Create a refund for an invoice.
        Keyword argument:
        invoice_id -- ID of the invoice
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/invoices/" + quote_plus(invoice_id) + "/refunds"
        data = {
            'amount': self.amount,
            'reason': self.reason,
            'information': self.information,
            'invoice_detail_ids': self.invoice_detail_ids,
            'metadata': options.get("metadata")
        }

        response = Response(request.post(path, data, options))
        return_values = []

        return_values.append(response.success)

        return return_values[0]

    def fetch_transaction_refunds(self, transaction_id, options={}):
        """Get the transaction's refunds.
        Keyword argument:
        transaction_id -- ID of the transaction
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/transactions/" + quote_plus(transaction_id) + "/refunds"
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        a = []
        body = response.body
        for v in body['refunds']:
            tmp = processout.Refund(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)

        return return_values[0]

    def find(self, transaction_id, refund_id, options={}):
        """Find a transaction's refund by its ID.
        Keyword argument:
        transaction_id -- ID of the transaction on which the refund was applied
        refund_id -- ID of the refund
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/transactions/" + \
            quote_plus(transaction_id) + "/refunds/" + quote_plus(refund_id) + ""
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        body = response.body
        body = body["refund"]

        obj = processout.Refund(self._client)
        return_values.append(obj.fill_with_data(body))

        return return_values[0]

    def create(self, options={}):
        """Create a refund for a transaction.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/transactions/" + quote_plus(self.transaction_id) + "/refunds"
        data = {
            'amount': self.amount,
            'reason': self.reason,
            'information': self.information,
            'invoice_detail_ids': self.invoice_detail_ids,
            'metadata': options.get("metadata")
        }

        response = Response(request.post(path, data, options))
        return_values = []

        return_values.append(response.success)

        return return_values[0]

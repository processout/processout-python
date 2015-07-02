# processout.invoice.tailoredinvoice

from ..processout          import ProcessOut
from ..networking.response import Response
from .invoiceabstract      import InvoiceAbstract
from .invoice              import Invoice

import requests

class TailoredInvoice(InvoiceAbstract):
    def __init__(self, processOut = None):
        """Create a new instance of a tailored invoice

        Keyword argument:
        processOut -- ProcessOut instance
        """
        if processOut == None:
            processOut = ProcessOut.getDefault()

        InvoiceAbstract.__init__(self, processOut)

        self._id = None

    def _setFields(self, response):
        """Set the tailored invoice fields from the data pulled from
        ProcessOut's servers"""
        self._itemName     = response['item_name']
        self._itemPrice    = response['item_price']
        self._itemQuantity = response['item_quantity']
        self._currency     = response['currency']
        self._taxes        = response['taxes']
        self._shipping     = response['shipping']
        self._returnUrl    = response['return_url']
        self._cancelUrl    = response['cancel_url']
        self._notifyUrl    = response['notify_url']

    def fromId(self, value):
        """Set the tailored invoice id and fetch data from ProcessOut

        Keyword argument:
        value -- new value of the tailored invoice id
        """
        self._id = value

        self._lastResponse = Response(requests.get(ProcessOut.HOST + '/tailored-invoices/' +
            self._id,
            auth = (self._processOut.projectId, self._processOut.projectKey),
            data = self._generateData(),
            verify = True))

        self._setFields(self._lastResponse.body)

        return self

    @property
    def id(self):
        """Return the current tailored invoice id associated with the
        TailoredInvoice"""
        return self._id

    def invoice(self):
        """Create a new invoice from this tailored invoice

        Create a new Invoice instance from this tailored invoice data
        """
        invoice               = Invoice(self._processOut)
        invoice.itemName      = self.itemName
        invoice.itemPrice     = self.itemPrice
        invoice.itemQuantity  = self.itemQuantity
        invoice.taxes         = self.taxes
        invoice.shipping      = self.shipping
        invoice.recurringDays = self.recurringDays
        invoice.currency      = self.currency
        invoice.returnUrl     = self.returnUrl
        invoice.cancelUrl     = self.cancelUrl
        invoice.notifyUrl     = self.notifyUrl
        invoice.custom        = self.custom

        return invoice
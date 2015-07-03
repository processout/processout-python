# processout.invoice.invoice

from ..processout              import ProcessOut
from ..networking.response     import Response
from .invoiceabstract          import InvoiceAbstract

import requests

class Invoice(InvoiceAbstract):
    def __init__(self, processOut = None):
        """Create a new instance of a simple invoice

        Keyword argument:
        processOut -- ProcessOut instance
        """
        if processOut == None:
            processOut = ProcessOut.getDefault()

        InvoiceAbstract.__init__(self, processOut)

        self._id                = None
        self._url               = None
        self._tailoredInvoiceId = None

    def fromTailored(self, tailoredInvoice):
        """Set the tailored invoice id to this invoice

        Keywork argument:
        tailoredInvoiceId -- id of the tailored invoice"""
        self._tailoredInvoiceId = tailoredInvoiceId.id

    def save(self):
        """Save the invoice and push data to ProcessOut"""
        if self.tailoredInvoiceId == None:
            self._saveNew()
        else:
            self._saveFromTailored()

        self._id  = self._lastResponse.body['id']
        self._url = self._lastResponse.body['url']

        return self


    def _saveNew(self):
        """Create the invoice

        Perform the ProcessOut's request to generate the invoice
        """
        self._lastResponse = Response(requests.post(ProcessOut.HOST + '/invoices',
            auth = (self.projectId, self.projectKey),
            data = self._generateData(),
            verify = True))

    def _saveFromTailored(self):
        """Create the invoice from the tailored invoice

        Perform the ProcessOut's request to generate the invoice from the
        tailored invoice
        """
        self._lastResponse = Response(requests.post(ProcessOut.HOST + '/invoices/from-tailored/' +
            self.tailoredInvoiceId,
            auth = (self.projectId, self.projectKey),
            data = self._generateData(),
            verify = True))

    @property
    def id(self):
        """Get the invoice id

        Return the id of the created invoice
        """
        return self._id

    @property
    def url(self):
        """Get the invoice url

        Return the URL to the created invoice
        """
        return self._url

    @property
    def tailoredInvoiceId(self):
        """Get the tailored invoice id

        Return the ID of the tailored invoice linked to this invoice
        """
        return self._tailoredInvoiceId

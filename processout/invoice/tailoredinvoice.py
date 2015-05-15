# processout.invoice.tailoredinvoice

from ..processout     import ProcessOut
from .invoiceabstract import InvoiceAbstract

import requests

class TailoredInvoice(InvoiceAbstract):
    def __init__(self, processOut, tailoredInvoiceId):
        """Create a new instance of a tailored invoice

        Keyword argument:
        processOut -- ProcessOut instance
        tailoredInvoiceId -- id of the tailored invoice
        """
        InvoiceAbstract.__init__(self, processOut)

        self._tailoredInvoiceId = tailoredInvoiceId

    @property
    def tailoredInvoiceId(self):
        """Return the current tailored invoice id associated with the
        TailoredInvoice"""
        return self._tailoredInvoiceId

    @tailoredInvoiceId.setter
    def tailoredInvoiceId(self, value):
        """Set the tailored invoice id

        Keyword argument:
        value -- new value of the tailored invoice id
        """
        self._tailoredInvoiceId = value

    def getLink(self):
        """Get the invoice url

        Perform the ProcessOut's request to generate the invoice, and return the
        URL to that invoice
        """
        response = requests.post(ProcessOut.HOST + '/invoices/from-tailored/' +
            self.tailoredInvoiceId,
            auth = (self._processOut.projectId, self._processOut.projectKey),
            data = self._generateData(),
            verify = True).json()

        if not response['success']:
            raise Exception(response['message'])

        return response['url']

    def _generateData(self):
        """Generate the data used during the ProcessOut's request"""
        return InvoiceAbstract._generateData(self)

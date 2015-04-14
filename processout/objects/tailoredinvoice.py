
from .baseinvoice import BaseInvoice
import requests

class TailoredInvoice(BaseInvoice):
    def __init__(self, projectId, projectSecret, tailoredInvoiceId):
        """Create a new instance of a tailored invoice

        Keyword argument:
        projectId -- id of the ProcessOut's project
        projectSecret -- secret of the ProcessOut's project
        tailoredInvoiceId -- id of the tailored invoice
        """
        BaseInvoice.__init__(self, projectId, projectSecret)

        self._tailoredInvoiceId = tailoredInvoiceId

    @property
    def tailoredInvoiceId(self):
        """Return the current tailored invoice id id associated with the TailoredInvoice"""
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
        response = requests.post(self.host + '/invoices/from-tailored/' +
            self.tailoredInvoiceId,
            auth = (self.projectId, self.projectSecret),
            data = self._generateData(),
            verify = True).json()

        if not response['success']:
            raise Exception(response['message'])

        return response['url']

    def _generateData(self):
        """Generate the data used during the ProcessOut's request"""
        return BaseInvoice._generateData(self)

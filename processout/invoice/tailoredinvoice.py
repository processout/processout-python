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

	def create(self):
		"""Create the invoice

		Perform the ProcessOut's request to generate the invoice
		"""
		self._lastResponse = requests.post(ProcessOut.HOST + '/invoices/from-tailored/' +
			self.tailoredInvoiceId,
			auth = (self._processOut.projectId, self._processOut.projectKey),
			data = self._generateData(),
			verify = True).json()

		if not self._lastResponse['success']:
			raise Exception(self._lastResponse['message'])

		return self._lastResponse

	def getLink(self):
		"""Get the invoice url

		Return the URL to the created invoice
		"""
		if not self._lastResponse:
			self.create()

		return self._lastResponse['url']

	def getId(self):
		"""Get the invoice id

		Return the id of the created invoice
		"""
		if not self._lastResponse:
			self.create()

		return self._lastResponse['id']

	def _generateData(self):
		"""Generate the data used during the ProcessOut's request"""
		return InvoiceAbstract._generateData(self)

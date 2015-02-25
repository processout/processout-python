
from .baseinvoice import BaseInvoice
import requests

class ProductInvoice(BaseInvoice):
	def __init__(self, projectId, projectSecret, productId):
		"""Create a new instance of a product invoice

		Keyword argument:
		projectId -- id of the ProcessOut's project
		projectSecret -- secret of the ProcessOut's project
		productId -- id of the product
		"""
		BaseInvoice.__init__(self, projectId, projectSecret)

		self._productId = productId

	@property
	def productId(self):
		"""Return the current product id associated with the ProductInvoice"""
		return self._productId

	@productId.setter
	def productId(self, value):
		"""Set the product id

		Keyword argument:
		value -- new value of the product id
		"""
		self._productId = value

	def getLink(self):
		"""Get the invoice url

		Perform the ProcessOut's request to generate the invoice, and return the
	 	URL to that invoice
		"""
		response = requests.post(self.host + '/invoices/product/' +
			self.productId,
			auth = (self.projectId, self.projectSecret),
			data = self._generateData(),
			verify = True).json()

		if not response['success']:
			raise Exception(response['message'])

		return response['url']

	def _generateData(self):
		"""Generate the data used during the ProcessOut's request"""
		return BaseInvoice._generateData(self)


from .baseinvoice import BaseInvoice
import requests

class ProductInvoice(BaseInvoice):
	def __init__(self, projectId, projectSecret, productId):
		BaseInvoice.__init__(self, projectId, projectSecret)

		self._productId = productId

	@property
	def productId(self):
		return self._productId

	@productId.setter
	def productId(self, value):
		self._productId = value

	def getLink(self):
		response = requests.post(self.host + '/invoices/product/' +
			self.productId,
			auth = (self.projectId, self.projectSecret),
			data = self._generateData(),
			verify = False).json()

		if not response['success']:
			raise Exception(response['message'])

		return response['url']

	def _generateData(self):
		return BaseInvoice._generateData(self)

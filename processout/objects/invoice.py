
from .baseinvoice import BaseInvoice
import requests

class Invoice(BaseInvoice):
	def __init__(self, projectId, projectSecret, itemName, itemAmount,
			itemQuantity, currency):
		BaseInvoice.__init__(self, projectId, projectSecret)

		self._itemName      = itemName
		self._itemAmount    = itemAmount
		self._itemQuantity  = itemQuantity
		self._currency      = currency
		self._taxes         = 0
		self._shipping      = 0
		self._discount      = 0

	@property
	def itemName(self):
		return self._itemName

	@itemName.setter
	def itemName(self, value):
		self._itemName = value

	@property
	def itemAmount(self):
		return self._itemAmount

	@itemAmount.setter
	def itemAmount(self, value):
		self._itemAmount = value

	@property
	def itemQuantity(self):
		return self._itemQuantity

	@itemQuantity.setter
	def itemQuantity(self, value):
		self._itemQuantity = value

	@property
	def currency(self):
		return self._currency

	@currency.setter
	def currency(self, value):
		self._currency = value

	@property
	def taxes(self):
		return self._taxes

	@taxes.setter
	def taxes(self, value):
		self._taxes = value

	@property
	def shipping(self):
		return self._shipping

	@shipping.setter
	def shipping(self, value):
		self._shipping = value

	@property
	def discount(self):
		return self._discount

	@discount.setter
	def discount(self, value):
		self._discount = value

	def getLink(self):
		response = requests.post(self.host + '/invoices/create',
			auth = (self.projectId, self.projectSecret),
			data = self._generateData(),
			verify = False).json()

		if not response['success']:
			raise Exception(response['message'])

		return response['url']

	def _generateData(self):
		data = {
			'item_name':     self.itemName,
			'item_amount':   self.itemAmount,
			'item_quantity': self.itemQuantity,
			'currency':      self.currency,
			'taxes':         self.taxes,
			'shipping':      self.shipping,
			'discount':      self.discount
		}
		data.update(BaseInvoice._generateData(self))
		return data

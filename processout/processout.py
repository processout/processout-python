# processout.py

import hmac
import hashlib
import base64
from .objects.invoice import Invoice
from .objects.productinvoice import ProductInvoice

class ProcessOut:

	def __init__(self, projectId, projectSecret):
		"""Create a new instance of ProcessOut

		Keyword argument:
		projectId -- id of the ProcessOut's project
		projectSecret -- secret key associated to the project
		"""
		self._projectId     = projectId
		self._projectSecret = projectSecret

	def newInvoice(self, itemName, itemAmount, itemQuantity, currency):
		"""Create a new invoice

		Keyword argument:
		itemName -- name of the item
		itemAmount -- amount of the item
		itemQuantity -- quantity of the item
		currency -- currency of the invoice
		"""
		return Invoice(self._projectId, self._projectSecret, itemName,
			itemAmount, itemQuantity, currency)

	def newProductInvoice(self, productId):
		"""Create a new invoie out of a product

		Keyword argument:
		productId -- id of the product
		"""
		return ProductInvoice(self._projectId, self._projectSecret,
			productId)

	def checkCallbackData(self, transactionId, hmacInput):
		"""Perform basic checks on the callback to make sure it's legit

		Keyword argument:
		transactionId -- id of the transaction returned by the callback
		hmacInput -- hmac returned by the callback
		"""
		newhmac = hmac.new(key=bytes(self._projectSecret.encode('utf-8')),
		    msg=transactionId.encode('utf-8'),
		    digestmod=hashlib.sha256).digest()

		return hmac.compare_digest(newhmac, base64.b64decode(hmacInput))

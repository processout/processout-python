# processout.py

import hmac
import base64
from .objects.invoice import Invoice
from .objects.productinvoice import ProductInvoice

class ProcessOut:

	def __init__(self, projectId, projectSecret):
		self._projectId     = projectId
		self._projectSecret = projectSecret

	def newInvoice(self, itemName, itemAmount, itemQuantity, currency):
		return Invoice(self._projectId, self._projectSecret, itemName,
			itemAmount, itemQuantity, currency)

	def newProductInvoice(self, productId):
		return ProductInvoice(self._projectId, self._projectSecret,
			productId)

	def checkCallbackData(self, transactionId, hmacInput):
		newhmac = hmac.new(key=self._projectSecret,
		    msg=transactionId,
		    digestmod=hashlib.sha256).digest()
			
		return hmac.compare_digest(newhmac, base64.b64decode(hmacInput))

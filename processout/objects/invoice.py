
from .baseinvoice import BaseInvoice
import requests

class Invoice(BaseInvoice):
    def __init__(self, projectId, projectSecret, itemName, itemPrice,
            itemQuantity, currency):
        """Create a new instance of a simple invoice

        Keyword argument:
        projectId -- id of the ProcessOut's project
        projectSecret -- secret of the ProcessOut's project
        itemName -- name of the item
        itemPrice -- price of the item
        itemQuantity -- quantity of the item
        currency -- currency of the invoice
        """
        BaseInvoice.__init__(self, projectId, projectSecret)

        self._itemName      = itemName
        self._itemPrice    = itemPrice
        self._itemQuantity  = itemQuantity
        self._currency      = currency
        self._taxes         = 0
        self._shipping      = 0
        self._discount      = 0

    @property
    def itemName(self):
        """Get the name of the item"""
        return self._itemName

    @itemName.setter
    def itemName(self, value):
        """Set the name of the item

        Keyword argument:
        value -- new name of the item
        """
        self._itemName = value

    @property
    def itemPrice(self):
        """Get the price of the item"""
        return self._itemPrice

    @itemPrice.setter
    def itemPrice(self, value):
        """Set the price of the item

        Keyword argument:
        value -- new price of the item
        """
        self._itemPrice = value

    @property
    def itemQuantity(self):
        """Get the quantity of the item"""
        return self._itemQuantity

    @itemQuantity.setter
    def itemQuantity(self, value):
        """Set the quantity of the item

        Keyword argument:
        value -- new quantity of the item
        """
        self._itemQuantity = value

    @property
    def currency(self):
        """Get the currency of the invoice"""
        return self._currency

    @currency.setter
    def currency(self, value):
        """Set the currency of the invoice

        Keyword argument:
        value -- new currency of the invoice
        """
        self._currency = value

    @property
    def taxes(self):
        """Get the taxes applied to the invoice"""
        return self._taxes

    @taxes.setter
    def taxes(self, value):
        """Set the taxes applied to the invoice

        Keyword argument:
        value -- new taxes applied to the invoice
        """
        self._taxes = value

    @property
    def shipping(self):
        """Get the shipping fee applied to the invoice"""
        return self._shipping

    @shipping.setter
    def shipping(self, value):
        """Set the shipping fee applied to the invoice

        Keyword argument:
        value -- new shipping fee applied to the invoice
        """
        self._shipping = value

    @property
    def discount(self):
        """Get the discount already applied to the invoice"""
        return self._discount

    @discount.setter
    def discount(self, value):
        """Set the discount already applied to the invoice

        Keyword argument:
        value -- new discount already applied to the invoice"""
        self._discount = value

    def getLink(self):
        """Get the invoice url

        Perform the ProcessOut's request to generate the invoice, and return the
        URL to that invoice
        """
        response = requests.post(self.host + '/invoices',
            auth = (self.projectId, self.projectSecret),
            data = self._generateData(),
            verify = True).json()

        if not response['success']:
            raise Exception(response['message'])

        return response['url']

    def _generateData(self):
        """Generate the data used during the ProcessOut's request"""
        data = {
            'item_name':     self.itemName,
            'item_price':    self.itemPrice,
            'item_quantity': self.itemQuantity,
            'currency':      self.currency,
            'taxes':         self.taxes,
            'shipping':      self.shipping,
            'discount':      self.discount
        }
        data.update(BaseInvoice._generateData(self))
        return data

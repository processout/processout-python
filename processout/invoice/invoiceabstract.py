# processout.invoice.invoiceabstract

from abc import ABCMeta, abstractmethod

class InvoiceAbstract:
    __metaclass__ = ABCMeta

    def __init__(self, processOut):
        """Create a new instance of InvoiceAbstract

        Keyword argument:
        processOut -- ProcessOut instance
        """
        self._processOut = processOut

        self._itemName      = None
        self._itemPrice     = None
        self._itemQuantity  = None
        self._currency      = None
        self._taxes         = None
        self._shipping      = None
        self._recurringDays = None
        self._returnUrl     = None
        self._cancelUrl     = None
        self._notifyUrl     = None
        self._custom        = None
        self._sandbox       = None

        self._lastResponse = None

    @property
    def projectId(self):
        """Get the ProcessOut's project id"""
        return self._processOut.projectId

    @property
    def projectKey(self):
        """Get the ProcessOut's project key"""
        return self._processOut.projectKey

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
        return self

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
        return self

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
        return self

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
        return self

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
        return self

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
        return self

    @property
    def recurringDays(self):
        """Get the recurring days"""
        return self._recurringDays

    @recurringDays.setter
    def recurringDays(self, value):
        """Set the recurring days

        Keyword argument:
        value -- new recurring days
        """
        self._recurringDays = value
        return self

    @property
    def returnUrl(self):
        """Get the return URL"""
        return self._returnUrl

    @returnUrl.setter
    def returnUrl(self, value):
        """Set the return URL

        Keyword argument:
        value -- new return URL
        """
        self._returnUrl = value
        return self

    @property
    def cancelUrl(self):
        """Get te cancel URL"""
        return self._cancelUrl

    @cancelUrl.setter
    def cancelUrl(self, value):
        """Set the cancel URL

        Keyword argument:
        value -- new cancel URL
        """
        self._cancelUrl = value
        return self

    @property
    def notifyUrl(self):
        """Get the notify URL (used for callbacks)"""
        return self._notifyUrl

    @notifyUrl.setter
    def notifyUrl(self, value):
        """Set the notify URL (used for callbacks)

        Keyword argument:
        value -- new notify URL
        """
        self._notifyUrl = value
        return self

    @property
    def custom(self):
        """Get the custom field value"""
        return self._custom

    @custom.setter
    def custom(self, value):
        """Set the custom field value

        Keyword argument:
        value -- new custom field value
        """
        self._custom = value
        return self

    @property
    def sandbox(self):
        """Get the sandbox field value"""
        return self._sandbox

    @sandbox.setter
    def sandbox(self, value):
        """Set the sandbox field value

        Keyword argument:
        value -- new sandbox field value
        """
        self._sandbox = value
        return self

    def enableSandbox(self):
        """Enable the sandbox mode"""
        self.sandbox = True
        return self

    def disableSandbox(self):
        """Disable the sandbox mode"""
        self.sandbox = False
        return self

    def _generateData(self):
        """Generate the data used during the ProcessOut's request"""
        return {
            'item_name':      self.itemName,
            'item_price':     self.itemPrice,
            'item_quantity':  self.itemQuantity,
            'currency':       self.currency,
            'taxes':          self.taxes,
            'shipping':       self.shipping,
            'recurring_days': self.recurringDays,
            'return_url':     self.returnUrl,
            'cancel_url':     self.cancelUrl,
            'notify_url':     self.notifyUrl,
            'custom':         self.custom,
            'sandbox':        self.sandbox
        }

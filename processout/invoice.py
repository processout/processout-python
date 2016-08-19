try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

from .processout import ProcessOut
from .networking.response import Response

try:
    from .activity import Activity
except ImportError:
    import sys
    Activity = sys.modules[__package__ + '.activity']
try:
    from .authorizationrequest import AuthorizationRequest
except ImportError:
    import sys
    AuthorizationRequest = sys.modules[__package__ + '.authorizationrequest']
try:
    from .customer import Customer
except ImportError:
    import sys
    Customer = sys.modules[__package__ + '.customer']
try:
    from .token import Token
except ImportError:
    import sys
    Token = sys.modules[__package__ + '.token']
try:
    from .event import Event
except ImportError:
    import sys
    Event = sys.modules[__package__ + '.event']
try:
    from .recurringinvoice import RecurringInvoice
except ImportError:
    import sys
    RecurringInvoice = sys.modules[__package__ + '.recurringinvoice']
try:
    from .tailoredinvoice import TailoredInvoice
except ImportError:
    import sys
    TailoredInvoice = sys.modules[__package__ + '.tailoredinvoice']
try:
    from .transaction import Transaction
except ImportError:
    import sys
    Transaction = sys.modules[__package__ + '.transaction']

from .networking.requestprocessoutprivate import RequestProcessoutPrivate


class Invoice:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        self._id = ""
        self._customer = None
        self._recurringInvoice = None
        self._url = ""
        self._name = ""
        self._price = ""
        self._currency = ""
        self._taxes = "0.00"
        self._shipping = "0.00"
        self._requestEmail = False
        self._requestShipping = False
        self._returnUrl = ""
        self._cancelUrl = ""
        self._custom = ""
        self._sandbox = False
        self._createdAt = ""
        
    @property
    def id(self):
        """Get id"""
        return self._id

    @id.setter
    def id(self, val):
        """Set id
        Keyword argument:
        val -- New id value"""
        self._id = val
        return self
    
    @property
    def customer(self):
        """Get customer"""
        return self._customer

    @customer.setter
    def customer(self, val):
        """Set customer
        Keyword argument:
        val -- New customer value"""
        if isinstance(val, Customer):
            self._customer = val
        else:
            obj = Customer(self._instance)
            obj.fillWithData(val)
            self._customer = obj
        return self
    
    @property
    def recurringInvoice(self):
        """Get recurringInvoice"""
        return self._recurringInvoice

    @recurringInvoice.setter
    def recurringInvoice(self, val):
        """Set recurringInvoice
        Keyword argument:
        val -- New recurringInvoice value"""
        if isinstance(val, RecurringInvoice):
            self._recurringInvoice = val
        else:
            obj = RecurringInvoice(self._instance)
            obj.fillWithData(val)
            self._recurringInvoice = obj
        return self
    
    @property
    def url(self):
        """Get url"""
        return self._url

    @url.setter
    def url(self, val):
        """Set url
        Keyword argument:
        val -- New url value"""
        self._url = val
        return self
    
    @property
    def name(self):
        """Get name"""
        return self._name

    @name.setter
    def name(self, val):
        """Set name
        Keyword argument:
        val -- New name value"""
        self._name = val
        return self
    
    @property
    def price(self):
        """Get price"""
        return self._price

    @price.setter
    def price(self, val):
        """Set price
        Keyword argument:
        val -- New price value"""
        self._price = val
        return self
    
    @property
    def currency(self):
        """Get currency"""
        return self._currency

    @currency.setter
    def currency(self, val):
        """Set currency
        Keyword argument:
        val -- New currency value"""
        self._currency = val
        return self
    
    @property
    def taxes(self):
        """Get taxes"""
        return self._taxes

    @taxes.setter
    def taxes(self, val):
        """Set taxes
        Keyword argument:
        val -- New taxes value"""
        self._taxes = val
        return self
    
    @property
    def shipping(self):
        """Get shipping"""
        return self._shipping

    @shipping.setter
    def shipping(self, val):
        """Set shipping
        Keyword argument:
        val -- New shipping value"""
        self._shipping = val
        return self
    
    @property
    def requestEmail(self):
        """Get requestEmail"""
        return self._requestEmail

    @requestEmail.setter
    def requestEmail(self, val):
        """Set requestEmail
        Keyword argument:
        val -- New requestEmail value"""
        self._requestEmail = val
        return self
    
    @property
    def requestShipping(self):
        """Get requestShipping"""
        return self._requestShipping

    @requestShipping.setter
    def requestShipping(self, val):
        """Set requestShipping
        Keyword argument:
        val -- New requestShipping value"""
        self._requestShipping = val
        return self
    
    @property
    def returnUrl(self):
        """Get returnUrl"""
        return self._returnUrl

    @returnUrl.setter
    def returnUrl(self, val):
        """Set returnUrl
        Keyword argument:
        val -- New returnUrl value"""
        self._returnUrl = val
        return self
    
    @property
    def cancelUrl(self):
        """Get cancelUrl"""
        return self._cancelUrl

    @cancelUrl.setter
    def cancelUrl(self, val):
        """Set cancelUrl
        Keyword argument:
        val -- New cancelUrl value"""
        self._cancelUrl = val
        return self
    
    @property
    def custom(self):
        """Get custom"""
        return self._custom

    @custom.setter
    def custom(self, val):
        """Set custom
        Keyword argument:
        val -- New custom value"""
        self._custom = val
        return self
    
    @property
    def sandbox(self):
        """Get sandbox"""
        return self._sandbox

    @sandbox.setter
    def sandbox(self, val):
        """Set sandbox
        Keyword argument:
        val -- New sandbox value"""
        self._sandbox = val
        return self
    
    @property
    def createdAt(self):
        """Get createdAt"""
        return self._createdAt

    @createdAt.setter
    def createdAt(self, val):
        """Set createdAt
        Keyword argument:
        val -- New createdAt value"""
        self._createdAt = val
        return self
    

    def fillWithData(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "id" in data.keys():
            self.id = data["id"]
        if "customer" in data.keys():
            self.customer = data["customer"]
        if "recurring_invoice" in data.keys():
            self.recurringInvoice = data["recurring_invoice"]
        if "url" in data.keys():
            self.url = data["url"]
        if "name" in data.keys():
            self.name = data["name"]
        if "price" in data.keys():
            self.price = data["price"]
        if "currency" in data.keys():
            self.currency = data["currency"]
        if "taxes" in data.keys():
            self.taxes = data["taxes"]
        if "shipping" in data.keys():
            self.shipping = data["shipping"]
        if "request_email" in data.keys():
            self.requestEmail = data["request_email"]
        if "request_shipping" in data.keys():
            self.requestShipping = data["request_shipping"]
        if "return_url" in data.keys():
            self.returnUrl = data["return_url"]
        if "cancel_url" in data.keys():
            self.cancelUrl = data["cancel_url"]
        if "custom" in data.keys():
            self.custom = data["custom"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.createdAt = data["created_at"]
        
        return self

    def customer(self, options = None):
        """Get the customer linked to the invoice.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/invoices/" + quote_plus(self.invoiceId) + "/customers"
        data    = {

        }

        response = Response(request.get(path, data, options))
        body = response.body
        body = body["customer"]
        customer = Customer(instance)
        return customer.fillWithData(body)
        
    def assignCustomer(self, customerId, options = None):
        """Assign a customer to the invoice.
        Keyword argument:
		customerId -- ID of the customer to be linked to the invoice
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/invoices/" + quote_plus(self.invoiceId) + "/customers"
        data    = {
			'customer_id': customerId
        }

        response = Response(request.post(path, data, options))
        body = response.body
        body = body["customer"]
        customer = Customer(instance)
        return customer.fillWithData(body)
        
    def charge(self, tokenId, options = None):
        """Charge the invoice using the given customer token ID.
        Keyword argument:
		tokenId -- ID of the customer token
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/invoices/" + quote_plus(self.invoiceId) + "/tokens/" + quote_plus(tokenId) + "/charges"
        data    = {

        }

        response = Response(request.post(path, data, options))
        return response.success
        
    def tokens(self, options = None):
        """Get all the customer tokens available on the current invoice.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/invoices/" + quote_plus(self.invoiceId) + "/tokens"
        data    = {

        }

        response = Response(request.get(path, data, options))
        a    = []
        body = response.body
        for v in body['tokens']:
            tmp = Token(instance)
            tmp.fillWithData(v)
            a.append(tmp)

        return a
        
    @staticmethod
    def all(options = None):
        """Get all the invoices.
        Keyword argument:
		
        options -- Options for the request"""
        instance = ProcessOut.getDefault()
        request = RequestProcessoutPrivate(instance)
        path    = "/invoices"
        data    = {

        }

        response = Response(request.get(path, data, options))
        a    = []
        body = response.body
        for v in body['invoices']:
            tmp = Invoice(instance)
            tmp.fillWithData(v)
            a.append(tmp)

        return a
        
    def create(self, options = None):
        """Create a new invoice.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/invoices"
        data    = {
			'name': self.name, 
			'price': self.price, 
			'taxes': self.taxes, 
			'shipping': self.shipping, 
			'currency': self.currency, 
			'request_email': self.requestEmail, 
			'request_shipping': self.requestShipping, 
			'return_url': self.returnUrl, 
			'cancel_url': self.cancelUrl, 
			'custom': self.custom
        }

        response = Response(request.post(path, data, options))
        body = response.body
        body = body["invoice"]
        invoice = Invoice(instance)
        return invoice.fillWithData(body)
        
    @staticmethod
    def find(invoiceId, options = None):
        """Find an invoice by its ID.
        Keyword argument:
		invoiceId -- ID of the invoice
        options -- Options for the request"""
        instance = ProcessOut.getDefault()
        request = RequestProcessoutPrivate(instance)
        path    = "/invoices/" + quote_plus(invoiceId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        body = response.body
        body = body["invoice"]
        invoice = Invoice(instance)
        return invoice.fillWithData(body)
        
    def lock(self, options = None):
        """Lock the invoice so it can't be interacted with anymore.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/invoices/" + quote_plus(self.invoiceId) + ""
        data    = {

        }

        response = Response(request.delete(path, data, options))
        return response.success
        
    

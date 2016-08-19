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
    from .invoice import Invoice
except ImportError:
    import sys
    Invoice = sys.modules[__package__ + '.invoice']
try:
    from .recurringinvoice import RecurringInvoice
except ImportError:
    import sys
    RecurringInvoice = sys.modules[__package__ + '.recurringinvoice']
try:
    from .transaction import Transaction
except ImportError:
    import sys
    Transaction = sys.modules[__package__ + '.transaction']

from .networking.requestprocessoutprivate import RequestProcessoutPrivate


class TailoredInvoice:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        self._id = ""
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
        if "created_at" in data.keys():
            self.createdAt = data["created_at"]
        
        return self

    def invoice(self, options = None):
        """Create a new invoice from the tailored invoice.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/tailored-invoices/" + quote_plus(self.tailoredInvoiceId) + "/invoices"
        data    = {

        }

        response = Response(request.post(path, data, options))
        body = response.body
        body = body["invoice"]
        invoice = Invoice(instance)
        return invoice.fillWithData(body)
        
    @staticmethod
    def all(options = None):
        """Get all the tailored invoices.
        Keyword argument:
		
        options -- Options for the request"""
        instance = ProcessOut.getDefault()
        request = RequestProcessoutPrivate(instance)
        path    = "/tailored-invoices"
        data    = {

        }

        response = Response(request.get(path, data, options))
        a    = []
        body = response.body
        for v in body['tailored_invoices']:
            tmp = TailoredInvoice(instance)
            tmp.fillWithData(v)
            a.append(tmp)

        return a
        
    def create(self, options = None):
        """Create a new tailored invoice.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/tailored-invoices"
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
        body = body["tailored_invoice"]
        tailoredInvoice = TailoredInvoice(instance)
        return tailoredInvoice.fillWithData(body)
        
    @staticmethod
    def find(tailoredInvoiceId, options = None):
        """Find a tailored invoice by its ID.
        Keyword argument:
		tailoredInvoiceId -- ID of the tailored invoice
        options -- Options for the request"""
        instance = ProcessOut.getDefault()
        request = RequestProcessoutPrivate(instance)
        path    = "/tailored-invoices/" + quote_plus(tailoredInvoiceId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        body = response.body
        body = body["tailored_invoice"]
        tailoredInvoice = TailoredInvoice(instance)
        return tailoredInvoice.fillWithData(body)
        
    def save(self, options = None):
        """Save the updated tailored invoice attributes.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/tailored-invoices/" + quote_plus(self.tailoredInvoiceId) + ""
        data    = {

        }

        response = Response(request.put(path, data, options))
        body = response.body
        body = body["tailored_invoice"]
        return self.fillWithData(body)
        
    def delete(self, options = None):
        """Delete the tailored invoice.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/tailored-invoices/" + quote_plus(self.tailoredInvoiceId) + ""
        data    = {

        }

        response = Response(request.delete(path, data, options))
        return response.success
        
    

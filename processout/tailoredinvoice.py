try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

from .processout import ProcessOut
from .networking.response import Response

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
    from .customer import Customer
except ImportError:
    import sys
    Customer = sys.modules[__package__ + '.customer']
try:
    from .customertoken import CustomerToken
except ImportError:
    import sys
    CustomerToken = sys.modules[__package__ + '.customertoken']
try:
    from .customeraction import CustomerAction
except ImportError:
    import sys
    CustomerAction = sys.modules[__package__ + '.customeraction']
try:
    from .event import Event
except ImportError:
    import sys
    Event = sys.modules[__package__ + '.event']
try:
    from .project import Project
except ImportError:
    import sys
    Project = sys.modules[__package__ + '.project']
try:
    from .paymentgateway import PaymentGateway
except ImportError:
    import sys
    PaymentGateway = sys.modules[__package__ + '.paymentgateway']
try:
    from .paymentgatewaypublickey import PaymentGatewayPublicKey
except ImportError:
    import sys
    PaymentGatewayPublicKey = sys.modules[__package__ + '.paymentgatewaypublickey']

from .networking.requestprocessoutprivate import RequestProcessoutPrivate
from .networking.requestprocessoutpublic import RequestProcessoutPublic


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
        self._returnUrl = ""
        self._cancelUrl = ""
        
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
        if "return_url" in data.keys():
            self.returnUrl = data["return_url"]
        if "cancel_url" in data.keys():
            self.cancelUrl = data["cancel_url"]
        
        return self

    def invoice(self, options = None):
        """Create an invoice from a tailored invoice.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPublic(instance)
        path    = "/tailored-invoices/" + quote_plus(self.id) + "/invoices"
        data    = {

        }

        response = Response(request.post(path, data, options))
        body = response.body
        body = body["invoice"]
        invoice = Invoice(instance)
        return invoice.fillWithData(body)
        
    @staticmethod
    def all(options = None):
        """List all tailored invoices.
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
			'return_url': self.returnUrl, 
			'cancel_url': self.cancelUrl
        }

        response = Response(request.post(path, data, options))
        body = response.body
        body = body["tailored_invoice"]
        tailoredInvoice = TailoredInvoice(instance)
        return tailoredInvoice.fillWithData(body)
        
    @staticmethod
    def find(id, options = None):
        """Get tailored invoice data.
        Keyword argument:
		id -- Unique ID of your tailored invoice
        options -- Options for the request"""
        instance = ProcessOut.getDefault()
        request = RequestProcessoutPrivate(instance)
        path    = "/tailored-invoices/" + quote_plus(id) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        body = response.body
        body = body["tailored_invoice"]
        return self.fillWithData(body)
        
    def save(self, options = None):
        """Update the tailored invoice data.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/tailored-invoices/" + quote_plus(self.id) + ""
        data    = {
			'return_url': self.returnUrl, 
			'cancel_url': self.cancelUrl, 
			'notify_url': self.notifyUrl, 
			'name': self.name, 
			'price': self.price, 
			'currency': self.currency, 
			'taxes': self.taxes, 
			'shipping': self.shipping
        }

        response = Response(request.put(path, data, options))
        body = response.body
        body = body["tailored_invoice"]
        return self.fillWithData(body)
        
    def delete(self, options = None):
        """Delete a tailored invoice.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/tailored-invoices/" + quote_plus(self.id) + ""
        data    = {

        }

        response = Response(request.delete(path, data, options))
        return response.success
        
    

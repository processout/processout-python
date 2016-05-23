try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

from .processout import ProcessOut
from .networking.response import Response

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


class Invoice:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        self._id = ""
        self._url = ""
        self._name = ""
        self._price = ""
        self._currency = ""
        self._taxes = "0.00"
        self._shipping = "0.00"
        self._requestEmail = False
        self._requestShipping = False
        self._metas = {}
        self._returnUrl = ""
        self._cancelUrl = ""
        self._custom = ""
        
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
    def metas(self):
        """Get metas"""
        return self._metas

    @metas.setter
    def metas(self, val):
        """Set metas
        Keyword argument:
        val -- New metas value"""
        self._metas = val
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
    

    def fillWithData(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "id" in data.keys():
            self.id = data["id"]
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
        if "metas" in data.keys():
            self.metas = data["metas"]
        if "return_url" in data.keys():
            self.returnUrl = data["return_url"]
        if "cancel_url" in data.keys():
            self.cancelUrl = data["cancel_url"]
        if "custom" in data.keys():
            self.custom = data["custom"]
        
        return self

    def create(self, options = None):
        """Create an invoice.
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
			'metas': self.metas, 
			'custom': self.custom
        }

        response = Response(request.post(path, data, options))
        body = response.body
        body = body["invoice"]
        invoice = Invoice(instance)
        return invoice.fillWithData(body)
        
    @staticmethod
    def find(id, options = None):
        """Get the invoice data.
        Keyword argument:
		id -- ID of the invoice
        options -- Options for the request"""
        instance = ProcessOut.getDefault()
        request = RequestProcessoutPublic(instance)
        path    = "/invoices/" + quote_plus(id) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        body = response.body
        body = body["invoice"]
        return self.fillWithData(body)
        
    def customer(self, options = None):
        """Get the customer associated with the current invoice.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/invoices/" + quote_plus(self.id) + "/customers"
        data    = {

        }

        response = Response(request.get(path, data, options))
        body = response.body
        body = body["customer"]
        customer = Customer(instance)
        return customer.fillWithData(body)
        
    def setCustomer(self, customerId, options = None):
        """Link a customer to the invoice.
        Keyword argument:
		customerId -- ID of the customer
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/invoices/" + quote_plus(self.id) + "/customers"
        data    = {
			'customer_id': customerId
        }

        response = Response(request.post(path, data, options))
        body = response.body
        body = body["customer"]
        customer = Customer(instance)
        return customer.fillWithData(body)
        
    def charge(self, token, options = None):
        """Charge using a manually generated payment gateway token.
        Keyword argument:
		token -- Payment gateway token (ex: stripe card token)
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/invoices/" + quote_plus(self.id) + "/gateways/{gateway_name}/charges"
        data    = {
			'token': token
        }

        response = Response(request.post(path, data, options))
        body = response.body
        body = body["customer_action"]
        customerAction = CustomerAction(instance)
        return customerAction.fillWithData(body)
        
    def chargeWithToken(self, tokenId, options = None):
        """Charge using a customer token.
        Keyword argument:
		tokenId -- ID of the customer token
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/invoices/" + quote_plus(self.id) + "/tokens/" + quote_plus(tokenId) + "/charges"
        data    = {

        }

        response = Response(request.post(path, data, options))
        body = response.body
        body = body["customer_action"]
        customerAction = CustomerAction(instance)
        return customerAction.fillWithData(body)
        
    

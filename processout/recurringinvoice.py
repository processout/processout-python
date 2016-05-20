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


class RecurringInvoice:

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
        self._recurringDays = 0
        self._trialDays = 0
        self._ended = False
        self._endedReason = ""
        
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
    def recurringDays(self):
        """Get recurringDays"""
        return self._recurringDays

    @recurringDays.setter
    def recurringDays(self, val):
        """Set recurringDays
        Keyword argument:
        val -- New recurringDays value"""
        self._recurringDays = val
        return self
    
    @property
    def trialDays(self):
        """Get trialDays"""
        return self._trialDays

    @trialDays.setter
    def trialDays(self, val):
        """Set trialDays
        Keyword argument:
        val -- New trialDays value"""
        self._trialDays = val
        return self
    
    @property
    def ended(self):
        """Get ended"""
        return self._ended

    @ended.setter
    def ended(self, val):
        """Set ended
        Keyword argument:
        val -- New ended value"""
        self._ended = val
        return self
    
    @property
    def endedReason(self):
        """Get endedReason"""
        return self._endedReason

    @endedReason.setter
    def endedReason(self, val):
        """Set endedReason
        Keyword argument:
        val -- New endedReason value"""
        self._endedReason = val
        return self
    

    def fillWithData(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "0" in data.keys():
            self.id = data["id"]
        if "1" in data.keys():
            self.url = data["url"]
        if "2" in data.keys():
            self.name = data["name"]
        if "3" in data.keys():
            self.price = data["price"]
        if "4" in data.keys():
            self.currency = data["currency"]
        if "5" in data.keys():
            self.taxes = data["taxes"]
        if "6" in data.keys():
            self.shipping = data["shipping"]
        if "7" in data.keys():
            self.recurringDays = data["recurring_days"]
        if "8" in data.keys():
            self.trialDays = data["trial_days"]
        if "9" in data.keys():
            self.ended = data["ended"]
        if "10" in data.keys():
            self.endedReason = data["ended_reason"]
        

    def invoice(self, options = None):
        """Get the invoice representing the new recurring invoice iteration.
        Keyword argument:
		
        options -- Options for the request"""
        request = RequestProcessoutPublic(self._instance)
        path    = "/recurring-invoices/" + quote_plus(self.id) + "/invoices"
        data    = {

        }

        response = Response(request.get(path, data, options))
        body = response.body
        body = body["invoice"]
        invoice = Invoice(self._instance)
        return invoice.fillWithData(body)
        
    def create(self, customerId, options = None):
        """Create a new recurring invoice.
        Keyword argument:
		customerId -- ID of the customer to which the recurring invoice will be linked
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/customers/" + quote_plus(customerId) + "/recurring-invoices"
        data    = {
			'name': self.name, 
			'price': self.price, 
			'shipping': self.shipping, 
			'taxes': self.taxes, 
			'currency': self.currency, 
			'recurring_days': self.recurringDays, 
			'trial_days': self.trialDays, 
			'return_url': self.returnUrl, 
			'cancel_url': self.cancelUrl, 
			'custom': self.custom
        }

        response = Response(request.post(path, data, options))
        body = response.body
        body = body["recurring_invoice"]
        recurringInvoice = RecurringInvoice(self._instance)
        return recurringInvoice.fillWithData(body)
        
    @staticmethod
    def find(self, id, options = None):
        """Get the recurring invoice data.
        Keyword argument:
		id -- ID of the recurring invoice
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/recurring-invoices/" + quote_plus(id) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        body = response.body
        body = body["recurring_invoice"]
        return self.fillWithData(body)
        
    def end(self, reason, options = None):
        """End a recurring invoice.
        Keyword argument:
		reason -- Ending reason
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/recurring-invoices/" + quote_plus(self.id) + ""
        data    = {
			'reason': reason
        }

        response = Response(request.delete(path, data, options))
        return response.success
        
    def customer(self, options = None):
        """Get the customer linked to the recurring invoice.
        Keyword argument:
		
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/recurring-invoices/" + quote_plus(self.id) + "/customers"
        data    = {

        }

        response = Response(request.get(path, data, options))
        body = response.body
        body = body["customer"]
        customer = Customer(self._instance)
        return customer.fillWithData(body)
        
    

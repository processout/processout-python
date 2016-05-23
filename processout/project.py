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


class Project:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        self._name = ""
        self._email = ""
        self._logoUrl = ""
        self._id = ""
        self._secretKey = ""
        
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
    def email(self):
        """Get email"""
        return self._email

    @email.setter
    def email(self, val):
        """Set email
        Keyword argument:
        val -- New email value"""
        self._email = val
        return self
    
    @property
    def logoUrl(self):
        """Get logoUrl"""
        return self._logoUrl

    @logoUrl.setter
    def logoUrl(self, val):
        """Set logoUrl
        Keyword argument:
        val -- New logoUrl value"""
        self._logoUrl = val
        return self
    
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
    def secretKey(self):
        """Get secretKey"""
        return self._secretKey

    @secretKey.setter
    def secretKey(self, val):
        """Set secretKey
        Keyword argument:
        val -- New secretKey value"""
        self._secretKey = val
        return self
    

    def fillWithData(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "name" in data.keys():
            self.name = data["name"]
        if "email" in data.keys():
            self.email = data["email"]
        if "logo_url" in data.keys():
            self.logoUrl = data["logo_url"]
        if "id" in data.keys():
            self.id = data["id"]
        if "secret_key" in data.keys():
            self.secretKey = data["secret_key"]
        
        return self

    def createSupervised(self, options = None):
        """Create a new supervised project which will belong to current project.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/projects/supervised"
        data    = {
			'name': self.name, 
			'email': self.email, 
			'logo_url': self.logoUrl
        }

        response = Response(request.post(path, data, options))
        body = response.body
        body = body["project"]
        return self.fillWithData(body)
        
    

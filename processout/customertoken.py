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


class CustomerToken:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        self._id = ""
        self._name = ""
        self._gateway = ""
        
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
    def gateway(self):
        """Get gateway"""
        return self._gateway

    @gateway.setter
    def gateway(self, val):
        """Set gateway
        Keyword argument:
        val -- New gateway value"""
        self._gateway = val
        return self
    

    def fillWithData(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "id" in data.keys():
            self.id = data["id"]
        if "name" in data.keys():
            self.name = data["name"]
        if "gateway" in data.keys():
            self.gateway = data["gateway"]
        
        return self

    

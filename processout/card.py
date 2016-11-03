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
    from .coupon import Coupon
except ImportError:
    import sys
    Coupon = sys.modules[__package__ + '.coupon']
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
    from .discount import Discount
except ImportError:
    import sys
    Discount = sys.modules[__package__ + '.discount']
try:
    from .event import Event
except ImportError:
    import sys
    Event = sys.modules[__package__ + '.event']
try:
    from .gateway import Gateway
except ImportError:
    import sys
    Gateway = sys.modules[__package__ + '.gateway']
try:
    from .gatewayconfiguration import GatewayConfiguration
except ImportError:
    import sys
    GatewayConfiguration = sys.modules[__package__ + '.gatewayconfiguration']
try:
    from .invoice import Invoice
except ImportError:
    import sys
    Invoice = sys.modules[__package__ + '.invoice']
try:
    from .customeraction import CustomerAction
except ImportError:
    import sys
    CustomerAction = sys.modules[__package__ + '.customeraction']
try:
    from .plan import Plan
except ImportError:
    import sys
    Plan = sys.modules[__package__ + '.plan']
try:
    from .product import Product
except ImportError:
    import sys
    Product = sys.modules[__package__ + '.product']
try:
    from .project import Project
except ImportError:
    import sys
    Project = sys.modules[__package__ + '.project']
try:
    from .refund import Refund
except ImportError:
    import sys
    Refund = sys.modules[__package__ + '.refund']
try:
    from .subscription import Subscription
except ImportError:
    import sys
    Subscription = sys.modules[__package__ + '.subscription']
try:
    from .transaction import Transaction
except ImportError:
    import sys
    Transaction = sys.modules[__package__ + '.transaction']
try:
    from .webhook import Webhook
except ImportError:
    import sys
    Webhook = sys.modules[__package__ + '.webhook']

from .networking.requestprocessoutprivate import RequestProcessoutPrivate


# The content of this file was automatically generated

class Card:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        self._id = ""
        self._project = None
        self._brand = ""
        self._type = ""
        self._bankName = ""
        self._level = ""
        self._iin = ""
        self._last4Digits = ""
        self._expMonth = 0
        self._expYear = 0
        self._metadata = {}
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
    def project(self):
        """Get project"""
        return self._project

    @project.setter
    def project(self, val):
        """Set project
        Keyword argument:
        val -- New project value"""
        if isinstance(val, Project):
            self._project = val
        else:
            obj = Project(self._instance)
            obj.fillWithData(val)
            self._project = obj
        return self
    
    @property
    def brand(self):
        """Get brand"""
        return self._brand

    @brand.setter
    def brand(self, val):
        """Set brand
        Keyword argument:
        val -- New brand value"""
        self._brand = val
        return self
    
    @property
    def type(self):
        """Get type"""
        return self._type

    @type.setter
    def type(self, val):
        """Set type
        Keyword argument:
        val -- New type value"""
        self._type = val
        return self
    
    @property
    def bankName(self):
        """Get bankName"""
        return self._bankName

    @bankName.setter
    def bankName(self, val):
        """Set bankName
        Keyword argument:
        val -- New bankName value"""
        self._bankName = val
        return self
    
    @property
    def level(self):
        """Get level"""
        return self._level

    @level.setter
    def level(self, val):
        """Set level
        Keyword argument:
        val -- New level value"""
        self._level = val
        return self
    
    @property
    def iin(self):
        """Get iin"""
        return self._iin

    @iin.setter
    def iin(self, val):
        """Set iin
        Keyword argument:
        val -- New iin value"""
        self._iin = val
        return self
    
    @property
    def last4Digits(self):
        """Get last4Digits"""
        return self._last4Digits

    @last4Digits.setter
    def last4Digits(self, val):
        """Set last4Digits
        Keyword argument:
        val -- New last4Digits value"""
        self._last4Digits = val
        return self
    
    @property
    def expMonth(self):
        """Get expMonth"""
        return self._expMonth

    @expMonth.setter
    def expMonth(self, val):
        """Set expMonth
        Keyword argument:
        val -- New expMonth value"""
        self._expMonth = val
        return self
    
    @property
    def expYear(self):
        """Get expYear"""
        return self._expYear

    @expYear.setter
    def expYear(self, val):
        """Set expYear
        Keyword argument:
        val -- New expYear value"""
        self._expYear = val
        return self
    
    @property
    def metadata(self):
        """Get metadata"""
        return self._metadata

    @metadata.setter
    def metadata(self, val):
        """Set metadata
        Keyword argument:
        val -- New metadata value"""
        self._metadata = val
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
        if "project" in data.keys():
            self.project = data["project"]
        if "brand" in data.keys():
            self.brand = data["brand"]
        if "type" in data.keys():
            self.type = data["type"]
        if "bank_name" in data.keys():
            self.bankName = data["bank_name"]
        if "level" in data.keys():
            self.level = data["level"]
        if "iin" in data.keys():
            self.iin = data["iin"]
        if "last_4_digits" in data.keys():
            self.last4Digits = data["last_4_digits"]
        if "exp_month" in data.keys():
            self.expMonth = data["exp_month"]
        if "exp_year" in data.keys():
            self.expYear = data["exp_year"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.createdAt = data["created_at"]
        
        return self

    

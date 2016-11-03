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
    from .card import Card
except ImportError:
    import sys
    Card = sys.modules[__package__ + '.card']
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
    from .webhook import Webhook
except ImportError:
    import sys
    Webhook = sys.modules[__package__ + '.webhook']

from .networking.requestprocessoutprivate import RequestProcessoutPrivate


# The content of this file was automatically generated

class Transaction:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        self._id = ""
        self._project = None
        self._subscription = None
        self._customer = None
        self._token = None
        self._card = None
        self._name = ""
        self._authorizedAmount = ""
        self._capturedAmount = ""
        self._currency = ""
        self._status = ""
        self._authorized = False
        self._captured = False
        self._processoutFee = ""
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
    def subscription(self):
        """Get subscription"""
        return self._subscription

    @subscription.setter
    def subscription(self, val):
        """Set subscription
        Keyword argument:
        val -- New subscription value"""
        if isinstance(val, Subscription):
            self._subscription = val
        else:
            obj = Subscription(self._instance)
            obj.fillWithData(val)
            self._subscription = obj
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
    def token(self):
        """Get token"""
        return self._token

    @token.setter
    def token(self, val):
        """Set token
        Keyword argument:
        val -- New token value"""
        if isinstance(val, Token):
            self._token = val
        else:
            obj = Token(self._instance)
            obj.fillWithData(val)
            self._token = obj
        return self
    
    @property
    def card(self):
        """Get card"""
        return self._card

    @card.setter
    def card(self, val):
        """Set card
        Keyword argument:
        val -- New card value"""
        if isinstance(val, Card):
            self._card = val
        else:
            obj = Card(self._instance)
            obj.fillWithData(val)
            self._card = obj
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
    def authorizedAmount(self):
        """Get authorizedAmount"""
        return self._authorizedAmount

    @authorizedAmount.setter
    def authorizedAmount(self, val):
        """Set authorizedAmount
        Keyword argument:
        val -- New authorizedAmount value"""
        self._authorizedAmount = val
        return self
    
    @property
    def capturedAmount(self):
        """Get capturedAmount"""
        return self._capturedAmount

    @capturedAmount.setter
    def capturedAmount(self, val):
        """Set capturedAmount
        Keyword argument:
        val -- New capturedAmount value"""
        self._capturedAmount = val
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
    def status(self):
        """Get status"""
        return self._status

    @status.setter
    def status(self, val):
        """Set status
        Keyword argument:
        val -- New status value"""
        self._status = val
        return self
    
    @property
    def authorized(self):
        """Get authorized"""
        return self._authorized

    @authorized.setter
    def authorized(self, val):
        """Set authorized
        Keyword argument:
        val -- New authorized value"""
        self._authorized = val
        return self
    
    @property
    def captured(self):
        """Get captured"""
        return self._captured

    @captured.setter
    def captured(self, val):
        """Set captured
        Keyword argument:
        val -- New captured value"""
        self._captured = val
        return self
    
    @property
    def processoutFee(self):
        """Get processoutFee"""
        return self._processoutFee

    @processoutFee.setter
    def processoutFee(self, val):
        """Set processoutFee
        Keyword argument:
        val -- New processoutFee value"""
        self._processoutFee = val
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
        if "subscription" in data.keys():
            self.subscription = data["subscription"]
        if "customer" in data.keys():
            self.customer = data["customer"]
        if "token" in data.keys():
            self.token = data["token"]
        if "card" in data.keys():
            self.card = data["card"]
        if "name" in data.keys():
            self.name = data["name"]
        if "authorized_amount" in data.keys():
            self.authorizedAmount = data["authorized_amount"]
        if "captured_amount" in data.keys():
            self.capturedAmount = data["captured_amount"]
        if "currency" in data.keys():
            self.currency = data["currency"]
        if "status" in data.keys():
            self.status = data["status"]
        if "authorized" in data.keys():
            self.authorized = data["authorized"]
        if "captured" in data.keys():
            self.captured = data["captured"]
        if "processout_fee" in data.keys():
            self.processoutFee = data["processout_fee"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.createdAt = data["created_at"]
        
        return self

    def refunds(self, options = None):
        """Get the transaction's refunds.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/transactions/" + quote_plus(self.id) + "/refunds"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        a    = []
        body = response.body
        for v in body['refunds']:
            tmp = Refund(instance)
            tmp.fillWithData(v)
            a.append(tmp)

        returnValues.append(a)
            

        return tuple(returnValues)

    @staticmethod
    def all(options = None):
        """Get all the transactions.
        Keyword argument:
		
        options -- Options for the request"""
        instance = ProcessOut.getDefault()
        request = RequestProcessoutPrivate(instance)
        path    = "/transactions"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        a    = []
        body = response.body
        for v in body['transactions']:
            tmp = Transaction(instance)
            tmp.fillWithData(v)
            a.append(tmp)

        returnValues.append(a)
            

        return tuple(returnValues)

    @staticmethod
    def find(transactionId, options = None):
        """Find a transaction by its ID.
        Keyword argument:
		transactionId -- ID of the transaction
        options -- Options for the request"""
        instance = ProcessOut.getDefault()
        request = RequestProcessoutPrivate(instance)
        path    = "/transactions/" + quote_plus(transactionId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["transaction"]
                
                
        obj = Transaction()
        returnValues.append(obj.fillWithData(body))
                

        return tuple(returnValues)

    

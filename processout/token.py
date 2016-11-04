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

class Token:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        self._id = ""
        self._customer = None
        self._metadata = {}
        self._isSubscriptionOnly = False
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
    def isSubscriptionOnly(self):
        """Get isSubscriptionOnly"""
        return self._isSubscriptionOnly

    @isSubscriptionOnly.setter
    def isSubscriptionOnly(self, val):
        """Set isSubscriptionOnly
        Keyword argument:
        val -- New isSubscriptionOnly value"""
        self._isSubscriptionOnly = val
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
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "is_subscription_only" in data.keys():
            self.isSubscriptionOnly = data["is_subscription_only"]
        if "created_at" in data.keys():
            self.createdAt = data["created_at"]
        
        return self

    @staticmethod
    def find(customerId, tokenId, options = None):
        """Find a customer's token by its ID.
        Keyword argument:
        customerId -- ID of the customer
        tokenId -- ID of the token
        options -- Options for the request"""
        instance = ProcessOut.getDefault()
        request = RequestProcessoutPrivate(instance)
        path    = "/customers/" + quote_plus(customerId) + "/tokens/" + quote_plus(tokenId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["token"]
                
                
        obj = Token()
        returnValues.append(obj.fillWithData(body))
                

        return tuple(returnValues)

    def create(self, customerId, source, options = None):
        """Create a new token for the given customer ID.
        Keyword argument:
        customerId -- ID of the customer
        source -- Source used to create the token (most likely a card token generated by ProcessOut.js)
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/customers/" + quote_plus(customerId) + "/tokens"
        data    = {
            'metadata': self.metadata, 
            'source': source
        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["token"]
                
                
        returnValues.append(self.fillWithData(body))
                

        return tuple(returnValues)

    def createFromRequest(self, customerId, source, target, options = None):
        """Create a new token for the given customer ID from an authorization request
        Keyword argument:
        customerId -- ID of the customer
        source -- Source used to create the token (most likely a card token generated by ProcessOut.js)
        target -- Authorization request ID
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/customers/" + quote_plus(customerId) + "/tokens"
        data    = {
            'metadata': self.metadata, 
            'source': source, 
            'target': target
        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["token"]
                
                
        returnValues.append(self.fillWithData(body))
                

        return tuple(returnValues)

    

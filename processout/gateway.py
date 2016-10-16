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


class Gateway:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        self._id = ""
        self._name = ""
        self._displayName = ""
        self._logoUrl = ""
        self._url = ""
        self._flows = []
        self._tags = []
        self._description = ""
        
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
    def displayName(self):
        """Get displayName"""
        return self._displayName

    @displayName.setter
    def displayName(self, val):
        """Set displayName
        Keyword argument:
        val -- New displayName value"""
        self._displayName = val
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
    def flows(self):
        """Get flows"""
        return self._flows

    @flows.setter
    def flows(self, val):
        """Set flows
        Keyword argument:
        val -- New flows value"""
        self._flows = val
        return self
    
    @property
    def tags(self):
        """Get tags"""
        return self._tags

    @tags.setter
    def tags(self, val):
        """Set tags
        Keyword argument:
        val -- New tags value"""
        self._tags = val
        return self
    
    @property
    def description(self):
        """Get description"""
        return self._description

    @description.setter
    def description(self, val):
        """Set description
        Keyword argument:
        val -- New description value"""
        self._description = val
        return self
    

    def fillWithData(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "id" in data.keys():
            self.id = data["id"]
        if "name" in data.keys():
            self.name = data["name"]
        if "display_name" in data.keys():
            self.displayName = data["display_name"]
        if "logo_url" in data.keys():
            self.logoUrl = data["logo_url"]
        if "url" in data.keys():
            self.url = data["url"]
        if "flows" in data.keys():
            self.flows = data["flows"]
        if "tags" in data.keys():
            self.tags = data["tags"]
        if "description" in data.keys():
            self.description = data["description"]
        
        return self

    

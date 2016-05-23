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
    from .project import Project
except ImportError:
    import sys
    Project = sys.modules[__package__ + '.project']
try:
    from .paymentgatewaypublickey import PaymentGatewayPublicKey
except ImportError:
    import sys
    PaymentGatewayPublicKey = sys.modules[__package__ + '.paymentgatewaypublickey']

from .networking.requestprocessoutprivate import RequestProcessoutPrivate
from .networking.requestprocessoutpublic import RequestProcessoutPublic


class PaymentGateway:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        self._name = ""
        self._displayName = ""
        self._beta = False
        self._publicKeys = []
        self._settings = {}
        
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
    def beta(self):
        """Get beta"""
        return self._beta

    @beta.setter
    def beta(self, val):
        """Set beta
        Keyword argument:
        val -- New beta value"""
        self._beta = val
        return self
    
    @property
    def publicKeys(self):
        """Get publicKeys"""
        return self._publicKeys

    @publicKeys.setter
    def publicKeys(self, val):
        """Set publicKeys
        Keyword argument:
        val -- New publicKeys value"""
        if len(val) > 0 and isinstance(val[0], PaymentGatewayPublicKey):
            self._publicKeys = val
        else:
            l = []
            for v in val:
                obj = PaymentGatewayPublicKey(self._instance)
                obj.fillWithData(v)
                l.append(obj)
            self._publicKeys = l
        return self
    
    @property
    def settings(self):
        """Get settings"""
        return self._settings

    @settings.setter
    def settings(self, val):
        """Set settings
        Keyword argument:
        val -- New settings value"""
        self._settings = val
        return self
    

    def fillWithData(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "name" in data.keys():
            self.name = data["name"]
        if "display_name" in data.keys():
            self.displayName = data["display_name"]
        if "beta" in data.keys():
            self.beta = data["beta"]
        if "public_keys" in data.keys():
            self.publicKeys = data["public_keys"]
        if "settings" in data.keys():
            self.settings = data["settings"]
        
        return self

    def save(self, gatewayName, options = None):
        """Update or set the payment gateway settings.
        Keyword argument:
		gatewayName -- Name of the payment gateway (ex: paypal)
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/gateways/" + quote_plus(gatewayName) + ""
        data    = {
			'settings': self.settings
        }

        response = Response(request.put(path, data, options))
        body = response.body
        body = body["gateway"]
        paymentGateway = PaymentGateway(self._instance)
        return paymentGateway.fillWithData(body)
        
    @staticmethod
    def delete(gatewayName, options = None):
        """Remove the payment gateway and its settings from the current project.
        Keyword argument:
		gatewayName -- Name of the payment gateway (ex: paypal)
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/gateways/" + quote_plus(gatewayName) + ""
        data    = {

        }

        response = Response(request.delete(path, data, options))
        return response.success
        
    

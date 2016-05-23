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


class Event:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        self._id = ""
        self._name = ""
        self._data = {}
        self._date = ""
        self._sandbox = False
        
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
    def data(self):
        """Get data"""
        return self._data

    @data.setter
    def data(self, val):
        """Set data
        Keyword argument:
        val -- New data value"""
        self._data = val
        return self
    
    @property
    def date(self):
        """Get date"""
        return self._date

    @date.setter
    def date(self, val):
        """Set date
        Keyword argument:
        val -- New date value"""
        self._date = val
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
    

    def fillWithData(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "id" in data.keys():
            self.id = data["id"]
        if "name" in data.keys():
            self.name = data["name"]
        if "data" in data.keys():
            self.data = data["data"]
        if "date" in data.keys():
            self.date = data["date"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        
        return self

    @staticmethod
    def pull(options = None):
        """Get the 15 oldest events pending processing.
        Keyword argument:
		
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/events"
        data    = {

        }

        response = Response(request.get(path, data, options))
        a    = []
        body = response.body
        for v in body['events']:
            tmp = Event(self._instance)
            tmp.fillWithData(v)
            a.append(tmp)

        return a
        
    @staticmethod
    def setAllProcessed(options = None):
        """Set all the events as processed.
        Keyword argument:
		
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/events"
        data    = {

        }

        response = Response(request.delete(path, data, options))
        return response.success
        
    @staticmethod
    def find(id, options = None):
        """Get the information related to the specific event.
        Keyword argument:
		id -- ID of the event
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/events/" + quote_plus(id) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        body = response.body
        body = body["event"]
        return self.fillWithData(body)
        
    def markProcessed(self, options = None):
        """Set the specific event as processed.
        Keyword argument:
		
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/events/" + quote_plus(self.id) + ""
        data    = {

        }

        response = Response(request.delete(path, data, options))
        return response.success
        
    

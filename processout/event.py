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
    from .transaction import Transaction
except ImportError:
    import sys
    Transaction = sys.modules[__package__ + '.transaction']

from .networking.requestprocessoutprivate import RequestProcessoutPrivate


class Event:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        self._id = ""
        self._name = ""
        self._data = {}
        self._processed = False
        self._sandbox = False
        self._firedAt = ""
        
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
    def processed(self):
        """Get processed"""
        return self._processed

    @processed.setter
    def processed(self, val):
        """Set processed
        Keyword argument:
        val -- New processed value"""
        self._processed = val
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
    def firedAt(self):
        """Get firedAt"""
        return self._firedAt

    @firedAt.setter
    def firedAt(self, val):
        """Set firedAt
        Keyword argument:
        val -- New firedAt value"""
        self._firedAt = val
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
        if "processed" in data.keys():
            self.processed = data["processed"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "fired_at" in data.keys():
            self.firedAt = data["fired_at"]
        
        return self

    def webhooks(self, options = None):
        """Get all the webhooks of the event.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/events/" + quote_plus(self.eventId) + "/webhooks"
        data    = {

        }

        response = Response(request.get(path, data, options))
        a    = []
        body = response.body
        for v in body['webhooks']:
            tmp = Webhook(instance)
            tmp.fillWithData(v)
            a.append(tmp)

        return a
        
    @staticmethod
    def all(options = None):
        """Get all the events.
        Keyword argument:
		
        options -- Options for the request"""
        instance = ProcessOut.getDefault()
        request = RequestProcessoutPrivate(instance)
        path    = "/events"
        data    = {

        }

        response = Response(request.get(path, data, options))
        a    = []
        body = response.body
        for v in body['events']:
            tmp = Event(instance)
            tmp.fillWithData(v)
            a.append(tmp)

        return a
        
    @staticmethod
    def find(eventId, options = None):
        """Find an event by its ID.
        Keyword argument:
		eventId -- ID of the event
        options -- Options for the request"""
        instance = ProcessOut.getDefault()
        request = RequestProcessoutPrivate(instance)
        path    = "/events/" + quote_plus(eventId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        body = response.body
        body = body["event"]
        event = Event(instance)
        return event.fillWithData(body)
        
    def markProcessed(self, options = None):
        """Mark the event as processed.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/events/" + quote_plus(self.eventId) + ""
        data    = {

        }

        response = Response(request.put(path, data, options))
        return response.success
        
    

from urllib.parse import quote_plus

from .processout import ProcessOut
from .networking.response import Response

from .networking.requestprocessoutprivate import RequestProcessoutPrivate

from .networking.requestprocessoutpublic import RequestProcessoutPublic


class Event:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        
        self._data = {}
        
        self._date = ""
        
        self._id = ""
        
        self._name = ""
        
        self._sandbox = False
        

    
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
    

    def fillWithData(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        
        if "data" in data.keys():
            self.data = data["data"]
        
        if "date" in data.keys():
            self.date = data["date"]
        
        if "id" in data.keys():
            self.id = data["id"]
        
        if "name" in data.keys():
            self.name = data["name"]
        
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        

    
    
    @staticmethod
    
    def pull(self):
        """Get the 15 oldest events pending processing.
        Keyword argument:
		"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/events"
        data    = {

        }

        
        response = Response(request.get(path, data))
        

        
        a    = []
        body = response.body
        for v in body['events']:
            tmp = Event($this->instance)
            tmp.fillWithData(v)
            a.append(tmp)

        return a;
        
    
    
    @staticmethod
    
    def setAllProcessed(self):
        """Set all the events as processed.
        Keyword argument:
		"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/events"
        data    = {

        }

        
        response = Response(request.delete(path, data))
        

        
        return response.success
        
    
    
    @staticmethod
    
    def find(self, id):
        """Get the information related to the specific event.
        Keyword argument:
		id -- Unique ID of the event"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/events/" + quote_plus(id) + ""
        data    = {

        }

        
        response = Response(request.get(path, data))
        

        
        return self.fillWithData(response.body)
        
    
    
    def markProcessed(self):
        """Set the specific event as processed.
        Keyword argument:
		"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/events/" + quote_plus(self.id) + ""
        data    = {

        }

        
        response = Response(request.delete(path, data))
        

        
        return response.success
        
    

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Card(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = None
        self._project = None
        self._scheme = None
        self._type = None
        self._bank_name = None
        self._brand = None
        self._iin = None
        self._last_4_digits = None
        self._exp_month = None
        self._exp_year = None
        self._metadata = None
        self._sandbox = None
        self._created_at = None
        if prefill != None:
            self.fill_with_data(prefill)

    
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
        if isinstance(val, dict):
            obj = processout.Project(self._client)
            obj.fill_with_data(val)
            self._project = obj
        else:
            self._project = val
        return self
    
    @property
    def scheme(self):
        """Get scheme"""
        return self._scheme

    @scheme.setter
    def scheme(self, val):
        """Set scheme
        Keyword argument:
        val -- New scheme value"""
        self._scheme = val
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
    def bank_name(self):
        """Get bank_name"""
        return self._bank_name

    @bank_name.setter
    def bank_name(self, val):
        """Set bank_name
        Keyword argument:
        val -- New bank_name value"""
        self._bank_name = val
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
    def last_4_digits(self):
        """Get last_4_digits"""
        return self._last_4_digits

    @last_4_digits.setter
    def last_4_digits(self, val):
        """Set last_4_digits
        Keyword argument:
        val -- New last_4_digits value"""
        self._last_4_digits = val
        return self
    
    @property
    def exp_month(self):
        """Get exp_month"""
        return self._exp_month

    @exp_month.setter
    def exp_month(self, val):
        """Set exp_month
        Keyword argument:
        val -- New exp_month value"""
        self._exp_month = val
        return self
    
    @property
    def exp_year(self):
        """Get exp_year"""
        return self._exp_year

    @exp_year.setter
    def exp_year(self, val):
        """Set exp_year
        Keyword argument:
        val -- New exp_year value"""
        self._exp_year = val
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
    def created_at(self):
        """Get created_at"""
        return self._created_at

    @created_at.setter
    def created_at(self, val):
        """Set created_at
        Keyword argument:
        val -- New created_at value"""
        self._created_at = val
        return self
    

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "id" in data.keys():
            self.id = data["id"]
        if "project" in data.keys():
            self.project = data["project"]
        if "scheme" in data.keys():
            self.scheme = data["scheme"]
        if "type" in data.keys():
            self.type = data["type"]
        if "bank_name" in data.keys():
            self.bank_name = data["bank_name"]
        if "brand" in data.keys():
            self.brand = data["brand"]
        if "iin" in data.keys():
            self.iin = data["iin"]
        if "last_4_digits" in data.keys():
            self.last_4_digits = data["last_4_digits"]
        if "exp_month" in data.keys():
            self.exp_month = data["exp_month"]
        if "exp_year" in data.keys():
            self.exp_year = data["exp_year"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        
        return self

    

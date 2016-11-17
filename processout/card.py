try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Card:
    def __init__(self, client, prefill = None):
        self._client = client

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
        if prefill != None:
            self.fillWithData(prefill)

    
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
            obj = processout.Project(self._client)
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

    

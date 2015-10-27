from urllib.parse import quote_plus

from .processout import ProcessOut
from .networking.response import Response

from .networking.requestprocessoutprivate import RequestProcessoutPrivate

from .networking.requestprocessoutpublic import RequestProcessoutPublic


class Project:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        
        self._email = ""
        
        self._id = ""
        
        self._logoUrl = ""
        
        self._name = ""
        
        self._secretKey = ""
        

    
    @property
    def email(self):
        """Get email"""
        return self._email

    @email.setter
    def email(self, val):
        """Set email
        Keyword argument:
        val -- New email value"""
        self._email = val
    
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
    def logoUrl(self):
        """Get logoUrl"""
        return self._logoUrl

    @logoUrl.setter
    def logoUrl(self, val):
        """Set logoUrl
        Keyword argument:
        val -- New logoUrl value"""
        self._logoUrl = val
    
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
    def secretKey(self):
        """Get secretKey"""
        return self._secretKey

    @secretKey.setter
    def secretKey(self, val):
        """Set secretKey
        Keyword argument:
        val -- New secretKey value"""
        self._secretKey = val
    

    def fillWithData(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        
        if "email" in data.keys():
            self.email = data["email"]
        
        if "id" in data.keys():
            self.id = data["id"]
        
        if "logo_url" in data.keys():
            self.logoUrl = data["logo_url"]
        
        if "name" in data.keys():
            self.name = data["name"]
        
        if "secret_key" in data.keys():
            self.secretKey = data["secret_key"]
        

    
    
    def createSupervised(self):
        """Create a new supervised project which will belong to current project.
        Keyword argument:
		"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/projects/supervised"
        data    = {
			'name': self.name, 
			'email': self.email, 
			'logo_url': self.logoUrl
        }

        
        response = Response(request.post(path, data))
        

        
        return self.fillWithData(response.body)
        
    

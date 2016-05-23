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


class Customer:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        self._id = ""
        self._firstName = ""
        self._lastName = ""
        self._address1 = ""
        self._address2 = ""
        self._city = ""
        self._state = ""
        self._zip = ""
        self._countryCode = ""
        
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
    def firstName(self):
        """Get firstName"""
        return self._firstName

    @firstName.setter
    def firstName(self, val):
        """Set firstName
        Keyword argument:
        val -- New firstName value"""
        self._firstName = val
        return self
    
    @property
    def lastName(self):
        """Get lastName"""
        return self._lastName

    @lastName.setter
    def lastName(self, val):
        """Set lastName
        Keyword argument:
        val -- New lastName value"""
        self._lastName = val
        return self
    
    @property
    def address1(self):
        """Get address1"""
        return self._address1

    @address1.setter
    def address1(self, val):
        """Set address1
        Keyword argument:
        val -- New address1 value"""
        self._address1 = val
        return self
    
    @property
    def address2(self):
        """Get address2"""
        return self._address2

    @address2.setter
    def address2(self, val):
        """Set address2
        Keyword argument:
        val -- New address2 value"""
        self._address2 = val
        return self
    
    @property
    def city(self):
        """Get city"""
        return self._city

    @city.setter
    def city(self, val):
        """Set city
        Keyword argument:
        val -- New city value"""
        self._city = val
        return self
    
    @property
    def state(self):
        """Get state"""
        return self._state

    @state.setter
    def state(self, val):
        """Set state
        Keyword argument:
        val -- New state value"""
        self._state = val
        return self
    
    @property
    def zip(self):
        """Get zip"""
        return self._zip

    @zip.setter
    def zip(self, val):
        """Set zip
        Keyword argument:
        val -- New zip value"""
        self._zip = val
        return self
    
    @property
    def countryCode(self):
        """Get countryCode"""
        return self._countryCode

    @countryCode.setter
    def countryCode(self, val):
        """Set countryCode
        Keyword argument:
        val -- New countryCode value"""
        self._countryCode = val
        return self
    

    def fillWithData(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "id" in data.keys():
            self.id = data["id"]
        if "first_name" in data.keys():
            self.firstName = data["first_name"]
        if "last_name" in data.keys():
            self.lastName = data["last_name"]
        if "address1" in data.keys():
            self.address1 = data["address1"]
        if "address2" in data.keys():
            self.address2 = data["address2"]
        if "city" in data.keys():
            self.city = data["city"]
        if "state" in data.keys():
            self.state = data["state"]
        if "zip" in data.keys():
            self.zip = data["zip"]
        if "country_code" in data.keys():
            self.countryCode = data["country_code"]
        
        return self

    @staticmethod
    def all(options = None):
        """Get the customers list belonging to the project.
        Keyword argument:
		
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/customers"
        data    = {

        }

        response = Response(request.get(path, data, options))
        a    = []
        body = response.body
        for v in body['customers']:
            tmp = Customer(self._instance)
            tmp.fillWithData(v)
            a.append(tmp)

        return a
        
    def create(self, options = None):
        """Create a new customer.
        Keyword argument:
		
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/customers"
        data    = {
			'email': self.email, 
			'first_name': self.firstName, 
			'last_name': self.lastName, 
			'address1': self.address1, 
			'address2': self.address2, 
			'city': self.city, 
			'zip': self.zip, 
			'country_code': self.countryCode
        }

        response = Response(request.post(path, data, options))
        body = response.body
        body = body["customer"]
        customer = Customer(self._instance)
        return customer.fillWithData(body)
        
    @staticmethod
    def find(id, options = None):
        """Get the customer data.
        Keyword argument:
		id -- ID of the customer
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/customers/" + quote_plus(id) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        body = response.body
        body = body["customer"]
        return self.fillWithData(body)
        
    def save(self, options = None):
        """Update the customer data.
        Keyword argument:
		
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/customers/" + quote_plus(self.id) + ""
        data    = {
			'email': self.email, 
			'first_name': self.firstName, 
			'last_name': self.lastName, 
			'address1': self.address1, 
			'address2': self.address2, 
			'city': self.city, 
			'zip': self.zip, 
			'country_code': self.countryCode
        }

        response = Response(request.post(path, data, options))
        body = response.body
        body = body["customer"]
        customer = Customer(self._instance)
        return customer.fillWithData(body)
        
    def delete(self, options = None):
        """Delete the customer.
        Keyword argument:
		
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/customers/" + quote_plus(self.id) + ""
        data    = {

        }

        response = Response(request.delete(path, data, options))
        return response.success
        
    def tokens(self, options = None):
        """Get all the authorization tokens of the customer.
        Keyword argument:
		
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/customers/" + quote_plus(self.id) + "/tokens"
        data    = {

        }

        response = Response(request.get(path, data, options))
        a    = []
        body = response.body
        for v in body['tokens']:
            tmp = CustomerToken(self._instance)
            tmp.fillWithData(v)
            a.append(tmp)

        return a
        
    def findToken(self, tokenId, options = None):
        """Find a specific customer token.
        Keyword argument:
		tokenId -- ID of the customer token
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/customers/" + quote_plus(self.id) + "/tokens/" + quote_plus(tokenId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        body = response.body
        body = body["token"]
        customerToken = CustomerToken(self._instance)
        return customerToken.fillWithData(body)
        
    def revokeToken(self, tokenId, options = None):
        """Revoke (delete) a specific customer token.
        Keyword argument:
		tokenId -- ID of the customer token
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/customers/" + quote_plus(self.id) + "/tokens/" + quote_plus(tokenId) + ""
        data    = {

        }

        response = Response(request.delete(path, data, options))
        return response.success
        
    def authorize(self, gatewayName, name, token, options = None):
        """Authorize (create) a new customer token.
        Keyword argument:
		gatewayName -- Name of the payment gateway
		name -- Name of the customer token
		token -- Payment gateway token (ex: stripe customer token)
        options -- Options for the request"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/customers/" + quote_plus(self.id) + "/gateways/" + quote_plus(gatewayName) + "/tokens"
        data    = {
			'name': name, 
			'token': token
        }

        response = Response(request.post(path, data, options))
        body = response.body
        body = body["token"]
        customerToken = CustomerToken(self._instance)
        return customerToken.fillWithData(body)
        
    

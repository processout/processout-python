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
try:
    from .webhook import Webhook
except ImportError:
    import sys
    Webhook = sys.modules[__package__ + '.webhook']

from .networking.requestprocessoutprivate import RequestProcessoutPrivate


class Customer:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        self._id = ""
        self._email = ""
        self._firstName = ""
        self._lastName = ""
        self._address1 = ""
        self._address2 = ""
        self._city = ""
        self._state = ""
        self._zip = ""
        self._countryCode = ""
        self._hasPin = False
        self._sandbox = False
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
    def email(self):
        """Get email"""
        return self._email

    @email.setter
    def email(self, val):
        """Set email
        Keyword argument:
        val -- New email value"""
        self._email = val
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
    
    @property
    def hasPin(self):
        """Get hasPin"""
        return self._hasPin

    @hasPin.setter
    def hasPin(self, val):
        """Set hasPin
        Keyword argument:
        val -- New hasPin value"""
        self._hasPin = val
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
        if "email" in data.keys():
            self.email = data["email"]
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
        if "has_pin" in data.keys():
            self.hasPin = data["has_pin"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.createdAt = data["created_at"]
        
        return self

    def recurringInvoices(self, options = None):
        """Get the recurring invoices linked to the customer.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/customers/" + quote_plus(self.id) + "/recurring-invoices"
        data    = {

        }

        response = Response(request.get(path, data, options))
        a    = []
        body = response.body
        for v in body['recurring_invoices']:
            tmp = RecurringInvoice(instance)
            tmp.fillWithData(v)
            a.append(tmp)

        return a
        
    def tokens(self, options = None):
        """Get the customer's tokens.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/customers/" + quote_plus(self.id) + "/tokens"
        data    = {

        }

        response = Response(request.get(path, data, options))
        a    = []
        body = response.body
        for v in body['tokens']:
            tmp = Token(instance)
            tmp.fillWithData(v)
            a.append(tmp)

        return a
        
    def token(self, tokenId, options = None):
        """Get a specific customer's token by its ID.
        Keyword argument:
		tokenId -- ID of the token
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/customers/" + quote_plus(self.id) + "/tokens/" + quote_plus(tokenId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        body = response.body
        body = body["token"]
        token = Token(instance)
        return token.fillWithData(body)
        
    @staticmethod
    def all(options = None):
        """Get all the customers.
        Keyword argument:
		
        options -- Options for the request"""
        instance = ProcessOut.getDefault()
        request = RequestProcessoutPrivate(instance)
        path    = "/customers"
        data    = {

        }

        response = Response(request.get(path, data, options))
        a    = []
        body = response.body
        for v in body['customers']:
            tmp = Customer(instance)
            tmp.fillWithData(v)
            a.append(tmp)

        return a
        
    def create(self, options = None):
        """Create a new customer.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/customers"
        data    = {
			'email': self.email, 
			'first_name': self.firstName, 
			'last_name': self.lastName, 
			'address1': self.address1, 
			'address2': self.address2, 
			'city': self.city, 
			'state': self.state, 
			'zip': self.zip, 
			'country_code': self.countryCode
        }

        response = Response(request.post(path, data, options))
        body = response.body
        body = body["customer"]
        customer = Customer(instance)
        return customer.fillWithData(body)
        
    @staticmethod
    def find(customerId, options = None):
        """Find a customer by its ID.
        Keyword argument:
		customerId -- ID of the customer
        options -- Options for the request"""
        instance = ProcessOut.getDefault()
        request = RequestProcessoutPrivate(instance)
        path    = "/customers/" + quote_plus(customerId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        body = response.body
        body = body["customer"]
        customer = Customer(instance)
        return customer.fillWithData(body)
        
    def save(self, options = None):
        """Save the updated customer attributes.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/customers/" + quote_plus(self.id) + ""
        data    = {

        }

        response = Response(request.put(path, data, options))
        body = response.body
        body = body["customer"]
        return self.fillWithData(body)
        
    def delete(self, options = None):
        """Delete the customer.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/customers/" + quote_plus(self.id) + ""
        data    = {

        }

        response = Response(request.delete(path, data, options))
        return response.success
        
    

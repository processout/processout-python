try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Customer(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = ""
        self._project = None
        self._email = ""
        self._firstName = ""
        self._lastName = ""
        self._address1 = ""
        self._address2 = ""
        self._city = ""
        self._state = ""
        self._zip = ""
        self._countryCode = ""
        self._balance = "0"
        self._currency = ""
        self._metadata = {}
        self._hasPin = False
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
        if isinstance(val, dict):
            obj = processout.Project(self._client)
            obj.fillWithData(val)
            self._project = obj
        else:
            self._project = val
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
    def balance(self):
        """Get balance"""
        return self._balance

    @balance.setter
    def balance(self, val):
        """Set balance
        Keyword argument:
        val -- New balance value"""
        self._balance = val
        return self
    
    @property
    def currency(self):
        """Get currency"""
        return self._currency

    @currency.setter
    def currency(self, val):
        """Set currency
        Keyword argument:
        val -- New currency value"""
        self._currency = val
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
        if "project" in data.keys():
            self.project = data["project"]
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
        if "balance" in data.keys():
            self.balance = data["balance"]
        if "currency" in data.keys():
            self.currency = data["currency"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "has_pin" in data.keys():
            self.hasPin = data["has_pin"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.createdAt = data["created_at"]
        
        return self

    def fetchSubscriptions(self, options = None):
        """Get the subscriptions belonging to the customer.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/customers/" + quote_plus(self.id) + "/subscriptions"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        a    = []
        body = response.body
        for v in body['subscriptions']:
            tmp = Subscription(self._client)
            tmp.fillWithData(v)
            a.append(tmp)

        returnValues.append(a)
            

        
        return returnValues[0];

    def fetchTokens(self, options = None):
        """Get the customer's tokens.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/customers/" + quote_plus(self.id) + "/tokens"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        a    = []
        body = response.body
        for v in body['tokens']:
            tmp = Token(self._client)
            tmp.fillWithData(v)
            a.append(tmp)

        returnValues.append(a)
            

        
        return returnValues[0];

    def findToken(self, tokenId, options = None):
        """Find a customer's token by its ID.
        Keyword argument:
        tokenId -- ID of the token
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/customers/" + quote_plus(self.id) + "/tokens/" + quote_plus(tokenId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["token"]
        token = Token(self._client)
        returnValues.append(token.fillWithData(body))

        
        return returnValues[0];

    def deleteToken(self, tokenId, options = None):
        """Delete a customer's token by its ID.
        Keyword argument:
        tokenId -- ID of the token
        options -- Options for the request"""
        request = Request(self._client)
        path    = "customers/" + quote_plus(self.id) + "/tokens/" + quote_plus(tokenId) + ""
        data    = {

        }

        response = Response(request.delete(path, data, options))
        returnValues = []
        
        returnValues.append(response.success)

        
        return returnValues[0];

    def fetchTransactions(self, options = None):
        """Get the transactions belonging to the customer.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/customers/" + quote_plus(self.id) + "/transactions"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        a    = []
        body = response.body
        for v in body['transactions']:
            tmp = Transaction(self._client)
            tmp.fillWithData(v)
            a.append(tmp)

        returnValues.append(a)
            

        
        return returnValues[0];

    def all(self, options = None):
        """Get all the customers.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/customers"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        a    = []
        body = response.body
        for v in body['customers']:
            tmp = Customer(self._client)
            tmp.fillWithData(v)
            a.append(tmp)

        returnValues.append(a)
            

        
        return returnValues[0];

    def create(self, options = None):
        """Create a new customer.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/customers"
        data    = {
            'balance': self.balance, 
            'currency': self.currency, 
            'email': self.email, 
            'first_name': self.firstName, 
            'last_name': self.lastName, 
            'address1': self.address1, 
            'address2': self.address2, 
            'city': self.city, 
            'state': self.state, 
            'zip': self.zip, 
            'country_code': self.countryCode, 
            'metadata': self.metadata
        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["customer"]
                
                
        returnValues.append(self.fillWithData(body))
                

        
        return returnValues[0];

    def find(self, customerId, options = None):
        """Find a customer by its ID.
        Keyword argument:
        customerId -- ID of the customer
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/customers/" + quote_plus(customerId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["customer"]
                
                
        obj = processout.Customer(self._client)
        returnValues.append(obj.fillWithData(body))
                

        
        return returnValues[0];

    def save(self, options = None):
        """Save the updated customer attributes.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/customers/" + quote_plus(self.id) + ""
        data    = {
            'balance': self.balance, 
            'email': self.email, 
            'first_name': self.firstName, 
            'last_name': self.lastName, 
            'address1': self.address1, 
            'address2': self.address2, 
            'city': self.city, 
            'state': self.state, 
            'zip': self.zip, 
            'country_code': self.countryCode, 
            'metadata': self.metadata
        }

        response = Response(request.put(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["customer"]
                
                
        returnValues.append(self.fillWithData(body))
                

        
        return returnValues[0];

    def delete(self, options = None):
        """Delete the customer.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/customers/" + quote_plus(self.id) + ""
        data    = {

        }

        response = Response(request.delete(path, data, options))
        returnValues = []
        
        returnValues.append(response.success)

        
        return returnValues[0];

    

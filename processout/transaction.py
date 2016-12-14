try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Transaction(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = None
        self._project = None
        self._customer = None
        self._subscription = None
        self._token = None
        self._card = None
        self._name = None
        self._authorized_amount = None
        self._captured_amount = None
        self._currency = None
        self._status = None
        self._authorized = None
        self._captured = None
        self._processout_fee = None
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
    def customer(self):
        """Get customer"""
        return self._customer

    @customer.setter
    def customer(self, val):
        """Set customer
        Keyword argument:
        val -- New customer value"""
        if isinstance(val, dict):
            obj = processout.Customer(self._client)
            obj.fill_with_data(val)
            self._customer = obj
        else:
            self._customer = val
        return self
    
    @property
    def subscription(self):
        """Get subscription"""
        return self._subscription

    @subscription.setter
    def subscription(self, val):
        """Set subscription
        Keyword argument:
        val -- New subscription value"""
        if isinstance(val, dict):
            obj = processout.Subscription(self._client)
            obj.fill_with_data(val)
            self._subscription = obj
        else:
            self._subscription = val
        return self
    
    @property
    def token(self):
        """Get token"""
        return self._token

    @token.setter
    def token(self, val):
        """Set token
        Keyword argument:
        val -- New token value"""
        if isinstance(val, dict):
            obj = processout.Token(self._client)
            obj.fill_with_data(val)
            self._token = obj
        else:
            self._token = val
        return self
    
    @property
    def card(self):
        """Get card"""
        return self._card

    @card.setter
    def card(self, val):
        """Set card
        Keyword argument:
        val -- New card value"""
        if isinstance(val, dict):
            obj = processout.Card(self._client)
            obj.fill_with_data(val)
            self._card = obj
        else:
            self._card = val
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
    def authorized_amount(self):
        """Get authorized_amount"""
        return self._authorized_amount

    @authorized_amount.setter
    def authorized_amount(self, val):
        """Set authorized_amount
        Keyword argument:
        val -- New authorized_amount value"""
        self._authorized_amount = val
        return self
    
    @property
    def captured_amount(self):
        """Get captured_amount"""
        return self._captured_amount

    @captured_amount.setter
    def captured_amount(self, val):
        """Set captured_amount
        Keyword argument:
        val -- New captured_amount value"""
        self._captured_amount = val
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
    def status(self):
        """Get status"""
        return self._status

    @status.setter
    def status(self, val):
        """Set status
        Keyword argument:
        val -- New status value"""
        self._status = val
        return self
    
    @property
    def authorized(self):
        """Get authorized"""
        return self._authorized

    @authorized.setter
    def authorized(self, val):
        """Set authorized
        Keyword argument:
        val -- New authorized value"""
        self._authorized = val
        return self
    
    @property
    def captured(self):
        """Get captured"""
        return self._captured

    @captured.setter
    def captured(self, val):
        """Set captured
        Keyword argument:
        val -- New captured value"""
        self._captured = val
        return self
    
    @property
    def processout_fee(self):
        """Get processout_fee"""
        return self._processout_fee

    @processout_fee.setter
    def processout_fee(self, val):
        """Set processout_fee
        Keyword argument:
        val -- New processout_fee value"""
        self._processout_fee = val
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
        if "customer" in data.keys():
            self.customer = data["customer"]
        if "subscription" in data.keys():
            self.subscription = data["subscription"]
        if "token" in data.keys():
            self.token = data["token"]
        if "card" in data.keys():
            self.card = data["card"]
        if "name" in data.keys():
            self.name = data["name"]
        if "authorized_amount" in data.keys():
            self.authorized_amount = data["authorized_amount"]
        if "captured_amount" in data.keys():
            self.captured_amount = data["captured_amount"]
        if "currency" in data.keys():
            self.currency = data["currency"]
        if "status" in data.keys():
            self.status = data["status"]
        if "authorized" in data.keys():
            self.authorized = data["authorized"]
        if "captured" in data.keys():
            self.captured = data["captured"]
        if "processout_fee" in data.keys():
            self.processout_fee = data["processout_fee"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        
        return self

    def fetch_refunds(self, options = {}):
        """Get the transaction's refunds.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/transactions/" + quote_plus(self.id) + "/refunds"
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        a    = []
        body = response.body
        for v in body['refunds']:
            tmp = processout.Refund(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)
            

        
        return return_values[0]

    def find_refund(self, refund_id, options = {}):
        """Find a transaction's refund by its ID.
        Keyword argument:
        refund_id -- ID of the refund
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/transactions/" + quote_plus(self.id) + "/refunds/" + quote_plus(refund_id) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        body = response.body
        body = body["refund"]
        refund = processout.Refund(self._client)
        return_values.append(refund.fill_with_data(body))

        
        return return_values[0]

    def all(self, options = {}):
        """Get all the transactions.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/transactions"
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        a    = []
        body = response.body
        for v in body['transactions']:
            tmp = processout.Transaction(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)
            

        
        return return_values[0]

    def find(self, transaction_id, options = {}):
        """Find a transaction by its ID.
        Keyword argument:
        transaction_id -- ID of the transaction
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/transactions/" + quote_plus(transaction_id) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        body = response.body
        body = body["transaction"]
                
                
        obj = processout.Transaction(self._client)
        return_values.append(obj.fill_with_data(body))
                

        
        return return_values[0]

    

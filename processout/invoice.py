try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Invoice:
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = ""
        self._project = None
        self._transaction = None
        self._customer = None
        self._subscription = None
        self._url = ""
        self._name = ""
        self._amount = ""
        self._currency = ""
        self._metadata = {}
        self._requestEmail = False
        self._requestShipping = False
        self._returnUrl = ""
        self._cancelUrl = ""
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
    def transaction(self):
        """Get transaction"""
        return self._transaction

    @transaction.setter
    def transaction(self, val):
        """Set transaction
        Keyword argument:
        val -- New transaction value"""
        if isinstance(val, Transaction):
            self._transaction = val
        else:
            obj = processout.Transaction(self._client)
            obj.fillWithData(val)
            self._transaction = obj
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
        if isinstance(val, Customer):
            self._customer = val
        else:
            obj = processout.Customer(self._client)
            obj.fillWithData(val)
            self._customer = obj
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
        if isinstance(val, Subscription):
            self._subscription = val
        else:
            obj = processout.Subscription(self._client)
            obj.fillWithData(val)
            self._subscription = obj
        return self
    
    @property
    def url(self):
        """Get url"""
        return self._url

    @url.setter
    def url(self, val):
        """Set url
        Keyword argument:
        val -- New url value"""
        self._url = val
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
    def amount(self):
        """Get amount"""
        return self._amount

    @amount.setter
    def amount(self, val):
        """Set amount
        Keyword argument:
        val -- New amount value"""
        self._amount = val
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
    def requestEmail(self):
        """Get requestEmail"""
        return self._requestEmail

    @requestEmail.setter
    def requestEmail(self, val):
        """Set requestEmail
        Keyword argument:
        val -- New requestEmail value"""
        self._requestEmail = val
        return self
    
    @property
    def requestShipping(self):
        """Get requestShipping"""
        return self._requestShipping

    @requestShipping.setter
    def requestShipping(self, val):
        """Set requestShipping
        Keyword argument:
        val -- New requestShipping value"""
        self._requestShipping = val
        return self
    
    @property
    def returnUrl(self):
        """Get returnUrl"""
        return self._returnUrl

    @returnUrl.setter
    def returnUrl(self, val):
        """Set returnUrl
        Keyword argument:
        val -- New returnUrl value"""
        self._returnUrl = val
        return self
    
    @property
    def cancelUrl(self):
        """Get cancelUrl"""
        return self._cancelUrl

    @cancelUrl.setter
    def cancelUrl(self, val):
        """Set cancelUrl
        Keyword argument:
        val -- New cancelUrl value"""
        self._cancelUrl = val
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
        if "transaction" in data.keys():
            self.transaction = data["transaction"]
        if "customer" in data.keys():
            self.customer = data["customer"]
        if "subscription" in data.keys():
            self.subscription = data["subscription"]
        if "url" in data.keys():
            self.url = data["url"]
        if "name" in data.keys():
            self.name = data["name"]
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "currency" in data.keys():
            self.currency = data["currency"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "request_email" in data.keys():
            self.requestEmail = data["request_email"]
        if "request_shipping" in data.keys():
            self.requestShipping = data["request_shipping"]
        if "return_url" in data.keys():
            self.returnUrl = data["return_url"]
        if "cancel_url" in data.keys():
            self.cancelUrl = data["cancel_url"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.createdAt = data["created_at"]
        
        return self

    def authorize(self, source, options = None):
        """Authorize the invoice using the given source (customer or token)
        Keyword argument:
        source -- Source used to authorization the payment. Can be a card, a token or a gateway request
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/invoices/" + quote_plus(self.id) + "/authorize"
        data    = {
            'source': source
        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["transaction"]
        transaction = Transaction(self._client)
        returnValues.append(transaction.fillWithData(body))

        
        return returnValues[0];

    def capture(self, source, options = None):
        """Capture the invoice using the given source (customer or token)
        Keyword argument:
        source -- Source used to authorization the payment. Can be a card, a token or a gateway request
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/invoices/" + quote_plus(self.id) + "/capture"
        data    = {
            'source': source
        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["transaction"]
        transaction = Transaction(self._client)
        returnValues.append(transaction.fillWithData(body))

        
        return returnValues[0];

    def fetchCustomer(self, options = None):
        """Get the customer linked to the invoice.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/invoices/" + quote_plus(self.id) + "/customers"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["customer"]
        customer = Customer(self._client)
        returnValues.append(customer.fillWithData(body))

        
        return returnValues[0];

    def assignCustomer(self, customerId, options = None):
        """Assign a customer to the invoice.
        Keyword argument:
        customerId -- ID of the customer to be linked to the invoice
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/invoices/" + quote_plus(self.id) + "/customers"
        data    = {
            'customer_id': customerId
        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["customer"]
        customer = Customer(self._client)
        returnValues.append(customer.fillWithData(body))

        
        return returnValues[0];

    def fetchTransaction(self, options = None):
        """Get the transaction of the invoice.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/invoices/" + quote_plus(self.id) + "/transactions"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["transaction"]
        transaction = Transaction(self._client)
        returnValues.append(transaction.fillWithData(body))

        
        return returnValues[0];

    def void(self, options = None):
        """Void the invoice
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/invoices/" + quote_plus(self.id) + "/void"
        data    = {

        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["transaction"]
        transaction = Transaction(self._client)
        returnValues.append(transaction.fillWithData(body))

        
        return returnValues[0];

    def all(self, options = None):
        """Get all the invoices.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/invoices"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        a    = []
        body = response.body
        for v in body['invoices']:
            tmp = Invoice(self._client)
            tmp.fillWithData(v)
            a.append(tmp)

        returnValues.append(a)
            

        
        return returnValues[0];

    def create(self, options = None):
        """Create a new invoice.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/invoices"
        data    = {
            'name': self.name, 
            'amount': self.amount, 
            'currency': self.currency, 
            'metadata': self.metadata, 
            'request_email': self.requestEmail, 
            'request_shipping': self.requestShipping, 
            'return_url': self.returnUrl, 
            'cancel_url': self.cancelUrl
        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["invoice"]
                
                
        returnValues.append(self.fillWithData(body))
                

        
        return returnValues[0];

    def createForCustomer(self, customerId, options = None):
        """Create a new invoice for the given customer ID.
        Keyword argument:
        customerId -- ID of the customer
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/invoices"
        data    = {
            'name': self.name, 
            'amount': self.amount, 
            'currency': self.currency, 
            'metadata': self.metadata, 
            'request_email': self.requestEmail, 
            'request_shipping': self.requestShipping, 
            'return_url': self.returnUrl, 
            'cancel_url': self.cancelUrl, 
            'customer_id': customerId
        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["invoice"]
                
                
        returnValues.append(self.fillWithData(body))
                

        
        return returnValues[0];

    def find(self, invoiceId, options = None):
        """Find an invoice by its ID.
        Keyword argument:
        invoiceId -- ID of the invoice
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/invoices/" + quote_plus(invoiceId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["invoice"]
                
                
        obj = processout.Invoice(self._client)
        returnValues.append(obj.fillWithData(body))
                

        
        return returnValues[0];

    

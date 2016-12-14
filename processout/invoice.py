try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Invoice(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = None
        self._project = None
        self._transaction = None
        self._customer = None
        self._subscription = None
        self._url = None
        self._name = None
        self._statement_descriptor = None
        self._statement_descriptor_phone = None
        self._statement_descriptor_city = None
        self._statement_descriptor_company = None
        self._statement_descriptor_url = None
        self._amount = None
        self._currency = None
        self._metadata = None
        self._request_email = None
        self._request_shipping = None
        self._return_url = None
        self._cancel_url = None
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
    def transaction(self):
        """Get transaction"""
        return self._transaction

    @transaction.setter
    def transaction(self, val):
        """Set transaction
        Keyword argument:
        val -- New transaction value"""
        if isinstance(val, dict):
            obj = processout.Transaction(self._client)
            obj.fill_with_data(val)
            self._transaction = obj
        else:
            self._transaction = val
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
    def statement_descriptor(self):
        """Get statement_descriptor"""
        return self._statement_descriptor

    @statement_descriptor.setter
    def statement_descriptor(self, val):
        """Set statement_descriptor
        Keyword argument:
        val -- New statement_descriptor value"""
        self._statement_descriptor = val
        return self
    
    @property
    def statement_descriptor_phone(self):
        """Get statement_descriptor_phone"""
        return self._statement_descriptor_phone

    @statement_descriptor_phone.setter
    def statement_descriptor_phone(self, val):
        """Set statement_descriptor_phone
        Keyword argument:
        val -- New statement_descriptor_phone value"""
        self._statement_descriptor_phone = val
        return self
    
    @property
    def statement_descriptor_city(self):
        """Get statement_descriptor_city"""
        return self._statement_descriptor_city

    @statement_descriptor_city.setter
    def statement_descriptor_city(self, val):
        """Set statement_descriptor_city
        Keyword argument:
        val -- New statement_descriptor_city value"""
        self._statement_descriptor_city = val
        return self
    
    @property
    def statement_descriptor_company(self):
        """Get statement_descriptor_company"""
        return self._statement_descriptor_company

    @statement_descriptor_company.setter
    def statement_descriptor_company(self, val):
        """Set statement_descriptor_company
        Keyword argument:
        val -- New statement_descriptor_company value"""
        self._statement_descriptor_company = val
        return self
    
    @property
    def statement_descriptor_url(self):
        """Get statement_descriptor_url"""
        return self._statement_descriptor_url

    @statement_descriptor_url.setter
    def statement_descriptor_url(self, val):
        """Set statement_descriptor_url
        Keyword argument:
        val -- New statement_descriptor_url value"""
        self._statement_descriptor_url = val
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
    def request_email(self):
        """Get request_email"""
        return self._request_email

    @request_email.setter
    def request_email(self, val):
        """Set request_email
        Keyword argument:
        val -- New request_email value"""
        self._request_email = val
        return self
    
    @property
    def request_shipping(self):
        """Get request_shipping"""
        return self._request_shipping

    @request_shipping.setter
    def request_shipping(self, val):
        """Set request_shipping
        Keyword argument:
        val -- New request_shipping value"""
        self._request_shipping = val
        return self
    
    @property
    def return_url(self):
        """Get return_url"""
        return self._return_url

    @return_url.setter
    def return_url(self, val):
        """Set return_url
        Keyword argument:
        val -- New return_url value"""
        self._return_url = val
        return self
    
    @property
    def cancel_url(self):
        """Get cancel_url"""
        return self._cancel_url

    @cancel_url.setter
    def cancel_url(self, val):
        """Set cancel_url
        Keyword argument:
        val -- New cancel_url value"""
        self._cancel_url = val
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
        if "statement_descriptor" in data.keys():
            self.statement_descriptor = data["statement_descriptor"]
        if "statement_descriptor_phone" in data.keys():
            self.statement_descriptor_phone = data["statement_descriptor_phone"]
        if "statement_descriptor_city" in data.keys():
            self.statement_descriptor_city = data["statement_descriptor_city"]
        if "statement_descriptor_company" in data.keys():
            self.statement_descriptor_company = data["statement_descriptor_company"]
        if "statement_descriptor_url" in data.keys():
            self.statement_descriptor_url = data["statement_descriptor_url"]
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "currency" in data.keys():
            self.currency = data["currency"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "request_email" in data.keys():
            self.request_email = data["request_email"]
        if "request_shipping" in data.keys():
            self.request_shipping = data["request_shipping"]
        if "return_url" in data.keys():
            self.return_url = data["return_url"]
        if "cancel_url" in data.keys():
            self.cancel_url = data["cancel_url"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        
        return self

    def authorize(self, source, options = {}):
        """Authorize the invoice using the given source (customer or token)
        Keyword argument:
        source -- Source used to authorization the payment. Can be a card, a token or a gateway request
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/invoices/" + quote_plus(self.id) + "/authorize"
        data    = {
            'authorize_only': options.get("authorize_only"), 
            'synchronous': options.get("synchronous"), 
            'source': source
        }

        response = Response(request.post(path, data, options))
        return_values = []
        
        body = response.body
        body = body["transaction"]
        transaction = processout.Transaction(self._client)
        return_values.append(transaction.fill_with_data(body))

        
        return return_values[0]

    def capture(self, source, options = {}):
        """Capture the invoice using the given source (customer or token)
        Keyword argument:
        source -- Source used to authorization the payment. Can be a card, a token or a gateway request
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/invoices/" + quote_plus(self.id) + "/capture"
        data    = {
            'authorize_only': options.get("authorize_only"), 
            'synchronous': options.get("synchronous"), 
            'source': source
        }

        response = Response(request.post(path, data, options))
        return_values = []
        
        body = response.body
        body = body["transaction"]
        transaction = processout.Transaction(self._client)
        return_values.append(transaction.fill_with_data(body))

        
        return return_values[0]

    def fetch_customer(self, options = {}):
        """Get the customer linked to the invoice.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/invoices/" + quote_plus(self.id) + "/customers"
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        body = response.body
        body = body["customer"]
        customer = processout.Customer(self._client)
        return_values.append(customer.fill_with_data(body))

        
        return return_values[0]

    def assign_customer(self, customer_id, options = {}):
        """Assign a customer to the invoice.
        Keyword argument:
        customer_id -- ID of the customer to be linked to the invoice
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/invoices/" + quote_plus(self.id) + "/customers"
        data    = {
            'customer_id': customer_id
        }

        response = Response(request.post(path, data, options))
        return_values = []
        
        body = response.body
        body = body["customer"]
        customer = processout.Customer(self._client)
        return_values.append(customer.fill_with_data(body))

        
        return return_values[0]

    def fetch_transaction(self, options = {}):
        """Get the transaction of the invoice.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/invoices/" + quote_plus(self.id) + "/transactions"
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        body = response.body
        body = body["transaction"]
        transaction = processout.Transaction(self._client)
        return_values.append(transaction.fill_with_data(body))

        
        return return_values[0]

    def void(self, options = {}):
        """Void the invoice
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/invoices/" + quote_plus(self.id) + "/void"
        data    = {

        }

        response = Response(request.post(path, data, options))
        return_values = []
        
        body = response.body
        body = body["transaction"]
        transaction = processout.Transaction(self._client)
        return_values.append(transaction.fill_with_data(body))

        
        return return_values[0]

    def all(self, options = {}):
        """Get all the invoices.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/invoices"
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        a    = []
        body = response.body
        for v in body['invoices']:
            tmp = processout.Invoice(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)
            

        
        return return_values[0]

    def create(self, options = {}):
        """Create a new invoice.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/invoices"
        data    = {
            'name': self.name, 
            'amount': self.amount, 
            'currency': self.currency, 
            'metadata': self.metadata, 
            'statement_descriptor': self.statement_descriptor, 
            'statement_descriptor_phone': self.statement_descriptor_phone, 
            'statement_descriptor_city': self.statement_descriptor_city, 
            'statement_descriptor_company': self.statement_descriptor_company, 
            'statement_descriptor_url': self.statement_descriptor_url, 
            'request_email': self.request_email, 
            'request_shipping': self.request_shipping, 
            'return_url': self.return_url, 
            'cancel_url': self.cancel_url, 
            'customer_id': options.get("customer_id")
        }

        response = Response(request.post(path, data, options))
        return_values = []
        
        body = response.body
        body = body["invoice"]
                
                
        return_values.append(self.fill_with_data(body))
                

        
        return return_values[0]

    def create_for_customer(self, customer_id, options = {}):
        """Create a new invoice for the given customer ID.
        Keyword argument:
        customer_id -- ID of the customer
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/invoices"
        data    = {
            'name': self.name, 
            'amount': self.amount, 
            'currency': self.currency, 
            'metadata': self.metadata, 
            'statement_descriptor': self.statement_descriptor, 
            'statement_descriptor_phone': self.statement_descriptor_phone, 
            'statement_descriptor_city': self.statement_descriptor_city, 
            'statement_descriptor_company': self.statement_descriptor_company, 
            'statement_descriptor_url': self.statement_descriptor_url, 
            'request_email': self.request_email, 
            'request_shipping': self.request_shipping, 
            'return_url': self.return_url, 
            'cancel_url': self.cancel_url, 
            'customer_id': customer_id
        }

        response = Response(request.post(path, data, options))
        return_values = []
        
        body = response.body
        body = body["invoice"]
                
                
        return_values.append(self.fill_with_data(body))
                

        
        return return_values[0]

    def find(self, invoice_id, options = {}):
        """Find an invoice by its ID.
        Keyword argument:
        invoice_id -- ID of the invoice
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/invoices/" + quote_plus(invoice_id) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        body = response.body
        body = body["invoice"]
                
                
        obj = processout.Invoice(self._client)
        return_values.append(obj.fill_with_data(body))
                

        
        return return_values[0]

    

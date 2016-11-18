try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Product(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = ""
        self._project = None
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
        if isinstance(val, dict):
            obj = processout.Project(self._client)
            obj.fillWithData(val)
            self._project = obj
        else:
            self._project = val
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

    def createInvoice(self, options = None):
        """Create a new invoice from the product.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/products/" + quote_plus(self.id) + "/invoices"
        data    = {

        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["invoice"]
        invoice = Invoice(self._client)
        returnValues.append(invoice.fillWithData(body))

        
        return returnValues[0];

    def all(self, options = None):
        """Get all the products.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/products"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        a    = []
        body = response.body
        for v in body['products']:
            tmp = Product(self._client)
            tmp.fillWithData(v)
            a.append(tmp)

        returnValues.append(a)
            

        
        return returnValues[0];

    def create(self, options = None):
        """Create a new product.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/products"
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
        body = body["product"]
                
                
        returnValues.append(self.fillWithData(body))
                

        
        return returnValues[0];

    def find(self, productId, options = None):
        """Find a product by its ID.
        Keyword argument:
        productId -- ID of the product
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/products/" + quote_plus(productId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["product"]
                
                
        obj = processout.Product(self._client)
        returnValues.append(obj.fillWithData(body))
                

        
        return returnValues[0];

    def save(self, options = None):
        """Save the updated product attributes.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/products/" + quote_plus(self.id) + ""
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

        response = Response(request.put(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["product"]
                
                
        returnValues.append(self.fillWithData(body))
                

        
        return returnValues[0];

    def delete(self, options = None):
        """Delete the product.
        Keyword argument:
        
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/products/" + quote_plus(self.id) + ""
        data    = {

        }

        response = Response(request.delete(path, data, options))
        returnValues = []
        
        returnValues.append(response.success)

        
        return returnValues[0];

    

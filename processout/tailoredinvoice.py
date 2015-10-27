from urllib.parse import quote_plus

from .processout import ProcessOut
from .networking.response import Response

from .networking.requestprocessoutprivate import RequestProcessoutPrivate

from .networking.requestprocessoutpublic import RequestProcessoutPublic


class TailoredInvoice:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        
        self._cancelUrl = ""
        
        self._currency = ""
        
        self._id = ""
        
        self._name = ""
        
        self._notifyUrl = ""
        
        self._price = ""
        
        self._recurringDays = 0
        
        self._returnUrl = ""
        
        self._shipping = "0.00"
        
        self._taxes = "0.00"
        

    
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
    def notifyUrl(self):
        """Get notifyUrl"""
        return self._notifyUrl

    @notifyUrl.setter
    def notifyUrl(self, val):
        """Set notifyUrl
        Keyword argument:
        val -- New notifyUrl value"""
        self._notifyUrl = val
    
    @property
    def price(self):
        """Get price"""
        return self._price

    @price.setter
    def price(self, val):
        """Set price
        Keyword argument:
        val -- New price value"""
        self._price = val
    
    @property
    def recurringDays(self):
        """Get recurringDays"""
        return self._recurringDays

    @recurringDays.setter
    def recurringDays(self, val):
        """Set recurringDays
        Keyword argument:
        val -- New recurringDays value"""
        self._recurringDays = val
    
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
    
    @property
    def shipping(self):
        """Get shipping"""
        return self._shipping

    @shipping.setter
    def shipping(self, val):
        """Set shipping
        Keyword argument:
        val -- New shipping value"""
        self._shipping = val
    
    @property
    def taxes(self):
        """Get taxes"""
        return self._taxes

    @taxes.setter
    def taxes(self, val):
        """Set taxes
        Keyword argument:
        val -- New taxes value"""
        self._taxes = val
    

    def fillWithData(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        
        if "cancel_url" in data.keys():
            self.cancelUrl = data["cancel_url"]
        
        if "currency" in data.keys():
            self.currency = data["currency"]
        
        if "id" in data.keys():
            self.id = data["id"]
        
        if "name" in data.keys():
            self.name = data["name"]
        
        if "notify_url" in data.keys():
            self.notifyUrl = data["notify_url"]
        
        if "price" in data.keys():
            self.price = data["price"]
        
        if "recurring_days" in data.keys():
            self.recurringDays = data["recurring_days"]
        
        if "return_url" in data.keys():
            self.returnUrl = data["return_url"]
        
        if "shipping" in data.keys():
            self.shipping = data["shipping"]
        
        if "taxes" in data.keys():
            self.taxes = data["taxes"]
        

    
    
    @staticmethod
    
    def find(self, id):
        """Get tailored invoice information.
        Keyword argument:
		id -- Unique ID of your tailored invoice"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/tailored-invoices/" + quote_plus(id) + ""
        data    = {

        }

        
        response = Response(request.get(path, data))
        

        
        return self.fillWithData(response.body)
        
    
    
    def save(self):
        """Update the tailored invoice information.
        Keyword argument:
		"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/tailored-invoices/" + quote_plus(self.id) + ""
        data    = {
			'return_url': self.returnUrl, 
			'cancel_url': self.cancelUrl, 
			'notify_url': self.notifyUrl, 
			'name': self.name, 
			'price': self.price, 
			'currency': self.currency, 
			'taxes': self.taxes, 
			'shipping': self.shipping
        }

        
        response = Response(request.put(path, data))
        

        
        return self.fillWithData(response.body)
        
    
    
    def delete(self):
        """Delete a tailored invoice.
        Keyword argument:
		"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/tailored-invoices/" + quote_plus(self.id) + ""
        data    = {

        }

        
        response = Response(request.delete(path, data))
        

        
        return response.success
        
    
    
    @staticmethod
    
    def invoice(self, tailoredInvoiceId):
        """Create an invoice from a tailored invoice.
        Keyword argument:
		tailoredInvoiceId -- Unique ID of the tailored invoice"""
        request = RequestProcessoutPublic(self._instance)
        path    = "/invoices/from-tailored/" + quote_plus(tailoredInvoiceId) + ""
        data    = {

        }

        
        response = Response(request.post(path, data))
        

        
        invoice = Invoice(self._instance)
        return invoice.fillWithData(response.body)
        
    
    
    @staticmethod
    
    def all(self):
        """Get all available tailored invoices information.
        Keyword argument:
		"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/tailored-invoices"
        data    = {

        }

        
        response = Response(request.get(path, data))
        

        
        a    = []
        body = response.body
        for v in body['tailored-invoices']:
            tmp = TailoredInvoice($this->instance)
            tmp.fillWithData(v)
            a.append(tmp)

        return a;
        
    
    
    def create(self):
        """Create a new tailored invoice.
        Keyword argument:
		"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/tailored-invoices"
        data    = {
			'return_url': self.returnUrl, 
			'cancel_url': self.cancelUrl, 
			'notify_url': self.notifyUrl, 
			'name': self.name, 
			'price': self.price, 
			'currency': self.currency, 
			'taxes': self.taxes, 
			'shipping': self.shipping
        }

        
        response = Response(request.post(path, data))
        

        
        return self.fillWithData(response.body)
        
    

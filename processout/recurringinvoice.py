from urllib.parse import quote_plus

from .processout import ProcessOut
from .networking.response import Response

from .networking.requestprocessoutprivate import RequestProcessoutPrivate

from .networking.requestprocessoutpublic import RequestProcessoutPublic


class RecurringInvoice:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        
        self._cancelUrl = ""
        
        self._currency = ""
        
        self._custom = ""
        
        self._ended = False
        
        self._endedReason = ""
        
        self._expired = False
        
        self._id = ""
        
        self._meta = {}
        
        self._name = ""
        
        self._notifyUrl = ""
        
        self._price = ""
        
        self._recurringDays = 0
        
        self._requestEmail = False
        
        self._requestShipping = False
        
        self._returnUrl = ""
        
        self._shipping = "0.00"
        
        self._taxes = "0.00"
        
        self._url = ""
        

    
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
    def custom(self):
        """Get custom"""
        return self._custom

    @custom.setter
    def custom(self, val):
        """Set custom
        Keyword argument:
        val -- New custom value"""
        self._custom = val
    
    @property
    def ended(self):
        """Get ended"""
        return self._ended

    @ended.setter
    def ended(self, val):
        """Set ended
        Keyword argument:
        val -- New ended value"""
        self._ended = val
    
    @property
    def endedReason(self):
        """Get endedReason"""
        return self._endedReason

    @endedReason.setter
    def endedReason(self, val):
        """Set endedReason
        Keyword argument:
        val -- New endedReason value"""
        self._endedReason = val
    
    @property
    def expired(self):
        """Get expired"""
        return self._expired

    @expired.setter
    def expired(self, val):
        """Set expired
        Keyword argument:
        val -- New expired value"""
        self._expired = val
    
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
    def meta(self):
        """Get meta"""
        return self._meta

    @meta.setter
    def meta(self, val):
        """Set meta
        Keyword argument:
        val -- New meta value"""
        self._meta = val
    
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
    def requestEmail(self):
        """Get requestEmail"""
        return self._requestEmail

    @requestEmail.setter
    def requestEmail(self, val):
        """Set requestEmail
        Keyword argument:
        val -- New requestEmail value"""
        self._requestEmail = val
    
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
    

    def fillWithData(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        
        if "cancel_url" in data.keys():
            self.cancelUrl = data["cancel_url"]
        
        if "currency" in data.keys():
            self.currency = data["currency"]
        
        if "custom" in data.keys():
            self.custom = data["custom"]
        
        if "ended" in data.keys():
            self.ended = data["ended"]
        
        if "ended_reason" in data.keys():
            self.endedReason = data["ended_reason"]
        
        if "expired" in data.keys():
            self.expired = data["expired"]
        
        if "id" in data.keys():
            self.id = data["id"]
        
        if "meta" in data.keys():
            self.meta = data["meta"]
        
        if "name" in data.keys():
            self.name = data["name"]
        
        if "notify_url" in data.keys():
            self.notifyUrl = data["notify_url"]
        
        if "price" in data.keys():
            self.price = data["price"]
        
        if "recurring_days" in data.keys():
            self.recurringDays = data["recurring_days"]
        
        if "request_email" in data.keys():
            self.requestEmail = data["request_email"]
        
        if "request_shipping" in data.keys():
            self.requestShipping = data["request_shipping"]
        
        if "return_url" in data.keys():
            self.returnUrl = data["return_url"]
        
        if "shipping" in data.keys():
            self.shipping = data["shipping"]
        
        if "taxes" in data.keys():
            self.taxes = data["taxes"]
        
        if "url" in data.keys():
            self.url = data["url"]
        

    
    
    @staticmethod
    
    def find(self, id):
        """Get the information related to a recurring invoice.
        Keyword argument:
		id -- """
        request = RequestProcessoutPrivate(self._instance)
        path    = "/recurring-invoices/" + quote_plus(id) + ""
        data    = {

        }

        
        response = Response(request.get(path, data))
        

        
        return self.fillWithData(response.body)
        
    
    
    def delete(self):
        """Stop a recurring invoice.
        Keyword argument:
		"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/recurring-invoices/" + quote_plus(self.id) + ""
        data    = {

        }

        
        response = Response(request.delete(path, data))
        

        
        return response.success
        
    
    
    def create(self):
        """Create a recurring invoice.
        Keyword argument:
		"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/invoices"
        data    = {
			'request_email': self.requestEmail, 
			'request_shipping': self.requestShipping, 
			'meta': self.meta, 
			'return_url': self.returnUrl, 
			'cancel_url': self.cancelUrl, 
			'notify_url': self.notifyUrl, 
			'custom': self.custom, 
			'name': self.name, 
			'price': self.price, 
			'currency': self.currency, 
			'taxes': self.taxes, 
			'shipping': self.shipping, 
			'recurring_days': self.recurringDays
        }

        
        response = Response(request.post(path, data))
        

        
        return self.fillWithData(response.body)
        
    

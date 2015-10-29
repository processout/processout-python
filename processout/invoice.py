from urllib.parse import quote_plus

from .processout import ProcessOut
from .networking.response import Response

from .networking.requestprocessoutprivate import RequestProcessoutPrivate

from .networking.requestprocessoutpublic import RequestProcessoutPublic


class Invoice:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance


        self._cancelUrl = ""

        self._currency = ""

        self._custom = ""

        self._id = ""

        self._metas = {}

        self._name = ""

        self._notifyUrl = ""

        self._price = ""

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
    def metas(self):
        """Get metas"""
        return self._metas

    @metas.setter
    def metas(self, val):
        """Set metas
        Keyword argument:
        val -- New metas value"""
        self._metas = val

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

        if "id" in data.keys():
            self.id = data["id"]

        if "metas" in data.keys():
            self.metas = data["metas"]

        if "name" in data.keys():
            self.name = data["name"]

        if "notify_url" in data.keys():
            self.notifyUrl = data["notify_url"]

        if "price" in data.keys():
            self.price = data["price"]

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




    def create(self):
        """Create an invoice.
        Keyword argument:
		"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/invoices"
        data    = {
			'request_email': self.requestEmail,
			'request_shipping': self.requestShipping,
			'metas': self.metas,
			'return_url': self.returnUrl,
			'cancel_url': self.cancelUrl,
			'notify_url': self.notifyUrl,
			'custom': self.custom,
			'name': self.name,
			'price': self.price,
			'currency': self.currency,
			'taxes': self.taxes,
			'shipping': self.shipping
        }


        response = Response(request.post(path, data))



        return self.fillWithData(response.body)



    @staticmethod

    def find(self, id):
        """Get the invoice information.
        Keyword argument:
		id -- Unique ID of the invoice"""
        request = RequestProcessoutPublic(self._instance)
        path    = "/invoices/" + quote_plus(id) + ""
        data    = {

        }


        response = Response(request.get(path, data))



        invoice = Invoice(self._instance)
        return invoice.fillWithData(response.body)



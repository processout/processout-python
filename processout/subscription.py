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
    from .card import Card
except ImportError:
    import sys
    Card = sys.modules[__package__ + '.card']
try:
    from .coupon import Coupon
except ImportError:
    import sys
    Coupon = sys.modules[__package__ + '.coupon']
try:
    from .customer import Customer
except ImportError:
    import sys
    Customer = sys.modules[__package__ + '.customer']
try:
    from .token import Token
except ImportError:
    import sys
    Token = sys.modules[__package__ + '.token']
try:
    from .discount import Discount
except ImportError:
    import sys
    Discount = sys.modules[__package__ + '.discount']
try:
    from .event import Event
except ImportError:
    import sys
    Event = sys.modules[__package__ + '.event']
try:
    from .gateway import Gateway
except ImportError:
    import sys
    Gateway = sys.modules[__package__ + '.gateway']
try:
    from .gatewayconfiguration import GatewayConfiguration
except ImportError:
    import sys
    GatewayConfiguration = sys.modules[__package__ + '.gatewayconfiguration']
try:
    from .invoice import Invoice
except ImportError:
    import sys
    Invoice = sys.modules[__package__ + '.invoice']
try:
    from .customeraction import CustomerAction
except ImportError:
    import sys
    CustomerAction = sys.modules[__package__ + '.customeraction']
try:
    from .plan import Plan
except ImportError:
    import sys
    Plan = sys.modules[__package__ + '.plan']
try:
    from .product import Product
except ImportError:
    import sys
    Product = sys.modules[__package__ + '.product']
try:
    from .project import Project
except ImportError:
    import sys
    Project = sys.modules[__package__ + '.project']
try:
    from .refund import Refund
except ImportError:
    import sys
    Refund = sys.modules[__package__ + '.refund']
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


# The content of this file was automatically generated

class Subscription:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        self._id = ""
        self._project = None
        self._plan = None
        self._customer = None
        self._token = None
        self._url = ""
        self._name = ""
        self._amount = ""
        self._currency = ""
        self._metadata = {}
        self._interval = ""
        self._trialEndAt = ""
        self._activated = False
        self._active = False
        self._canceled = False
        self._cancellationReason = ""
        self._pendingCancellation = False
        self._cancelAt = ""
        self._returnUrl = ""
        self._cancelUrl = ""
        self._sandbox = False
        self._createdAt = ""
        self._activatedAt = ""
        self._iterateAt = ""
        
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
            obj = Project(self._instance)
            obj.fillWithData(val)
            self._project = obj
        return self
    
    @property
    def plan(self):
        """Get plan"""
        return self._plan

    @plan.setter
    def plan(self, val):
        """Set plan
        Keyword argument:
        val -- New plan value"""
        if isinstance(val, Plan):
            self._plan = val
        else:
            obj = Plan(self._instance)
            obj.fillWithData(val)
            self._plan = obj
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
            obj = Customer(self._instance)
            obj.fillWithData(val)
            self._customer = obj
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
        if isinstance(val, Token):
            self._token = val
        else:
            obj = Token(self._instance)
            obj.fillWithData(val)
            self._token = obj
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
    def interval(self):
        """Get interval"""
        return self._interval

    @interval.setter
    def interval(self, val):
        """Set interval
        Keyword argument:
        val -- New interval value"""
        self._interval = val
        return self
    
    @property
    def trialEndAt(self):
        """Get trialEndAt"""
        return self._trialEndAt

    @trialEndAt.setter
    def trialEndAt(self, val):
        """Set trialEndAt
        Keyword argument:
        val -- New trialEndAt value"""
        self._trialEndAt = val
        return self
    
    @property
    def activated(self):
        """Get activated"""
        return self._activated

    @activated.setter
    def activated(self, val):
        """Set activated
        Keyword argument:
        val -- New activated value"""
        self._activated = val
        return self
    
    @property
    def active(self):
        """Get active"""
        return self._active

    @active.setter
    def active(self, val):
        """Set active
        Keyword argument:
        val -- New active value"""
        self._active = val
        return self
    
    @property
    def canceled(self):
        """Get canceled"""
        return self._canceled

    @canceled.setter
    def canceled(self, val):
        """Set canceled
        Keyword argument:
        val -- New canceled value"""
        self._canceled = val
        return self
    
    @property
    def cancellationReason(self):
        """Get cancellationReason"""
        return self._cancellationReason

    @cancellationReason.setter
    def cancellationReason(self, val):
        """Set cancellationReason
        Keyword argument:
        val -- New cancellationReason value"""
        self._cancellationReason = val
        return self
    
    @property
    def pendingCancellation(self):
        """Get pendingCancellation"""
        return self._pendingCancellation

    @pendingCancellation.setter
    def pendingCancellation(self, val):
        """Set pendingCancellation
        Keyword argument:
        val -- New pendingCancellation value"""
        self._pendingCancellation = val
        return self
    
    @property
    def cancelAt(self):
        """Get cancelAt"""
        return self._cancelAt

    @cancelAt.setter
    def cancelAt(self, val):
        """Set cancelAt
        Keyword argument:
        val -- New cancelAt value"""
        self._cancelAt = val
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
    
    @property
    def activatedAt(self):
        """Get activatedAt"""
        return self._activatedAt

    @activatedAt.setter
    def activatedAt(self, val):
        """Set activatedAt
        Keyword argument:
        val -- New activatedAt value"""
        self._activatedAt = val
        return self
    
    @property
    def iterateAt(self):
        """Get iterateAt"""
        return self._iterateAt

    @iterateAt.setter
    def iterateAt(self, val):
        """Set iterateAt
        Keyword argument:
        val -- New iterateAt value"""
        self._iterateAt = val
        return self
    

    def fillWithData(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "id" in data.keys():
            self.id = data["id"]
        if "project" in data.keys():
            self.project = data["project"]
        if "plan" in data.keys():
            self.plan = data["plan"]
        if "customer" in data.keys():
            self.customer = data["customer"]
        if "token" in data.keys():
            self.token = data["token"]
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
        if "interval" in data.keys():
            self.interval = data["interval"]
        if "trial_end_at" in data.keys():
            self.trialEndAt = data["trial_end_at"]
        if "activated" in data.keys():
            self.activated = data["activated"]
        if "active" in data.keys():
            self.active = data["active"]
        if "canceled" in data.keys():
            self.canceled = data["canceled"]
        if "cancellation_reason" in data.keys():
            self.cancellationReason = data["cancellation_reason"]
        if "pending_cancellation" in data.keys():
            self.pendingCancellation = data["pending_cancellation"]
        if "cancel_at" in data.keys():
            self.cancelAt = data["cancel_at"]
        if "return_url" in data.keys():
            self.returnUrl = data["return_url"]
        if "cancel_url" in data.keys():
            self.cancelUrl = data["cancel_url"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.createdAt = data["created_at"]
        if "activated_at" in data.keys():
            self.activatedAt = data["activated_at"]
        if "iterate_at" in data.keys():
            self.iterateAt = data["iterate_at"]
        
        return self

    def customer(self, options = None):
        """Get the customer owning the subscription.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/subscriptions/" + quote_plus(self.id) + "/customers"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["customer"]
        customer = Customer(instance)
        returnValues.append(customer.fillWithData(body))

        return tuple(returnValues)

    def discounts(self, options = None):
        """Get the discounts applied to the subscription.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/subscriptions/" + quote_plus(self.id) + "/discounts"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        a    = []
        body = response.body
        for v in body['discounts']:
            tmp = Discount(instance)
            tmp.fillWithData(v)
            a.append(tmp)

        returnValues.append(a)
            

        return tuple(returnValues)

    def transactions(self, options = None):
        """Get the subscriptions past transactions.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/subscriptions/" + quote_plus(self.id) + "/transactions"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        a    = []
        body = response.body
        for v in body['transactions']:
            tmp = Transaction(instance)
            tmp.fillWithData(v)
            a.append(tmp)

        returnValues.append(a)
            

        return tuple(returnValues)

    @staticmethod
    def all(options = None):
        """Get all the subscriptions.
        Keyword argument:
		
        options -- Options for the request"""
        instance = ProcessOut.getDefault()
        request = RequestProcessoutPrivate(instance)
        path    = "/subscriptions"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        a    = []
        body = response.body
        for v in body['subscriptions']:
            tmp = Subscription(instance)
            tmp.fillWithData(v)
            a.append(tmp)

        returnValues.append(a)
            

        return tuple(returnValues)

    def create(self, customerId, options = None):
        """Create a new subscription for the given customer.
        Keyword argument:
		customerId -- ID of the customer
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/subscriptions"
        data    = {
			'cancel_at': self.cancelAt, 
			'name': self.name, 
			'amount': self.amount, 
			'currency': self.currency, 
			'metadata': self.metadata, 
			'interval': self.interval, 
			'trial_end_at': self.trialEndAt, 
			'return_url': self.returnUrl, 
			'cancel_url': self.cancelUrl, 
			'customer_id': customerId
        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["subscription"]
                
                
        returnValues.append(self.fillWithData(body))
                

        return tuple(returnValues)

    def createFromPlan(self, customerId, planId, options = None):
        """Create a new subscription for the customer from the given plan ID.
        Keyword argument:
		customerId -- ID of the customer
		planId -- ID of the plan
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/subscriptions"
        data    = {
			'cancel_at': self.cancelAt, 
			'name': self.name, 
			'amount': self.amount, 
			'currency': self.currency, 
			'metadata': self.metadata, 
			'interval': self.interval, 
			'trial_end_at': self.trialEndAt, 
			'return_url': self.returnUrl, 
			'cancel_url': self.cancelUrl, 
			'customer_id': customerId, 
			'plan_id': planId
        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["subscription"]
                
                
        returnValues.append(self.fillWithData(body))
                

        return tuple(returnValues)

    @staticmethod
    def find(subscriptionId, options = None):
        """Find a subscription by its ID.
        Keyword argument:
		subscriptionId -- ID of the subscription
        options -- Options for the request"""
        instance = ProcessOut.getDefault()
        request = RequestProcessoutPrivate(instance)
        path    = "/subscriptions/" + quote_plus(subscriptionId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["subscription"]
                
                
        obj = Subscription()
        returnValues.append(obj.fillWithData(body))
                

        return tuple(returnValues)

    def update(self, options = None):
        """Update the subscription.
        Keyword argument:
		
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/subscriptions/" + quote_plus(self.id) + ""
        data    = {
			'trial_end_at': self.trialEndAt
        }

        response = Response(request.put(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["subscription"]
                
                
        returnValues.append(self.fillWithData(body))
                

        return tuple(returnValues)

    def updatePlan(self, planId, prorate, options = None):
        """Update the subscription's plan.
        Keyword argument:
		planId -- ID of the new plan to be applied on the subscription
		prorate -- Define if proration should be done when updating the plan
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/subscriptions/" + quote_plus(self.id) + ""
        data    = {
			'plan_id': planId, 
			'prorate': prorate
        }

        response = Response(request.put(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["subscription"]
                
                
        returnValues.append(self.fillWithData(body))
                

        return tuple(returnValues)

    def applySource(self, source, options = None):
        """Apply a source to the subscription to activate or update the subscription's source.
        Keyword argument:
		source -- Source to be applied on the subscription and used to pay future invoices. Can be a card, a token or a gateway request
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/subscriptions/" + quote_plus(self.id) + ""
        data    = {
			'source': source
        }

        response = Response(request.put(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["subscription"]
                
                
        returnValues.append(self.fillWithData(body))
                

        return tuple(returnValues)

    def cancel(self, cancellationReason, options = None):
        """Cancel a subscription. The reason may be provided as well.
        Keyword argument:
		cancellationReason -- Cancellation reason
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/subscriptions/" + quote_plus(self.id) + ""
        data    = {
			'cancellation_reason': cancellationReason
        }

        response = Response(request.delete(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["subscription"]
                
                
        returnValues.append(self.fillWithData(body))
                

        return tuple(returnValues)

    def cancelAt(self, cancelAt, cancellationReason, options = None):
        """Schedule the cancellation of the subscription. The reason may be provided as well.
        Keyword argument:
		cancelAt -- Cancellation date, in the form of a string
		cancellationReason -- Cancellation reason
        options -- Options for the request"""
        instance = self._instance
        request = RequestProcessoutPrivate(instance)
        path    = "/subscriptions/" + quote_plus(self.id) + ""
        data    = {
			'cancel_at': cancelAt, 
			'cancellation_reason': cancellationReason
        }

        response = Response(request.delete(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["subscription"]
                
                
        returnValues.append(self.fillWithData(body))
                

        return tuple(returnValues)

    

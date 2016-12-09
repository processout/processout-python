try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Subscription(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = None
        self._project = None
        self._planId = None
        self._plan = None
        self._customer = None
        self._token = None
        self._url = None
        self._name = None
        self._amount = None
        self._currency = None
        self._metadata = None
        self._interval = None
        self._trialEndAt = None
        self._activated = None
        self._active = None
        self._canceled = None
        self._cancellationReason = None
        self._pendingCancellation = None
        self._cancelAt = None
        self._returnUrl = None
        self._cancelUrl = None
        self._sandbox = None
        self._createdAt = None
        self._activatedAt = None
        self._iterateAt = None
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
    def planId(self):
        """Get planId"""
        return self._planId

    @planId.setter
    def planId(self, val):
        """Set planId
        Keyword argument:
        val -- New planId value"""
        self._planId = val
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
        if isinstance(val, dict):
            obj = processout.Plan(self._client)
            obj.fillWithData(val)
            self._plan = obj
        else:
            self._plan = val
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
            obj.fillWithData(val)
            self._customer = obj
        else:
            self._customer = val
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
            obj.fillWithData(val)
            self._token = obj
        else:
            self._token = val
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
        if "plan_id" in data.keys():
            self.planId = data["plan_id"]
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

    def fetchCustomer(self, options = {}):
        """Get the customer owning the subscription.
        Keyword argument:
        
        options -- Options for the request"""
        self.fillWithData(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(self.id) + "/customers"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["customer"]
        customer = Customer(self._client)
        returnValues.append(customer.fillWithData(body))

        
        return returnValues[0]

    def fetchDiscounts(self, options = {}):
        """Get the discounts applied to the subscription.
        Keyword argument:
        
        options -- Options for the request"""
        self.fillWithData(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(self.id) + "/discounts"
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        a    = []
        body = response.body
        for v in body['discounts']:
            tmp = Discount(self._client)
            tmp.fillWithData(v)
            a.append(tmp)

        returnValues.append(a)
            

        
        return returnValues[0]

    def applyCoupon(self, couponId, options = {}):
        """Apply a coupon on the subscription.
        Keyword argument:
        couponId -- ID of the coupon
        options -- Options for the request"""
        self.fillWithData(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(self.id) + "/discounts"
        data    = {
            'coupon_id': couponId
        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["discount"]
        discount = Discount(self._client)
        returnValues.append(discount.fillWithData(body))

        
        return returnValues[0]

    def findDiscount(self, discountId, options = {}):
        """Find a subscription's discount by its ID.
        Keyword argument:
        discountId -- ID of the discount
        options -- Options for the request"""
        self.fillWithData(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(self.id) + "/discounts/" + quote_plus(discountId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["discount"]
        discount = Discount(self._client)
        returnValues.append(discount.fillWithData(body))

        
        return returnValues[0]

    def removeDiscount(self, discountId, options = {}):
        """Remove a discount applied to a subscription.
        Keyword argument:
        discountId -- ID of the discount or coupon to be removed from the subscription
        options -- Options for the request"""
        self.fillWithData(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(self.id) + "/discounts/" + quote_plus(discountId) + ""
        data    = {

        }

        response = Response(request.delete(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["discount"]
                
                
        returnValues.append(self.fillWithData(body))
                

        
        return returnValues[0]

    def fetchTransactions(self, options = {}):
        """Get the subscriptions past transactions.
        Keyword argument:
        
        options -- Options for the request"""
        self.fillWithData(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(self.id) + "/transactions"
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
            

        
        return returnValues[0]

    def all(self, options = {}):
        """Get all the subscriptions.
        Keyword argument:
        
        options -- Options for the request"""
        self.fillWithData(options)

        request = Request(self._client)
        path    = "/subscriptions"
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
            

        
        return returnValues[0]

    def create(self, customerId, options = {}):
        """Create a new subscription for the given customer.
        Keyword argument:
        customerId -- ID of the customer
        options -- Options for the request"""
        self.fillWithData(options)

        request = Request(self._client)
        path    = "/subscriptions"
        data    = {
            'plan_id': self.planId, 
            'cancel_at': self.cancelAt, 
            'name': self.name, 
            'amount': self.amount, 
            'currency': self.currency, 
            'metadata': self.metadata, 
            'interval': self.interval, 
            'trial_end_at': self.trialEndAt, 
            'return_url': self.returnUrl, 
            'cancel_url': self.cancelUrl, 
            'source': options.get("source"), 
            'prorate': options.get("prorate"), 
            'customer_id': customerId
        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["subscription"]
                
                
        returnValues.append(self.fillWithData(body))
                

        
        return returnValues[0]

    def createFromPlan(self, customerId, planId, options = {}):
        """Create a new subscription for the customer from the given plan ID.
        Keyword argument:
        customerId -- ID of the customer
        planId -- ID of the plan
        options -- Options for the request"""
        self.fillWithData(options)

        request = Request(self._client)
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
            'source': options.get("source"), 
            'customer_id': customerId, 
            'plan_id': planId
        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["subscription"]
                
                
        returnValues.append(self.fillWithData(body))
                

        
        return returnValues[0]

    def find(self, subscriptionId, options = {}):
        """Find a subscription by its ID.
        Keyword argument:
        subscriptionId -- ID of the subscription
        options -- Options for the request"""
        self.fillWithData(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(subscriptionId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["subscription"]
                
                
        obj = processout.Subscription(self._client)
        returnValues.append(obj.fillWithData(body))
                

        
        return returnValues[0]

    def save(self, options = {}):
        """Save the updated subscription attributes.
        Keyword argument:
        
        options -- Options for the request"""
        self.fillWithData(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(self.id) + ""
        data    = {
            'plan_id': self.planId, 
            'name': self.name, 
            'amount': self.amount, 
            'interval': self.interval, 
            'trial_end_at': self.trialEndAt, 
            'metadata': self.metadata, 
            'coupon_id': options.get("coupon_id"), 
            'source': options.get("source"), 
            'prorate': options.get("prorate"), 
            'proration_date': options.get("proration_date")
        }

        response = Response(request.put(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["subscription"]
                
                
        returnValues.append(self.fillWithData(body))
                

        
        return returnValues[0]

    def cancel(self, cancellationReason, options = {}):
        """Cancel a subscription. The reason may be provided as well.
        Keyword argument:
        cancellationReason -- Cancellation reason
        options -- Options for the request"""
        self.fillWithData(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(self.id) + ""
        data    = {
            'cancellation_reason': cancellationReason
        }

        response = Response(request.delete(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["subscription"]
                
                
        returnValues.append(self.fillWithData(body))
                

        
        return returnValues[0]

    def cancelAtDate(self, cancelAt, cancellationReason, options = {}):
        """Schedule the cancellation of the subscription. The reason may be provided as well.
        Keyword argument:
        cancelAt -- Cancellation date, in the form of a string
        cancellationReason -- Cancellation reason
        options -- Options for the request"""
        self.fillWithData(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(self.id) + ""
        data    = {
            'cancel_at_end': options.get("cancel_at_end"), 
            'cancel_at': cancelAt, 
            'cancellation_reason': cancellationReason
        }

        response = Response(request.delete(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["subscription"]
                
                
        returnValues.append(self.fillWithData(body))
                

        
        return returnValues[0]

    

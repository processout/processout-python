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
        self._plan_id = None
        self._plan = None
        self._customer = None
        self._token = None
        self._url = None
        self._name = None
        self._amount = None
        self._currency = None
        self._metadata = None
        self._interval = None
        self._trial_end_at = None
        self._activated = None
        self._active = None
        self._canceled = None
        self._cancellation_reason = None
        self._pending_cancellation = None
        self._cancel_at = None
        self._return_url = None
        self._cancel_url = None
        self._sandbox = None
        self._created_at = None
        self._activated_at = None
        self._iterate_at = None
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
    def plan_id(self):
        """Get plan_id"""
        return self._plan_id

    @plan_id.setter
    def plan_id(self, val):
        """Set plan_id
        Keyword argument:
        val -- New plan_id value"""
        self._plan_id = val
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
            obj.fill_with_data(val)
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
            obj.fill_with_data(val)
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
            obj.fill_with_data(val)
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
    def trial_end_at(self):
        """Get trial_end_at"""
        return self._trial_end_at

    @trial_end_at.setter
    def trial_end_at(self, val):
        """Set trial_end_at
        Keyword argument:
        val -- New trial_end_at value"""
        self._trial_end_at = val
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
    def cancellation_reason(self):
        """Get cancellation_reason"""
        return self._cancellation_reason

    @cancellation_reason.setter
    def cancellation_reason(self, val):
        """Set cancellation_reason
        Keyword argument:
        val -- New cancellation_reason value"""
        self._cancellation_reason = val
        return self
    
    @property
    def pending_cancellation(self):
        """Get pending_cancellation"""
        return self._pending_cancellation

    @pending_cancellation.setter
    def pending_cancellation(self, val):
        """Set pending_cancellation
        Keyword argument:
        val -- New pending_cancellation value"""
        self._pending_cancellation = val
        return self
    
    @property
    def cancel_at(self):
        """Get cancel_at"""
        return self._cancel_at

    @cancel_at.setter
    def cancel_at(self, val):
        """Set cancel_at
        Keyword argument:
        val -- New cancel_at value"""
        self._cancel_at = val
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
    
    @property
    def activated_at(self):
        """Get activated_at"""
        return self._activated_at

    @activated_at.setter
    def activated_at(self, val):
        """Set activated_at
        Keyword argument:
        val -- New activated_at value"""
        self._activated_at = val
        return self
    
    @property
    def iterate_at(self):
        """Get iterate_at"""
        return self._iterate_at

    @iterate_at.setter
    def iterate_at(self, val):
        """Set iterate_at
        Keyword argument:
        val -- New iterate_at value"""
        self._iterate_at = val
        return self
    

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "id" in data.keys():
            self.id = data["id"]
        if "project" in data.keys():
            self.project = data["project"]
        if "plan_id" in data.keys():
            self.plan_id = data["plan_id"]
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
            self.trial_end_at = data["trial_end_at"]
        if "activated" in data.keys():
            self.activated = data["activated"]
        if "active" in data.keys():
            self.active = data["active"]
        if "canceled" in data.keys():
            self.canceled = data["canceled"]
        if "cancellation_reason" in data.keys():
            self.cancellation_reason = data["cancellation_reason"]
        if "pending_cancellation" in data.keys():
            self.pending_cancellation = data["pending_cancellation"]
        if "cancel_at" in data.keys():
            self.cancel_at = data["cancel_at"]
        if "return_url" in data.keys():
            self.return_url = data["return_url"]
        if "cancel_url" in data.keys():
            self.cancel_url = data["cancel_url"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        if "activated_at" in data.keys():
            self.activated_at = data["activated_at"]
        if "iterate_at" in data.keys():
            self.iterate_at = data["iterate_at"]
        
        return self

    def fetch_customer(self, options = {}):
        """Get the customer owning the subscription.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(self.id) + "/customers"
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        body = response.body
        body = body["customer"]
        customer = Customer(self._client)
        return_values.append(customer.fill_with_data(body))

        
        return return_values[0]

    def fetch_discounts(self, options = {}):
        """Get the discounts applied to the subscription.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(self.id) + "/discounts"
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        a    = []
        body = response.body
        for v in body['discounts']:
            tmp = Discount(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)
            

        
        return return_values[0]

    def apply_coupon(self, coupon_id, options = {}):
        """Apply a coupon on the subscription.
        Keyword argument:
        coupon_id -- ID of the coupon
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(self.id) + "/discounts"
        data    = {
            'coupon_id': coupon_id
        }

        response = Response(request.post(path, data, options))
        return_values = []
        
        body = response.body
        body = body["discount"]
        discount = Discount(self._client)
        return_values.append(discount.fill_with_data(body))

        
        return return_values[0]

    def find_discount(self, discount_id, options = {}):
        """Find a subscription's discount by its ID.
        Keyword argument:
        discount_id -- ID of the discount
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(self.id) + "/discounts/" + quote_plus(discount_id) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        body = response.body
        body = body["discount"]
        discount = Discount(self._client)
        return_values.append(discount.fill_with_data(body))

        
        return return_values[0]

    def remove_discount(self, discount_id, options = {}):
        """Remove a discount applied to a subscription.
        Keyword argument:
        discount_id -- ID of the discount or coupon to be removed from the subscription
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(self.id) + "/discounts/" + quote_plus(discount_id) + ""
        data    = {

        }

        response = Response(request.delete(path, data, options))
        return_values = []
        
        body = response.body
        body = body["discount"]
                
                
        return_values.append(self.fill_with_data(body))
                

        
        return return_values[0]

    def fetch_transactions(self, options = {}):
        """Get the subscriptions past transactions.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(self.id) + "/transactions"
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        a    = []
        body = response.body
        for v in body['transactions']:
            tmp = Transaction(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)
            

        
        return return_values[0]

    def all(self, options = {}):
        """Get all the subscriptions.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/subscriptions"
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        a    = []
        body = response.body
        for v in body['subscriptions']:
            tmp = Subscription(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)
            

        
        return return_values[0]

    def create(self, customer_id, options = {}):
        """Create a new subscription for the given customer.
        Keyword argument:
        customer_id -- ID of the customer
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/subscriptions"
        data    = {
            'plan_id': self.plan_id, 
            'cancel_at': self.cancel_at, 
            'name': self.name, 
            'amount': self.amount, 
            'currency': self.currency, 
            'metadata': self.metadata, 
            'interval': self.interval, 
            'trial_end_at': self.trial_end_at, 
            'return_url': self.return_url, 
            'cancel_url': self.cancel_url, 
            'source': options.get("source"), 
            'prorate': options.get("prorate"), 
            'customer_id': customer_id
        }

        response = Response(request.post(path, data, options))
        return_values = []
        
        body = response.body
        body = body["subscription"]
                
                
        return_values.append(self.fill_with_data(body))
                

        
        return return_values[0]

    def create_from_plan(self, customer_id, plan_id, options = {}):
        """Create a new subscription for the customer from the given plan ID.
        Keyword argument:
        customer_id -- ID of the customer
        plan_id -- ID of the plan
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/subscriptions"
        data    = {
            'cancel_at': self.cancel_at, 
            'name': self.name, 
            'amount': self.amount, 
            'currency': self.currency, 
            'metadata': self.metadata, 
            'interval': self.interval, 
            'trial_end_at': self.trial_end_at, 
            'return_url': self.return_url, 
            'cancel_url': self.cancel_url, 
            'source': options.get("source"), 
            'customer_id': customer_id, 
            'plan_id': plan_id
        }

        response = Response(request.post(path, data, options))
        return_values = []
        
        body = response.body
        body = body["subscription"]
                
                
        return_values.append(self.fill_with_data(body))
                

        
        return return_values[0]

    def find(self, subscription_id, options = {}):
        """Find a subscription by its ID.
        Keyword argument:
        subscription_id -- ID of the subscription
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(subscription_id) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        body = response.body
        body = body["subscription"]
                
                
        obj = processout.Subscription(self._client)
        return_values.append(obj.fill_with_data(body))
                

        
        return return_values[0]

    def save(self, options = {}):
        """Save the updated subscription attributes.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(self.id) + ""
        data    = {
            'plan_id': self.plan_id, 
            'name': self.name, 
            'amount': self.amount, 
            'interval': self.interval, 
            'trial_end_at': self.trial_end_at, 
            'metadata': self.metadata, 
            'coupon_id': options.get("coupon_id"), 
            'source': options.get("source"), 
            'prorate': options.get("prorate"), 
            'proration_date': options.get("proration_date")
        }

        response = Response(request.put(path, data, options))
        return_values = []
        
        body = response.body
        body = body["subscription"]
                
                
        return_values.append(self.fill_with_data(body))
                

        
        return return_values[0]

    def cancel(self, cancellation_reason, options = {}):
        """Cancel a subscription. The reason may be provided as well.
        Keyword argument:
        cancellation_reason -- Cancellation reason
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(self.id) + ""
        data    = {
            'cancellation_reason': cancellation_reason
        }

        response = Response(request.delete(path, data, options))
        return_values = []
        
        body = response.body
        body = body["subscription"]
                
                
        return_values.append(self.fill_with_data(body))
                

        
        return return_values[0]

    def cancel_at_date(self, cancel_at, cancellation_reason, options = {}):
        """Schedule the cancellation of the subscription. The reason may be provided as well.
        Keyword argument:
        cancel_at -- Cancellation date, in the form of a string
        cancellation_reason -- Cancellation reason
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/subscriptions/" + quote_plus(self.id) + ""
        data    = {
            'cancel_at_end': options.get("cancel_at_end"), 
            'cancel_at': cancel_at, 
            'cancellation_reason': cancellation_reason
        }

        response = Response(request.delete(path, data, options))
        return_values = []
        
        body = response.body
        body = body["subscription"]
                
                
        return_values.append(self.fill_with_data(body))
                

        
        return return_values[0]

    

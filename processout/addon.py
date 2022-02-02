try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class Addon(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._id = None
        self._project = None
        self._project_id = None
        self._subscription = None
        self._subscription_id = None
        self._plan = None
        self._plan_id = None
        self._type = None
        self._name = None
        self._amount = None
        self._quantity = None
        self._metadata = None
        self._sandbox = None
        self._created_at = None
        if prefill is not None:
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
        if val is None:
            self._project = val
            return self

        if isinstance(val, dict):
            obj = processout.Project(self._client)
            obj.fill_with_data(val)
            self._project = obj
        else:
            self._project = val
        return self

    @property
    def project_id(self):
        """Get project_id"""
        return self._project_id

    @project_id.setter
    def project_id(self, val):
        """Set project_id
        Keyword argument:
        val -- New project_id value"""
        self._project_id = val
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
        if val is None:
            self._subscription = val
            return self

        if isinstance(val, dict):
            obj = processout.Subscription(self._client)
            obj.fill_with_data(val)
            self._subscription = obj
        else:
            self._subscription = val
        return self

    @property
    def subscription_id(self):
        """Get subscription_id"""
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, val):
        """Set subscription_id
        Keyword argument:
        val -- New subscription_id value"""
        self._subscription_id = val
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
        if val is None:
            self._plan = val
            return self

        if isinstance(val, dict):
            obj = processout.Plan(self._client)
            obj.fill_with_data(val)
            self._plan = obj
        else:
            self._plan = val
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
    def type(self):
        """Get type"""
        return self._type

    @type.setter
    def type(self, val):
        """Set type
        Keyword argument:
        val -- New type value"""
        self._type = val
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
    def quantity(self):
        """Get quantity"""
        return self._quantity

    @quantity.setter
    def quantity(self, val):
        """Set quantity
        Keyword argument:
        val -- New quantity value"""
        self._quantity = val
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
        if "project_id" in data.keys():
            self.project_id = data["project_id"]
        if "subscription" in data.keys():
            self.subscription = data["subscription"]
        if "subscription_id" in data.keys():
            self.subscription_id = data["subscription_id"]
        if "plan" in data.keys():
            self.plan = data["plan"]
        if "plan_id" in data.keys():
            self.plan_id = data["plan_id"]
        if "type" in data.keys():
            self.type = data["type"]
        if "name" in data.keys():
            self.name = data["name"]
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "quantity" in data.keys():
            self.quantity = data["quantity"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]

        return self

    def to_json(self):
        return {
            "id": self.id,
            "project": self.project,
            "project_id": self.project_id,
            "subscription": self.subscription,
            "subscription_id": self.subscription_id,
            "plan": self.plan,
            "plan_id": self.plan_id,
            "type": self.type,
            "name": self.name,
            "amount": self.amount,
            "quantity": self.quantity,
            "metadata": self.metadata,
            "sandbox": self.sandbox,
            "created_at": self.created_at,
        }

    def fetch_subscription_addons(self, subscription_id, options={}):
        """Get the addons applied to the subscription.
        Keyword argument:
        subscription_id -- ID of the subscription
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/subscriptions/" + quote_plus(subscription_id) + "/addons"
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        a = []
        body = response.body
        for v in body['addons']:
            tmp = processout.Addon(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)

        return return_values[0]

    def create(self, options={}):
        """Create a new addon to the given subscription ID.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/subscriptions/" + quote_plus(self.subscription_id) + "/addons"
        data = {
            'plan_id': self.plan_id,
            'type': self.type,
            'name': self.name,
            'amount': self.amount,
            'quantity': self.quantity,
            'metadata': self.metadata,
            'prorate': options.get("prorate"),
            'proration_date': options.get("proration_date"),
            'preview': options.get("preview")
        }

        response = Response(request.post(path, data, options))
        return_values = []

        body = response.body
        body = body["addon"]

        return_values.append(self.fill_with_data(body))

        return return_values[0]

    def find(self, subscription_id, addon_id, options={}):
        """Find a subscription's addon by its ID.
        Keyword argument:
        subscription_id -- ID of the subscription on which the addon was applied
        addon_id -- ID of the addon
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/subscriptions/" + \
            quote_plus(subscription_id) + "/addons/" + quote_plus(addon_id) + ""
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        body = response.body
        body = body["addon"]

        obj = processout.Addon(self._client)
        return_values.append(obj.fill_with_data(body))

        return return_values[0]

    def save(self, options={}):
        """Save the updated addon attributes.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/subscriptions/" + \
            quote_plus(self.subscription_id) + "/addons/" + quote_plus(self.id) + ""
        data = {
            'plan_id': self.plan_id,
            'type': self.type,
            'name': self.name,
            'amount': self.amount,
            'quantity': self.quantity,
            'metadata': self.metadata,
            'prorate': options.get("prorate"),
            'proration_date': options.get("proration_date"),
            'preview': options.get("preview"),
            'increment_quantity_by': options.get("increment_quantity_by")
        }

        response = Response(request.put(path, data, options))
        return_values = []

        body = response.body
        body = body["addon"]

        return_values.append(self.fill_with_data(body))

        return return_values[0]

    def delete(self, options={}):
        """Delete an addon applied to a subscription.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/subscriptions/" + \
            quote_plus(self.subscription_id) + "/addons/" + quote_plus(self.id) + ""
        data = {
            'prorate': options.get("prorate"),
            'proration_date': options.get("proration_date"),
            'preview': options.get("preview")
        }

        response = Response(request.delete(path, data, options))
        return_values = []

        return_values.append(response.success)

        return return_values[0]

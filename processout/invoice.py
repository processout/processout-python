try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class Invoice(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._id = None
        self._project = None
        self._project_id = None
        self._transaction = None
        self._transaction_id = None
        self._customer = None
        self._customer_id = None
        self._subscription = None
        self._subscription_id = None
        self._token = None
        self._token_id = None
        self._details = None
        self._url = None
        self._name = None
        self._amount = None
        self._currency = None
        self._merchant_initiator_type = None
        self._statement_descriptor = None
        self._statement_descriptor_phone = None
        self._statement_descriptor_city = None
        self._statement_descriptor_company = None
        self._statement_descriptor_url = None
        self._metadata = None
        self._gateway_data = None
        self._return_url = None
        self._cancel_url = None
        self._webhook_url = None
        self._require_backend_capture = None
        self._sandbox = None
        self._created_at = None
        self._risk = None
        self._shipping = None
        self._device = None
        self._external_fraud_tools = None
        self._exemption_reason_3ds2 = None
        self._sca_exemption_reason = None
        self._challenge_indicator = None
        self._incremental = None
        self._tax = None
        self._payment_type = None
        self._initiation_type = None
        self._payment_intent = None
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
    def transaction(self):
        """Get transaction"""
        return self._transaction

    @transaction.setter
    def transaction(self, val):
        """Set transaction
        Keyword argument:
        val -- New transaction value"""
        if val is None:
            self._transaction = val
            return self

        if isinstance(val, dict):
            obj = processout.Transaction(self._client)
            obj.fill_with_data(val)
            self._transaction = obj
        else:
            self._transaction = val
        return self

    @property
    def transaction_id(self):
        """Get transaction_id"""
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, val):
        """Set transaction_id
        Keyword argument:
        val -- New transaction_id value"""
        self._transaction_id = val
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
        if val is None:
            self._customer = val
            return self

        if isinstance(val, dict):
            obj = processout.Customer(self._client)
            obj.fill_with_data(val)
            self._customer = obj
        else:
            self._customer = val
        return self

    @property
    def customer_id(self):
        """Get customer_id"""
        return self._customer_id

    @customer_id.setter
    def customer_id(self, val):
        """Set customer_id
        Keyword argument:
        val -- New customer_id value"""
        self._customer_id = val
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
    def token(self):
        """Get token"""
        return self._token

    @token.setter
    def token(self, val):
        """Set token
        Keyword argument:
        val -- New token value"""
        if val is None:
            self._token = val
            return self

        if isinstance(val, dict):
            obj = processout.Token(self._client)
            obj.fill_with_data(val)
            self._token = obj
        else:
            self._token = val
        return self

    @property
    def token_id(self):
        """Get token_id"""
        return self._token_id

    @token_id.setter
    def token_id(self, val):
        """Set token_id
        Keyword argument:
        val -- New token_id value"""
        self._token_id = val
        return self

    @property
    def details(self):
        """Get details"""
        return self._details

    @details.setter
    def details(self, val):
        """Set details
        Keyword argument:
        val -- New details value"""
        if val is None:
            self._details = []
            return self

        if len(val) > 0 and isinstance(val[0], processout.InvoiceDetail):
            self._details = val
        else:
            l = []
            for v in val:
                obj = processout.InvoiceDetail(self._client)
                obj.fill_with_data(v)
                l.append(obj)
            self._details = l
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
    def merchant_initiator_type(self):
        """Get merchant_initiator_type"""
        return self._merchant_initiator_type

    @merchant_initiator_type.setter
    def merchant_initiator_type(self, val):
        """Set merchant_initiator_type
        Keyword argument:
        val -- New merchant_initiator_type value"""
        self._merchant_initiator_type = val
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
    def gateway_data(self):
        """Get gateway_data"""
        return self._gateway_data

    @gateway_data.setter
    def gateway_data(self, val):
        """Set gateway_data
        Keyword argument:
        val -- New gateway_data value"""
        self._gateway_data = val
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
    def webhook_url(self):
        """Get webhook_url"""
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, val):
        """Set webhook_url
        Keyword argument:
        val -- New webhook_url value"""
        self._webhook_url = val
        return self

    @property
    def require_backend_capture(self):
        """Get require_backend_capture"""
        return self._require_backend_capture

    @require_backend_capture.setter
    def require_backend_capture(self, val):
        """Set require_backend_capture
        Keyword argument:
        val -- New require_backend_capture value"""
        self._require_backend_capture = val
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
    def risk(self):
        """Get risk"""
        return self._risk

    @risk.setter
    def risk(self, val):
        """Set risk
        Keyword argument:
        val -- New risk value"""
        if val is None:
            self._risk = val
            return self

        if isinstance(val, dict):
            obj = processout.InvoiceRisk(self._client)
            obj.fill_with_data(val)
            self._risk = obj
        else:
            self._risk = val
        return self

    @property
    def shipping(self):
        """Get shipping"""
        return self._shipping

    @shipping.setter
    def shipping(self, val):
        """Set shipping
        Keyword argument:
        val -- New shipping value"""
        if val is None:
            self._shipping = val
            return self

        if isinstance(val, dict):
            obj = processout.InvoiceShipping(self._client)
            obj.fill_with_data(val)
            self._shipping = obj
        else:
            self._shipping = val
        return self

    @property
    def device(self):
        """Get device"""
        return self._device

    @device.setter
    def device(self, val):
        """Set device
        Keyword argument:
        val -- New device value"""
        if val is None:
            self._device = val
            return self

        if isinstance(val, dict):
            obj = processout.InvoiceDevice(self._client)
            obj.fill_with_data(val)
            self._device = obj
        else:
            self._device = val
        return self

    @property
    def external_fraud_tools(self):
        """Get external_fraud_tools"""
        return self._external_fraud_tools

    @external_fraud_tools.setter
    def external_fraud_tools(self, val):
        """Set external_fraud_tools
        Keyword argument:
        val -- New external_fraud_tools value"""
        if val is None:
            self._external_fraud_tools = val
            return self

        if isinstance(val, dict):
            obj = processout.InvoiceExternalFraudTools(self._client)
            obj.fill_with_data(val)
            self._external_fraud_tools = obj
        else:
            self._external_fraud_tools = val
        return self

    @property
    def exemption_reason_3ds2(self):
        """Get exemption_reason_3ds2"""
        return self._exemption_reason_3ds2

    @exemption_reason_3ds2.setter
    def exemption_reason_3ds2(self, val):
        """Set exemption_reason_3ds2
        Keyword argument:
        val -- New exemption_reason_3ds2 value"""
        self._exemption_reason_3ds2 = val
        return self

    @property
    def sca_exemption_reason(self):
        """Get sca_exemption_reason"""
        return self._sca_exemption_reason

    @sca_exemption_reason.setter
    def sca_exemption_reason(self, val):
        """Set sca_exemption_reason
        Keyword argument:
        val -- New sca_exemption_reason value"""
        self._sca_exemption_reason = val
        return self

    @property
    def challenge_indicator(self):
        """Get challenge_indicator"""
        return self._challenge_indicator

    @challenge_indicator.setter
    def challenge_indicator(self, val):
        """Set challenge_indicator
        Keyword argument:
        val -- New challenge_indicator value"""
        self._challenge_indicator = val
        return self

    @property
    def incremental(self):
        """Get incremental"""
        return self._incremental

    @incremental.setter
    def incremental(self, val):
        """Set incremental
        Keyword argument:
        val -- New incremental value"""
        self._incremental = val
        return self

    @property
    def tax(self):
        """Get tax"""
        return self._tax

    @tax.setter
    def tax(self, val):
        """Set tax
        Keyword argument:
        val -- New tax value"""
        if val is None:
            self._tax = val
            return self

        if isinstance(val, dict):
            obj = processout.InvoiceTax(self._client)
            obj.fill_with_data(val)
            self._tax = obj
        else:
            self._tax = val
        return self

    @property
    def payment_type(self):
        """Get payment_type"""
        return self._payment_type

    @payment_type.setter
    def payment_type(self, val):
        """Set payment_type
        Keyword argument:
        val -- New payment_type value"""
        self._payment_type = val
        return self

    @property
    def initiation_type(self):
        """Get initiation_type"""
        return self._initiation_type

    @initiation_type.setter
    def initiation_type(self, val):
        """Set initiation_type
        Keyword argument:
        val -- New initiation_type value"""
        self._initiation_type = val
        return self

    @property
    def payment_intent(self):
        """Get payment_intent"""
        return self._payment_intent

    @payment_intent.setter
    def payment_intent(self, val):
        """Set payment_intent
        Keyword argument:
        val -- New payment_intent value"""
        self._payment_intent = val
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
        if "transaction" in data.keys():
            self.transaction = data["transaction"]
        if "transaction_id" in data.keys():
            self.transaction_id = data["transaction_id"]
        if "customer" in data.keys():
            self.customer = data["customer"]
        if "customer_id" in data.keys():
            self.customer_id = data["customer_id"]
        if "subscription" in data.keys():
            self.subscription = data["subscription"]
        if "subscription_id" in data.keys():
            self.subscription_id = data["subscription_id"]
        if "token" in data.keys():
            self.token = data["token"]
        if "token_id" in data.keys():
            self.token_id = data["token_id"]
        if "details" in data.keys():
            self.details = data["details"]
        if "url" in data.keys():
            self.url = data["url"]
        if "name" in data.keys():
            self.name = data["name"]
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "currency" in data.keys():
            self.currency = data["currency"]
        if "merchant_initiator_type" in data.keys():
            self.merchant_initiator_type = data["merchant_initiator_type"]
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
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "gateway_data" in data.keys():
            self.gateway_data = data["gateway_data"]
        if "return_url" in data.keys():
            self.return_url = data["return_url"]
        if "cancel_url" in data.keys():
            self.cancel_url = data["cancel_url"]
        if "webhook_url" in data.keys():
            self.webhook_url = data["webhook_url"]
        if "require_backend_capture" in data.keys():
            self.require_backend_capture = data["require_backend_capture"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        if "risk" in data.keys():
            self.risk = data["risk"]
        if "shipping" in data.keys():
            self.shipping = data["shipping"]
        if "device" in data.keys():
            self.device = data["device"]
        if "external_fraud_tools" in data.keys():
            self.external_fraud_tools = data["external_fraud_tools"]
        if "exemption_reason_3ds2" in data.keys():
            self.exemption_reason_3ds2 = data["exemption_reason_3ds2"]
        if "sca_exemption_reason" in data.keys():
            self.sca_exemption_reason = data["sca_exemption_reason"]
        if "challenge_indicator" in data.keys():
            self.challenge_indicator = data["challenge_indicator"]
        if "incremental" in data.keys():
            self.incremental = data["incremental"]
        if "tax" in data.keys():
            self.tax = data["tax"]
        if "payment_type" in data.keys():
            self.payment_type = data["payment_type"]
        if "initiation_type" in data.keys():
            self.initiation_type = data["initiation_type"]
        if "payment_intent" in data.keys():
            self.payment_intent = data["payment_intent"]

        return self

    def to_json(self):
        return {
            "id": self.id,
            "project": self.project,
            "project_id": self.project_id,
            "transaction": self.transaction,
            "transaction_id": self.transaction_id,
            "customer": self.customer,
            "customer_id": self.customer_id,
            "subscription": self.subscription,
            "subscription_id": self.subscription_id,
            "token": self.token,
            "token_id": self.token_id,
            "details": self.details,
            "url": self.url,
            "name": self.name,
            "amount": self.amount,
            "currency": self.currency,
            "merchant_initiator_type": self.merchant_initiator_type,
            "statement_descriptor": self.statement_descriptor,
            "statement_descriptor_phone": self.statement_descriptor_phone,
            "statement_descriptor_city": self.statement_descriptor_city,
            "statement_descriptor_company": self.statement_descriptor_company,
            "statement_descriptor_url": self.statement_descriptor_url,
            "metadata": self.metadata,
            "gateway_data": self.gateway_data,
            "return_url": self.return_url,
            "cancel_url": self.cancel_url,
            "webhook_url": self.webhook_url,
            "require_backend_capture": self.require_backend_capture,
            "sandbox": self.sandbox,
            "created_at": self.created_at,
            "risk": self.risk,
            "shipping": self.shipping,
            "device": self.device,
            "external_fraud_tools": self.external_fraud_tools,
            "exemption_reason_3ds2": self.exemption_reason_3ds2,
            "sca_exemption_reason": self.sca_exemption_reason,
            "challenge_indicator": self.challenge_indicator,
            "incremental": self.incremental,
            "tax": self.tax,
            "payment_type": self.payment_type,
            "initiation_type": self.initiation_type,
            "payment_intent": self.payment_intent,
        }

    def increment_authorization(self, amount, options={}):
        """Create an incremental authorization
        Keyword argument:
        amount -- Amount to increment authorization by
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/invoices/" + quote_plus(self.id) + "/increment_authorization"
        data = {
            'metadata': options.get("metadata"),
            'amount': amount
        }

        response = Response(request.post(path, data, options))
        return_values = []

        body = response.body
        body = body["transaction"]
        transaction = processout.Transaction(self._client)
        return_values.append(transaction.fill_with_data(body))

        return return_values[0]

    def authorize(self, source, options={}):
        """Authorize the invoice using the given source (customer or token)
        Keyword argument:
        source -- Source used to authorization the payment. Can be a card, a token or a gateway request
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/invoices/" + quote_plus(self.id) + "/authorize"
        data = {
            'device': self.device,
            'incremental': self.incremental,
            'synchronous': options.get("synchronous"),
            'retry_drop_liability_shift': options.get("retry_drop_liability_shift"),
            'capture_amount': options.get("capture_amount"),
            'enable_three_d_s_2': options.get("enable_three_d_s_2"),
            'allow_fallback_to_sale': options.get("allow_fallback_to_sale"),
            'auto_capture_at': options.get("auto_capture_at"),
            'metadata': options.get("metadata"),
            'source': source}

        response = Response(request.post(path, data, options))
        return_values = []

        body = response.body
        body = body["transaction"]
        transaction = processout.Transaction(self._client)
        return_values.append(transaction.fill_with_data(body))

        return return_values[0]

    def capture(self, source, options={}):
        """Capture the invoice using the given source (customer or token)
        Keyword argument:
        source -- Source used to authorization the payment. Can be a card, a token or a gateway request
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/invoices/" + quote_plus(self.id) + "/capture"
        data = {
            'device': self.device,
            'incremental': self.incremental,
            'authorize_only': options.get("authorize_only"),
            'synchronous': options.get("synchronous"),
            'retry_drop_liability_shift': options.get("retry_drop_liability_shift"),
            'capture_amount': options.get("capture_amount"),
            'auto_capture_at': options.get("auto_capture_at"),
            'enable_three_d_s_2': options.get("enable_three_d_s_2"),
            'metadata': options.get("metadata"),
            'source': source}

        response = Response(request.post(path, data, options))
        return_values = []

        body = response.body
        body = body["transaction"]
        transaction = processout.Transaction(self._client)
        return_values.append(transaction.fill_with_data(body))

        return return_values[0]

    def fetch_customer(self, options={}):
        """Get the customer linked to the invoice.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/invoices/" + quote_plus(self.id) + "/customers"
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        body = response.body
        body = body["customer"]
        customer = processout.Customer(self._client)
        return_values.append(customer.fill_with_data(body))

        return return_values[0]

    def assign_customer(self, customer_id, options={}):
        """Assign a customer to the invoice.
        Keyword argument:
        customer_id -- ID of the customer to be linked to the invoice
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/invoices/" + quote_plus(self.id) + "/customers"
        data = {
            'customer_id': customer_id
        }

        response = Response(request.post(path, data, options))
        return_values = []

        body = response.body
        body = body["customer"]
        customer = processout.Customer(self._client)
        return_values.append(customer.fill_with_data(body))

        return return_values[0]

    def initiate_three_d_s(self, source, options={}):
        """Initiate a 3-D Secure authentication
        Keyword argument:
        source -- Source used to initiate the 3-D Secure authentication. Can be a card, or a token representing a card
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/invoices/" + quote_plus(self.id) + "/three-d-s"
        data = {
            'enable_three_d_s_2': options.get("enable_three_d_s_2"),
            'source': source
        }

        response = Response(request.post(path, data, options))
        return_values = []

        body = response.body
        body = body["customer_action"]
        customerAction = processout.CustomerAction(self._client)
        return_values.append(customerAction.fill_with_data(body))

        return return_values[0]

    def fetch_transaction(self, options={}):
        """Get the transaction of the invoice.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/invoices/" + quote_plus(self.id) + "/transactions"
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        body = response.body
        body = body["transaction"]
        transaction = processout.Transaction(self._client)
        return_values.append(transaction.fill_with_data(body))

        return return_values[0]

    def void(self, options={}):
        """Void the invoice
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/invoices/" + quote_plus(self.id) + "/void"
        data = {
            'metadata': options.get("metadata")
        }

        response = Response(request.post(path, data, options))
        return_values = []

        body = response.body
        body = body["transaction"]
        transaction = processout.Transaction(self._client)
        return_values.append(transaction.fill_with_data(body))

        return return_values[0]

    def all(self, options={}):
        """Get all the invoices.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/invoices"
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        a = []
        body = response.body
        for v in body['invoices']:
            tmp = processout.Invoice(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)

        return return_values[0]

    def create(self, options={}):
        """Create a new invoice.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/invoices"
        data = {
            'customer_id': self.customer_id,
            'name': self.name,
            'amount': self.amount,
            'currency': self.currency,
            'metadata': self.metadata,
            'details': self.details,
            'exemption_reason_3ds2': self.exemption_reason_3ds2,
            'sca_exemption_reason': self.sca_exemption_reason,
            'challenge_indicator': self.challenge_indicator,
            'gateway_data': self.gateway_data,
            'merchant_initiator_type': self.merchant_initiator_type,
            'initiation_type': self.initiation_type,
            'payment_intent': self.payment_intent,
            'statement_descriptor': self.statement_descriptor,
            'statement_descriptor_phone': self.statement_descriptor_phone,
            'statement_descriptor_city': self.statement_descriptor_city,
            'statement_descriptor_company': self.statement_descriptor_company,
            'statement_descriptor_url': self.statement_descriptor_url,
            'return_url': self.return_url,
            'cancel_url': self.cancel_url,
            'webhook_url': self.webhook_url,
            'risk': self.risk,
            'shipping': self.shipping,
            'device': self.device,
            'require_backend_capture': self.require_backend_capture,
            'external_fraud_tools': self.external_fraud_tools,
            'tax': self.tax,
            'payment_type': self.payment_type
        }

        response = Response(request.post(path, data, options))
        return_values = []

        body = response.body
        body = body["invoice"]

        return_values.append(self.fill_with_data(body))

        return return_values[0]

    def find(self, invoice_id, options={}):
        """Find an invoice by its ID.
        Keyword argument:
        invoice_id -- ID of the invoice
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/invoices/" + quote_plus(invoice_id) + ""
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        body = response.body
        body = body["invoice"]

        obj = processout.Invoice(self._client)
        return_values.append(obj.fill_with_data(body))

        return return_values[0]

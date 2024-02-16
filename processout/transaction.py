try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class Transaction(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._id = None
        self._project = None
        self._project_id = None
        self._invoice = None
        self._invoice_id = None
        self._customer = None
        self._customer_id = None
        self._subscription = None
        self._subscription_id = None
        self._token = None
        self._token_id = None
        self._card = None
        self._card_id = None
        self._gateway_configuration = None
        self._external_three_d_s_gateway_configuration = None
        self._gateway_configuration_id = None
        self._operations = None
        self._refunds = None
        self._name = None
        self._amount = None
        self._amount_local = None
        self._authorized_amount = None
        self._authorized_amount_local = None
        self._captured_amount = None
        self._captured_amount_local = None
        self._refunded_amount = None
        self._refunded_amount_local = None
        self._available_amount = None
        self._available_amount_local = None
        self._voided_amount = None
        self._voided_amount_local = None
        self._currency = None
        self._error_code = None
        self._error_message = None
        self._acquirer_name = None
        self._gateway_name = None
        self._three_d_s_status = None
        self._status = None
        self._authorized = None
        self._captured = None
        self._voided = None
        self._refunded = None
        self._chargedback = None
        self._received_fraud_notification = None
        self._received_retrieval_request = None
        self._processout_fee = None
        self._estimated_fee = None
        self._gateway_fee = None
        self._gateway_fee_local = None
        self._currency_fee = None
        self._metadata = None
        self._sandbox = None
        self._created_at = None
        self._chargedback_at = None
        self._refunded_at = None
        self._authorized_at = None
        self._captured_at = None
        self._voided_at = None
        self._three_d_s = None
        self._cvc_check = None
        self._avs_check = None
        self._initial_scheme_transaction_id = None
        self._scheme_id = None
        self._payment_type = None
        self._eci = None
        self._native_apm = None
        self._external_details = None
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
    def invoice(self):
        """Get invoice"""
        return self._invoice

    @invoice.setter
    def invoice(self, val):
        """Set invoice
        Keyword argument:
        val -- New invoice value"""
        if val is None:
            self._invoice = val
            return self

        if isinstance(val, dict):
            obj = processout.Invoice(self._client)
            obj.fill_with_data(val)
            self._invoice = obj
        else:
            self._invoice = val
        return self

    @property
    def invoice_id(self):
        """Get invoice_id"""
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, val):
        """Set invoice_id
        Keyword argument:
        val -- New invoice_id value"""
        self._invoice_id = val
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
    def card(self):
        """Get card"""
        return self._card

    @card.setter
    def card(self, val):
        """Set card
        Keyword argument:
        val -- New card value"""
        if val is None:
            self._card = val
            return self

        if isinstance(val, dict):
            obj = processout.Card(self._client)
            obj.fill_with_data(val)
            self._card = obj
        else:
            self._card = val
        return self

    @property
    def card_id(self):
        """Get card_id"""
        return self._card_id

    @card_id.setter
    def card_id(self, val):
        """Set card_id
        Keyword argument:
        val -- New card_id value"""
        self._card_id = val
        return self

    @property
    def gateway_configuration(self):
        """Get gateway_configuration"""
        return self._gateway_configuration

    @gateway_configuration.setter
    def gateway_configuration(self, val):
        """Set gateway_configuration
        Keyword argument:
        val -- New gateway_configuration value"""
        if val is None:
            self._gateway_configuration = val
            return self

        if isinstance(val, dict):
            obj = processout.GatewayConfiguration(self._client)
            obj.fill_with_data(val)
            self._gateway_configuration = obj
        else:
            self._gateway_configuration = val
        return self

    @property
    def external_three_d_s_gateway_configuration(self):
        """Get external_three_d_s_gateway_configuration"""
        return self._external_three_d_s_gateway_configuration

    @external_three_d_s_gateway_configuration.setter
    def external_three_d_s_gateway_configuration(self, val):
        """Set external_three_d_s_gateway_configuration
        Keyword argument:
        val -- New external_three_d_s_gateway_configuration value"""
        if val is None:
            self._external_three_d_s_gateway_configuration = val
            return self

        if isinstance(val, dict):
            obj = processout.GatewayConfiguration(self._client)
            obj.fill_with_data(val)
            self._external_three_d_s_gateway_configuration = obj
        else:
            self._external_three_d_s_gateway_configuration = val
        return self

    @property
    def gateway_configuration_id(self):
        """Get gateway_configuration_id"""
        return self._gateway_configuration_id

    @gateway_configuration_id.setter
    def gateway_configuration_id(self, val):
        """Set gateway_configuration_id
        Keyword argument:
        val -- New gateway_configuration_id value"""
        self._gateway_configuration_id = val
        return self

    @property
    def operations(self):
        """Get operations"""
        return self._operations

    @operations.setter
    def operations(self, val):
        """Set operations
        Keyword argument:
        val -- New operations value"""
        if val is None:
            self._operations = []
            return self

        if len(val) > 0 and isinstance(
                val[0], processout.TransactionOperation):
            self._operations = val
        else:
            l = []
            for v in val:
                obj = processout.TransactionOperation(self._client)
                obj.fill_with_data(v)
                l.append(obj)
            self._operations = l
        return self

    @property
    def refunds(self):
        """Get refunds"""
        return self._refunds

    @refunds.setter
    def refunds(self, val):
        """Set refunds
        Keyword argument:
        val -- New refunds value"""
        if val is None:
            self._refunds = []
            return self

        if len(val) > 0 and isinstance(val[0], processout.Refund):
            self._refunds = val
        else:
            l = []
            for v in val:
                obj = processout.Refund(self._client)
                obj.fill_with_data(v)
                l.append(obj)
            self._refunds = l
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
    def amount_local(self):
        """Get amount_local"""
        return self._amount_local

    @amount_local.setter
    def amount_local(self, val):
        """Set amount_local
        Keyword argument:
        val -- New amount_local value"""
        self._amount_local = val
        return self

    @property
    def authorized_amount(self):
        """Get authorized_amount"""
        return self._authorized_amount

    @authorized_amount.setter
    def authorized_amount(self, val):
        """Set authorized_amount
        Keyword argument:
        val -- New authorized_amount value"""
        self._authorized_amount = val
        return self

    @property
    def authorized_amount_local(self):
        """Get authorized_amount_local"""
        return self._authorized_amount_local

    @authorized_amount_local.setter
    def authorized_amount_local(self, val):
        """Set authorized_amount_local
        Keyword argument:
        val -- New authorized_amount_local value"""
        self._authorized_amount_local = val
        return self

    @property
    def captured_amount(self):
        """Get captured_amount"""
        return self._captured_amount

    @captured_amount.setter
    def captured_amount(self, val):
        """Set captured_amount
        Keyword argument:
        val -- New captured_amount value"""
        self._captured_amount = val
        return self

    @property
    def captured_amount_local(self):
        """Get captured_amount_local"""
        return self._captured_amount_local

    @captured_amount_local.setter
    def captured_amount_local(self, val):
        """Set captured_amount_local
        Keyword argument:
        val -- New captured_amount_local value"""
        self._captured_amount_local = val
        return self

    @property
    def refunded_amount(self):
        """Get refunded_amount"""
        return self._refunded_amount

    @refunded_amount.setter
    def refunded_amount(self, val):
        """Set refunded_amount
        Keyword argument:
        val -- New refunded_amount value"""
        self._refunded_amount = val
        return self

    @property
    def refunded_amount_local(self):
        """Get refunded_amount_local"""
        return self._refunded_amount_local

    @refunded_amount_local.setter
    def refunded_amount_local(self, val):
        """Set refunded_amount_local
        Keyword argument:
        val -- New refunded_amount_local value"""
        self._refunded_amount_local = val
        return self

    @property
    def available_amount(self):
        """Get available_amount"""
        return self._available_amount

    @available_amount.setter
    def available_amount(self, val):
        """Set available_amount
        Keyword argument:
        val -- New available_amount value"""
        self._available_amount = val
        return self

    @property
    def available_amount_local(self):
        """Get available_amount_local"""
        return self._available_amount_local

    @available_amount_local.setter
    def available_amount_local(self, val):
        """Set available_amount_local
        Keyword argument:
        val -- New available_amount_local value"""
        self._available_amount_local = val
        return self

    @property
    def voided_amount(self):
        """Get voided_amount"""
        return self._voided_amount

    @voided_amount.setter
    def voided_amount(self, val):
        """Set voided_amount
        Keyword argument:
        val -- New voided_amount value"""
        self._voided_amount = val
        return self

    @property
    def voided_amount_local(self):
        """Get voided_amount_local"""
        return self._voided_amount_local

    @voided_amount_local.setter
    def voided_amount_local(self, val):
        """Set voided_amount_local
        Keyword argument:
        val -- New voided_amount_local value"""
        self._voided_amount_local = val
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
    def error_code(self):
        """Get error_code"""
        return self._error_code

    @error_code.setter
    def error_code(self, val):
        """Set error_code
        Keyword argument:
        val -- New error_code value"""
        self._error_code = val
        return self

    @property
    def error_message(self):
        """Get error_message"""
        return self._error_message

    @error_message.setter
    def error_message(self, val):
        """Set error_message
        Keyword argument:
        val -- New error_message value"""
        self._error_message = val
        return self

    @property
    def acquirer_name(self):
        """Get acquirer_name"""
        return self._acquirer_name

    @acquirer_name.setter
    def acquirer_name(self, val):
        """Set acquirer_name
        Keyword argument:
        val -- New acquirer_name value"""
        self._acquirer_name = val
        return self

    @property
    def gateway_name(self):
        """Get gateway_name"""
        return self._gateway_name

    @gateway_name.setter
    def gateway_name(self, val):
        """Set gateway_name
        Keyword argument:
        val -- New gateway_name value"""
        self._gateway_name = val
        return self

    @property
    def three_d_s_status(self):
        """Get three_d_s_status"""
        return self._three_d_s_status

    @three_d_s_status.setter
    def three_d_s_status(self, val):
        """Set three_d_s_status
        Keyword argument:
        val -- New three_d_s_status value"""
        self._three_d_s_status = val
        return self

    @property
    def status(self):
        """Get status"""
        return self._status

    @status.setter
    def status(self, val):
        """Set status
        Keyword argument:
        val -- New status value"""
        self._status = val
        return self

    @property
    def authorized(self):
        """Get authorized"""
        return self._authorized

    @authorized.setter
    def authorized(self, val):
        """Set authorized
        Keyword argument:
        val -- New authorized value"""
        self._authorized = val
        return self

    @property
    def captured(self):
        """Get captured"""
        return self._captured

    @captured.setter
    def captured(self, val):
        """Set captured
        Keyword argument:
        val -- New captured value"""
        self._captured = val
        return self

    @property
    def voided(self):
        """Get voided"""
        return self._voided

    @voided.setter
    def voided(self, val):
        """Set voided
        Keyword argument:
        val -- New voided value"""
        self._voided = val
        return self

    @property
    def refunded(self):
        """Get refunded"""
        return self._refunded

    @refunded.setter
    def refunded(self, val):
        """Set refunded
        Keyword argument:
        val -- New refunded value"""
        self._refunded = val
        return self

    @property
    def chargedback(self):
        """Get chargedback"""
        return self._chargedback

    @chargedback.setter
    def chargedback(self, val):
        """Set chargedback
        Keyword argument:
        val -- New chargedback value"""
        self._chargedback = val
        return self

    @property
    def received_fraud_notification(self):
        """Get received_fraud_notification"""
        return self._received_fraud_notification

    @received_fraud_notification.setter
    def received_fraud_notification(self, val):
        """Set received_fraud_notification
        Keyword argument:
        val -- New received_fraud_notification value"""
        self._received_fraud_notification = val
        return self

    @property
    def received_retrieval_request(self):
        """Get received_retrieval_request"""
        return self._received_retrieval_request

    @received_retrieval_request.setter
    def received_retrieval_request(self, val):
        """Set received_retrieval_request
        Keyword argument:
        val -- New received_retrieval_request value"""
        self._received_retrieval_request = val
        return self

    @property
    def processout_fee(self):
        """Get processout_fee"""
        return self._processout_fee

    @processout_fee.setter
    def processout_fee(self, val):
        """Set processout_fee
        Keyword argument:
        val -- New processout_fee value"""
        self._processout_fee = val
        return self

    @property
    def estimated_fee(self):
        """Get estimated_fee"""
        return self._estimated_fee

    @estimated_fee.setter
    def estimated_fee(self, val):
        """Set estimated_fee
        Keyword argument:
        val -- New estimated_fee value"""
        self._estimated_fee = val
        return self

    @property
    def gateway_fee(self):
        """Get gateway_fee"""
        return self._gateway_fee

    @gateway_fee.setter
    def gateway_fee(self, val):
        """Set gateway_fee
        Keyword argument:
        val -- New gateway_fee value"""
        self._gateway_fee = val
        return self

    @property
    def gateway_fee_local(self):
        """Get gateway_fee_local"""
        return self._gateway_fee_local

    @gateway_fee_local.setter
    def gateway_fee_local(self, val):
        """Set gateway_fee_local
        Keyword argument:
        val -- New gateway_fee_local value"""
        self._gateway_fee_local = val
        return self

    @property
    def currency_fee(self):
        """Get currency_fee"""
        return self._currency_fee

    @currency_fee.setter
    def currency_fee(self, val):
        """Set currency_fee
        Keyword argument:
        val -- New currency_fee value"""
        self._currency_fee = val
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

    @property
    def chargedback_at(self):
        """Get chargedback_at"""
        return self._chargedback_at

    @chargedback_at.setter
    def chargedback_at(self, val):
        """Set chargedback_at
        Keyword argument:
        val -- New chargedback_at value"""
        self._chargedback_at = val
        return self

    @property
    def refunded_at(self):
        """Get refunded_at"""
        return self._refunded_at

    @refunded_at.setter
    def refunded_at(self, val):
        """Set refunded_at
        Keyword argument:
        val -- New refunded_at value"""
        self._refunded_at = val
        return self

    @property
    def authorized_at(self):
        """Get authorized_at"""
        return self._authorized_at

    @authorized_at.setter
    def authorized_at(self, val):
        """Set authorized_at
        Keyword argument:
        val -- New authorized_at value"""
        self._authorized_at = val
        return self

    @property
    def captured_at(self):
        """Get captured_at"""
        return self._captured_at

    @captured_at.setter
    def captured_at(self, val):
        """Set captured_at
        Keyword argument:
        val -- New captured_at value"""
        self._captured_at = val
        return self

    @property
    def voided_at(self):
        """Get voided_at"""
        return self._voided_at

    @voided_at.setter
    def voided_at(self, val):
        """Set voided_at
        Keyword argument:
        val -- New voided_at value"""
        self._voided_at = val
        return self

    @property
    def three_d_s(self):
        """Get three_d_s"""
        return self._three_d_s

    @three_d_s.setter
    def three_d_s(self, val):
        """Set three_d_s
        Keyword argument:
        val -- New three_d_s value"""
        if val is None:
            self._three_d_s = val
            return self

        if isinstance(val, dict):
            obj = processout.ThreeDS(self._client)
            obj.fill_with_data(val)
            self._three_d_s = obj
        else:
            self._three_d_s = val
        return self

    @property
    def cvc_check(self):
        """Get cvc_check"""
        return self._cvc_check

    @cvc_check.setter
    def cvc_check(self, val):
        """Set cvc_check
        Keyword argument:
        val -- New cvc_check value"""
        self._cvc_check = val
        return self

    @property
    def avs_check(self):
        """Get avs_check"""
        return self._avs_check

    @avs_check.setter
    def avs_check(self, val):
        """Set avs_check
        Keyword argument:
        val -- New avs_check value"""
        self._avs_check = val
        return self

    @property
    def initial_scheme_transaction_id(self):
        """Get initial_scheme_transaction_id"""
        return self._initial_scheme_transaction_id

    @initial_scheme_transaction_id.setter
    def initial_scheme_transaction_id(self, val):
        """Set initial_scheme_transaction_id
        Keyword argument:
        val -- New initial_scheme_transaction_id value"""
        self._initial_scheme_transaction_id = val
        return self

    @property
    def scheme_id(self):
        """Get scheme_id"""
        return self._scheme_id

    @scheme_id.setter
    def scheme_id(self, val):
        """Set scheme_id
        Keyword argument:
        val -- New scheme_id value"""
        self._scheme_id = val
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
    def eci(self):
        """Get eci"""
        return self._eci

    @eci.setter
    def eci(self, val):
        """Set eci
        Keyword argument:
        val -- New eci value"""
        self._eci = val
        return self

    @property
    def native_apm(self):
        """Get native_apm"""
        return self._native_apm

    @native_apm.setter
    def native_apm(self, val):
        """Set native_apm
        Keyword argument:
        val -- New native_apm value"""
        if val is None:
            self._native_apm = val
            return self

        if isinstance(val, dict):
            obj = processout.NativeAPMResponse(self._client)
            obj.fill_with_data(val)
            self._native_apm = obj
        else:
            self._native_apm = val
        return self

    @property
    def external_details(self):
        """Get external_details"""
        return self._external_details

    @external_details.setter
    def external_details(self, val):
        """Set external_details
        Keyword argument:
        val -- New external_details value"""
        self._external_details = val
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
        if "invoice" in data.keys():
            self.invoice = data["invoice"]
        if "invoice_id" in data.keys():
            self.invoice_id = data["invoice_id"]
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
        if "card" in data.keys():
            self.card = data["card"]
        if "card_id" in data.keys():
            self.card_id = data["card_id"]
        if "gateway_configuration" in data.keys():
            self.gateway_configuration = data["gateway_configuration"]
        if "external_three_d_s_gateway_configuration" in data.keys():
            self.external_three_d_s_gateway_configuration = data[
                "external_three_d_s_gateway_configuration"]
        if "gateway_configuration_id" in data.keys():
            self.gateway_configuration_id = data["gateway_configuration_id"]
        if "operations" in data.keys():
            self.operations = data["operations"]
        if "refunds" in data.keys():
            self.refunds = data["refunds"]
        if "name" in data.keys():
            self.name = data["name"]
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "amount_local" in data.keys():
            self.amount_local = data["amount_local"]
        if "authorized_amount" in data.keys():
            self.authorized_amount = data["authorized_amount"]
        if "authorized_amount_local" in data.keys():
            self.authorized_amount_local = data["authorized_amount_local"]
        if "captured_amount" in data.keys():
            self.captured_amount = data["captured_amount"]
        if "captured_amount_local" in data.keys():
            self.captured_amount_local = data["captured_amount_local"]
        if "refunded_amount" in data.keys():
            self.refunded_amount = data["refunded_amount"]
        if "refunded_amount_local" in data.keys():
            self.refunded_amount_local = data["refunded_amount_local"]
        if "available_amount" in data.keys():
            self.available_amount = data["available_amount"]
        if "available_amount_local" in data.keys():
            self.available_amount_local = data["available_amount_local"]
        if "voided_amount" in data.keys():
            self.voided_amount = data["voided_amount"]
        if "voided_amount_local" in data.keys():
            self.voided_amount_local = data["voided_amount_local"]
        if "currency" in data.keys():
            self.currency = data["currency"]
        if "error_code" in data.keys():
            self.error_code = data["error_code"]
        if "error_message" in data.keys():
            self.error_message = data["error_message"]
        if "acquirer_name" in data.keys():
            self.acquirer_name = data["acquirer_name"]
        if "gateway_name" in data.keys():
            self.gateway_name = data["gateway_name"]
        if "three_d_s_status" in data.keys():
            self.three_d_s_status = data["three_d_s_status"]
        if "status" in data.keys():
            self.status = data["status"]
        if "authorized" in data.keys():
            self.authorized = data["authorized"]
        if "captured" in data.keys():
            self.captured = data["captured"]
        if "voided" in data.keys():
            self.voided = data["voided"]
        if "refunded" in data.keys():
            self.refunded = data["refunded"]
        if "chargedback" in data.keys():
            self.chargedback = data["chargedback"]
        if "received_fraud_notification" in data.keys():
            self.received_fraud_notification = data["received_fraud_notification"]
        if "received_retrieval_request" in data.keys():
            self.received_retrieval_request = data["received_retrieval_request"]
        if "processout_fee" in data.keys():
            self.processout_fee = data["processout_fee"]
        if "estimated_fee" in data.keys():
            self.estimated_fee = data["estimated_fee"]
        if "gateway_fee" in data.keys():
            self.gateway_fee = data["gateway_fee"]
        if "gateway_fee_local" in data.keys():
            self.gateway_fee_local = data["gateway_fee_local"]
        if "currency_fee" in data.keys():
            self.currency_fee = data["currency_fee"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        if "chargedback_at" in data.keys():
            self.chargedback_at = data["chargedback_at"]
        if "refunded_at" in data.keys():
            self.refunded_at = data["refunded_at"]
        if "authorized_at" in data.keys():
            self.authorized_at = data["authorized_at"]
        if "captured_at" in data.keys():
            self.captured_at = data["captured_at"]
        if "voided_at" in data.keys():
            self.voided_at = data["voided_at"]
        if "three_d_s" in data.keys():
            self.three_d_s = data["three_d_s"]
        if "cvc_check" in data.keys():
            self.cvc_check = data["cvc_check"]
        if "avs_check" in data.keys():
            self.avs_check = data["avs_check"]
        if "initial_scheme_transaction_id" in data.keys():
            self.initial_scheme_transaction_id = data["initial_scheme_transaction_id"]
        if "scheme_id" in data.keys():
            self.scheme_id = data["scheme_id"]
        if "payment_type" in data.keys():
            self.payment_type = data["payment_type"]
        if "eci" in data.keys():
            self.eci = data["eci"]
        if "native_apm" in data.keys():
            self.native_apm = data["native_apm"]
        if "external_details" in data.keys():
            self.external_details = data["external_details"]

        return self

    def to_json(self):
        return {
            "id": self.id,
            "project": self.project,
            "project_id": self.project_id,
            "invoice": self.invoice,
            "invoice_id": self.invoice_id,
            "customer": self.customer,
            "customer_id": self.customer_id,
            "subscription": self.subscription,
            "subscription_id": self.subscription_id,
            "token": self.token,
            "token_id": self.token_id,
            "card": self.card,
            "card_id": self.card_id,
            "gateway_configuration": self.gateway_configuration,
            "external_three_d_s_gateway_configuration": self.external_three_d_s_gateway_configuration,
            "gateway_configuration_id": self.gateway_configuration_id,
            "operations": self.operations,
            "refunds": self.refunds,
            "name": self.name,
            "amount": self.amount,
            "amount_local": self.amount_local,
            "authorized_amount": self.authorized_amount,
            "authorized_amount_local": self.authorized_amount_local,
            "captured_amount": self.captured_amount,
            "captured_amount_local": self.captured_amount_local,
            "refunded_amount": self.refunded_amount,
            "refunded_amount_local": self.refunded_amount_local,
            "available_amount": self.available_amount,
            "available_amount_local": self.available_amount_local,
            "voided_amount": self.voided_amount,
            "voided_amount_local": self.voided_amount_local,
            "currency": self.currency,
            "error_code": self.error_code,
            "error_message": self.error_message,
            "acquirer_name": self.acquirer_name,
            "gateway_name": self.gateway_name,
            "three_d_s_status": self.three_d_s_status,
            "status": self.status,
            "authorized": self.authorized,
            "captured": self.captured,
            "voided": self.voided,
            "refunded": self.refunded,
            "chargedback": self.chargedback,
            "received_fraud_notification": self.received_fraud_notification,
            "received_retrieval_request": self.received_retrieval_request,
            "processout_fee": self.processout_fee,
            "estimated_fee": self.estimated_fee,
            "gateway_fee": self.gateway_fee,
            "gateway_fee_local": self.gateway_fee_local,
            "currency_fee": self.currency_fee,
            "metadata": self.metadata,
            "sandbox": self.sandbox,
            "created_at": self.created_at,
            "chargedback_at": self.chargedback_at,
            "refunded_at": self.refunded_at,
            "authorized_at": self.authorized_at,
            "captured_at": self.captured_at,
            "voided_at": self.voided_at,
            "three_d_s": self.three_d_s,
            "cvc_check": self.cvc_check,
            "avs_check": self.avs_check,
            "initial_scheme_transaction_id": self.initial_scheme_transaction_id,
            "scheme_id": self.scheme_id,
            "payment_type": self.payment_type,
            "eci": self.eci,
            "native_apm": self.native_apm,
            "external_details": self.external_details,
        }

    def fetch_refunds(self, options={}):
        """Get the transaction's refunds.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/transactions/" + quote_plus(self.id) + "/refunds"
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        a = []
        body = response.body
        for v in body['refunds']:
            tmp = processout.Refund(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)

        return return_values[0]

    def find_refund(self, refund_id, options={}):
        """Find a transaction's refund by its ID.
        Keyword argument:
        refund_id -- ID of the refund
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/transactions/" + \
            quote_plus(self.id) + "/refunds/" + quote_plus(refund_id) + ""
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        body = response.body
        body = body["refund"]
        refund = processout.Refund(self._client)
        return_values.append(refund.fill_with_data(body))

        return return_values[0]

    def all(self, options={}):
        """Get all the transactions.
        Keyword argument:

        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/transactions"
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        a = []
        body = response.body
        for v in body['transactions']:
            tmp = processout.Transaction(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)

        return return_values[0]

    def find(self, transaction_id, options={}):
        """Find a transaction by its ID.
        Keyword argument:
        transaction_id -- ID of the transaction
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path = "/transactions/" + quote_plus(transaction_id) + ""
        data = {

        }

        response = Response(request.get(path, data, options))
        return_values = []

        body = response.body
        body = body["transaction"]

        obj = processout.Transaction(self._client)
        return_values.append(obj.fill_with_data(body))

        return return_values[0]

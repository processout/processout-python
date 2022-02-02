try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class TransactionOperation(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._id = None
        self._transaction = None
        self._transaction_id = None
        self._token = None
        self._token_id = None
        self._card = None
        self._card_id = None
        self._gateway_configuration = None
        self._gateway_configuration_id = None
        self._amount = None
        self._currency = None
        self._is_attempt = None
        self._has_failed = None
        self._is_accountable = None
        self._type = None
        self._gateway_operation_id = None
        self._arn = None
        self._error_code = None
        self._gateway_data = None
        self._payment_data_three_d_s_request = None
        self._payment_data_three_d_s_authentication = None
        self._payment_data_network_authentication = None
        self._metadata = None
        self._gateway_fee = None
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
    def is_attempt(self):
        """Get is_attempt"""
        return self._is_attempt

    @is_attempt.setter
    def is_attempt(self, val):
        """Set is_attempt
        Keyword argument:
        val -- New is_attempt value"""
        self._is_attempt = val
        return self

    @property
    def has_failed(self):
        """Get has_failed"""
        return self._has_failed

    @has_failed.setter
    def has_failed(self, val):
        """Set has_failed
        Keyword argument:
        val -- New has_failed value"""
        self._has_failed = val
        return self

    @property
    def is_accountable(self):
        """Get is_accountable"""
        return self._is_accountable

    @is_accountable.setter
    def is_accountable(self, val):
        """Set is_accountable
        Keyword argument:
        val -- New is_accountable value"""
        self._is_accountable = val
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
    def gateway_operation_id(self):
        """Get gateway_operation_id"""
        return self._gateway_operation_id

    @gateway_operation_id.setter
    def gateway_operation_id(self, val):
        """Set gateway_operation_id
        Keyword argument:
        val -- New gateway_operation_id value"""
        self._gateway_operation_id = val
        return self

    @property
    def arn(self):
        """Get arn"""
        return self._arn

    @arn.setter
    def arn(self, val):
        """Set arn
        Keyword argument:
        val -- New arn value"""
        self._arn = val
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
    def payment_data_three_d_s_request(self):
        """Get payment_data_three_d_s_request"""
        return self._payment_data_three_d_s_request

    @payment_data_three_d_s_request.setter
    def payment_data_three_d_s_request(self, val):
        """Set payment_data_three_d_s_request
        Keyword argument:
        val -- New payment_data_three_d_s_request value"""
        if val is None:
            self._payment_data_three_d_s_request = val
            return self

        if isinstance(val, dict):
            obj = processout.PaymentDataThreeDSRequest(self._client)
            obj.fill_with_data(val)
            self._payment_data_three_d_s_request = obj
        else:
            self._payment_data_three_d_s_request = val
        return self

    @property
    def payment_data_three_d_s_authentication(self):
        """Get payment_data_three_d_s_authentication"""
        return self._payment_data_three_d_s_authentication

    @payment_data_three_d_s_authentication.setter
    def payment_data_three_d_s_authentication(self, val):
        """Set payment_data_three_d_s_authentication
        Keyword argument:
        val -- New payment_data_three_d_s_authentication value"""
        if val is None:
            self._payment_data_three_d_s_authentication = val
            return self

        if isinstance(val, dict):
            obj = processout.PaymentDataThreeDSAuthentication(self._client)
            obj.fill_with_data(val)
            self._payment_data_three_d_s_authentication = obj
        else:
            self._payment_data_three_d_s_authentication = val
        return self

    @property
    def payment_data_network_authentication(self):
        """Get payment_data_network_authentication"""
        return self._payment_data_network_authentication

    @payment_data_network_authentication.setter
    def payment_data_network_authentication(self, val):
        """Set payment_data_network_authentication
        Keyword argument:
        val -- New payment_data_network_authentication value"""
        if val is None:
            self._payment_data_network_authentication = val
            return self

        if isinstance(val, dict):
            obj = processout.PaymentDataNetworkAuthentication(self._client)
            obj.fill_with_data(val)
            self._payment_data_network_authentication = obj
        else:
            self._payment_data_network_authentication = val
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
        if "transaction" in data.keys():
            self.transaction = data["transaction"]
        if "transaction_id" in data.keys():
            self.transaction_id = data["transaction_id"]
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
        if "gateway_configuration_id" in data.keys():
            self.gateway_configuration_id = data["gateway_configuration_id"]
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "currency" in data.keys():
            self.currency = data["currency"]
        if "is_attempt" in data.keys():
            self.is_attempt = data["is_attempt"]
        if "has_failed" in data.keys():
            self.has_failed = data["has_failed"]
        if "is_accountable" in data.keys():
            self.is_accountable = data["is_accountable"]
        if "type" in data.keys():
            self.type = data["type"]
        if "gateway_operation_id" in data.keys():
            self.gateway_operation_id = data["gateway_operation_id"]
        if "arn" in data.keys():
            self.arn = data["arn"]
        if "error_code" in data.keys():
            self.error_code = data["error_code"]
        if "gateway_data" in data.keys():
            self.gateway_data = data["gateway_data"]
        if "payment_data_three_d_s_request" in data.keys():
            self.payment_data_three_d_s_request = data["payment_data_three_d_s_request"]
        if "payment_data_three_d_s_authentication" in data.keys():
            self.payment_data_three_d_s_authentication = data["payment_data_three_d_s_authentication"]
        if "payment_data_network_authentication" in data.keys():
            self.payment_data_network_authentication = data["payment_data_network_authentication"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "gateway_fee" in data.keys():
            self.gateway_fee = data["gateway_fee"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]

        return self

    def to_json(self):
        return {
            "id": self.id,
            "transaction": self.transaction,
            "transaction_id": self.transaction_id,
            "token": self.token,
            "token_id": self.token_id,
            "card": self.card,
            "card_id": self.card_id,
            "gateway_configuration": self.gateway_configuration,
            "gateway_configuration_id": self.gateway_configuration_id,
            "amount": self.amount,
            "currency": self.currency,
            "is_attempt": self.is_attempt,
            "has_failed": self.has_failed,
            "is_accountable": self.is_accountable,
            "type": self.type,
            "gateway_operation_id": self.gateway_operation_id,
            "arn": self.arn,
            "error_code": self.error_code,
            "gateway_data": self.gateway_data,
            "payment_data_three_d_s_request": self.payment_data_three_d_s_request,
            "payment_data_three_d_s_authentication": self.payment_data_three_d_s_authentication,
            "payment_data_network_authentication": self.payment_data_network_authentication,
            "metadata": self.metadata,
            "gateway_fee": self.gateway_fee,
            "created_at": self.created_at,
        }

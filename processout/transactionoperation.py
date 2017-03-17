try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class TransactionOperation(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = None
        self._transaction = None
        self._transaction_id = None
        self._token = None
        self._token_id = None
        self._card = None
        self._card_id = None
        self._amount = None
        self._is_attempt = None
        self._has_failed = None
        self._is_accountable = None
        self._type = None
        self._error_code = None
        self._metadata = None
        self._gateway_fee = None
        self._created_at = None
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
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "is_attempt" in data.keys():
            self.is_attempt = data["is_attempt"]
        if "has_failed" in data.keys():
            self.has_failed = data["has_failed"]
        if "is_accountable" in data.keys():
            self.is_accountable = data["is_accountable"]
        if "type" in data.keys():
            self.type = data["type"]
        if "error_code" in data.keys():
            self.error_code = data["error_code"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "gateway_fee" in data.keys():
            self.gateway_fee = data["gateway_fee"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        
        return self

    

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Refund:
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = ""
        self._transaction = None
        self._reason = ""
        self._information = ""
        self._amount = ""
        self._metadata = {}
        self._sandbox = False
        self._createdAt = ""
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
    def transaction(self):
        """Get transaction"""
        return self._transaction

    @transaction.setter
    def transaction(self, val):
        """Set transaction
        Keyword argument:
        val -- New transaction value"""
        if isinstance(val, Transaction):
            self._transaction = val
        else:
            obj = processout.Transaction(self._client)
            obj.fillWithData(val)
            self._transaction = obj
        return self
    
    @property
    def reason(self):
        """Get reason"""
        return self._reason

    @reason.setter
    def reason(self, val):
        """Set reason
        Keyword argument:
        val -- New reason value"""
        self._reason = val
        return self
    
    @property
    def information(self):
        """Get information"""
        return self._information

    @information.setter
    def information(self, val):
        """Set information
        Keyword argument:
        val -- New information value"""
        self._information = val
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
    

    def fillWithData(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "id" in data.keys():
            self.id = data["id"]
        if "transaction" in data.keys():
            self.transaction = data["transaction"]
        if "reason" in data.keys():
            self.reason = data["reason"]
        if "information" in data.keys():
            self.information = data["information"]
        if "amount" in data.keys():
            self.amount = data["amount"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.createdAt = data["created_at"]
        
        return self

    def find(self, transactionId, refundId, options = None):
        """Find a transaction's refund by its ID.
        Keyword argument:
        transactionId -- ID of the transaction on which the refund was applied
        refundId -- ID of the refund
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/transactions/" + quote_plus(transactionId) + "/refunds/" + quote_plus(refundId) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        returnValues = []
        
        body = response.body
        body = body["refund"]
                
                
        obj = processout.Refund(self._client)
        returnValues.append(obj.fillWithData(body))
                

        
        return returnValues[0];

    def apply(self, transactionId, options = None):
        """Apply a refund to a transaction.
        Keyword argument:
        transactionId -- ID of the transaction
        options -- Options for the request"""
        request = Request(self._client)
        path    = "/transactions/" + quote_plus(transactionId) + "/refunds"
        data    = {
            'amount': self.amount, 
            'metadata': self.metadata, 
            'reason': self.reason, 
            'information': self.information
        }

        response = Response(request.post(path, data, options))
        returnValues = []
        
        returnValues.append(response.success)

        
        return returnValues[0];

    

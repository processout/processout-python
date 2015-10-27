from .processout import ProcessOut

import hmac
import hashlib
import base64

class Callback:
    def __init__(self, processOut = None):
        """Create a new callback instance
        Keyword argument:
        processOut -- ProcessOut instance
        """
        if processOut == None:
            processOut = ProcessOut.getDefault()

        self._processOut = processOut

    def validate(self, transactionId, hmacInput):
        """Perform basic checks on the callback to make sure it's legit
        Keyword argument:
        transactionId -- id of the transaction returned by the callback
        hmacInput -- hmac returned by the callback
        """
        newhmac = hmac.new(key=bytes(self._processOut.projectKey.encode('utf-8')),
            msg=transactionId.encode('utf-8'),
            digestmod=hashlib.sha256).digest()

        return hmac.compare_digest(newhmac, base64.b64decode(hmacInput))

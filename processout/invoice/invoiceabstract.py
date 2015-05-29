# processout.invoice.invoiceabstract

from abc import ABCMeta, abstractmethod

class InvoiceAbstract:
    __metaclass__ = ABCMeta

    def __init__(self, processOut):
        """Create a new instance of InvoiceAbstract

        Keyword argument:
        processOut -- ProcessOut instance
        """
        self._processOut = processOut

        self._returnUrl    = None
        self._cancelUrl    = None
        self._notifyUrl    = None
        self._custom       = None
        self._lastResponse = None

    @property
    def host(self):
        """Get the ProcessOut's host"""
        return self._host

    @property
    def projectId(self):
        """Get the ProcessOut's project id"""
        return self._projectId

    @property
    def projectSecret(self):
        """Get the ProcessOut's project secret"""
        return self._projectSecret

    @property
    def returnUrl(self):
        """Get the return URL"""
        return self._returnUrl

    @returnUrl.setter
    def returnUrl(self, value):
        """Set the return URL

        Keyword argument:
        value -- new return URL
        """
        self._returnUrl = value

    @property
    def cancelUrl(self):
        """Get te cancel URL"""
        return self._cancelUrl

    @cancelUrl.setter
    def cancelUrl(self, value):
        """Set the cancel URL

        Keyword argument:
        value -- new cancel URL
        """
        self._cancelUrl = value

    @property
    def notifyUrl(self):
        """Get the notify URL (used for callbacks)"""
        return self._notifyUrl

    @notifyUrl.setter
    def notifyUrl(self, value):
        """Set the notify URL (used for callbacks)

        Keyword argument:
        value -- new notify URL
        """
        self._notifyUrl = value

    @property
    def custom(self):
        """Get the custom field value"""
        return self._custom

    @custom.setter
    def custom(self, value):
        """Set the custom field value

        Keyword argument:
        value -- new custom field value
        """
        self._custom = value

    @property
    def sandbox(self):
        """Get the sandbox field value"""
        return self._sandbox

    @sandbox.setter
    def sandbox(self, value):
        """Set the sandbox field value

        Keyword argument:
        value -- new sandbox field value
        """
        self._sandbox = value

    def enableSandbox(self):
        """Enable the sandbox mode"""
        self.sandbox = True

    def disableSandbox(self):
        """Disable the sandbox mode"""
        self.sandbox = False

    def _generateData(self):
        """Generate the data used during the ProcessOut's request"""
        return {
            'return_url':     self.returnUrl,
            'cancel_url':     self.cancelUrl,
            'notify_url':     self.notifyUrl,
            'custom':         self.custom
        }

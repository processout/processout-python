from .exceptions.apiexception import ApiException

class ProcessOut:
    HOST = 'https://api.processout.com/'

    default = None

    def __init__(self):
        """Create a new instance of ProcessOut"""
        
        self._projectId = ""
        
        self._projectSecret = ""
        

    @property
    def projectId(self):
        """Get projectId"""
        return self._projectId

    @projectId.setter
    def projectId(self, val):
        """Set projectId
        Keyword argument:
        val -- New projectId value"""
        self._projectId = val

    @property
    def projectSecret(self):
        """Get projectSecret"""
        return self._projectSecret

    @projectSecret.setter
    def projectSecret(self, val):
        """Set projectSecret
        Keyword argument:
        val -- New projectSecret value"""
        self._projectSecret = val

    @staticmethod
    def getDefault():
        """Get the default ProcessOut instance"""
        if default == None:
            raise ApiAuthenticationException(
                'You need to define a default ProcessOut object (ProcessOut.setDefault()).')

    @staticmethod
    def setDefault(processout):
        """Set the default ProcessOut instance
        Keyword argument:
        processout -- ProcessOut's instance"""
        ProcessOut.default = processout

# processout.processout

from .exceptions.apiexception import ApiException

class ProcessOut:
    HOST = 'https://api.processout.com/v1'

    default = None

    def __init__(self, projectId, projectKey):
        """Create a new instance of ProcessOut

        Keyword argument:
        projectId -- id of the ProcessOut's project
        projectKey -- secret key associated to the project
        """
        self._projectId  = projectId
        self._projectKey = projectKey

    @property
    def projectId(self):
        """Get the project id"""
        return self._projectId

    @property
    def projectKey(self):
        """Get the project secret key"""
        return self._projectKey

    @staticmethod
    def getDefault():
    	"""Get the default ProcessOut instance"""
    	if default == None:
    		raise ApiAuthenticationException(
    			'You need to define a default ProcessOut object (ProcessOut::setDefault()).')

    @staticmethod
    def setDefault(processout):
    	"""Set the default ProcessOut instance

    	Keyword argument:
    	processout -- ProcessOut's instance"""
    	ProcessOut.default = processout
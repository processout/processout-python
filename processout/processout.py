# processout.processout

class ProcessOut:
    HOST = 'https://api.processout.com/v1'

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
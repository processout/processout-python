import requests
import urllib.parse

from ..processout import ProcessOut

class RequestProcessoutPrivate:
    def __init__(self, instance):
        """Create a new Request instance

        Keyword argument:
        instance -- ProcessOut instance
        """
        self._instance = instance

    def _authenticate(self):
        """Return the correct needed authentication"""
        

        
        username = self._instance.projectId
        

        
        password = self._instance.projectSecret
        

        return (username, password)

        

    def get(self, path, data):
        """Perform a GET request

        Keyword argument:
        path -- Path of the request
        data -- Data to be passed along with the request
        """
        return requests.get(ProcessOut.HOST + path + '?' +
                urllib.parse.urlencode(data),
            auth   = self._authenticate(),
            verify = True)

    def post(self, path, data):
        """Perform a POST request

        Keyword argument:
        path -- Path of the request
        data -- Data to be passed along with the request
        """
        return requests.post(ProcessOut.HOST + path,
            auth   = self._authenticate(),
            json   = data,
            verify = True)

    def put(self, path, data):
        """Perform a PUT request

        Keyword argument:
        path -- Path of the request
        data -- Data to be passed along with the request
        """
        return requests.put(ProcessOut.HOST + path,
            auth   = self._authenticate(),
            json   = data,
            verify = True)

    def delete(self, path, data):
        """Perform a DELETE request

        Keyword argument:
        path -- Path of the request
        data -- Data to be passed along with the request
        """
        return requests.delete(ProcessOut.HOST + path,
            auth   = self._authenticate(),
            json   = data,
            verify = True)

from urllib.parse import quote_plus

from .processout import ProcessOut
from .networking.response import Response

from .networking.requestprocessoutprivate import RequestProcessoutPrivate

from .networking.requestprocessoutpublic import RequestProcessoutPublic


class PaymentGateway:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

        
        self._settings = {}
        

    
    @property
    def settings(self):
        """Get settings"""
        return self._settings

    @settings.setter
    def settings(self, val):
        """Set settings
        Keyword argument:
        val -- New settings value"""
        self._settings = val
    

    def fillWithData(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        
        if "settings" in data.keys():
            self.settings = data["settings"]
        

    
    
    def save(self, name):
        """Update or set the payment gateway settings.
        Keyword argument:
		name -- Name of the payment gateway (ex: paypal)"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/payment-gateway/" + quote_plus(name) + ""
        data    = {
			'settings': self.settings
        }

        
        response = Response(request.put(path, data))
        

        
        return response.success
        
    
    
    @staticmethod
    
    def delete(self, name):
        """Remove the payment gateway and its settings from the current project.
        Keyword argument:
		name -- Name of the payment gateway (ex: paypal)"""
        request = RequestProcessoutPrivate(self._instance)
        path    = "/payment-gateway/" + quote_plus(name) + ""
        data    = {

        }

        
        response = Response(request.delete(path, data))
        

        
        return response.success
        
    

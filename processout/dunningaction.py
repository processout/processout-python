try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class DunningAction(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._action = None
        self._delay_in_days = None
        if prefill != None:
            self.fill_with_data(prefill)

    
    @property
    def action(self):
        """Get action"""
        return self._action

    @action.setter
    def action(self, val):
        """Set action
        Keyword argument:
        val -- New action value"""
        self._action = val
        return self
    
    @property
    def delay_in_days(self):
        """Get delay_in_days"""
        return self._delay_in_days

    @delay_in_days.setter
    def delay_in_days(self, val):
        """Set delay_in_days
        Keyword argument:
        val -- New delay_in_days value"""
        self._delay_in_days = val
        return self
    

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "action" in data.keys():
            self.action = data["action"]
        if "delay_in_days" in data.keys():
            self.delay_in_days = data["delay_in_days"]
        
        return self

    

from .processout import ProcessOut

class Webhook:

    def __init__(self, instance = None):
        if instance == None:
            instance = ProcessOut.getDefault()

        self._instance = instance

    def validate(self, reqBody, hmacInput):
        #TODO
        return True

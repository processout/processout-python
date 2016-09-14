import json
import base64

class GatewayRequest:
    def __init__(self, gatewayConfigurationID, method, url, headers, data):
        """Create a new GatewayRequest instance from the current request
        Keyword argument:
        gatewayConfigurationID -- gateway configuration ID
        method -- Request method
        url -- Request URL
        headers -- Request headers (map format)
        body -- Request body (raw string)"""
        self._gatewayConfigurationID = gatewayConfigurationID
        self._method                 = method
        self._url                    = url
        self._headers                = headers
        self._data                   = data

    def toString(self):
        return "gway_req_" + base64.b64encode(bytes(json.dumps({
            "gateway_configuration_id": self._gatewayConfigurationID,
            "method":                   self._method,
            "url":                      self._url,
            "headers":                  self._headers,
            "body":                     self._body
        }), "utf-8"))

    def __str___(self):
        return self.toString()

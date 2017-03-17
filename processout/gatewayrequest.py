import json
import base64

class GatewayRequest:
    def __init__(self, gateway_configuration_id, method, url, headers, body):
        """Create a new GatewayRequest instance from the current request
        Keyword argument:
        gatewayConfigurationID -- gateway configuration ID
        method -- Request method
        url -- Request URL
        headers -- Request headers (map format)
        body -- Request body (raw string)"""
        self._gateway_configuration_id = gateway_configuration_id
        self._method = method
        self._url = url
        self._headers = headers
        self._body = body

    def to_string(self):
        return "gway_req_" + base64.b64encode(json.dumps({
            "gateway_configuration_id": self._gateway_configuration_id,
            "method": self._method,
            "url": self._url,
            "headers": self._headers,
            "body": self._body
        }).encode("utf-8")).decode("utf-8")

    def __str___(self):
        return self.to_string()

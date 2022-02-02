try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class PaymentDataThreeDSRequest(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._acs_url = None
        self._pareq = None
        self._md = None
        self._term_url = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def acs_url(self):
        """Get acs_url"""
        return self._acs_url

    @acs_url.setter
    def acs_url(self, val):
        """Set acs_url
        Keyword argument:
        val -- New acs_url value"""
        self._acs_url = val
        return self

    @property
    def pareq(self):
        """Get pareq"""
        return self._pareq

    @pareq.setter
    def pareq(self, val):
        """Set pareq
        Keyword argument:
        val -- New pareq value"""
        self._pareq = val
        return self

    @property
    def md(self):
        """Get md"""
        return self._md

    @md.setter
    def md(self, val):
        """Set md
        Keyword argument:
        val -- New md value"""
        self._md = val
        return self

    @property
    def term_url(self):
        """Get term_url"""
        return self._term_url

    @term_url.setter
    def term_url(self, val):
        """Set term_url
        Keyword argument:
        val -- New term_url value"""
        self._term_url = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "acs_url" in data.keys():
            self.acs_url = data["acs_url"]
        if "pareq" in data.keys():
            self.pareq = data["pareq"]
        if "md" in data.keys():
            self.md = data["md"]
        if "term_url" in data.keys():
            self.term_url = data["term_url"]

        return self

    def to_json(self):
        return {
            "acs_url": self.acs_url,
            "pareq": self.pareq,
            "md": self.md,
            "term_url": self.term_url,
        }

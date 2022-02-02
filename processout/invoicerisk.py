try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class InvoiceRisk(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._score = None
        self._is_legit = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def score(self):
        """Get score"""
        return self._score

    @score.setter
    def score(self, val):
        """Set score
        Keyword argument:
        val -- New score value"""
        self._score = val
        return self

    @property
    def is_legit(self):
        """Get is_legit"""
        return self._is_legit

    @is_legit.setter
    def is_legit(self, val):
        """Set is_legit
        Keyword argument:
        val -- New is_legit value"""
        self._is_legit = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "score" in data.keys():
            self.score = data["score"]
        if "is_legit" in data.keys():
            self.is_legit = data["is_legit"]

        return self

    def to_json(self):
        return {
            "score": self.score,
            "is_legit": self.is_legit,
        }

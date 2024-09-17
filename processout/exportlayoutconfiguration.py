try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout
import json

from processout.networking.request import Request
from processout.networking.response import Response

# The content of this file was automatically generated


class ExportLayoutConfiguration(object):
    def __init__(self, client, prefill=None):
        self._client = client

        self._columns = None
        self._time = None
        self._amount = None
        if prefill is not None:
            self.fill_with_data(prefill)

    @property
    def columns(self):
        """Get columns"""
        return self._columns

    @columns.setter
    def columns(self, val):
        """Set columns
        Keyword argument:
        val -- New columns value"""
        if val is None:
            self._columns = []
            return self

        if len(val) > 0 and isinstance(
                val[0], processout.ExportLayoutConfigurationColumn):
            self._columns = val
        else:
            l = []
            for v in val:
                obj = processout.ExportLayoutConfigurationColumn(self._client)
                obj.fill_with_data(v)
                l.append(obj)
            self._columns = l
        return self

    @property
    def time(self):
        """Get time"""
        return self._time

    @time.setter
    def time(self, val):
        """Set time
        Keyword argument:
        val -- New time value"""
        if val is None:
            self._time = val
            return self

        if isinstance(val, dict):
            obj = processout.ExportLayoutConfigurationTime(self._client)
            obj.fill_with_data(val)
            self._time = obj
        else:
            self._time = val
        return self

    @property
    def amount(self):
        """Get amount"""
        return self._amount

    @amount.setter
    def amount(self, val):
        """Set amount
        Keyword argument:
        val -- New amount value"""
        if val is None:
            self._amount = val
            return self

        if isinstance(val, dict):
            obj = processout.ExportLayoutConfigurationAmount(self._client)
            obj.fill_with_data(val)
            self._amount = obj
        else:
            self._amount = val
        return self

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "columns" in data.keys():
            self.columns = data["columns"]
        if "time" in data.keys():
            self.time = data["time"]
        if "amount" in data.keys():
            self.amount = data["amount"]

        return self

    def to_json(self):
        return {
            "columns": self.columns,
            "time": self.time,
            "amount": self.amount,
        }

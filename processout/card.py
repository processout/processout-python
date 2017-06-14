try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class Card(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = None
        self._project = None
        self._project_id = None
        self._token = None
        self._scheme = None
        self._type = None
        self._bank_name = None
        self._brand = None
        self._iin = None
        self._last_4_digits = None
        self._exp_month = None
        self._exp_year = None
        self._cvc_check = None
        self._avs_check = None
        self._name = None
        self._address1 = None
        self._address2 = None
        self._city = None
        self._state = None
        self._country_code = None
        self._zip = None
        self._metadata = None
        self._expires_soon = None
        self._sandbox = None
        self._created_at = None
        if prefill != None:
            self.fill_with_data(prefill)

    
    @property
    def id(self):
        """Get id"""
        return self._id

    @id.setter
    def id(self, val):
        """Set id
        Keyword argument:
        val -- New id value"""
        self._id = val
        return self
    
    @property
    def project(self):
        """Get project"""
        return self._project

    @project.setter
    def project(self, val):
        """Set project
        Keyword argument:
        val -- New project value"""
        if val is None:
            self._project = val
            return self

        if isinstance(val, dict):
            obj = processout.Project(self._client)
            obj.fill_with_data(val)
            self._project = obj
        else:
            self._project = val
        return self
    
    @property
    def project_id(self):
        """Get project_id"""
        return self._project_id

    @project_id.setter
    def project_id(self, val):
        """Set project_id
        Keyword argument:
        val -- New project_id value"""
        self._project_id = val
        return self
    
    @property
    def token(self):
        """Get token"""
        return self._token

    @token.setter
    def token(self, val):
        """Set token
        Keyword argument:
        val -- New token value"""
        if val is None:
            self._token = val
            return self

        if isinstance(val, dict):
            obj = processout.Token(self._client)
            obj.fill_with_data(val)
            self._token = obj
        else:
            self._token = val
        return self
    
    @property
    def scheme(self):
        """Get scheme"""
        return self._scheme

    @scheme.setter
    def scheme(self, val):
        """Set scheme
        Keyword argument:
        val -- New scheme value"""
        self._scheme = val
        return self
    
    @property
    def type(self):
        """Get type"""
        return self._type

    @type.setter
    def type(self, val):
        """Set type
        Keyword argument:
        val -- New type value"""
        self._type = val
        return self
    
    @property
    def bank_name(self):
        """Get bank_name"""
        return self._bank_name

    @bank_name.setter
    def bank_name(self, val):
        """Set bank_name
        Keyword argument:
        val -- New bank_name value"""
        self._bank_name = val
        return self
    
    @property
    def brand(self):
        """Get brand"""
        return self._brand

    @brand.setter
    def brand(self, val):
        """Set brand
        Keyword argument:
        val -- New brand value"""
        self._brand = val
        return self
    
    @property
    def iin(self):
        """Get iin"""
        return self._iin

    @iin.setter
    def iin(self, val):
        """Set iin
        Keyword argument:
        val -- New iin value"""
        self._iin = val
        return self
    
    @property
    def last_4_digits(self):
        """Get last_4_digits"""
        return self._last_4_digits

    @last_4_digits.setter
    def last_4_digits(self, val):
        """Set last_4_digits
        Keyword argument:
        val -- New last_4_digits value"""
        self._last_4_digits = val
        return self
    
    @property
    def exp_month(self):
        """Get exp_month"""
        return self._exp_month

    @exp_month.setter
    def exp_month(self, val):
        """Set exp_month
        Keyword argument:
        val -- New exp_month value"""
        self._exp_month = val
        return self
    
    @property
    def exp_year(self):
        """Get exp_year"""
        return self._exp_year

    @exp_year.setter
    def exp_year(self, val):
        """Set exp_year
        Keyword argument:
        val -- New exp_year value"""
        self._exp_year = val
        return self
    
    @property
    def cvc_check(self):
        """Get cvc_check"""
        return self._cvc_check

    @cvc_check.setter
    def cvc_check(self, val):
        """Set cvc_check
        Keyword argument:
        val -- New cvc_check value"""
        self._cvc_check = val
        return self
    
    @property
    def avs_check(self):
        """Get avs_check"""
        return self._avs_check

    @avs_check.setter
    def avs_check(self, val):
        """Set avs_check
        Keyword argument:
        val -- New avs_check value"""
        self._avs_check = val
        return self
    
    @property
    def name(self):
        """Get name"""
        return self._name

    @name.setter
    def name(self, val):
        """Set name
        Keyword argument:
        val -- New name value"""
        self._name = val
        return self
    
    @property
    def address1(self):
        """Get address1"""
        return self._address1

    @address1.setter
    def address1(self, val):
        """Set address1
        Keyword argument:
        val -- New address1 value"""
        self._address1 = val
        return self
    
    @property
    def address2(self):
        """Get address2"""
        return self._address2

    @address2.setter
    def address2(self, val):
        """Set address2
        Keyword argument:
        val -- New address2 value"""
        self._address2 = val
        return self
    
    @property
    def city(self):
        """Get city"""
        return self._city

    @city.setter
    def city(self, val):
        """Set city
        Keyword argument:
        val -- New city value"""
        self._city = val
        return self
    
    @property
    def state(self):
        """Get state"""
        return self._state

    @state.setter
    def state(self, val):
        """Set state
        Keyword argument:
        val -- New state value"""
        self._state = val
        return self
    
    @property
    def country_code(self):
        """Get country_code"""
        return self._country_code

    @country_code.setter
    def country_code(self, val):
        """Set country_code
        Keyword argument:
        val -- New country_code value"""
        self._country_code = val
        return self
    
    @property
    def zip(self):
        """Get zip"""
        return self._zip

    @zip.setter
    def zip(self, val):
        """Set zip
        Keyword argument:
        val -- New zip value"""
        self._zip = val
        return self
    
    @property
    def metadata(self):
        """Get metadata"""
        return self._metadata

    @metadata.setter
    def metadata(self, val):
        """Set metadata
        Keyword argument:
        val -- New metadata value"""
        self._metadata = val
        return self
    
    @property
    def expires_soon(self):
        """Get expires_soon"""
        return self._expires_soon

    @expires_soon.setter
    def expires_soon(self, val):
        """Set expires_soon
        Keyword argument:
        val -- New expires_soon value"""
        self._expires_soon = val
        return self
    
    @property
    def sandbox(self):
        """Get sandbox"""
        return self._sandbox

    @sandbox.setter
    def sandbox(self, val):
        """Set sandbox
        Keyword argument:
        val -- New sandbox value"""
        self._sandbox = val
        return self
    
    @property
    def created_at(self):
        """Get created_at"""
        return self._created_at

    @created_at.setter
    def created_at(self, val):
        """Set created_at
        Keyword argument:
        val -- New created_at value"""
        self._created_at = val
        return self
    

    def fill_with_data(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "id" in data.keys():
            self.id = data["id"]
        if "project" in data.keys():
            self.project = data["project"]
        if "project_id" in data.keys():
            self.project_id = data["project_id"]
        if "token" in data.keys():
            self.token = data["token"]
        if "scheme" in data.keys():
            self.scheme = data["scheme"]
        if "type" in data.keys():
            self.type = data["type"]
        if "bank_name" in data.keys():
            self.bank_name = data["bank_name"]
        if "brand" in data.keys():
            self.brand = data["brand"]
        if "iin" in data.keys():
            self.iin = data["iin"]
        if "last_4_digits" in data.keys():
            self.last_4_digits = data["last_4_digits"]
        if "exp_month" in data.keys():
            self.exp_month = data["exp_month"]
        if "exp_year" in data.keys():
            self.exp_year = data["exp_year"]
        if "cvc_check" in data.keys():
            self.cvc_check = data["cvc_check"]
        if "avs_check" in data.keys():
            self.avs_check = data["avs_check"]
        if "name" in data.keys():
            self.name = data["name"]
        if "address1" in data.keys():
            self.address1 = data["address1"]
        if "address2" in data.keys():
            self.address2 = data["address2"]
        if "city" in data.keys():
            self.city = data["city"]
        if "state" in data.keys():
            self.state = data["state"]
        if "country_code" in data.keys():
            self.country_code = data["country_code"]
        if "zip" in data.keys():
            self.zip = data["zip"]
        if "metadata" in data.keys():
            self.metadata = data["metadata"]
        if "expires_soon" in data.keys():
            self.expires_soon = data["expires_soon"]
        if "sandbox" in data.keys():
            self.sandbox = data["sandbox"]
        if "created_at" in data.keys():
            self.created_at = data["created_at"]
        
        return self

    def all(self, options = {}):
        """Get all the cards.
        Keyword argument:
        
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/cards"
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        a    = []
        body = response.body
        for v in body['cards']:
            tmp = processout.Card(self._client)
            tmp.fill_with_data(v)
            a.append(tmp)

        return_values.append(a)
            

        
        return return_values[0]

    def find(self, card_id, options = {}):
        """Find a card by its ID.
        Keyword argument:
        card_id -- ID of the card
        options -- Options for the request"""
        self.fill_with_data(options)

        request = Request(self._client)
        path    = "/cards/" + quote_plus(card_id) + ""
        data    = {

        }

        response = Response(request.get(path, data, options))
        return_values = []
        
        body = response.body
        body = body["card"]
                
                
        obj = processout.Card(self._client)
        return_values.append(obj.fill_with_data(body))
                

        
        return return_values[0]

    

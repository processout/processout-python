ProcessOut Python
=================

[![Code Climate](https://codeclimate.com/github/ProcessOut/processout-python/badges/gpa.svg)](https://codeclimate.com/github/ProcessOut/processout-python)
[![PyPI version](https://badge.fury.io/py/processout.svg)](http://badge.fury.io/py/processout)

This package provides bindings to the ProcessOut API. Manage your callbacks,
create new invoices, redirect your users to a newly generated checkout
page and more.

ProcessOut allows you to manage a lot of payment gateways such as PayPal,
Crypto currencies, Payza or Dwolla, with no effort.
Learn more on the [ProcessOut website](https://www.processout.com).

Dependencies
------------

* Python 2.4 or higher
* Requests

Installation
------------

This ProcessOut package is published on pypi:
``` sh
pip install processout
```

If you don't want to use pip to install this package, you may simply do a
git clone:

``` sh
git clone https://github.com/ProcessOut/ProcessOut-python-server .
```

-------------------------

Prerequisites
-------------

### Import the modules

``` python
from processout.processout import ProcessOut

from processout.invoice.invoice         import Invoice
from processout.invoice.tailoredinvoice import TailoredInvoice

from processout.callback.callback import Callback
```

### Instantiate a new ProcessOut instance

``` python
projectId     = '21184268-76fa-4b33-99a0-63fb15f9041a'
projectSecret = 'key-24a2061d0fd2853b75728073d5406de437d525b2ff941fe34ca061cb2180d0f8'

processout = ProcessOut(projectId, projectSecret)
```

Usage
-----

### Create a new invoice from scratch

``` python
invoice = Invoice(processout)
invoice.itemName = 'Amazing product'
# Set more attributes here
invoice.save()
```


### Create a new invoice from a tailored invoice

``` python
tailored = TailoredInvoice(processout)
invoice = tailored.fromId('1ca570ac-0cb4-4c54-8ff2-f7c82f4fb12b').invoice()
# You can set more attributes here too, invoice is an instance of Invoice
invoice.save()
```

##### Shared invoice attributes

The following attributes are shared between Invoice and TailoredInvoice instances

- *attribute*     - *example*
- itemName        - **Amazing product**
- itemPrice       - **4.20**
- itemQuantity    - *2*
- currency        - **USD**
- taxes           - *4.20*
- shipping        - *4.20*
- recurringDays   - *7*
- requestEmail    - *False*
- requestShipping - *False*
- metas           - *{"key 1": "value 1", "key 2": "value 2"}*
- returnUrl       - *URL to which the customer will be redirected upon purchase*
- cancelUrl       - *URL to which the customer will be redirected upon cancellation*
- notifyUrl       - *URL being called by ProcessOut to send callbacks upon transaction updates*
- custom          - *A custom field containing anything you want, sent back within all callbacks*
- sandbox         - *Decide weither or not to activate the sandbox mode*

#### Attribute getters and setters

Every attribute has its own getter and setter, as follows:

``` python
@property
def custom(self):
    return self._custom

@custom.setter
def custom(self, value):
    self._custom = value
```

### Getting the link to an invoice

``` python
print(invoice.getLink())

# You may also get the id of the invoice (which can be used with the modal)
print(invoice.getId())
```

### Receiving callbacks / Webhooks

Callbacks can be used to automate transaction management once a payment has
been placed by one of your customers. One example could be adding credit to
an account once the user has paid their subscription.

However, it doesn't stop there. ProcessOut also supports chargeback handling,
and much more. Please refer to the
[API documentation](http://docs.processout.apiary.io/#) to learn what data is
sent through callbacks.

Once a callback has been sent to your server, you need to check its authenticity,
as follows:

``` python
callback = Callback(processout)
if not callback.validate(data['transaction_id'], data['hmac_signature']):
	print('Bad callback')
    return

# Continue normally here, the callback is verified
# One common thing to do would be to check the price, currency, etc...
```

### Error and exception handling

The library will throw different kind of exception when errors happen.
This can be extremely useful to see what part of the application crashed,
and why.
Currently, the library supports 3 kind of exceptions, each verbose-friendly.

``` python
from processout.exceptions.apiauthenticationexception import ApiAuthenticationException
from processout.exceptions.apiexception               import ApiException
from processout.exceptions.notfoundexception          import NotFoundException

raise APIAuthenticationException();
raise ApiException();
raise NotFoundException();
```

-------------------------

Full API documentation
----------------------

### Apiary

The ProcessOut's full API documentation can be found on
[Apiary](http://docs.processout.apiary.io). It contains all the needed
information, including callback data, and much more.

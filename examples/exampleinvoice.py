# exampleinvoice.py

import sys

# Let's load our processout modules
from ..processout.processout              import ProcessOut
from ..processout.invoice.invoice         import Invoice
from ..processout.invoice.tailoredinvoice import TailoredInvoice

from ..processout.exceptions.apiauthenticationexception import ApiAuthenticationException
from ..processout.exceptions.apiexception               import ApiException
from ..processout.exceptions.notfoundexception          import NotFoundException


def main(argv):
    # Create a new ProcessOut instance
    processout = ProcessOut(
        '008a8331-db1b-4cf4-b905-e21fd4aa78e9',
        'key-bb6edef7b8b486b8fabb3097c21f171ad85022b057e9422f960509016a6afcdc')

    # Create a new invoice, with custom name, price and currency
    invoice           = Invoice(processout)
    invoice.itemName  = 'Amazing product'
    invoice.itemPrice = 4.20
    invoice.currency  = 'USD'

    try:
        invoice.save()

    except ApiAuthenticationException as e:
        print('Looks like your project id or secret is wrong. ' + str(e))
        return

    except ApiException as e:
        print('Looks like theres been an API error. ' + str(e))
        return

    # Get its invoice url
    print(invoice.url)

    # Or get its id
    print(invoice.id)


    ############################


    # Create a new invoice thanks to a tailored invoice id
    tailoredInvoice = TailoredInvoice(processout)

    try:
        tailoredInvoice.fromId('a4fb38dd-b36c-42c9-8b92-c515de122a16')
    except NotFoundException as e:
        print('Looks like the tailored invoice could not be found.')
        return

    # Get a new invoice generated from this tailored invoice
    invoice = tailoredInvoice.invoice().save()

    # Get its invoice url
    print(invoice.url)

    # Or its id
    print(invoice.id)

if __name__ == '__main__':
    main(sys.argv[1:])

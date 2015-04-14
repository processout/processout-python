# exampleinvoice.py

import sys

# Let's load our processout module
from processout.processout import ProcessOut


def main(argv):
    # Create a new ProcessOut instance
    processout = ProcessOut(
        '4d65cebe-c2f0-4803-9eab-3f9e190aaeb5',
        'key-9db060c19281bb39656df61c63ddecff674d80b1178533db0ceffb29b87ce40a')

    # Create a new invoice, with custom name, price and currency
    invoice = processout.newInvoice(
        '1 copy of a wonderful product at $4.99 USD',  # Title
        4.99,                                          # Price
        1,                                             # Quantity
        'USD')                                         # Currency

    # Get its invoice link
    print(invoice.getLink())


    # Create a new invoice thanks to a tailored invoice id
    productInvoice = processout.newTailoredInvoice(
        '2fac6a3a-b5da-4067-a694-67373de3283d')

    # Get its invoice link
    print(productInvoice.getLink())

if __name__ == '__main__':
    main(sys.argv[1:])

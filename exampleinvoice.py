# exampleinvoice.py

import sys

# Let's load our processout modules
from processout.processout              import ProcessOut
from processout.invoice.invoice         import Invoice
from processout.invoice.tailoredinvoice import TailoredInvoice


def main(argv):
    # Create a new ProcessOut instance
    processout = ProcessOut(
        '8722fce8-f8c0-44be-997e-d4954cf32fc0',
        'key-3022bbac0a88514dff79c0d95f5b8486ba0884bb665834ea9ad79610ac31ab43')

    # Create a new invoice, with custom name, price and currency
    invoice = Invoice(
    	processout,                                    # ProcessOut instance
        '1 copy of a wonderful product at $4.99 USD',  # Title
        4.99,                                          # Price
        1,                                             # Quantity
        'USD')                                         # Currency

    # Get its invoice link
    print(invoice.getLink())

    # Or get its id
    print(invoice.getId())


    # Create a new invoice thanks to a tailored invoice id
    tailoredInvoice = TailoredInvoice(
    	processout,                             # ProcessOut instance
        '1ca570ac-0cb4-4c54-8ff2-f7c82f4fb12b') # Tailored invoice id

    # Get its invoice link
    print(tailoredInvoice.getLink())

    # Or its id
    print(tailoredInvoice.getId())

if __name__ == '__main__':
    main(sys.argv[1:])

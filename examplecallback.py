# examplecallback.py

import sys

# Let's load our processout modules
from processout.processout        import ProcessOut
from processout.callback.callback import Callback


def main(argv):
    # Create a new ProcessOut instance
    processout = ProcessOut(
        '008a8331-db1b-4cf4-b905-e21fd4aa78e9',
    	'key-bb6edef7b8b486b8fabb3097c21f171ad85022b057e9422f960509016a6afcdc')

    # Create a dummy request data
    data = {
        'transaction_id': '2fac6a3a-b5da-4067-a694-67373de3283d',
        'hmac_signature': 'qnR8UCqJggD55PohusaBNviGoOJ67HC6Btry4qXLVZc=',
        'action':         'invoice.completed'
        # ...
        # For a full list of the data returned by a callback, please visit
        # http://docs.processout.apiary.io/#reference/callbacks-/-web-hooks
    }

    # Create a new callback instance
    callback = Callback(processout)

    # Checking if the callback seems to be legit
    if not callback.validate(data['transaction_id'], data['hmac_signature']):
        print('Bad callback')
        return


    # Callback is legit! Perform actions on it
    # /!\ Be sure to still check the amount, currencies... /!\

    if data['action'] == 'invoice.completed':
        # Transaction completed / successful
        pass

    elif data['action'] == 'invoice.pending':
        # Transaction still needs some time to be processed
        pass

    elif data['action'] == 'invoice.failed':
        # Damn, something went wrong
        pass

    elif data['action'] == 'invoice.disputed':
        # Your customer opened a dispute on the transaction
        pass

    elif data['action'] == 'invoice.solved':
        # You won/solved a dispute
        pass

    elif data['action'] == 'invoice.reversed':
        # You most likely lost a dispute and the transaction got reversed
        pass

    elif data['action'] == 'invoice.refunded':
        # You refunded the transaction
        pass

    else:
        # Shouldn't be here..
        print('Unknown callback action')


if __name__ == '__main__':
    main(sys.argv[1:])

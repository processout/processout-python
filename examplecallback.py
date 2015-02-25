# examplecallback.py

import sys

# Let's load our processout module
from processout.processout import ProcessOut


def main(argv):
	# Create a new ProcessOut instance
	processout = ProcessOut(
		'4d65cebe-c2f0-4803-9eab-3f9e190aaeb5',
		'key-9db060c19281bb39656df61c63ddecff674d80b1178533db0ceffb29b87ce40a')

	# Create a dummy request data
	data = {
		'transaction_id': '2fac6a3a-b5da-4067-a694-67373de3283d',
		'hmac_signature': 'qnR8UCqJggD55PohusaBNviGoOJ67HC6Btry4qXLVZc=',
		'action':         'invoice.completed'
		# ...
		# For a full list of the data returned by a callback, please visit
		# http://docs.processout.apiary.io/#reference/callbacks-/-web-hooks
	}

	# Checking if the callback seems to be legit
	if not processout.checkCallbackData(
			data['transaction_id'], data['hmac_signature']):
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

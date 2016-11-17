import sys
import processout

def main(argv):
	client = processout.ProcessOut("proj_gAO1Uu0ysZJvDuUpOGPkUBeE3pGalk3x", 
		"key_fBjPvkgT8gyKc1SUpy0PfjL7UgsRmUug")

	# Create and fetch an invoice
	invoice = client.newInvoice({
		"name": "Test invoice",
		"amount": "9.99",
		"currency": "USD"
	}).create()
	assert invoice.id != "", "The invoice ID should not be empty"

	fetched = client.newInvoice().find(invoice.id)
	assert fetched.id != "", "The fetched invoice ID should not be empty"
	assert invoice.id == fetched.id, "The invoices ID should be equal"

	# Fetch the customers
	customers = client.newCustomer().all()

	# Create a subscription for a customer
	customer = client.newCustomer().create()
	assert customer.id != "", "The created customer ID should not be empty"

	subscription = client.newSubscription({
		"name": "Test subscription",
		"amount": "9.99",
		"currency": "USD",
		"interval": "1d"
	}).create(customer.id)
	assert subscription.id != "", "The created subscription ID should not be empty"

if __name__ == '__main__':
	main(sys.argv[1:])
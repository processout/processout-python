import processout
from processout.errors.notfounderror import NotFoundError
from processout.gatewayrequest import GatewayRequest

def main():
    client = processout.ProcessOut("test-proj_gAO1Uu0ysZJvDuUpOGPkUBeE3pGalk3x",
                                   "key_jqSPvwq3AG5MlYAgqxlwwgOcAC3Zy7d8")

    # Create and fetch an invoice
    invoice = client.new_invoice({
        "name": "Test invoice",
        "amount": "9.99",
        "currency": "USD"
    }).create()
    assert invoice.id != "", "The invoice ID should not be empty"

    fetched = client.new_invoice().find(invoice.id)
    assert fetched.id != "", "The fetched invoice ID should not be empty"
    assert invoice.id == fetched.id, "The invoices ID should be equal"

    # Capture an invoice
    gr = GatewayRequest("sandbox", "POST", "https://processout.com", {
        "Content-Type": "application/json"
    }, "{\"token\": \"test-valid\"}")
    transaction = invoice.capture(gr.to_string())
    assert transaction.status == "completed", "The transaction status was not completed"

    # Expand the gateway configuration used on the transaction
    transaction = transaction.find(transaction.id, {
        "expand": ["gateway_configuration"]
    })
    assert transaction.gateway_configuration.id != "", "The transaction gateway configuration ID is empty"

    # Fetch the customers
    client.new_customer().all()

    # Create a subscription for a customer
    customer = client.new_customer().create()
    assert customer.id != "", "The created customer ID should not be empty"

    subscription = client.new_subscription({
        "customer_id": customer.id,
        "name": "Test subscription",
        "amount": "9.99",
        "currency": "USD",
        "interval": "1d"
    }).create()
    assert subscription.id != "", "The created subscription ID should not be empty"

    # Expand a customers' project and fetch gateways
    customer = client.new_customer().create({"expand": ["project"]})
    assert customer.project != None, "The customer project should be expanded"

    # Check error code
    try:
        pass
    except NotFoundError as err:
        assert err.code == "resource.customer.not-found", "The error code was invalid"

if __name__ == "__main__":
    main()

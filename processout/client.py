import processout


class ProcessOut:
    def __init__(self, project_id, project_secret):
        """Create a new instance of ProcessOut"""

        self._host = 'https://api.processout.com'

        self._project_id = project_id
        self._project_secret = project_secret

    @property
    def host(self):
        """Get the library host URL"""
        return self._host

    @host.setter
    def host(self, val):
        """Set the library host URL
        Keyword argument:
        val -- New host URL"""
        self._host = val

    @property
    def project_id(self):
        """Get the project ID"""
        return self._project_id

    @property
    def project_secret(self):
        """Get the project secret"""
        return self._project_secret

    def new_activity(self, prefill=None):
        """Create a new Activity instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Activity(self, prefill)

    def new_addon(self, prefill=None):
        """Create a new Addon instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Addon(self, prefill)

    def new_api_version(self, prefill=None):
        """Create a new APIVersion instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.APIVersion(self, prefill)

    def new_apple_pay_alternative_merchant_certificates(self, prefill=None):
        """Create a new ApplePayAlternativeMerchantCertificates instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.ApplePayAlternativeMerchantCertificates(
            self, prefill)

    def new_alternative_merchant_certificate(self, prefill=None):
        """Create a new AlternativeMerchantCertificate instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.AlternativeMerchantCertificate(self, prefill)

    def new_balances(self, prefill=None):
        """Create a new Balances instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Balances(self, prefill)

    def new_balance(self, prefill=None):
        """Create a new Balance instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Balance(self, prefill)

    def new_card(self, prefill=None):
        """Create a new Card instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Card(self, prefill)

    def new_card_information(self, prefill=None):
        """Create a new CardInformation instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.CardInformation(self, prefill)

    def new_phone(self, prefill=None):
        """Create a new Phone instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Phone(self, prefill)

    def new_coupon(self, prefill=None):
        """Create a new Coupon instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Coupon(self, prefill)

    def new_customer(self, prefill=None):
        """Create a new Customer instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Customer(self, prefill)

    def new_customer_phone(self, prefill=None):
        """Create a new CustomerPhone instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.CustomerPhone(self, prefill)

    def new_token(self, prefill=None):
        """Create a new Token instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Token(self, prefill)

    def new_discount(self, prefill=None):
        """Create a new Discount instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Discount(self, prefill)

    def new_event(self, prefill=None):
        """Create a new Event instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Event(self, prefill)

    def new_gateway(self, prefill=None):
        """Create a new Gateway instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Gateway(self, prefill)

    def new_gateway_configuration(self, prefill=None):
        """Create a new GatewayConfiguration instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.GatewayConfiguration(self, prefill)

    def new_invoice(self, prefill=None):
        """Create a new Invoice instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Invoice(self, prefill)

    def new_native_apm_request(self, prefill=None):
        """Create a new NativeAPMRequest instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.NativeAPMRequest(self, prefill)

    def new_native_apm_parameter_value(self, prefill=None):
        """Create a new NativeAPMParameterValue instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.NativeAPMParameterValue(self, prefill)

    def new_invoice_tax(self, prefill=None):
        """Create a new InvoiceTax instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.InvoiceTax(self, prefill)

    def new_invoice_external_fraud_tools(self, prefill=None):
        """Create a new InvoiceExternalFraudTools instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.InvoiceExternalFraudTools(self, prefill)

    def new_invoice_risk(self, prefill=None):
        """Create a new InvoiceRisk instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.InvoiceRisk(self, prefill)

    def new_invoice_device(self, prefill=None):
        """Create a new InvoiceDevice instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.InvoiceDevice(self, prefill)

    def new_invoice_shipping(self, prefill=None):
        """Create a new InvoiceShipping instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.InvoiceShipping(self, prefill)

    def new_invoice_shipping_phone(self, prefill=None):
        """Create a new InvoiceShippingPhone instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.InvoiceShippingPhone(self, prefill)

    def new_invoice_billing(self, prefill=None):
        """Create a new InvoiceBilling instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.InvoiceBilling(self, prefill)

    def new_unsupported_feature_bypass(self, prefill=None):
        """Create a new UnsupportedFeatureBypass instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.UnsupportedFeatureBypass(self, prefill)

    def new_invoice_detail(self, prefill=None):
        """Create a new InvoiceDetail instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.InvoiceDetail(self, prefill)

    def new_customer_action(self, prefill=None):
        """Create a new CustomerAction instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.CustomerAction(self, prefill)

    def new_dunning_action(self, prefill=None):
        """Create a new DunningAction instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.DunningAction(self, prefill)

    def new_payout(self, prefill=None):
        """Create a new Payout instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Payout(self, prefill)

    def new_payout_item(self, prefill=None):
        """Create a new PayoutItem instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.PayoutItem(self, prefill)

    def new_payout_item_amount_breakdowns(self, prefill=None):
        """Create a new PayoutItemAmountBreakdowns instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.PayoutItemAmountBreakdowns(self, prefill)

    def new_plan(self, prefill=None):
        """Create a new Plan instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Plan(self, prefill)

    def new_product(self, prefill=None):
        """Create a new Product instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Product(self, prefill)

    def new_project(self, prefill=None):
        """Create a new Project instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Project(self, prefill)

    def new_project_sftp_settings(self, prefill=None):
        """Create a new ProjectSFTPSettings instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.ProjectSFTPSettings(self, prefill)

    def new_refund(self, prefill=None):
        """Create a new Refund instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Refund(self, prefill)

    def new_subscription(self, prefill=None):
        """Create a new Subscription instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Subscription(self, prefill)

    def new_transaction(self, prefill=None):
        """Create a new Transaction instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Transaction(self, prefill)

    def new_native_apm_response(self, prefill=None):
        """Create a new NativeAPMResponse instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.NativeAPMResponse(self, prefill)

    def new_native_apm_parameter_definition(self, prefill=None):
        """Create a new NativeAPMParameterDefinition instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.NativeAPMParameterDefinition(self, prefill)

    def new_native_apm_parameter_value_definition(self, prefill=None):
        """Create a new NativeAPMParameterValueDefinition instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.NativeAPMParameterValueDefinition(self, prefill)

    def new_three_ds(self, prefill=None):
        """Create a new ThreeDS instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.ThreeDS(self, prefill)

    def new_payment_data_three_ds_request(self, prefill=None):
        """Create a new PaymentDataThreeDSRequest instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.PaymentDataThreeDSRequest(self, prefill)

    def new_payment_data_network_authentication(self, prefill=None):
        """Create a new PaymentDataNetworkAuthentication instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.PaymentDataNetworkAuthentication(self, prefill)

    def new_payment_data_three_ds_authentication(self, prefill=None):
        """Create a new PaymentDataThreeDSAuthentication instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.PaymentDataThreeDSAuthentication(self, prefill)

    def new_transaction_operation(self, prefill=None):
        """Create a new TransactionOperation instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.TransactionOperation(self, prefill)

    def new_webhook(self, prefill=None):
        """Create a new Webhook instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Webhook(self, prefill)

    def new_webhook_endpoint(self, prefill=None):
        """Create a new WebhookEndpoint instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.WebhookEndpoint(self, prefill)

    def new_card_create_request(self, prefill=None):
        """Create a new CardCreateRequest instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.CardCreateRequest(self, prefill)

    def new_device(self, prefill=None):
        """Create a new Device instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Device(self, prefill)

    def new_card_contact(self, prefill=None):
        """Create a new CardContact instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.CardContact(self, prefill)

    def new_card_shipping(self, prefill=None):
        """Create a new CardShipping instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.CardShipping(self, prefill)

    def new_card_update_request(self, prefill=None):
        """Create a new CardUpdateRequest instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.CardUpdateRequest(self, prefill)

    def new_error_codes(self, prefill=None):
        """Create a new ErrorCodes instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.ErrorCodes(self, prefill)

    def new_category_error_codes(self, prefill=None):
        """Create a new CategoryErrorCodes instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.CategoryErrorCodes(self, prefill)

    def new_native_apm_transaction_details_gateway(self, prefill=None):
        """Create a new NativeAPMTransactionDetailsGateway instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.NativeAPMTransactionDetailsGateway(self, prefill)

    def new_native_apm_transaction_details_invoice(self, prefill=None):
        """Create a new NativeAPMTransactionDetailsInvoice instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.NativeAPMTransactionDetailsInvoice(self, prefill)

    def new_native_apm_transaction_details(self, prefill=None):
        """Create a new NativeAPMTransactionDetails instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.NativeAPMTransactionDetails(self, prefill)

    def new_invoices_process_native_payment_response(self, prefill=None):
        """Create a new InvoicesProcessNativePaymentResponse instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.InvoicesProcessNativePaymentResponse(self, prefill)

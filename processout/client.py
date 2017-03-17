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

    def new_activity(self, prefill = None):
        """Create a new Activity instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Activity(self, prefill)

    def new_addon(self, prefill = None):
        """Create a new Addon instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Addon(self, prefill)

    def new_api_request(self, prefill = None):
        """Create a new APIRequest instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.APIRequest(self, prefill)

    def new_api_version(self, prefill = None):
        """Create a new APIVersion instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.APIVersion(self, prefill)

    def new_authorization_request(self, prefill = None):
        """Create a new AuthorizationRequest instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.AuthorizationRequest(self, prefill)

    def new_card(self, prefill = None):
        """Create a new Card instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Card(self, prefill)

    def new_card_information(self, prefill = None):
        """Create a new CardInformation instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.CardInformation(self, prefill)

    def new_coupon(self, prefill = None):
        """Create a new Coupon instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Coupon(self, prefill)

    def new_customer(self, prefill = None):
        """Create a new Customer instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Customer(self, prefill)

    def new_token(self, prefill = None):
        """Create a new Token instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Token(self, prefill)

    def new_discount(self, prefill = None):
        """Create a new Discount instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Discount(self, prefill)

    def new_event(self, prefill = None):
        """Create a new Event instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Event(self, prefill)

    def new_gateway(self, prefill = None):
        """Create a new Gateway instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Gateway(self, prefill)

    def new_gateway_configuration(self, prefill = None):
        """Create a new GatewayConfiguration instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.GatewayConfiguration(self, prefill)

    def new_invoice(self, prefill = None):
        """Create a new Invoice instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Invoice(self, prefill)

    def new_invoice_detail(self, prefill = None):
        """Create a new InvoiceDetail instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.InvoiceDetail(self, prefill)

    def new_customer_action(self, prefill = None):
        """Create a new CustomerAction instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.CustomerAction(self, prefill)

    def new_dunning_action(self, prefill = None):
        """Create a new DunningAction instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.DunningAction(self, prefill)

    def new_plan(self, prefill = None):
        """Create a new Plan instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Plan(self, prefill)

    def new_product(self, prefill = None):
        """Create a new Product instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Product(self, prefill)

    def new_project(self, prefill = None):
        """Create a new Project instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Project(self, prefill)

    def new_refund(self, prefill = None):
        """Create a new Refund instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Refund(self, prefill)

    def new_subscription(self, prefill = None):
        """Create a new Subscription instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Subscription(self, prefill)

    def new_transaction(self, prefill = None):
        """Create a new Transaction instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Transaction(self, prefill)

    def new_transaction_operation(self, prefill = None):
        """Create a new TransactionOperation instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.TransactionOperation(self, prefill)

    def new_webhook(self, prefill = None):
        """Create a new Webhook instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Webhook(self, prefill)

    def new_webhook_endpoint(self, prefill = None):
        """Create a new WebhookEndpoint instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.WebhookEndpoint(self, prefill)

    

import processout

class ProcessOut:
    def __init__(self, projectID, projectSecret):
        """Create a new instance of ProcessOut"""

        self._host = 'https://api.processout.com'
        
        self._projectID = projectID
        self._projectSecret = projectSecret

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
    def projectID(self):
        """Get the project ID"""
        return self._projectID

    @property
    def projectSecret(self):
        """Get the project secret"""
        return self._projectSecret

    def newActivity(self, prefill = None):
        """Create a new Activity instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Activity(self, prefill)

    def newAuthorizationRequest(self, prefill = None):
        """Create a new AuthorizationRequest instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.AuthorizationRequest(self, prefill)

    def newCard(self, prefill = None):
        """Create a new Card instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Card(self, prefill)

    def newCoupon(self, prefill = None):
        """Create a new Coupon instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Coupon(self, prefill)

    def newCustomer(self, prefill = None):
        """Create a new Customer instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Customer(self, prefill)

    def newToken(self, prefill = None):
        """Create a new Token instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Token(self, prefill)

    def newDiscount(self, prefill = None):
        """Create a new Discount instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Discount(self, prefill)

    def newEvent(self, prefill = None):
        """Create a new Event instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Event(self, prefill)

    def newGateway(self, prefill = None):
        """Create a new Gateway instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Gateway(self, prefill)

    def newGatewayConfiguration(self, prefill = None):
        """Create a new GatewayConfiguration instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.GatewayConfiguration(self, prefill)

    def newInvoice(self, prefill = None):
        """Create a new Invoice instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Invoice(self, prefill)

    def newCustomerAction(self, prefill = None):
        """Create a new CustomerAction instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.CustomerAction(self, prefill)

    def newPlan(self, prefill = None):
        """Create a new Plan instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Plan(self, prefill)

    def newProduct(self, prefill = None):
        """Create a new Product instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Product(self, prefill)

    def newProject(self, prefill = None):
        """Create a new Project instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Project(self, prefill)

    def newRefund(self, prefill = None):
        """Create a new Refund instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Refund(self, prefill)

    def newSubscription(self, prefill = None):
        """Create a new Subscription instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Subscription(self, prefill)

    def newTransaction(self, prefill = None):
        """Create a new Transaction instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Transaction(self, prefill)

    def newWebhook(self, prefill = None):
        """Create a new Webhook instance
        Keyword argument:
        prefill -- Data used to prefill the object (optional)"""
        return processout.Webhook(self, prefill)

    

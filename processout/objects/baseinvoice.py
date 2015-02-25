
class BaseInvoice:
	def __init__(self, projectId, projectSecret):
		self._host          = 'https://api.processout.com/v1'
		self._projectId     = projectId
		self._projectSecret = projectSecret

		self._enableCoupon = False
		self._returnUrl    = None
		self._cancelUrl    = None
		self._notifyUrl    = None
		self._custom       = None

	@property
	def host(self):
		return self._host

	@property
	def projectId(self):
		return self._projectId

	@property
	def projectSecret(self):
		return self._projectSecret

	@property
	def enableCoupon(self):
		return self._enableCoupon

	@enableCoupon.setter
	def enableCoupon(self, value):
		self._enableCoupon = value

	@property
	def returnUrl(self):
		return self._returnUrl

	@returnUrl.setter
	def returnUrl(self, value):
		self._returnUrl = value

	@property
	def cancelUrl(self):
		return self._cancelUrl

	@cancelUrl.setter
	def cancelUrl(self, value):
		self._cancelUrl = value

	@property
	def notifyUrl(self):
		return self._notifyUrl

	@notifyUrl.setter
	def notifyUrl(self, value):
		self._notifyUrl = value

	@property
	def custom(self):
		return self._custom

	@custom.setter
	def custom(self, value):
		self._custom = value


	def _generateData(self):
		return {
			'enabled_coupon': self.enableCoupon,
			'return_url':     self.returnUrl,
			'cancel_url':     self.cancelUrl,
			'notify_url':     self.notifyUrl,
			'custom':         self.custom
		}

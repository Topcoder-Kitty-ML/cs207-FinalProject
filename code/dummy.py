
class dummy:
	'''
	A dummy class which covers all the cases
	which are difficult to deal with. This
	class only stores the value and derivative
	and abstracts everything away.
	'''
	def __init__(self, val, der):
		self.val = val
		self.der = der

	def __add__(self, other):
		try:
			new_val = self.val + other.val
			new_der = self.der + other.der
			return dummy(new_val, new_der)
		except:
			raise AttributeError()

	def __radd__(self, other):
		try:
			new_val = self.val + other.val
			new_der = self.der + other.der
			return dummy(new_val, new_der)
		except:
			raise AttributeError()

	def __sub__(self, other):
		try:
			new_val = self.val - other.val
			new_der = self.der - other.der
			return dummy(new_val, new_der)
		except:
			raise AttributeError()

	def __rsub__(self, other):
		try:
			new_val = other.val - self.val
			new_der = other.der - self.der
			return dummy(new_val, new_der)
		except:
			raise AttributeError()

	def __mul__(self, other):
		'''
		Apply the product rule
		'''
		try:
			new_val = self.val * other.val
			new_der = self.val * other.der + other.val * self.der
			return dummy(new_val, new_der)
		except:
			raise AttributeError()


	def __rmul__(self, other):
		'''
		E.g. case of sin multiply by dummy class
		'''
		try:
			new_val = self.val * other.val
			new_der = self.val * other.der + other.val * self.der
			return dummy(new_val, new_der)
		except:
			raise AttributeError()

	def __div__(self, other):
		pass

	def __rdiv__(self, other):
		pass

	def __pow__(self, other):
		pass

	def __rpow__(self, other):
		pass


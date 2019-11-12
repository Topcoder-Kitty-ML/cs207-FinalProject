#!/usr/bin/python

import math

class trigo():
	'''
	Toy forward automatic differentiation
	class.
	E.g.
	f(x) = alpha * sin(gamma * x) + beta
	'''
	def __init__(self, a, alpha=1, beta=0, gamma=1):

		self.a = a # value to evaluate at
		self.alpha = alpha # regard as a x variable with coefficient of x = 1
		self.beta = beta # regard as a x variable with no constant
		self.gamma = gamma # regard as the coefficient of the 

		self.val = self.calc_function_val()
		self.der = self.calc_function_derivative_val()


	def calc_function_val(self):
		'''
		Calculate the current value of this
		function at the 
		'''
		value = self.alpha * self.a + self.beta

		return value

	
	def calc_function_derivative_val(self):
		'''
		Calculate the derivative of this function
		at the a value of interest
		'''

		derivative_val = self.alpha

		return derivative_val


	def update_value_and_derivative(self):
		'''
		Run functions to update the function values
		and derivatives
		'''
		self.val = self.calc_function_val()
		self.der = self.calc_function_derivative_val()


	def __add__(self, other):
		'''
		Performs addition of two autodifftoyobjects,
		or autodifftoyobject with a float/int
		'''

		# Assume that both objects are AutoDiffToyObjects
		try:
			alpha = self.alpha + other.alpha
			beta = self.beta + other.beta
			new_toy = AutoDiffToy(self.a, alpha, beta)
			return(new_toy)

		# Perhaps the 'other' is not an AutoDiffToyObject.
		# So we'll just add the constant values
		except:
			try:
				beta = self.beta + other.real
				new_toy = AutoDiffToy(self.a, self.alpha, beta)
				return(new_toy)
			except:
				raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for multiplication.')


	def __radd__(self, other):
		'''
		Allows for commuative cases of addition, where a
		float or integer are added to the autodifftoy object.
		'''
		# Assume that both objects are AutoDiffToyObjects
		try:
			alpha = self.alpha + other.alpha
			beta = self.beta + other.beta
			new_toy = AutoDiffToy(self.a, alpha, beta)
			return(new_toy)
		# Perhaps the 'other' is not an AutoDiffToyObject.
		# So we'll just add the constant values
		except:
			try:
				beta = self.beta + other.real
				new_toy = AutoDiffToy(self.a, self.alpha, beta)
				return(new_toy)
			except:
				#pass
				raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for multiplication.')


	def __mul__(self, other):
		'''
		This allows for multiplication between a coefficient 
		value and a AutoDiffToy object
		'''
		# Multiply a number with a 'x' class
		try:
			alpha = self.alpha * other.real
			new_toy = AutoDiffToy(self.a, alpha, self.beta)
			return(new_toy)

		# Catch weird cases. E.g. when we're multiplying two 'x' classes
		except:
			raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for multiplication.')


	def __rmul__(self, other):
		'''
		We use rmul as it allows us to deal with commutative case
		in which we have to multiply a float value with a AutoDiffToy
		class, without having to overlaod __mul__ function in the
		float class. (__mul__ function is called from the first variable
		in a multiplication)
		'''
		try:
			alpha = self.alpha * other.real
			new_toy = AutoDiffToy(self.a, alpha, self.beta)
			return(new_toy)
		except:
			raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for multiplication.')


class sin(trigo):
	'''
	E.g.
	f(x) = alpha * sin(gamma * x) + beta
	'''

	def calc_function_val(self):
		'''
		Calculate the current value of this
		function at the 
		'''
		value = self.alpha * math.sin(self.gamma * self.a) + self.beta

		return value

	
	def calc_function_derivative_val(self):
		'''
		Calculate the derivative of this function
		at the a value of interest
		'''

		derivative_val = self.alpha * self.gamma * math.cos(self.gamma * self.a)

		return derivative_val


class cos(trigo):
	'''
	E.g.
	f(x) = alpha * cos(gamma * x) + beta
	'''

	def calc_function_val(self):
		'''
		Calculate the current value of this
		function at the 
		'''
		value = self.alpha * math.cos(self.gamma * self.a) + self.beta

		return value

	
	def calc_function_derivative_val(self):
		'''
		Calculate the derivative of this function
		at the a value of interest
		'''

		derivative_val = (-1) * self.alpha * self.gamma * math.sin(self.gamma * self.a)

		return derivative_val


class tan(trigo):
	'''
	E.g.
	f(x) = alpha * tax(gamma * x) + beta
	'''

	def calc_function_val(self):
		'''
		Calculate the current value of this
		function at the 
		'''
		value = self.alpha * math.cos(self.gamma * self.a) + self.beta

		return value

	
	def calc_function_derivative_val(self):
		'''
		Calculate the derivative of this function
		at the a value of interest
		'''

		derivative_val = self.alpha * self.gamma * (1 / math.cos(self.gamma * self.a) ** 2)

		return derivative_val


class exponential(trigo):
	'''
	E.g.
	f(x) = alpha * exp(gamma * x) + beta
	'''

	def calc_function_val(self):
		'''
		Calculate the current value of this
		function at the 
		'''
		value = self.alpha * math.exp(self.gamma * self.a) + self.beta

		return value

	
	def calc_function_derivative_val(self):
		'''
		Calculate the derivative of this function
		at the a value of interest
		'''

		derivative_val = self.alpha * self.gamma * math.exp(self.gamma * self.a)

		return derivative_val



a = 2.0 # Value to evaluate at

alpha = 2.0
beta = 3.0
gamma = 4.0

x = sin(a=a, gamma=gamma)
#f = alpha * x + beta
f = x + beta
print(f.val, f.der)


#f = alpha * x + beta
#f = x * alpha + beta

# f = beta + alpha * x 

# f = alpha * x + beta
# print(f.val, f.der)
# print("====================")


# print("Testing: f = alpha * x + beta")
# f_1 = alpha * x + beta
# print(f_1.val, f_1.der)
# print("====================")

# print("Testing: f = x * alpha + beta")
# f_2 = x * alpha + beta
# print(f_2.val, f_2.der)
# print("====================")

# print("Testing: f = beta + alpha * x")
# f_3 = beta + alpha * x
# print(f_3.val, f_3.der)
# print("====================")

# print("Testing: f = beta + x * alpha")
# f_4 = beta + x * alpha
# print(f_4.val, f_4.der)
# print("====================")




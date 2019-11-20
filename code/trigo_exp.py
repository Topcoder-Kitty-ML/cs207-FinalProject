#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from linear import AutoDiffToy as x_simple
from dummy import dummy


class trigo_exp():
	'''
	Toy forward automatic differentiation
	class.
	E.g.
	f(x) = alpha * trigo_func(x) + beta
	Note:
	x is a class object
	'''
	def __init__(self, x_object, alpha=1, beta=0):
		self.alpha = alpha # regard as a x variable with coefficient of the trigo operation (e.g. sine)
		self.beta = beta # regard as a x variable with no constant
		self.x_object = x_object # regard as a simple x_object class within the trigo operation (e.g. sine)

		self.val = self.calc_function_val()
		self.der = self.calc_function_derivative_val()


	def calc_function_val(self):
		'''
		Calculate the current value of this
		function at the 
		'''
		raise NotImplementedError

	
	def calc_function_derivative_val(self):
		'''
		Calculate the derivative of this function
		at the a value of interest
		'''
		raise NotImplementedError


	def update_value_and_derivative(self):
		'''
		Run functions to update the function values
		and derivatives
		'''
		self.val = self.calc_function_val()
		self.der = self.calc_function_derivative_val()


	def __add__(self, other):
		'''
		Performs addition of two trigo objects,
		or trigo object with a float/int
		'''
		return self.__perform_add__(self, other)


	@classmethod
	def __perform_add__(cls, self, other):
		# Assumes that other is a number, and self is
		# an object of interest.
		try:
			alpha = self.alpha
			beta = self.beta + other.real
			new_object = cls(self.x_object, alpha=alpha, beta=beta)

			return new_object
			
		except AttributeError:
			pass

		try:
			# Deals with case where both self and other
			# are weird unrecognized cases. We covert
			# them to dummy classes and extract their values
			# and derivatives only for subsequent use.
			self_dummy = dummy(self.val, self.der)
			other_dummy = dummy(other.val, other.der)

			return self_dummy + other_dummy
		except:
			raise AttributeError



		# # Assume that both objects are the same type
		# # Check if both objects are of the same type
		# if isinstance(self, type(other)):
		# 	alpha = self.alpha + other.alpha
		# 	beta = self.beta + other.beta
		# 	new_object = cls(self.x_object, alpha=alpha, beta=beta)
		# 	return(new_object)

		# # Perhaps the 'other' is not an AutoDiffToyObject.
		# else:
		# 	try:
		# 		return self.__radd__(other)
		# 	except:
		# 		raise AttributeError(f'{other.__class__.__name__} is invalid for addition.')


	def __radd__(self, other):
		'''
		Allows for commuative cases of addition, where a
		float or integer are added to the autodifftoy object.
		'''
		radd_result = self.__perform_radd__(self, other)
		return(radd_result)


	@classmethod
	def __perform_radd__(cls, self, other):
		# We assume that the 'other' is a simple number, and
		# we will add our current object to it

		# For case of x + y, assume that self is a class of interest,
		# other is a number
		try:
			alpha = self.alpha
			beta = self.beta + other.real
			new_toy = cls(self.x_object, alpha=alpha, beta=beta)

			return new_toy
		except AttributeError:
			pass
		# For case of x + y, assume that other is a class of interest,
		# self is a number
		try:
			alpha = other.alpha
			beta = other.beta + self.real
			new_toy = cls(other.x_object, alpha=alpha, beta=beta)

			return new_toy
		except AttributeError:
			pass


		try:
			# Deals with case where both self and other
			# are weird unrecognized cases. We covert
			# them to dummy classes and extract their values
			# and derivatives only for subsequent use.
			self_dummy = dummy(self.val, self.der)
			other_dummy = dummy(other.val, other.der)

			return self_dummy + other_dummy
		except:
			raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for multiplication.')


		# try:
		# 	alpha = self.alpha + other.alpha
		# 	beta = self.beta + other.beta
		# 	new_toy = cls(self.x_object, alpha=alpha, beta=beta)
		# 	return(new_toy)

		# # Perhaps the 'other' is not an AutoDiffToyObject.
		# # So we'll just add the constant values
		# except:
		# 	try:
		# 		if isinstance(self, cls):
		# 			alpha = self.alpha
		# 			beta = self.beta + other.real
		# 			new_toy = cls(self.x_object, alpha=alpha, beta=beta)
		# 		elif isinstance(other, cls):
		# 			alpha = other.alpha
		# 			beta = other.beta + self.real
		# 			new_toy = cls(other.x_object, alpha=alpha, beta=beta)
		# 		else:
		# 			raise AttributeError(f'{other.__class__.__name__} is invalid for addition.')
		# 		return(new_toy)
		# 	except:
		# 		raise AttributeError(f'{other.__class__.__name__} is invalid for addition.')


	def __sub__(self, other):
		'''
		Performs subtraction of two trigo objects,
		or trigo object with a float/int
		'''
		return self.__perform_sub__(self, other)


	@classmethod
	def __perform_sub__(cls, self, other):
		# Assume that both objects are AutoDiffToyObjects
		# Check if both objects are of the same type
		# Self is probably the object on the LHS of the equation
		# if isinstance(self, type(other)):
		# 	alpha = self.alpha - other.alpha
		# 	beta = self.beta - other.beta
		# 	new_object = cls(self.x_object, alpha=alpha, beta=beta)
		# 	return(new_object)

		# # Perhaps the 'other' is not an AutoDiffToyObject.
		# else:
		# 	try:
		# 		return self.__rsub__(other)
		# 	except:
		# 		raise AttributeError(f'{other.__class__.__name__} is invalid for addition.')


		# Assume that other is a number, and self
		# is an object of interest.
		try:
			alpha = self.alpha
			beta = self.beta - other.real
			new_object = cls(self.x_object, alpha=alpha, beta=beta)

			return new_object
			
		except AttributeError:
			pass

		try:
			# Deals with case where both self and other
			# are weird unrecognized cases. We covert
			# them to dummy classes and extract their values
			# and derivatives only for subsequent use.
			self_dummy = dummy(self.val, self.der)
			other_dummy = dummy(other.val, other.der)

			return self_dummy - other_dummy
		except:
			raise AttributeError

	def __rsub__(self, other):
		'''
		Allows for commuative cases of subtraction, where a
		float or integer are added to the autodifftoy object.
		Note:
		For the equation x - y,
		__rsub__ works as y.__rsub(x)
		Thus,
		other --> x
		self --> y
		https://docs.python.org/2/reference/datamodel.html#object.__rsub__
		'''
		rsub_result = self.__perform_rsub__(self, other)
		return(rsub_result)


	@classmethod
	def __perform_rsub__(cls, self, other):
		# try:
		# 	# Maybe need to make this more stringent!!!
		# 	# E.g. the self.x_object (why not other?)
		# 	# A bit dangerous if we are using a sin subtracting a cos
		# 	alpha = other.alpha - self.alpha
		# 	beta = other.beta - self.beta
		# 	new_toy = cls(self.x_object, alpha=alpha, beta=beta)
		# 	return(new_toy)

		# # Perhaps the 'other' is not an AutoDiffToyObject.
		# # So we'll just add the constant values
		# except:
		# 	try:
		# 		if isinstance(self, cls):
		# 			alpha = self.alpha
		# 			beta = other.real - self.beta
		# 			new_toy = cls(self.x_object, alpha=alpha, beta=beta)
		# 		elif isinstance(other, cls):
		# 			# I dun think we will ever get here
		# 			alpha = other.alpha
		# 			beta = other.beta - self.real
		# 			new_toy = cls(other.x_object, alpha=alpha, beta=beta)
		# 		else:
		# 			raise AttributeError(f'{other.__class__.__name__} is invalid for addition.')
		# 		return(new_toy)
		# 	except:
		# 		raise AttributeError(f'{other.__class__.__name__} is invalid for addition.')

		# Assume that this is a case where x - y, where x is a
		# number, and y is a class of interest.
		# x is other, y is self.
		try:
			alpha = self.alpha
			beta = other.real - self.beta
			new_toy = cls(self.x_object, alpha=alpha, beta=beta)
			return new_toy
		except AttributeError:
			pass

		try:
			# Deals with case where both self and other
			# are weird unrecognized cases. We covert
			# them to dummy classes and extract their values
			# and derivatives only for subsequent use.
			self_dummy = dummy(self.val, self.der)
			other_dummy = dummy(other.val, other.der)

			return other_dummy - self_dummy
		except:
			raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for multiplication.')

	def __mul__(self, other):
		'''
		This allows for multiplication between a coefficient 
		value and a AutoDiffToy object
		'''
		# Multiply a number with a 'x' class
		try:
			# alpha = self.alpha * other.real
			# new_toy = AutoDiffToy(self.a, alpha, self.beta)
			# return(new_toy)
			return self.__perform_muliplication__(self, other)

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
			# alpha = self.alpha * other.real
			# new_toy = AutoDiffToy(self.a, alpha, self.beta)
			# return(new_toy)
			return self.__perform_muliplication__(self, other)
		except:
			raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for multiplication.')


	# @classmethod
	# def __perform_muliplication__(cls, self, other):
	# 	'''
	# 	Perform multiplication
	# 	'''
	# 	try:
	# 		if isinstance(self, cls):
	# 			# Muliply object with an integer
	# 			alpha = self.alpha * other.real
	# 			beta = self.beta * other.real
	# 			new_toy = cls(self.x_object, alpha=alpha, beta=beta)
	# 			return(new_toy)
	# 		elif isinstance(other, cls):
	# 			# Allows commutative multiplication
	# 			alpha = other.alpha * self.real
	# 			beta = other.beta * self.real
	# 			new_toy = cls(other.x_object, alpha=alpha, beta=beta)
	# 			return(new_toy)
	# 		else:
	# 			AttributeError(f'{other.__class__.__name__}.{name} is invalid for multiplication.')
	# 	except:
	# 		raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for multiplication.')
	@classmethod
	def __perform_muliplication__(cls, self, other):
		'''
		Perform multiplication
		'''
		try:
			# Assume 'other' is a single number and try
			# to multiple
			alpha = self.alpha * other.real
			beta = self.beta * other.real
			new_toy = cls(self.x_object, alpha=alpha, beta=beta)
			return(new_toy)
		except AttributeError:
			pass
		try:
			# Allows commutative multiplication. Assumes
			# that 'self' is a number (probably not needed)
			alpha = other.alpha * self.real
			beta = other.beta * self.real
			new_toy = cls(other.x_object, alpha=alpha, beta=beta)
			return(new_toy)
		except AttributeError:
			pass
		try:
			# Deals with case where both self and other
			# are weird unrecognized cases. We covert
			# them to dummy classes and extract their values
			# and derivatives only for subsequent use.
			self_dummy = dummy(self.val, self.der)
			other_dummy = dummy(other.val, other.der)

			return self_dummy * other_dummy
		except:
			raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for multiplication.')


	def __div__(self, other):
		'''
		This allows for division between a coefficient 
		value and a AutoDiffToy object
		'''
		try:

			return self.__perform_division__(self, other)


		except:
			raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for division.')


	def __rdiv__(self, other):
		try:
	
			return self.__perform_division__(self, other)
		except:
			raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for division.')


	@classmethod
	def __perform_division__(cls, self, other):
		'''
		Perform division
		'''
		try:
		
			alpha = self.alpha / other.real
			beta = self.beta / other.real
			new_toy = cls(self.x_object, alpha=alpha, beta=beta)
			return(new_toy)
		except AttributeError:
			pass
		try:
			alpha = other.alpha / self.real
			beta = other.beta / self.real
			new_toy = cls(other.x_object, alpha=alpha, beta=beta)
			return(new_toy)
		except AttributeError:
			pass
		try:

			self_dummy = dummy(self.val, self.der)
			other_dummy = dummy(other.val, other.der)

			return self_dummy / other_dummy
		except:
			raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for division.')

	def __pow__(self, other):
		try:	
			return self.__perform_higherorder__(self, other)
		except:
			raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for higher order.')


	def __rpow__(self, other): 
		try:
			return self.__perform_higherorder__(self, other)
		except:
			raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for higher order.')

	@classmethod
	def __perform_higherpower__(cls, self, other):
		'''
		Perform power
		'''
		try: 
		
			alpha = self.alpha ** other.real
			beta = self.beta ** other.real
			new_toy = cls(self.x_object, alpha=alpha, beta=beta)
			return(new_toy)
		except AttributeError:
			pass
		try:
			alpha = other.alpha ** self.real
			beta = other.beta ** self.real
			new_toy = cls(other.x_object, alpha=alpha, beta=beta)
			return(new_toy)
		except AttributeError:
			pass
		try:

			self_dummy = dummy(self.val, self.der)
			other_dummy = dummy(other.val, other.der)
			return self_dummy ** other_dummy
		except:
			raise AttributeError


	def __neg__(self):
		try:
			return self.__perform_negation__(self)
		# Catch weird cases.
		except:
			raise AttributeError

	@classmethod
	def __perform_negation__(self):
		try:
			alpha = -1 * self.alpha
			beta = -1 * self.beta
			new_object = cls(self.x_object, alpha=alpha, beta=beta)

			return new_object
		except:
			raise AttributeError




class sin(trigo_exp):
	'''
	E.g.
	f(x) = alpha * sin(x) + beta
	'''
	def calc_function_val(self):
		'''
		Calculate the current value of this
		function at the value of x
		'''
		value = self.alpha * math.sin(self.x_object.val) + self.beta

		return value

	def calc_function_derivative_val(self):
		'''
		Calculate the derivative of this function
		at the a value of interest
		'''
		derivative_val = self.alpha * self.x_object.der * math.cos(self.x_object.val)

		return derivative_val


class cos(trigo_exp):
	'''
	E.g.
	f(x) = alpha * cos(x) + beta
	'''
	def calc_function_val(self):
		'''
		Calculate the current value of this
		function at the value of x
		'''
		value = self.alpha * math.cos(self.x_object.val) + self.beta
		return value

	
	def calc_function_derivative_val(self):
		'''
		Calculate the derivative of this function
		at the a value of interest
		'''
		derivative_val = (-1) * self.alpha * self.x_object.der * math.sin(self.x_object.val)

		return derivative_val


class tan(trigo_exp):
	'''
	E.g.
	f(x) = alpha * tan(x) + beta
	'''
	def calc_function_val(self):
		'''
		Calculate the current value of this
		function at the 
		'''
		value = self.alpha * math.tan(self.x_object.val) + self.beta
		return value

	
	def calc_function_derivative_val(self):
		'''
		Calculate the derivative of this function
		at the a value of interest
		'''
		derivative_val = self.alpha * self.x_object.der * (1 / (math.cos(self.x_object.val) ** 2))
		return derivative_val


class exponential(trigo_exp):
	'''
	E.g.
	f(x) = alpha * exp(x) + beta
	'''
	def calc_function_val(self):
		'''
		Calculate the current value of this
		function at the 
		'''
		value = self.alpha * math.exp(self.x_object.val) + self.beta
		return value

	
	def calc_function_derivative_val(self):
		'''
		Calculate the derivative of this function
		at the a value of interest
		'''
		derivative_val = self.alpha * self.x_object.der * math.exp(self.x_object.val)
		return derivative_val



if __name__ == "__main__":

	a = 2.0 # Value to evaluate at


	alpha = 2.0
	beta = 3.0
	gamma = 4.0


	a = 2.0 # Value to evaluate at
	x = x_simple(a)

	alpha = 2.0
	beta = 3.0
	f = alpha * x + beta

	print(f.val, f.der)
	x_2 = sin(f)
	print(x_2.val, x_2.der)


	x_3 = sin(f)



	x_4 = x_2 + x_3 + x_2
	#print(x_4.alpha)
	print(x_4.val, x_4.der)


	print("======")
	x_5 = x_4 + 1
	print(x_5)
	print(x_5.der)
	print(x_5.val, x_5.der)


	x_6 = 1 - x_4
	print(x_6.val, x_6.der)

	x_7 = x_6 * 2
	print(x_7.val, x_7.der)

	x_8 = 2 * x_6
	print(x_8.val, x_8.der)




	x_9 = 2 * cos(f) + 3
	print(x_9.val, x_9.der)



	x_9 = 2 * tan(f) + 3
	print(x_9.val, x_9.der)


	x_9 = 2 * exponential(f) + 3
	print(x_9.val, x_9.der)


	x_10 = x_9 * x_9
	print(x_10.val, x_10.der)

	# x = sin(a=a)
	# #f = alpha * x + beta
	# f = x + beta
	# print(f.val, f.der)


	x_10 = x_9 * x_9
	print(x_10.val, x_10.der)


	#f = alpha * x + beta
	#f = x * alpha + beta

	# f = beta + alpha * x 

	# f = alpha * x + beta
	# print(f.val, f.der)
	# print("====================")


	# f = beta + alpha * x 


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

	# print("Testing: f = beta + alpha * x")
	# f_3 = beta + alpha * x
	# print(f_3.val, f_3.der)
	# print("====================")

	# print("Testing: f = beta + x * alpha")
	# f_4 = beta + x * alpha
	# print(f_4.val, f_4.der)
	# print("====================")


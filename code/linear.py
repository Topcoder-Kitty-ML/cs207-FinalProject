#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dummy import dummy

class AutoDiffToy():
	'''
	Toy forward automatic differentiation
	class.
	'''
	def __init__(self, a, alpha=1, beta=0):

		self.a = a # value to evaluate at
		self.alpha = alpha # regard as a x variable with coefficient of x = 1
		self.beta = beta # regard as a x variable with no constant

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

		# Assumes that 'self' is an AutoDiff Object,
		# and other is a number.
		try:
			beta = self.beta + other.real
			new_toy = AutoDiffToy(self.a, self.alpha, beta)
			return(new_toy)
		except AttributeError:
			#raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for multiplication.')
			pass

		# # Assume that both objects are AutoDiffToyObjects
		# try:
		# 	alpha = self.alpha + other.alpha
		# 	beta = self.beta + other.beta
		# 	new_toy = AutoDiffToy(self.a, alpha, beta)
		# 	return(new_toy)
		# # Perhaps the 'other' is not an AutoDiffToyObject.
		# # So we'll just add the constant values
		# except:

		# We are adding two AutoDiff class, or an AutoDiff classs
		# with another object here. In which case, we replace this
		# with a dummy object and just retain the value and derivative
		try:
			self_dummy = dummy(self.val, self.der)
			other_dummy = dummy(other.val, other.der)

			return self_dummy + other_dummy
		except:
			raise AttributeError()


	def __radd__(self, other):
		'''
		Allows for commuative cases of addition, where a
		float or integer are added to the autodifftoy object.
		'''
		# We assume that 'other' is just a number being added 
		# to the autodiff object. Allows commutative case

		try:
			beta = self.beta + other.real
			new_toy = AutoDiffToy(self.a, self.alpha, beta)
			return(new_toy)
		except AttributeError:
			pass
			#raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for multiplication.')

		# # Assume that both objects are AutoDiffToyObjects
		# try:
		# 	alpha = self.alpha + other.alpha
		# 	beta = self.beta + other.beta
		# 	new_toy = AutoDiffToy(self.a, alpha, beta)
		# 	return(new_toy)
		# # Perhaps the 'other' is not an AutoDiffToyObject.
		# # So we'll just add the constant values
		# except:

		# We are adding two AutoDiff class, or an AutoDiff classs
		# with another object here. In which case, we replace this
		# with a dummy object and just retain the value and derivative
		try:
			self_dummy = dummy(self.val, self.der)
			other_dummy = dummy(other.val, other.der)
			return self_dummy + other_dummy
		except:
			raise AttributeError()


	def __sub__(self, other):
		# Assumes that 'self' is an AutoDiff Object,
		# and other is a number.
		try:
			alpha = self.alpha
			beta = self.beta - other.real
			new_toy = AutoDiffToy(self.a, alpha, beta)
			return(new_toy)
		except AttributeError:
			#raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for multiplication.')
			pass

		# We are substracting two AutoDiff class, or another class with
		# an AutoDiff class here. In which case, we replace this
		# with a dummy object and just retain the value and derivative
		try:
			# Note that for a case of x - y, x refers to self here,
			# and other refers to y.
			self_dummy = dummy(self.val, self.der)
			other_dummy = dummy(other.val, other.der)
			return self_dummy - other_dummy
		except:
			raise AttributeError()

	def __rsub__(self, other):
		# Assumes that 'self' is an AutoDiff Object,
		# and other is a number.
		# Allows commutative case.
		# Note that for a case of x - y, y refers to self here,
		# and other refers to x.
		try:
			alpha = self.alpha
			beta = other.real - self.beta
			new_toy = AutoDiffToy(self.a, alpha, beta)
			return(new_toy)
		except AttributeError:
			#raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for multiplication.')
			pass

		# We are substracting two AutoDiff class, or another class with
		# an AutoDiff class here. In which case, we replace this
		# with a dummy object and just retain the value and derivative
		try:

			self_dummy = dummy(self.val, self.der)
			other_dummy = dummy(other.val, other.der)
			return other_dummy - self_dummy
		except:
			raise AttributeError()


	def __mul__(self, other):
		'''
		This allows for multiplication between a coefficient 
		value and a AutoDiffToy object
		'''
		# We assume that 'other' is a number and try to 
		# multiply this class ('self') with the number
		# Multiply a number with a 'x' class
		try:
			alpha = self.alpha * other.real
			beta = self.beta * other.real
			new_toy = AutoDiffToy(self.a, alpha, beta)
			return(new_toy)
		except AttributeError:
			#raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for multiplication.')
			pass

		# We are multiplying two AutoDiff class, or an AutoDiff classs
		# with another object here. In which case, we replace both of these
		# with a dummy object and just retain the value and derivative
		try:
			self_dummy = dummy(self.val, self.der)
			other_dummy = dummy(other.val, other.der)
			return self_dummy * other_dummy
		except:
			raise AttributeError()


	def __rmul__(self, other):
		'''
		We use rmul as it allows us to deal with commutative case
		in which we have to multiply a float value with a AutoDiffToy
		class, without having to overlaod __mul__ function in the
		float class. (__mul__ function is called from the first variable
		in a multiplication)
		'''
		# We assume that 'other' is a number and try to 
		# multiply this class ('self') with the number
		# Allows commutative case of multiply
		try:
			alpha = self.alpha * other.real
			beta = self.beta * other.real
			new_toy = AutoDiffToy(self.a, alpha, beta)
			return(new_toy)
		except AttributeError:
			#raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for multiplication.')
			pass

		# We are multiplying two AutoDiff class, or an AutoDiff classs
		# with another object here. In which case, we replace both of these
		# with a dummy object and just retain the value and derivative
		try:
			self_dummy = dummy(self.val, self.der)
			other_dummy = dummy(other.val, other.der)
			return other_dummy * self_dummy
		except:
			raise AttributeError()


	def __div__(self, other):
		print("apple")
        
		try:
			alpha = self.alpha / other.real
			beta = self.beta / other.real
			new_toy = AutoDiffToy(self.a, alpha, beta)
			return(new_toy)
		except AttributeError:
			pass

		try:
			self_dummy = dummy(self.val, self.der)
			other_dummy = dummy(other.val, other.der)
			return self_dummy / other_dummy
		except:
			raise AttributeError()

	def __rdiv__(self, other):
		print("rdiv")
	
		try:
			alpha = self.alpha / other.real
			beta = self.beta / other.real
			new_toy = AutoDiffToy(self.a, alpha, beta)
			return(new_toy)
		except AttributeError:
			pass

		try:
			self_dummy = dummy(self.val, self.der)
			other_dummy = dummy(other.val, other.der)
			return other_dummy / self_dummy
		except:
			raise AttributeError()

	def __pow__(self, other):
		try:
			alpha = self.alpha ** other.real
			beta = self.beta ** other.real
			new_toy = AutoDiffToy(self.a, alpha, beta)
			return(new_toy)
		except AttributeError:
			pass

		try:
			self_dummy = dummy(self.val, self.der)
			other_dummy = dummy(other.val, other.der)
			return self_dummy ** other_dummy
		except:
			raise AttributeError()


	def __rpow__(self, other):
		try:
			alpha = self.alpha ** other.real
			beta = self.beta ** other.real
			new_toy = AutoDiffToy(self.a, alpha, beta)
			return(new_toy)
		except AttributeError:
			pass

		try:
			self_dummy = dummy(self.val, self.der)
			other_dummy = dummy(other.val, other.der)
			return other_dummy ** self_dummy
		except:
			raise AttributeError()

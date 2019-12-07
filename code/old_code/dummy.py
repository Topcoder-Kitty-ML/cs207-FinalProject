
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

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
		# Assume we're adding a simple number with a
		# a dummy object
		try:
			new_val = self.val + other.real
			new_der = self.der
			return dummy(new_val, new_der)
		except AttributeError:
			pass

		# Adding two dummy object, or a dummy with
		# another object
		try:
			new_val = self.val + other.val
			new_der = self.der + other.der
			return dummy(new_val, new_der)
		except:
			raise AttributeError()

	def __radd__(self, other):
		# Assume we're adding a simple number with
		# a dummy object
		try:
			new_val = other.real + self.val 
			new_der = self.der
			return dummy(new_val, new_der)
		except AttributeError:
			pass

		# Adding two dummy object, or a dummy with
		# another object
		try:
			new_val = self.val + other.val
			new_der = self.der + other.der
			return dummy(new_val, new_der)
		except:
			raise AttributeError()

	def __sub__(self, other):
		# Assume we're subtracting a simple number with a
		# a dummy object
		try:
			new_val = self.val - other.real
			new_der = - self.der
			return dummy(new_val, new_der)
		except AttributeError:
			pass

		# Subtracting two dummy object, or a dummy with
		# another object
		try:
			new_val = self.val - other.val
			new_der = self.der - other.der
			return dummy(new_val, new_der)
		except:
			raise AttributeError()

	def __rsub__(self, other):
		# Assume we're subtracting a simple number with a
		# a dummy object
		# E.g. num - dummy
		# num is 'other', dummy is 'self'
		try:
			new_val = other.real - self.val
			new_der = - self.der
			return dummy(new_val, new_der)
		except AttributeError:
			pass

		# Subtracting two dummy object, or a dummy with
		# another object
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
		# Assume we're multiplying a dummy object with
		# a simple number.
		try:
			new_val = self.val * other.real
			new_der = self.der * other.real
			return dummy(new_val, new_der)
		except AttributeError:
			pass

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

		# For case of x * y, where x is a number.
		# x is other, and y is self.
		try:
			new_val = other.real * self.val
			new_der = other.real * self.der
			return dummy(new_val, new_der)
		except AttributeError:
			pass

		try:
			new_val = self.val * other.val
			new_der = self.val * other.der + other.val * self.der
			return dummy(new_val, new_der)
		except:
			raise AttributeError()


	def __truediv__(self, other):
		'''
		Apply the quotient rule
		'''

		# Case where dummy is divided by number
		try:
			new_val = self.val / other.real
			new_der = self.der / other.real 
			return dummy(new_val, new_der)
		except AttributeError:
			pass

		# Case where dummy1 is divided by dummy2
		try:
			new_val = self.val / other.val
			new_der = (other.val * self.der - self.val * other.der) / (other.val ** 2)
			return dummy(new_val, new_der)
		except:
			raise AttributeError() 

	def __rtruediv__(self, other):

		# Case of x/y, where x is a number, and y is a 
		# dummy object. x is other, y is self.
		try:
			new_val = other.real / self.val
			#new_der = other.real / self.der
			new_der = (-1) * other.real * (self.val) ** (-2) * self.der
			return dummy(new_val, new_der)
		except AttributeError:
			pass

		# Case of two objects dividing by each other
		try:
			new_val = self.val / other.val
			new_der = (other.val * self.der - self.val * other.der) / (other.val ** 2)
			return dummy(new_val, new_der)
		except:
			raise AttributeError()

	def __pow__(self, other):
		# Assume that the self is a dummy class,
		# and the other is a simple number
		try:
			#print("====")
			#print(other)
			#print(self.val, other.real)
			new_val = self.val ** other.real
			#new_der = self.val ** other.real * (self.der * (other.real/self.val) + (0 * math.log(self.val)))
			new_der = self.val ** other.real * (self.der * (other.real/self.val))
			return dummy(new_val, new_der) 
		except AttributeError:
			pass 
		
		try:
			#print("-=-=-")
			new_val = self.val ** other.val
			#print("apple1")
			new_der = (self.val ** other.val) * (self.der * (other.val/self.val)+ (other.der* math.log(self.val)))
			#new_der = self.val ** other.val * (self.der * (other.val/self.val))
			#print("apple2")
			#print(new_der)
			return dummy(new_val, new_der) 
		except:
			pass

		# This deals with an edge case where 
		# self.val is a negative number, and cannot be log.
		# In this case, we assume other.der is zero
		# (self.val is the base of the exponenent)
		# e.g. x ** 2
		# (NEED DOUBLE CHECK IF THIS IS A GENERALIZED RULE!!!)
		try:
			#print("last chunk")
			new_val = self.val ** other.val
			new_der = (self.val ** other.val) * (self.der * (other.val/self.val))
				
			return dummy(new_val, new_der)
		except:
			raise AttributeError
			
	def __rpow__(self, other):
		# E.g. case of 2 ** dummy_class,
		# In this case, dummy_class is self, 2 is other
		try:
			print("-----")
			print(self.val)
			print(self)
			print(other)
			print(other.real)
			new_val = other.real ** self.val
			new_der = (other.real ** self.val) * (0 * (self.val/other.real) + (self.der * math.log(other.real)))
			return dummy(new_val, new_der) 
		except:
			raise AttributeError
		
		# case of dummy_A ** dummy_B
		try:
			new_val = other.val ** self.val
			new_der = (other.val ** self.val) * (other.der * (self.val/other.val) + (self.der * math.log(other.val)))
			return dummy(new_val, new_der) 
		except:
			raise AttributeError()

	def __neg__(self):
		try:
			new_val = -1 * self.val 
			new_der = -1 * self.der
			return dummy(new_val, new_der) 
		except:
			raise AttributeError()

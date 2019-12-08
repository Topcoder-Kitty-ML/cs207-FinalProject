#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
		
class GenericDiff:
	def __init__(self, val, der):
		self.val = val 
		self.der = der  

	def __add__(self, other):
		def __add__generic(self, other):   
			new_val = self.val + other.val
			new_der = self.der + other.der

			return GenericDiff(new_val, new_der)
		
		try:
			return __add__generic(self, other)
				
		except AttributeError:   
			other = Constant(other)
			return __add__generic(self, other)  

	def __radd__(self, other):
		def __radd__generic(self, other):
			new_val = other.val + self.val 
			new_der = other.der + self.der 

			return GenericDiff(new_val, new_der)
			
		try:
			return __radd__generic(self, other)

		except AttributeError: 
			other = Constant(other)
			return __radd__generic(self, other) 
	
	def __sub__(self, other):
		def __sub__generic(self, other):
			new_val = self.val - other.val
			new_der = self.der - other.der 

			return GenericDiff(new_val, new_der)

		try:
			return __sub__generic(self, other)
				
		except AttributeError: 
			other = Constant(other)
			return __sub__generic(self, other)  
   
	def __rsub__(self, other): 
		def __rsub__generic(self, other):
			new_val = other.val - self.val 
			new_der = other.der - self.der 

			return GenericDiff(new_val, new_der)
			
		try:
			return __rsub__generic(self, other)
				
		except AttributeError:
			other = Constant(other)
			return __rsub__generic(self, other) 

	
	def __mul__(self, other): 
		def __mul__generic(self, other):
			new_val = self.val * other.val
			new_der = self.val * other.der + other.val * self.der

			return GenericDiff(new_val, new_der)
		
		try:
			return __mul__generic(self, other)
			
		except AttributeError:
			other = Constant(other)
			return __mul__generic(self,other) 
			
	def __rmul__(self, other):
		def __rmul__generic(self, other):
			new_val = other.val * self.val
			new_der = other.val * self.der + self.val * other.der

			return GenericDiff(new_val, new_der)
			
		try:
			return __rmul__generic(self, other) 
			
		except AttributeError:
			other = Constant(other)
			return __rmul__generic(self, other)
	
	def __truediv__(self, other):
		def __truediv__generic(self, other):
			new_val = self.val / other.val
			new_der = (other.val * self.der - self.val * other.der) / (other.val ** 2)

			return GenericDiff(new_val, new_der)
			
		try:
			return __truediv__generic(self, other)
			
		except AttributeError:
			other = Constant(other)
			return __truediv__generic(self, other)
			
	def __rtruediv__(self, other):
		def __rtruediv__generic(self, other):
			new_val = other.val / self.val
			new_der = (self.val * other.der - other.val * self.der) / (self.val ** 2)

			return GenericDiff(new_val, new_der)

		try:
			# This code has syntax error. Removed colon
			return __rtruediv__generic(self, other)
				
		except AttributeError:
			other = Constant(other) 
			return __rtruediv__generic(self, other)
	  
	def __pow__(self, other):
		def __pow__generic(self, other):
			new_val = self.val ** other.val

			if other.der == 0:
				new_der = (self.val ** other.val) * (self.der * (other.val/self.val))
			else:
				new_der = (self.val ** other.val) * (self.der * (other.val/self.val)+ (other.der* math.log(self.val)))

			return GenericDiff(new_val, new_der)
				

		try:
			# This code has syntax error. Removed colon
			return __pow__generic(self, other)
		
		except AttributeError:
			# This code has syntax error. Removed colon
			other = Constant(other)
			return __pow__generic(self, other)
		
	def __rpow__(self, other):
		def __rpow__generic(self, other):
			new_val = other.val ** self.val 
			
			if self.der == 0:
				new_der = (other.val ** self.val) * (other.der * (self.val/other.val))
			else:
				new_der = (other.val ** self.val) * (other.der * (self.val/other.val) + (self.der * math.log(other.val)))

			return GenericDiff(new_val, new_der)
				
		try:
			return __rpow__generic(self, other)
				
		except AttributeError:
			other = Constant(other)
			
			return __rpow__generic(self, other)
		

	def __neg__(self):
		try:
			new_val = -1 * self.val 
			new_der = -1 * self.der

			return GenericDiff(new_val, new_der) 
			
		except:
			raise AttributeError()
    	
	def __lt__(self, other):
		'''
		We define the less than to be less
		than of the derivative instead of
		the value of the objects.
		'''
		try:
			return self.der < other.der	

		except AttributeError:
			other = Comparison(other)
			return self.der < other.der

	def __gt__(self, other):
		'''
		We compare the derivative instead of
		the value here by definition
		'''
		try:
			return self.der > other.der

		except AttributeError:
			other = Comparison(other)
			return self.der > other.der

	def __le__(self, other):
		'''
		We compare the derivative instead of
		the value here by definition
		'''
		try:
			return self.der <= other.der

		except AttributeError:
			other = Comparison(other)
			return self.der <= other.der

	def __ge__(self, other):
		'''
		We compare the derivative instead of
		the value here by definition
		'''
		try:
			return self.der >= other.der

		except AttributeError:
			other = Comparison(other)
			return self.der >= other.der

	def __eq__(self, other):
		'''
		When the equal operator is called, we compare
		the values of the derivative of the object instead
		of the values.
		'''
		try:
			return self.der == other.der

		except AttributeError:
			other = Comparison(other)
			return self.der == other.der


	def __ne__(self, other):
		'''
		When the not-equal operator is called, we compare
		the values of the derivative of the object instead
		of the values.
		'''
		try:
			return self.der != other.der

		except AttributeError:
			other = Comparison(other)
			return self.der != other.der


class Var(GenericDiff):
	def __init__(self, value):
		self.val = value
		self.der = 1

class Constant(GenericDiff):
	def __init__(self, value):
		self.val = value
		self.der = 0

class Comparison(GenericDiff):
	def __init__(self, value):
		self.der = value



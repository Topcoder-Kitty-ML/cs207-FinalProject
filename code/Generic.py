#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

class Var:
    
    def __init__(self, value): 
        self.val = value
        self.der = 1
        
class Generic:
    
    def __init__(self, val, der):
		self.val = val 
		self.der = der  

	def __add__(self, other):
		# Assume we're adding a simple number with a
		# a dummy object
		try:
			new_val = self.val + other.val
			new_der = self.der
			return Generic(new_val, new_der)    
        
		except AttributeError:  
			new_val = self.val + float(other)
            new_der = self.der
            return Generic(new_val, new_der) 

    __radd__ = __add__ # can you do this?
    
    def __sub__(self, other):
        
        try:
			new_val = self.val - other.val
			new_der = self.der - other.der
			return Generic(new_val, new_der)
        
		except AttributeError(): 
			new_val = self.val - float(other)
            new_der = self.der 
            return Generic(new_val, new_der)
    
    def __rsub__(self, other):
        
        try:
			new_val = other.val - self.val
			new_der = other.der - self.der
			return Generic(new_val, new_der)
        
		except AttributeError:
			new_val = other.val - float(self)
            new_der = other.der
            return Generic(new_val, new_der)
    
    def __mul__(self, other): 
        try:
		    new_val = self.val * other.val
		    new_der = self.val * other.der + other.val * self.der
            return Generic(new_val, new_der) 
            
        except AttributeError:
            new_val = self.val * float(other)
            new_der = float(other) * self.der 
            
    __rmul__ = __mul__
    
    def __truediv__(self, other):
		'''
		Apply the quotient rule
		'''
        try:
			new_val = self.val / other.val
			new_der = (other.val * self.der - self.val * other.der) / (other.val ** 2)
			return Generic(new_val, new_der) 
        
		except AttributeError:
			new_val = self.val / float(other)
            new_der = self.der / float(other)
            return Generic(new_val, new_der) 
            
    def __rtruediv__(self, other):x 

		# Case of two objects dividing by each other
		try:
			new_val = self.val / other.val
			new_der = (other.val * self.der - self.val * other.der) / (other.val ** 2)
			return Generic(new_val, new_der) 
        
		except AttributeError:
			new_val = self.val / float(other)
            new_der = self.der / float(other)
            return Generic(new_val, new_der) 
      
        # still have to fix pow and rpow!      
    def __pow__(self, other):
		# Assume that the self is a dummy class,
		# and the other is a simple number 
		
		try:
			new_val = self.val ** other.val
			new_der = (self.val ** other.val) * (self.der * (other.val/self.val)+ (other.der* math.log(self.val)))
			return Generic(new_val, new_der) 
        
		except AttributeError:
            new_val = self.val ** float(other)
			new_der = self.val ** float(other) * (self.der * (float(other)/self.val))
			return Generic(new_val, new_der) 
        
        except ValueError:
        

		# This deals with an edge case where 
		# self.val is a negative number, and cannot be log.
		# In this case, we assume other.der is zero
		# (self.val is the base of the exponenent)
		# e.g. x ** 2
		# (NEED DOUBLE CHECK IF THIS IS A GENERALIZED RULE!!!)
#		try:
#			#print("last chunk")
#			new_val = self.val ** other.val
#			new_der = (self.val ** other.val) * (self.der * (other.val/self.val))
#				
#			return Generic(new_val, new_der)
#		except:
#			raise AttributeError
		
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
			return generic(new_val, new_der) 
		except:
			raise AttributeError
		
		# case of dummy_A ** dummy_B
		try:
			new_val = other.val ** self.val 
			new_der = (other.val ** self.val) * (other.der * (self.val/other.val) + (self.der * math.log(other.val)))
			return generic(new_val, new_der) 
		except:
			raise AttributeError()

	def __neg__(self):
		try:
			new_val = -1 * self.val 
			new_der = -1 * self.der
			return generic(new_val, new_der) 
        
		except:
			raise AttributeError()
            
    def sin(Generic):
        
        try: 
			new_val = math.sin(self.val)
			new_der = math.cos(self.val)
			return generic(new_val, new_der) 
        
		except AttributeError:
			pass
    
    def cos(Generic): 
        
        try:
            new_val = math.cos(self.val)
            new_der = - math.sin(self.val)
            return generic(new_val, new_der)
        
        except AttributeError:
            pass
        
    
    
    

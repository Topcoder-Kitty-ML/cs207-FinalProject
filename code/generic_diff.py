#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

class Var:
    def __init__(self, value): 
        self.val = value
        self.der = 1

class Constant:
    def __init__(self, value):
        self.val = value
        self.der = 0        
        
class GenericDiff:
    def __init__(self, val, der):
        self.val = val 
        self.der = der  

	def __add__(self, other):
        def __add__generic(self, other):   
			self.val = self.val + other.val
			self.der = self.der
            
        try:
            __add__generic(self,other):
                
		except AttributeError:   
			other = Constant(other)
            __add__generic(self, other)  

    def __radd__(self, other):
        def __radd__generic(self, other):
            self.val = other.val + self.val 
			self.der = self.der 
            
        try:
            __radd__generic(self, other):
                
		except AttributeError: 
			other = Constant(other)
            __radd__generic(self, other) 
    
    def __sub__(self, other):
        def __sub__generic(self, other):
			self.val = self.val - other.val
			self.der = self.der - other.der 
        
        try:
            __sub__generic(self, other):
                
		except AttributeError(): 
			other = Constant(other)
            __sub__generic(self, other)  
   
    def __rsub__(self, other): 
        def __rsub__generic(self, other):
			self.val = other.val - self.val 
			self.der = other.der - self.der 
            
        try:
            __rsub__generic(self, other):
                
		except AttributeError:
			other = Constant(other)
            __rsub__generic(self, other) 

    
    def __mul__(self, other): 
        def __mul__generic(self, other):
		    self.val = self.val * other.val
		    self.der = self.val * other.der + other.val * self.der
        
        try:
            __mul__generic(self, other)
            
        except AttributeError:
            other = Constant(other)
            __mul__generic(self,other) 
            
    def __rmul__(self, other):
        def __rmul__generic(self, other):
			self.val = other.val * self.val
			self.der = other.val * self.der + self.val * other.der
            
        try:
            __rmul__generic(self, other) 
            
		except AttributeError:
			other = Constant(other)
            __rmul__generic(self, other)
    
    def __truediv__(self, other):
        def __truediv__generic(self, other):
			self.val = self.val / other.val
			self.der = (other.val * self.der - self.val * other.der) / (other.val ** 2)
            
        try:
            __truediv__generic(self, other)
            
		except AttributeError:
			other = Constant(other)
            __truediv__generic(self, other)
            
    def __rtruediv__(self, other):
        def __rtruediv__generic(self, other):
			self.val = self.val / other.val
			self.der = (other.val * self.der - self.val * other.der) / (other.val ** 2)
        
		try:
            __rtruediv__generic(self, other):
                
        except AttributeError:
			other = Constant(other) 
            __rtruediv__generic(self, other)
      
    def __pow__(self, other):
        def __pow__generic(self, other):
			self.val = self.val ** other.val
            
            if other.der == 0:
                self.der = self.val ** other.val) * (self.der * (other.val/self.val)
            else:
			    self.der = (self.val ** other.val) * (self.der * (other.val/self.val)+ (other.der* math.log(self.val)))
                
        try:
           __pow__generic(self, other): 
               
		except AttributeError:
            other = Constant(other):
            __pow__generic(self, other)
        
	def __rpow__(self, other):
        def __rpow__generic(self, other):
            self.val = other.val ** self.val 
            
            if self.der == 0:
                self.der = (other.val ** self.val) * (other.der * (self.val/other.val)
			else:
                self.der = (other.val ** self.val) * (other.der * (self.val/other.val) + (self.der * math.log(other.val)))
                
        try:
            __rpow__generic(self, other):
                
		except AttributeError:
            other = Constant(other):
            __rpow__generic(self, other)
        

    def __neg__(self):
    	try:
    		new_val = -1 * self.val 
    		new_der = -1 * self.der
    		return generic(new_val, new_der) 
            
    	except:
    		raise AttributeError()
            
    def __lt__(self, other):
        return self.der < other.der
    
    def __gt__(self, other):
        return self.der > other.der
    
    def __le__(self, other):
        return self.der <= other.der
        
    def __ge__(self, other):
        return self.der >= other.der
    
    def __eq__(self, other):
        return self.der == other.der
        
    def __ne__(self, other):
        return self.der != other.der
    
    

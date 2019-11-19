#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class nonlinear():

    def __init__(self, val, der = 1):  
        self.alpha = alpha
        self.beta = beta
        self.x_object = x_object
        self.y_object = y_object
        self.val = val #a
        self.der = der

    def __add__(self, beta):
        try:
            if type(beta) == int:
                return nonlinear(self.val + beta, self.der)
            if type(beta) == nonlinear:
                return nonlinear(self.val + beta.val, self.der + beta.der)
            
        except AttributeError:
            print('Error! Your input beta is neither a number nor an AutoDiffToy object!')

    def __radd__(self,beta):
        return self.__add__(beta)

    def __mul__(self, alpha):
        try:
            if type(alpha) == int:
                return nonlinear(self.val * alpha, self.der * alpha)
            if type(alpha) == nonlinear:
                return nonlinear(self.val * alpha.val, self.der * alpha.val + self.val * alpha.der)
        except AttributeError:
            print('Error! Your input alpha is neither a number nor an AutoDiffToy object!')

    def __rmul__(self, alpha):
        return self.__mul__(alpha)
    
class higher_order(nonlinear):
    
	def calc_function_val(self, order):
		value = self.alpha * (self.x_object.val ** order  ) + self.beta
		return value

	def calc_function_derivative_val(self, order):
		derivative_val = order * self.alpha * self.x_object.der ** (order-1) 
		return derivative_val 
    
class product_rule(nonlinear):
    
    def calc_function_val(self):
        value = self.x_object.val * self.y_object.val
        return value

    def calc_function_derivative_val(self):
        derivative_val = (self.x_object.val * self.y_object.der) + (self.y_object.val * self.x_object.der)
		return derivative_val 
    
class quotient_rule(nonlinear):
    
    def calc_function_val(self):
        value = self.x_object.val / self.y_object.val
        return value

    def calc_function_derivative_val(self):
		derivative_val = (self.y_object.val * self.x_object.der) - (self.x_object.val * self.y_object.der) / (self.y_object.val ** 2)
		return derivative_val 
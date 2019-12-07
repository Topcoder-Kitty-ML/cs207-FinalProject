from generic_diff import *
import math

class sin(GenericDiff):

    def __init__(self, obj):

        def _sin_generic(obj):
            self.val = math.sin(obj.val)
            self.der = math.cos(obj.val)*obj.der

        try:
            _sin_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            _sin_generic(obj)

class cos(GenericDiff):

    def __init__(self, obj):

        def _cos_generic(obj):
            self.val = math.cos(obj.val)
            self.der = -math.sin(obj.val)*obj.der

        try:
            _cos_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            _cos_generic(obj)

class tan(GenericDiff):


    def __init__(self, obj):
        def _tan_generic(obj):
            self.val = math.tan(obj.val)
            self.der = obj.der/(math.cos(obj.val)**2.0)

        try:
            _tan_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            _tan_generic(obj)

class sinh(GenericDiff):

    def __init__(self, obj):
        def _sinh_generic(obj):
            self.val = math.sinh(obj.val)
            self.der = math.cosh(obj.val) * obj.der

        try:
            _sinh_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            _sinh_generic(obj)

class cosh(GenericDiff):

    def __init__(self, obj):
        def _cosh_generic(obj):
            self.val = math.cosh(obj.val)
            self.der = math.sinh(obj.val) * obj.der

        try:
            _cosh_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            _cosh_generic(obj)


class tanh(GenericDiff):

    def __init__(self, obj):
        def _tanh_generic(obj):
            self.val = math.tanh(obj.val)
            self.der = obj.der/(math.cosh(obj.val)**2.0)

        try:
            _tanh_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            _tanh_generic(obj)

class acos(GenericDiff):

    def __init__(self, obj):
        def _acos_generic(obj):
            self.val = math.acos(obj.val)
            self.der = -obj.der/(math.sqrt(1.0 - obj.val**2.0))

        try:
            _acos_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            _acos_generic(obj)

class asin(GenericDiff):

    def __init__(self, obj):
        def _asin_generic(obj):
            self.val = math.asin(obj.val)
            self.der = obj.der/(math.sqrt(1.0 - obj.val**2.0))

        try:
            _asin_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            _asin_generic(obj)

class atan(GenericDiff):

    def __init__(self, obj):
        def _atan_generic(obj):
            self.val = math.atan(obj.val)
            self.der = obj.der / (math.sqrt(1.0 + obj.val ** 2.0))

        try:
            _atan_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            _atan_generic(obj)

#exponential for base e
class exp(GenericDiff):

    def __init__(self, obj):
        def _exp_generic(obj):
            self.val = math.exp(obj.val)
            if obj.der == 0:
                self.der = 0
            else:
                self.der = math.exp(obj.val)*obj.der

        try:
            _exp_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            _exp_generic(obj)


# will handle any base with default = e
class log(GenericDiff):

    def __init__(self, obj, base=math.e):
        def _log_generic(obj):
            self.val = math.log(obj.val, base)
            if obj.der == 0:
                self.der = 0
            else:
                self.der = obj.der/(obj.val*math.log(base))

        try:
            _log_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            _log_generic(obj)

#logistic function
class logit(GenericDiff):

    def __init__(self, obj):
        def _logit_generic(obj):
            self.val = math.exp(obj.val)/(1+math.exp(obj.val))
            self.der = -(1+math.exp(-obj.val))**(-2)*(-obj.der*math.exp(-obj.val))

        try:
            _logit_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            _logit_generic(obj)

#sqrt function
class sqrt(GenericDiff):

    def __init__(self, obj, base=math.e):
        def _sqrt_generic(obj):
            if obj.der <= 0:
                raise ValueError("Cannot take the sqrt derivative of 0 or negative number.\n\
                                 This package only outputs real numbers.")
            else:
                self.val = math.sqrt(obj.val)
                self.der = 1/(2*math.sqrt(obj.val))

        try:
            _sqrt_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            _sqrt_generic(obj)


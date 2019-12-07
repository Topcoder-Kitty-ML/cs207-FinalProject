from generic_diff import *
import math

class sin(GenericDiff):

    def __init__(self, obj):

        def _sin_generic(obj):
            new_val = math.sin(obj.val)
            new_der = math.cos(ojb.val)*obj.der
            return GenericDiff(new_val, new_der)

        try:
            return _sin_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            return _sin_generic(obj)

class cos(GenericDiff):

    def __init__(self, obj):

        def _cos_generic(obj):
            new_val = math.cos(obj.val)
            new_der = -math.sin(obj.val)*obj.der
            return GenericDiff(new_val, new_der)

        try:
            return _cos_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            return _cos_generic(obj)

class tan(GenericDiff):


    def __init__(self, obj):
        def _tan_generic(obj):
            new_val = math.tan(obj.val)
            new_der = obj.der/(math.cos(obj.val)**2.0)
            return GenericDiff(new_val, new_der)

        try:
            return _tan_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            return _tan_generic(obj)

class sinh(GenericDiff):

    def __init__(self, obj):
        def _sinh_generic(obj):
            new_val = math.sinh(obj.val)
            new_der = math.cosh(obj.val) * obj.der
            return GenericDiff(new_val, new_der)

        try:
            return _sinh_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            return _sinh_generic(obj)

class cosh(GenericDiff):

    def __init__(self, obj):
        def _cosh_generic(obj):
            new_val = math.cosh(obj.val)
            new_der = math.sinh(obj.val) * obj.der
            return GenericDiff(new_val, new_der)

        try:
            return _cosh_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            return _cosh_generic(obj)


class tanh(GenericDiff):

    def __init__(self, obj):
        def _tanh_generic(obj):
            new_val = math.tanh(obj.val)
            new_der = obj.der/(math.cosh(obj.val)**2.0)
            return GenericDiff(new_val, new_der)

        try:
            return _tanh_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            return _tanh_generic(obj)

class acos(GenericDiff):

    def __init__(self, obj):
        def _acos_generic(obj):
            new_val = math.acos(obj.val)
            new_der = -obj.der/(math.sqrt(1.0 - obj.val**2.0))
            return GenericDiff(new_val, new_der)

        try:
            return _acos_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            return _acos_generic(obj)

class asin(GenericDiff):

    def __init__(self, obj):
        def _asin_generic(obj):
            new_val = math.asin(obj.val)
            new_der = obj.der/(math.sqrt(1.0 - obj.val**2.0))
            return GenericDiff(new_val, new_der)

        try:
            return _asin_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            return _asin_generic(obj)

class atan(GenericDiff):

    def __init__(self, obj):
        def _atan_generic(obj):
            new_val = math.atan(obj.val)
            new_der = obj.der / (math.sqrt(1.0 + obj.val ** 2.0))
            return GenericDiff(new_val, new_der)

        try:
            return _atan_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            return _atan_generic(obj)

#exponential for base e
class exp(GenericDiff):

    def __init__(self, obj):
        def _exp_generic(obj):
            new_val = math.exp(obj.val)
            if obj.der == 0:
                new_der = 0
                return GenericDiff(new_val, new_der)
            else:
                new_der = math.exp(obj.val)*obj.der
                return GenericDiff(new_val, new_der)

        try:
            return _exp_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            return _exp_generic(obj)


# will handle any base with default = e
class log(GenericDiff):

    def __init__(self, obj, base=math.e):
        def _log_generic(obj):
            new_val = math.log(obj.val, base)
            if obj.der == 0:
                new_der = 0
                return GenericDiff(new_val, new_der)
            else:
                new_der = obj.der/(obj.val*math.log(base))
                return GenericDiff(new_val, new_der)

        try:
            return _log_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            return _log_generic(obj)

#logistic function
class logit(GenericDiff):

    def __init__(self, obj):
        def _logit_generic(obj):
            new_val = math.exp(obj.val)/(1+math.exp(obj.val))
            new_der = -(1+math.exp(-obj.val))**(-2)*(-obj.der*math.exp(-obj.val))
            return GenericDiff(new_val, new_der)

        try:
            return _logit_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            return _logit_generic(obj)

#sqrt function
class sqrt(GenericDiff):

    def __init__(self, obj, base=math.e):
        def _sqrt_generic(obj):
            if obj.der <= 0:
                raise ValueError("Cannot take the sqrt derivative of 0 or negative number.\n\
                                 This package only outputs real numbers.")
            else:
                new_val = math.sqrt(obj.val)
                new_der = 1/(2*math.sqrt(obj.val))
                return GenericDiff(new_val, new_der)

        try:
            return _sqrt_generic(obj)

        except AttributeError:
            obj = Constant(obj)
            return _sqrt_generic(obj)


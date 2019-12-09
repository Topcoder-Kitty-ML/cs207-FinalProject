import pytest
import math
from genericdiff import *

# Elemental function tests ====================

## sin with Var
def test_sin_var():
    f = sin(Var(2))
    assert  (f.val, f.der) == (math.sin(2), math.cos(2)*1)

## sin with Constant
def test_sin_const():
    f = sin(2)
    assert  (f.val, f.der) == (math.sin(2), 0)

## cos with Var
def test_cos_var():
    f = cos(Var(2))
    assert  (f.val, f.der) == (math.cos(2), -math.sin(2)*1)

## cos with Constant
def test_cos_const():
    f = cos(2)
    assert  (f.val, f.der) == (math.cos(2), 0)

## tan with Var
def test_tan_var():
    f = tan(Var(2))
    assert  (f.val, f.der) == (math.tan(2), 1/(math.cos(2)**2))

## tan with Constant
def test_tan_const():
    f = tan(2)
    assert  (f.val, f.der) == (math.tan(2), 0)


## sinh with Var
def test_sinh_var():
    f = sinh(Var(2))
    assert (f.val, f.der) == (math.sinh(2), math.cosh(2) * 1)


## sinh with Constant
def test_sinh_const():
    f = sinh(2)
    assert (f.val, f.der) == (math.sinh(2), 0)


## cosh with Var
def test_cosh_var():
    f = cosh(Var(2))
    assert (f.val, f.der) == (math.cosh(2), math.sinh(2) * 1)


## cosh with Constant
def test_cosh_const():
    f = cosh(2)
    assert (f.val, f.der) == (math.cosh(2), 0)


## tanh with Var
def test_tanh_var():
    f = tanh(Var(2))
    assert (f.val, f.der) == (math.tanh(2), 1 / (math.cosh(2) ** 2))


## tanh with Constant
def test_tanh_const():
    f = tanh(2)
    assert (f.val, f.der) == (math.tanh(2), 0)

def test_asin_var():
    f = asin(Var(0.5))
    assert (f.val, f.der) == (math.asin(0.5), 1/(math.sqrt(1-0.5**2)))

def test_asin_const():
    f = asin(0.5)
    assert (f.val, f.der) == (math.asin(0.5), 0)

def test_acos_var():
    f = acos(Var(0.5))
    assert (f.val, f.der) == (math.acos(0.5), -1/(math.sqrt(1-0.5**2)))

def test_acos_const():
    f = acos(0.5)
    assert (f.val, f.der) == (math.acos(0.5), 0)

def test_atan_var():
    f = atan(Var(0.5))
    assert (f.val, f.der) == (math.atan(0.5), 1 / (math.sqrt(1+0.5**2)))

def test_atan_const():
    f = atan(0.5)
    assert (f.val, f.der) == (math.atan(0.5), 0)

def test_exp_var():
    f = exp(Var(2))
    assert (f.val, f.der) == (math.exp(2), 1*math.exp(2))

def test_exp_const():
    f = exp(2)
    assert (f.val, f.der) == (math.exp(2), 0)

def test_log_var():
    f = log(Var(2))
    assert (f.val, f.der) == (math.log(2), 1/(2*math.log(math.e)))

def test_log_const():
    f = log(2)
    assert (f.val, f.der) == (math.log(2), 0)

def test_logit_var():
    f = logit(Var(2))
    assert (f.val, f.der) == (math.exp(2)/(1+math.exp(2)),\
                              (1 + math.exp(-2)) ** (-2) * (-1 * math.exp(-2)))

def test_logit_const():
    f=logit(2)
    assert (f.val, f.der) == (math.exp(2)/(1+math.exp(2)), 0)

def test_sqrt_var():
    f=sqrt(Var(2))
    assert (f.val, f.der) == (math.sqrt(2), 1/(2*math.sqrt(2)))

def test_sqrt_const():
    f=sqrt(2)
    assert (f.val, f.der) == (math.sqrt(2), 0)

def test_sqrt_value_error():
    with pytest.raises(ValueError):
        f=sqrt(-3)





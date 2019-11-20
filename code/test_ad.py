import pytest
from trigo_exp import *
from linear import AutoDiffToy as autodiff
from vector_jacobian import *
import math

# Elemental function tests ====================

## Linear
### Intended behavior
def test_linear_1(): #TEST 1
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    assert  (f.val, f.der) == (7.0, 2.0)

def test_linear_mult(): #TEST
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + 5
    mult_f = f * h
    assert (mult_f.val, mult_f.der) == (f.val*h.val, f.val*h.der + f.der*h.val)

def test_linear_add(): #TEST
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + 5
    add_f = f + h
    assert (add_f.val, add_f.der) == (f.val + h.val, f.der + h.der)

def test_linear_sub():
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + 5
    sub_f = f - h
    assert (sub_f.val, sub_f.der) == (f.val - h.val, f.der - h.der)

def test_linear_div():
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + 5
    div_f = f / h
    assert (div_f.val, div_f.der) == (f.val/h.val, (h.val*f.der - f.val*h.der)/(h.val**2))

## Trig
### Intended behavior
def test_sin_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    x_2 = sin(f)
    assert (x_2.val, x_2.der) == (0.6569865987187891, 1.5078045086866092)

def test_cos_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    x_2 = cos(f)
    assert (x_2.val, x_2.der) == (0.7539022543433046, -1.3139731974375781)

def test_tan_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    x_2 = tan(f)
    assert (x_2.val, x_2.der) == (0.8714479827243188, 3.5188431731885697)

def test_trig_add_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + beta
    x_2 = tan(f)
    x_3 = cos(h)
    x_4 = x_2 + x_3
    assert (x_4.val, x_4.der) == (x_2.val + x_3.val, x_2.der + x_3.der)

def test_trig_mult_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + beta
    x_2 = tan(f)
    x_3 = cos(h)
    x_4 = x_2 * x_3
    assert (x_4.val, x_4.der) == (x_2.val * x_3.val, x_3.val*x_2.der + x_3.der*x_2.val)

def test_trig_sub_1():
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + beta
    x_2 = tan(f)
    x_3 = cos(h)
    x_4 = x_2 - x_3
    assert (x_4.val, x_4.der) == (x_2.val - x_3.val, x_2.der - x_3.der)

def test_trig_div_1():
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + beta
    x_2 = tan(f)
    x_3 = cos(h)
    x_4 = x_2 / x_3
    assert (x_4.val, x_4.der) == (x_2.val/x_3.val, (x_3.val*x_2.der - x_2.val*x_3.der)/(x_3.val**2))

## Exp
### Intended behavivor

def test_exp_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    x_2 = 2 * exponential(f) + 3
    assert (x_2.val, x_2.der) == (2196.266316856917, 4386.532633713834)

def test_exp_add_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + 5
    x_2 = 2 * exponential(f) + 3
    x_3 = exponential(h)
    x_4 = x_2 + x_3
    assert (x_4.val, x_4.der) == (x_2.val + x_3.val, x_2.der + x_3.der)

def test_exp_mult_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + 5
    x_2 = 2 * exponential(f) + 3
    x_3 = exponential(h)
    x_4 = x_2 * x_3
    assert (x_4.val, x_4.der) == (x_2.val * x_3.val, x_3.val*x_2.der + x_3.der*x_2.val)

def test_exp_sub_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + beta
    x_2 = 2 * exponential(f) + 3
    x_3 = exponential(h)
    x_4 = x_2 - x_3
    assert (x_4.val, x_4.der) == (x_2.val - x_3.val, x_2.der - x_3.der)

def test_exp_div_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + beta
    x_2 = 2 * exponential(f) + 3
    x_3 = exponential(h)
    x_4 = x_2 / x_3
    assert (x_4.val, x_4.der) == (x_2.val/x_3.val, (x_3.val*x_2.der - x_2.val*x_3.der)/(x_3.val**2))

## Powers
### Intended behavior

def test_pow_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x ** 2 + beta
    assert (f.val, f.der) == (11, 8)

def test_pow_add_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x ** 2 + beta
    h = 4 * y ** 2 + 5
    add_f = f + h
    assert (add_f.val, add_f.der) == (f.val + h.val, f.der + h.der)

def test_pow_mult_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x ** 2 + beta
    h = 4 * y ** 2 + 5
    mult_f = f * h
    assert (mult_f.val, mult_f.der) == (f.val * h.val, f.der*h.val + h.der*f.val)

def test_pow_sub_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x ** 2 + beta
    h = 4 * y ** 2 + 5
    sub_f = f - h
    assert (sub_f.val, sub_f.der) == (f.val - h.val, f.der - h.der)

def test_exp_div_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x ** 2 + beta
    h = 4 * y ** 2 + 5
    div_f = f / h
    assert (div_f.val, div_f.der) == (f.val/h.val, (h.val*f.der - f.val*h.der)/(h.val**2))


# Test trigo exp overloaded functions ==========

## Test radd
def test_trig_radd_1():
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + beta
    x_2 = 2
    x_3 = cos(h)
    x_4 = x_2 + x_3
    assert (x_4.val, x_4.der) == (x_2 + x_3.val, x_3.der)

## Test rmult
def test_trig_rmult_1():
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + beta
    x_2 = 2
    x_3 = cos(h)
    x_4 = x_2 * x_3
    assert (x_4.val, x_4.der) == (x_2 * x_3.val, x_2 * x_3.der)

## Test rsub
def test_trig_rsub_1():
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + beta
    x_2 = 2
    x_3 = cos(h)
    x_4 = x_2 - x_3
    assert (x_4.val, x_4.der) == (x_2 - x_3.val, -x_3.der)

## Test rdiv
def test_trig_rdiv_1():
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + beta
    x_2 = 2
    x_3 = cos(h)
    x_4 = x_2 / x_3
    assert (x_4.val, x_4.der) == (x_2 / x_3.val, (x_3.val * 0 - x_2 * x_3.der)/(x_3.val **2))

## Test rpow
def test_trig_rpow_1():
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    y = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + beta
    x_2 = 2
    x_3 = cos(h)
    x_4 = x_2 ** x_3
    power_derivative = 2 ** h.val * (0*h.val/2+(h.der*math.log(2)))
    assert (x_4.val, x_4.der) == (x_2 ** x_3.val, power_derivative)

## Test unintended behavior

## Test radd error
def test_trig_radd_error():
    with pytest.raises(AttributeError):
        a = 2.0  # Value to evaluate at
        x = autodiff(a)
        y = autodiff(a)
        alpha = 2.0
        beta = 3.0
        f = alpha * x + beta
        h = 4 * y + beta
        x_2 = "string"
        x_3 = cos(h)
        x_4 = x_2 + x_3


## Test rmult error
def test_trig_rmult_error():
    with pytest.raises(AttributeError):
        a = 2.0  # Value to evaluate at
        x = autodiff(a)
        y = autodiff(a)
        alpha = 2.0
        beta = 3.0
        f = alpha * x + beta
        h = 4 * y + beta
        x_2 = "string"
        x_3 = cos(h)
        x_4 = x_2 * x_3

## Test rsub error
def test_trig_rsub_error():
    with pytest.raises(AttributeError):
        a = 2.0  # Value to evaluate at
        x = autodiff(a)
        y = autodiff(a)
        alpha = 2.0
        beta = 3.0
        f = alpha * x + beta
        h = 4 * y + beta
        x_2 = "string"
        x_3 = cos(h)
        x_4 = x_2 - x_3

## Test rdiv error
def test_trig_rdiv_error():
    with pytest.raises(AttributeError):
        a = 2.0  # Value to evaluate at
        x = autodiff(a)
        y = autodiff(a)
        alpha = 2.0
        beta = 3.0
        f = alpha * x + beta
        h = 4 * y + beta
        x_2 = "string"
        x_3 = cos(h)
        x_4 = x_2 / x_3

## Test rpow error
def test_trig_rpow_error():
    with pytest.raises(AttributeError):
        a = 2.0  # Value to evaluate at
        x = autodiff(a)
        y = autodiff(a)
        alpha = 2.0
        beta = 3.0
        f = alpha * x + beta
        h = 4 * y + beta
        x_2 = "string"
        x_3 = cos(h)
        x_4 = x_2 ** x_3

## Test add error
def test_trig_add_error():
    with pytest.raises(AttributeError):
        a = 2.0  # Value to evaluate at
        x = autodiff(a)
        y = autodiff(a)
        alpha = 2.0
        beta = 3.0
        f = alpha * x + beta
        h = 4 * y + beta
        x_3 = "string"
        x_2 = cos(h)
        x_4 = x_2 + x_3


## Test mult error
def test_trig_mult_error():
    with pytest.raises(AttributeError):
        a = 2.0  # Value to evaluate at
        x = autodiff(a)
        y = autodiff(a)
        alpha = 2.0
        beta = 3.0
        f = alpha * x + beta
        h = 4 * y + beta
        x_3 = "string"
        x_2 = cos(h)
        x_4 = x_2 * x_3

## Test sub error
def test_trig_sub_error():
    with pytest.raises(AttributeError):
        a = 2.0  # Value to evaluate at
        x = autodiff(a)
        y = autodiff(a)
        alpha = 2.0
        beta = 3.0
        f = alpha * x + beta
        h = 4 * y + beta
        x_3 = "string"
        x_2 = cos(h)
        x_4 = x_2 - x_3

## Test div error
def test_trig_div_error():
    with pytest.raises(AttributeError):
        a = 2.0  # Value to evaluate at
        x = autodiff(a)
        y = autodiff(a)
        alpha = 2.0
        beta = 3.0
        f = alpha * x + beta
        h = 4 * y + beta
        x_3 = "string"
        x_2= cos(h)
        x_4 = x_2 / x_3

## Test pow error
def test_trig_pow_error():
    with pytest.raises(AttributeError):
        a = 2.0  # Value to evaluate at
        x = autodiff(a)
        y = autodiff(a)
        alpha = 2.0
        beta = 3.0
        f = alpha * x + beta
        h = 4 * y + beta
        x_3 = "string"
        x_2 = cos(h)
        x_4 = x_2 ** x_3

# Test autodiiff class =========================

# ax + b
def test_ax_b():
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    assert (f.val, f.der) == (7, 2)

# b + ax
def test_b_ax():
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = beta + alpha * x
    assert (f.val, f.der) == (7, 2)

# xa + b
def test_xa_b():
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = x*alpha + beta
    assert (f.val, f.der) == (7, 2)

# b + xa
def test_b_xa():
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = beta + x*alpha
    assert (f.val, f.der) == (7, 2)

# Test dummy class =============================

## add and radd
def test_dummy_add_1():
    f = dummy(1, 0)
    h = dummy(2, 2)
    d_obj = f + h
    assert (d_obj.val, d_obj.der) == (f.val + h.val, f.der + h.der)

def test_dummy_add_2():
    f = dummy(1, 0)
    h = 2
    d_obj = f + h
    assert (d_obj.val, d_obj.der) == (f.val + 2, f.der)

def test_dummy_radd_1():
    f = 2
    h = dummy(1, 0)
    d_obj = f + h
    assert (d_obj.val, d_obj.der) == (2 + h.val, h.der)

## sub and rsub
def test_dummy_sub_1():
    f = dummy(1, 0)
    h = dummy(2, 2)
    d_obj = f - h
    assert (d_obj.val, d_obj.der) == (f.val - h.val, f.der - h.der)

def test_dummy_sub_2():
    f = dummy(1, 0)
    h = 2
    d_obj = f - h
    assert (d_obj.val, d_obj.der) == (f.val - 2, f.der)

def test_dummy_rsub_1():
    f = 2
    h = dummy(1, 0)
    d_obj = f - h
    assert (d_obj.val, d_obj.der) == (2 - h.val, h.der)

## mul and rmul
def test_dummy_mul_1():
    f = dummy(1, 0)
    h = dummy(2, 2)
    d_obj = f * h
    assert (d_obj.val, d_obj.der) == (f.val * h.val, f.der*h.val + h.der*f.val)

def test_dummy_mul_2():
    f = dummy(1, 0)
    h = 2
    d_obj = f * h
    assert (d_obj.val, d_obj.der) == (f.val * 2, f.der * 2)

def test_dummy_rmul_1():
    f = 2
    h = dummy(1, 0)
    d_obj = f * h
    assert (d_obj.val, d_obj.der) == (2 * h.val, 2 * h.der)

## div and rdiv
def test_dummy_div_1():
    f = dummy(1, 0)
    h = dummy(2, 2)
    d_obj = f / h
    assert (div_f.val, div_f.der) == (f.val/h.val, (h.val*f.der - f.val*h.der)/(h.val**2))

def test_dummy_div_2():
    f = dummy(1, 0)
    h = 2
    d_obj = f / h
    assert (d_obj.val, d_obj.der) == (f.val / 2, f.der/2)

def test_dummy_rdiv_1():
    f = 2
    h = dummy(1, 2)
    d_obj = f * h
    assert (d_obj.val, d_obj.der) == (2/h.val, (h.val*0-2*h.der)/(h.val**2))

## pow and rpow
def test_dummy_pow_1():
    f = dummy(1, 0)
    h = dummy(2, 2)
    d_obj = f ** h
    power_derivative = f.val ** h.val * (f.der*h.val/f.val+(h.der*math.log(f.val)))
    assert (d_obj.val, d_obj.der) == (f.val ** h.val, power_derivative)

def test_dummy_pow_2():
    f = dummy(1, 0)
    h = 2
    d_obj = f ** h
    assert (d_obj.val, d_obj.der) == (f.val ** 2, 2*(f.val))

def test_dummy_rpow_1():
    f = 2
    h = dummy(1, 2)
    d_obj = f ** h
    power_derivative = 2 ** h.val * (0*h.val/2+(h.der*math.log(2)))
    assert (d_obj.val, d_obj.der) == (2 ** h.val, power_derivative)

# Jacobian tests ===============================

### example taken from https: // harvard - iacs.github.io / 2019 - CS207 / lectures / lecture10 / notebook /

## 2 functions 2 variables
### Intended behavior
# TODO: Will be available in final version

### Non-intended behavior
# TODO: Will be available in final version



# test_linear_div()
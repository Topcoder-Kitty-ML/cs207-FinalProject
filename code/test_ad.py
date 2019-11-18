import pytest
import trigo_exp
import vector_jacobian

# Elemental function tests ====================

## Linear
### Intended behavior
def test_linear_1(): #TEST 1
    a = 2.0  # Value to evaluate at
    x = x_simple(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    assert  (f.val, f.der) == (7.0, 2.0)

def test_linear_mult(): #TEST
    a = 2.0  # Value to evaluate at
    x = x_simple(a)
    y = x_simple(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + 5
    mult_f = f * h
    assert (mult_f.val, mult_f.der) == (f.val*h.val, f.val*h.der + f.der*h.val)

def test_linear_add(): #TEST
    a = 2.0  # Value to evaluate at
    x = x_simple(a)
    y = x_simple(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + 5
    add_f = f + h
    assert (add_f.val, add_f.der) == (f.val + h.val, f.der + h.der)

### Non-intended behavior

## Trig
### Intended behavior
def test_sin_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = x_simple(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    x_2 = sin(f)
    assert (x_2.val, x_2.der) == (0.6569865987187891, 1.5078045086866092)

def test_cos_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = x_simple(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    x_2 = cos(f)
    assert (x_2.val, x_2.der) == (0.7539022543433046, -1.3139731974375781)

def test_tan_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = x_simple(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    x_2 = tan(f)
    assert (x_2.val, x_2.der) == (0.8714479827243188, 3.5188431731885697)

def test_trig_add_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = x_simple(a)
    y = x_simple(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + beta
    x_2 = tan(f)
    x_3 = tan(h)
    x_4 = x_2 + x_3
    assert (x_4.val, x_4.der) == (x_2.val + x_3.val, x_2.der + x_3.der)

def test_trig_mult_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = x_simple(a)
    y = x_simple(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + beta
    x_2 = tan(f)
    x_3 = tan(h)
    x_4 = x_2 * x_3
    assert (x_4.val, x_4.der) == (x_2.val * x_3.val, x_3.val*x_2.der + x_3.der*x_2.val)

### Non-intended behavior

## Exp
### Intended behavivor

def test_exp_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = x_simple(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    x_2 = 2 * exponential(f) + 3
    assert (x_2.val, x_2.der) == (2196.266316856917, 4386.532633713834)

def test_exp_add_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = x_simple(a)
    y = x_simple(a)
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
    x = x_simple(a)
    y = x_simple(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    h = 4 * y + 5
    x_2 = 2 * exponential(f) + 3
    x_3 = exponential(h)
    x_4 = x_2 * x_3
    assert (x_4.val, x_4.der) == (x_2.val * x_3.val, x_3.val*x_2.der + x_3.der*x_2.val)


### Non-intended behavior

## Powers
### Intended behavior

def test_pow_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = x_simple(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x ** 2 + beta
    assert (f.val, f.der) == (11, 8)

def test_pow_add_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = x_simple(a)
    y = x_simple(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x ** 2 + beta
    h = 4 * y ** 2 + 5
    add_f = f + h
    assert (add_f.val, add_f.der) == (f.val + h.val, f.der + h.der)

def test_pow_mult_1(): #TEST
    a = 2.0  # Value to evaluate at
    x = x_simple(a)
    y = x_simple(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x ** 2 + beta
    h = 4 * y ** 2 + 5
    mult_f = f * h
    assert (mult_f.val, mult_f.der) == (f.val * h.val, f.der*h.val + h.der*f.val)

### Non-intended behavior

# Jacobian tests ===============================

## example taken from https: // harvard - iacs.github.io / 2019 - CS207 / lectures / lecture10 / notebook /
## 2 functions 2 variables
### Intended behavior
# TODO
    x = 2
    y = 4
    vector = [x_simple(x)*x_simple(y) + sin(x_simple(x)),\
              x_simple(x)+x_simple(y) + sin(x_simple(x)*x_simple(y))]
    vals_dict = {"x": 2, "y": 4}
    assert get_jp_matrix(vector, vals_dict) ==

### Non-intended behavior

from vector_jacobian import *

# JacobianProduct class tests ====================

## Linear
### Intended behavior
def test_linear_1(): #TEST 1
    a = 2.0  # Value to evaluate at
    x = autodiff(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    assert  (f.val, f.der) == (7.0, 2.0)


import pytest
import math
from genericdiff import *

## test partial
def test_partial_1():
    f = lambda x, y: x**2 - y**3
    h = lambda x, y: x**3 + y**3
    function_vector = [f, h]
    jp_object = JacobianProduct(function_vector)
    # inputs are x = {1, 2, 3} and y = 0 (you can hold y constant at any value)
    inputs = [[1, 2, 3], 0]
    # getting partial with respect to x (position 0 in lambdas)
    partial_wrt_x = jp_object.partial_ders(wrt=0, inputs=inputs)
    # output is [[df/dx(1), df/dx(2), df/dx(3)], dh/dx(1), dh/dx(2), dh/dx(3)]]
    assert  partial_wrt_x == [[2, 4, 6], [3, 12, 27]]

def test_partial_2():
    f = lambda x, y: x**2 - y**3
    h = lambda x, y: x**3 + y**3
    function_vector = [f, h]
    jp_object = JacobianProduct(function_vector)
    # inputs are x = {1, 2, 3} and y = 0 (you can hold y constant at any value)
    inputs = [[1, 2, 3], 0]
    # getting partial with respect to x (position 0 in lambdas)
    partial_wrt_x = jp_object.partial_vals(wrt=0, inputs=inputs)
    # output is [[df/dx(1), df/dx(2), df/dx(3)], dh/dx(1), dh/dx(2), dh/dx(3)]]
    assert  partial_wrt_x == [[1, 4, 9], [1, 8, 27]]

## test jp
def test_jp_1():
    f = lambda x, y: x**2 - y**3
    h = lambda x, y: x**3 + y**3
    function_vector = [f, h]
    jp_object = JacobianProduct(function_vector)
    # inputs are x = {1, 2, 3} and y = {1, 2, 3}
    # this means we will calculate derivatives for
    # (1, 1), (2, 2), and (3, 3)
    inputs = [[1, 2, 3], [1, 2, 3]]
    # getting jp matrix with respect to all variables
    jp_matrix = jp_object.jacobian_product(inputs)
    # output is a list of 3 jacobian matrices:
    # an array  for (1, 1),
    # an array for (2, 2),
    # an array for (3, 3)
    #
    # [
    # np.array([[df/dx(1), df/dy(1)],
    #           [dh/dx(1), dh/dy(1)]]),
    # np.array([[df/dx(2), df/dy(2)],
    #           [dh/dx(2), dh/dy(2)]]),
    # np.array([[df/dx(3), df/dy(3)],
    #           [dh/dx(3), dh/dy(3)]])
    # ]
    #
    matrix_1 = np.array([[2,-3],[3, 3]])
    matrix_2 = np.array([[4, -12],[12, 12]])
    matrix_3 = np.array([[6, -27],[27, 27]])
    print(jp_matrix)
    assert  np.all(jp_matrix[0] == matrix_1) and np.all(jp_matrix[1] == matrix_2) and np.all(jp_matrix[2] == matrix_3)

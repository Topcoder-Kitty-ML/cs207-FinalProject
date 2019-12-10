from genericdiff import *

f = lambda x, y: x**2 - y**3
h = lambda x, y: x**3 + y**3

function_vector = [f, h]
jp_object = JacobianProduct(function_vector)

# inputs are x = {1, 2, 3} and y = {1, 2, 3}
# this means we will calculate jacobian products for
# (1, 1), (2, 2), and (3, 3)

inputs = [[1, 2, 3], [1, 2, 3]]

# getting jp matrix with respect to all variables
jp_matrix = jp_object.jacobian_product(inputs)

print(jp_matrix)
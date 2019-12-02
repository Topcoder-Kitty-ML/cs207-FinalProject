# import all necessary packages
from inspect import signature

def _partial(fun, inputs, wrt):
    raise NotImplementedError

class JacobianProduct:
    """
    Takes in a function vector and allows user to calculate partials or the full jacobian product based on
    values specified by the user

    This class will only take a vector of functions that have the SAME number of inputs that are in the
    SAME order. If the functions do not pass this check during class construction, InvalidFunctionsError is
    raised.

    The input should look like the following:

    f = lambda x, y: cos(x) + sin(y)
    h = lambda x, y: x + y
    function_vector = [f, h]
    jp_object = JacobianProduct(function_vector)

    The class has various methods:
    -partial()
        This method can calculate a partial for one function in the object or for all functions.
        The variable value inputs are specified in inputs. For example:

        inputs = [[1, 2, 3], 0] # x = 1, 2, 3 and y = 0
        # this evaluates the partial at all values of x holding y constant
        # returns a list of partial derivative evals for each function
        # wrt sets the variable to calculate the partial
        list_of_partials = jp_object.partial(wrt=0, inputs=inputs)

        [[2.4, 3.5, 2.5], [1, 2, 3]]

    -jacobian_product()
        This method calculates the jacobian product it either:
        takes in one value for each variable or multiple values for each input BUT the number of values
         for each variable must be the same. Calculates a separate jacobian for each element in the input vectors.

         inputs = [[1, 2, 3], [1, 2, 3]] # calculates 3 jacobian products: (1, 1), (2, 2), and (3, 3)
         list_of_jp_matrices = jp_object.jacobian_product(inputs=inputs)

        [ [[df/dx, df/dy],
         [dh/dx, dh/dy]],

         for (2,2),
         for (3,3)]

    """
    def __init__(self, function_vector):
        raise NotImplementedError

    def __repr__(self):
        #prints out functions

    def partial(self, wrt, inputs, fun_idx=-1):
        # check to see if input is singular for constants
        # convert scalar values to lists if not already in list form
        for idx, value in enumerate(inputs):
            if not isinstance(value, list):
                inputs[idx] = list(value)

        for idx, value in enumerate(inputs):
            if idx == wrt:


        # get partial

    def jacobian_product(self, inputs, fun_idx=-1):
        # check that all inputs have the same length

    def fun_map(self):

    def var_map(self):
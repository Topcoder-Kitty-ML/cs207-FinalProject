# import all necessary packages
from inspect import signature
import numpy as np

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
        self.function_vector = function_vector

        # runs a check on whether the function vector's functions all have
        # a) the same number of variables and
        # b) the same variables in the same order

        function_signature = None
        for function in self.function_vector:
            if function_signature:
                function_signature_c = signature(function)
                if function_signature_c == function_signature:
                    continue
                else:
                    raise AttributeError("Functions in the function vector must contain \n\
                                         the same number of variables in the same order with the same names.")
            if not function_signature:
                function_signature = signature(function)
        self.function_signature = function_signature

    def __repr__(self):
        #prints out functions
        raise NotImplementedError

    def input_format_check(self, inputs):
        # make sure all elements in inputs are lists
        # for example [[1,2,3],0] becomes [[1,2,3],[0]]
        for idx, element in enumerate(inputs):
            if not isinstance(element, list):
                inputs[idx] = list(element)
        return inputs

    def subset_functions(self, function_vector, fun_idx):
        if fun_idx == -1:
            return function_vector
        else:
            if not ifisinstance(fun_idx, list):
                fun_idx = list(fun_idx)

            subsetted_funs = [fun for idx, fun in enumerate(function_vector) if idx in fun_idx]
            return subsetted_funs

    def partial(self, wrt, inputs, fun_idx=-1):
        # make sure all elements in puts are lists
        inputs = self.input_format_check(inputs)

        # get number of inputs required from function signature
        n_inputs = len(self.function_signature.parameters)

        # check to see if input is of length one for constant values
        # check to see if input is of non-zero length for variable values
        for input in range(0, n_inputs):
            if input == wrt:
                if len(self.function_vector[input]) <= 0:
                    raise AttributeError("Input vector for your wrt variable needs to be of non-zero length.")
            else:
                if len(self.function_vector[input]) != 1:
                    raise AttributeError("Inputs for the variables you are holding constant need to be of length 1.")

        # convert wrt variable inputs to Var object
        # to differentiate
        diff_inputs = inputs.copy()
        for idx, value in enumerate(diff_inputs[wrt]):
            diff_inputs[wrt][idx] = Var(value)

        # create input vals list
        input_vals_list = []
        for input_wrt in diff_inputs[wrt]:
            input_vals_entry = []
            for idx, value in enumerate(diff_inputs):
                if idx == wrt:
                    input_vals_entry[idx] = input_wrt
                else:
                    input_vals_entry[idx] = diff_inputs[idx][0]
            input_vals_list.append(input_vals_entry)

        # create functions list
        diff_fun_vector = self.subset_functions(self.function_vector, fun_idx)

        # get partials given input vals list
        partials_list = []
        for function in diff_fun_vector:
            function_partials_list = []
            for input_vals in input_vals_list:
                partial_entry = function(*input_vals).der
                function_partials_list.append(partial_entry)
            partials_list.append(function_partials_list)

        # return the partials list
        # this a list of lists such that you can access the value for each function for each variable value
        # e.g. to access function 0 at variable value 1 from the inputs vector write out partials_list[0][1]
        return partials_list

    def jacobian_product(self, inputs, fun_idx=-1):
        # make sure all inputs are lists
        inputs = self.input_format_check(inputs)

        # make sure all inputs are non-zero length and are of the same length
        # if inputs are not, then return AttributeError
        input_length = None
        for input in inputs:
            # non zero length
            if len(input) <= 0:
                raise AttributeError("All input values for each variable must be non zero in length")

            if not input_length:
                input_length = len(input)
            else:
                input_length_c = len(input)
                if input_length != input_length_c:
                    raise AttributeError("Lengths of all input values for each variable must be the same")

        # create input_vals_list
        input_vals_list = []
        vals_list_length = len(inputs[0])
        for i in range(0, vals_list_length):
            input_vals_entry = []
            for j, variable in enumerate(inputs):
                input_vals_entry[j] = variable[i]
            input_vals_list.append(input_vals_entry)

        # instantiate jacobian list
        jp_list = []

        # calculate the jacobian product for each set of input values
        for input_vals in input_vals_list:
            # instantiate new jacobian matrix
            row_n = len(self.subset_functions(self.function_vector, fun_idx))
            col_n = len(self.function_signature.parameters)
            jp_array = np.empty((row_n, col_n))

            # for each variable calculate partials
            for wrt_idx in range(0, len(self.function_signature.parameters)):
                partials = self.partial(wrt_idx, input_vals, fun_idx)
                for function_idx, value in enumerate(partials):
                    # fill in the matrix with partials
                    jp_array[function_idx, wrt_idx] = partials[function_idx][0]

            # append the jp_array for current set of input_vals to jp_list
            jp_list.append(jp_array)

        # return list of jacobians
        return jp_list

    def fun_map(self):
        raise NotImplementedError

    def var_map(self):
        raise NotImplementedError
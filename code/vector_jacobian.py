from trigo_exp import *
from linear import AutoDiffToy as autodiff

class JacobianProduct:
    """
    For vector functions, the output of autodifferentiation in the forward mode
    is the Jacobian-product matrix - that is the partial derivatives multiplied by seed matrices.
    Each row corresponds to a function's partial derivative products and each column
    corresponds to a specific variable (x, y, z, etc.).
    The output should be a matrix of size [m functions X p variables]

    m is specified by the vector of autodiff objects (contained in a list)
    p variables are specified by the total number of variables in ALL functions in the vector

    input:

    - vector of autodiff objects

    methods that return:
    - get_variable_dict(): dictionary mapping column index p with variable
    - get_function_dict(): dicitionary mapping row index m with autodiff object
    - get_jp_matrix(): jacobian product matrix

    GOODTOHAVE - method to extract specific function sub- matrix or specific
    variable sub-matrix from jacobian product matrix
    """

    # constructor accepts a vector (list) of autodiff objects
    # accepts a dictionary of variable_values
    # TODO raise an error if variable dictionary does not have all variables in functions
    def __init__(self, vector, variable_vals):
        self.vector = vector
        self.variable_vals = variable_vals

    # maps variables to columns in matrix
    # I assume that the autodiff object generates
    # a dictionary of variables
    def get_variable_dict(self):
        var_list = list(self.variable_vals.keys())
        self.variable_dict = dict(enumerate(var_list))
        return self.variable_dict

    def get_function_dict(self):
        self.function_dict = dict(enumerate(self.vector))
        return self.function_dict

    def get_jp_matrix(self):
        # Determine variable column mapping
        var_column_map = self.get_variable_dict(self.variable_vals)
        # Determine function row mapping
        fun_row_map = self.get_function_dict
        # Evaluate each function with respect to variables in the function
        # and then create matrix - each row corresponds to a function's evaluation
        jp_matrix = []
        for obj in fun_row_map.values():
            # limit variables to only the ones relevant to the function
            # asume variable names stored in vars attribute of the autodiff object
            variable_vals_fun = [var for var in variable_vals if var in obj.vars]
            # should output a vector of derivatives based on values in
            # variable vals vector
            jp_matrix_row = obj(variable_vals_fun).der
            jp_matrix.append(jp_matrix_row)
        # conver to np array
        self.jp_matrix = np.asarray(jp_matrix)
        return self.jp_matrix

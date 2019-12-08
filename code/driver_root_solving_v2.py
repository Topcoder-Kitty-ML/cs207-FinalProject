# from linear import AutoDiffToy as x_simple
# from dummy import dummy
# from trigo_exp import *

from autodiff_module import *

def function_to_optimize(x_val = 2):
	# Define the x
	x = autodiff(x_val)

	# Define the function
	# func = x * x * x

	func = sin(x) - x * x * cos(x) ** 2 - 3 + tan(2 * x)

	return func


def optimize_and_get_root(initial_val, \
	learning_rate=0.1, stopping_threshold = 10 ** (-6)):
	new_x = initial_val
	f_val = ""
	f_der = ""
	while True:
		#print("-=-=-=-")
		curr_x = new_x
		f = function_to_optimize(x_val = curr_x)
		new_x = curr_x - learning_rate * float(f.val / f.der)
		f_val = f.val
		f_der = f.der
		#print(new_x)
		if abs(curr_x - new_x) < stopping_threshold:
			#print("The value of x is :%s, and the f(x) is: %s" %(new_x, f.val))
			break
	return new_x, f_val, f_der



reqr_func = function_to_optimize(x_val=2)
x_soln, f_val, f_der = optimize_and_get_root(3)


print("Optimal root: %s" %x_soln)
print("Function val: %s" %f_val)
print("Function derivative: %s" %f_der)




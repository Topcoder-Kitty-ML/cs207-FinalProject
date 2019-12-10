from genericdiff import *

# this gets the jacobian product for two variables
# using the JacobianProduct class and the partials methods

func = lambda x, y: sin(x) - x * x * cos(x) ** 2 - 3 + tan(2 * x) + y
# initialize jp object with function
jp_object = JacobianProduct([func])

def optimize_and_get_root(initial_val, variable_wrt, \
	learning_rate=0.1, stopping_threshold = 10 ** (-6)):

	new_x = initial_val
	f_val = ""
	f_der = ""
	while True:
		#print("-=-=-=-")
		curr_x = new_x
		inputs = [0, 0]
		inputs[variable_wrt] = curr_x
		value = jp_object.partial_vals(variable_wrt, inputs) [0][0]
		derivative = jp_object.partial_ders(variable_wrt, inputs) [0][0]
		new_x = curr_x - learning_rate * float(value / derivative)
		f_val = value
		f_der = derivative
		#print(new_x)
		if abs(curr_x - new_x) < stopping_threshold:
			#print("The value of x is :%s, and the f(x) is: %s" %(new_x, f.val))
			break
	return new_x, f_val, f_der


x_soln, f_val, f_der = optimize_and_get_root(initial_val=3, variable_wrt=0)
y_soln, f_val, f_der = optimize_and_get_root(initial_val=3, variable_wrt=1)


print(f"Optimal root: ({x_soln}, {y_soln})")
print("Function val: %s" %f_val)
print("Function derivative: %s" %f_der)

from linear import AutoDiffToy as x_simple
from dummy import dummy
from trigo_exp import *

a = 2.0 # Value to evaluate at
x = x_simple(a)
print(x)


# f_1 = 2 * sin(x) - cos(2 * x)
# print(f_1.val, f_1.der)



# f_1 = 2 * sin(x) - cos(x)
# print(f_1.val, f_1.der)


# f_1 = sin(x) + cos(x)
# print(f_1.val, f_1.der)

f_1 = 2 * x - x 
f_2 = f_1 * 2
print(f_1.val, f_1.der)
print(f_2.val, f_2.der)

f_3 = x * x * x
print(f_3.val, f_3.der)

learning_rate = 0.01
stopping_threshold = 10 ** (-6)


# Root finding code
# curr_x = 2.0
# x = x_simple(curr_x)
# f_3 = x * x * x
# new_x = curr_x - float(f_3.val / f_3.der)
# print(new_x)

# while True:
# 	curr_x = new_x
# 	x = x_simple(curr_x)
# 	f_3 = x * x * x
# 	new_x = curr_x - float(f_3.val / f_3.der)
# 	print(new_x)
# 	if abs(curr_x - new_x) < stopping_threshold:
# 		print("The value of x is :%s, and the f(x) is: %s" %(new_x, f_3.val))
# 		break


print(x)
print("-------")

f = x * x * x
print(x.a)
print(f.val, f.der)

x.a = 5
print(f.val, f.der)
print(x.a)

f = x * x * x
print(f.val, f.der)
print(x.a)

print(x.a)
f_1 = x * x * x
print(x)
print(f_1.val, f_1.der)
print(x.a)



def function_to_optimize(x_val = 2):
	# Define the x
	x = x_simple(x_val)

	# Define the function
	func = x * x * x

	return func


def optimize_and_get_root(initial_val, learning_rate=0.1):
	new_x = initial_val
	f_val = ""
	f_der = ""
	while True:
		#print("-=-=-=-")
		curr_x = new_x
		f = function_to_optimize(x_val = curr_x)
		new_x = curr_x - float(f.val / f.der)
		f_val = f.val
		f_der = f.der
		#print(new_x)
		if abs(curr_x - new_x) < stopping_threshold:
			#print("The value of x is :%s, and the f(x) is: %s" %(new_x, f.val))
			break
	return new_x, f_val, f_der


reqr_func = function_to_optimize(x_val=2)
print("-----")
print(reqr_func.der)
x_soln, f_val, f_der = optimize_and_get_root(3)

print(x_soln, f_val, f_der)



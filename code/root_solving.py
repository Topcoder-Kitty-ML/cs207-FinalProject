from linear import AutoDiffToy as x_simple
from dummy import dummy
from trigo_exp import *

a = 2.0 # Value to evaluate at
x = x_simple(a)


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

curr_x = 2.0
x = x_simple(curr_x)
f_3 = x * x * x
new_x = curr_x - float(f_3.val / f_3.der)
print(new_x)

while True:
	curr_x = new_x
	x = x_simple(curr_x)
	f_3 = x * x * x
	new_x = curr_x - float(f_3.val / f_3.der)
	print(new_x)
	if abs(curr_x - new_x) < stopping_threshold:
		print("The value of x is :%s, and the f(x) is: %s" %(new_x, f_3.val))
		break

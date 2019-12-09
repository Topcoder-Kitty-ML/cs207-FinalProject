#!/usr/bin/env python


# Performs optimization of the RNA velocity
# equation

import numpy as np
import random
import sys
from functions import *
#from code.autodiff_module import *
sys.path.append('../../code/')
from autodiff_module import *
from vector_jacobian import *
from functions import calc_u as u_t
from functions import calc_s as s_t

def cell():
	'''
	'''
	def __init__(self, time, index, alpha, gamma):
		self.time = time
		self.index = index
		# self.alpha = alpha
		# self.gamma = gamma
		self.spliced_velocity
		self.unspliced_velocity




# def calc_euclidian_distance(vector1, vector2):
# 	'''
# 	Calculate the euclidean distance between
# 	two input vectors
# 	'''

# 	dist = np.linalg.norm(a-b)
	
# 	return dist


def calc_euclidian_distance(vector1, vector2):
	'''
	Calculate the euclidean distance between
	two input vectors. This implementation
	allows us to calculate the derivative of this
	function
	'''

	total_dist = 0
	for i in range(len(vector1)):
		dist_curr = (vector1[i] - vector2[i]) ** 2
		total_dist = total_dist + dist_curr

	dist = total_dist ** 0.5

	return dist


def calc_loss_func(present_cell, future_cell):
	'''
	Calculate the loss function between the
	present cell and a future cell. We assume
	that the state of a future cell can be predicted
	based on the current cell 
	'''

	time_diff = future_cell.time - present_cell.time
	predicted_future_cell = calc_predicted_future_state(present_cell.velocity, time_diff)

	loss = calc_euclidian_distance(future_cell, predicted_future_cell)

	return loss


def calc_predicted_future_state(present_cell, currstate, velocity, delta_t):
	'''
	Calculate the predicted future state
	of the cell based on the current state,
	the velocity and the timestep, delta_t

	Here, we assume that the future state of
	a cell can be approximated by its current
	state, plus the velocity component multiplied
	by the delta_t.
	'''

	future_state = currstate + velocity * delta_t

	return future_state


def sort_cells_by_ascending_time(multiple_cells):
	pass



def calc_overall_loss_func(all_cells):
	'''
	Calculate the overall loss function

	TO CLEAN UP!!!!
	'''

	# Sort all the cells by time
	sorted_cells = sort_cells_by_ascending_time(multiple_cells)

	total_loss = 0

	for i in range(len(sorted_cells) - 1):
		present_cell = sorted_cells[i]
		future_cell = sorted_cells[i+1]
		curr_loss = calc_loss_func(present_cell, future_cell)

		total_loss += curr_loss


	return total_loss


def optimize_alpha():
	pass


def optimize_gamma():
	pass


def optimize_time():
	'''
	Optimize the best time values for the cells

	'''
	pass





# Read data in
data = np.load("processed_data/norm_filtered_cells.pickle")
print(data.shape) # type x genes x cells
num_cells = data.shape[2]
num_genes = data.shape[1]


# Randomize the time values (Time values are in per 10^6 scale)
time_cell = [ x / 1000000 for x in range(num_cells)]

# Shuffle the time values between cells
random.shuffle(time_cell)

# Get index sorted from smallest to largest
idx = np.argsort(time_cell)
print(idx)

# initial_cell_index = time_cell.index(0)
initial_cell_index = idx[0]
print(initial_cell_index)


# Randomize the alpha and gamma values
# for each gene
alpha_vals = [random.random() for i in range(num_genes)]
gamma_vals = [random.random() for i in range(num_genes)]



# print(alpha_vals)
# print(gamma_vals)


# Get the indices of the cells based on
# ordered temporal ordering
##########
# CHECK!!!! I think this should work
##########
# order_cell_index = range(num_cells)[time_cell]



# Approach 2

def optimization_function(data, alpha, gamma):
	# Do this for a single gene first
	curr_gene_idx = 100

	s_0 = data[0][curr_gene_idx][initial_cell_index]
	u_0 = data[1][curr_gene_idx][initial_cell_index]


	unspliced_vals_predicted = []
	spliced_vals_predicted = []
	unspliced_vals_actual = []
	spliced_vals_actual = []
	for i in range(len(idx)):
		# print(i)
		curr_index = idx[i]

		# Curr index
		alpha = alpha_vals[curr_index]
		gamma = gamma_vals[curr_index]
		t_curr = time_cell[curr_index]

		# Predicted values based on equations
		u_t = calc_u(alpha, u_0, t_curr)
		s_t = calc_s(alpha, gamma, u_0, s_0, t_curr)

		# Actual state at t
		u_t_actual = data[0][100][curr_index]
		s_t_actual = data[1][100][curr_index]
		# print(u_t, s_t)
		# print(u_t_actual, s_t_actual)

		unspliced_vals_predicted.append(u_t)
		spliced_vals_predicted.append(s_t)
		unspliced_vals_actual.append(u_t_actual)
		spliced_vals_actual.append(s_t_actual)


	# Combine the list
	vals_predicted = unspliced_vals_predicted + spliced_vals_predicted
	vals_actual = unspliced_vals_actual + spliced_vals_actual


	# print(len(vals_predicted ))

	dist = calc_euclidian_distance(vals_predicted, vals_actual)
	return dist




# function_vector = [optimization_function]
# jp_object = JacobianProduct(function_vector)

# inputs = [data, alpha_vals, gamma_vals]
# # getting partial with respect to x (position 0 in lambdas)
# partial_wrt_x = jp_object.partial(wrt=1, inputs=inputs)
# print(partial_wrt_x)






euclidean_distance = lambda u_t, s_t, u_t_actual, s_t_actual: sqrt((u_t - u_t_actual)**2 + (s_t - s_t_actual)**2)
# where u_t is a function defined above,
# where s_t is a function defined above,
# u_t_actual is a data point, 
# s_t_actual is a data point

# Now combine them into final function that makes explicit what are variables (these can be your differentiating variables of interest but also your variable inputs):
combined = lambda alpha, gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual:\
euclidean_distance(u_t(alpha, u_0, t_curr), s_t(alpha, gamma, u_0, s_0, t_curr), u_t_actual, s_t_actual)


# Then make a jacobian product class
jp_object = JacobianProduct([combined])


# get jp matrix with respect to alpha
# alpha = list of alpha values
# gamma = list of gamma values
# u_0 = list of u 0 values
# s_0 = list of s 0 values
# t_curr = list of t curr values
# u_t_actual = list of u_t_actual values
# s_t_actual = list of s_t_actual values

curr_gene_idx = 100
curr_index = 189

s_0 = data[0][curr_gene_idx][initial_cell_index]
u_0 = data[1][curr_gene_idx][initial_cell_index]
alpha = alpha_vals[curr_index]
gamma = gamma_vals[curr_index]
t_curr = time_cell[curr_index]
u_t_actual = data[0][curr_gene_idx][curr_index]
s_t_actual = data[1][curr_gene_idx][curr_index]


# alpha = list of alpha values
# gamma = list of gamma values
# u_0 = list of u 0 values
# s_0 = list of s 0 values
# t_curr = list of t curr values
# u_t_actual = list of u_t_actual values
# s_t_actual = list of s_t_actual values
inputs = [alpha, gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual] # in the same order in which we defined the python variables in the combined function


#this will loop through each input in inputs from 0 to length(alpha). Note that all input vectors need to be the same length.
jp_matrix = jp_object.jacobian_product(inputs)














	# print("Time===")
	# print(t_curr)






# # Create the function vector
# function_vector_unspliced = []
# for i in range(len(idx) - 1):
# 	print(i)
# 	curr_index = idx[i]
# 	future_index = idx[i+1]

# 	print(curr_index, future_index)

# 	# Curr index
# 	alpha = alpha_vals[curr_index]
# 	gamma = gamma_vals[curr_index]
# 	t_curr = time_cell[curr_index]

# 	# Future index
# 	t_future = time_cell[future_index]

# 	print("Time===")
# 	print(t_curr, t_future)


	# Calc predicted "spliced"

	# Calc predicted "unspliced"


	# calc_predicted_future_state(present_cell, currstate, velocity, delta_t)


	# # Get the distance values for each gene

	# distance_splice = calc_euclidian_distance
	# distance_unspliced = 

	# distance_total = distance_splice + distance_unspliced

	# # Add each distance value for each gene to
	# # the vector.
	# function_vector_unspliced.append(distance_total)





# calc_du_dt(alpha, u_t)


# # Overall loss function
# # func --> loss func of each pair of cells in time

# # Loss func of each pair of cells
# # func --> predicted future state of cell from current cell (variable)
# #      --> actual future state of cell (constant from raw data)

# # Predicted future state of cell
# # func --> current state of cell
# #      --> velocity of cell
# #      --> time difference between cell

# # velocity of cell
# # func --> alpha
# #      --> gamma
# #      --> u_t
# #      --> s_t

# # u_t
# # func --> alpha (var)
# #      --> u_0 (const)
# #      --> t (non-diff var)

# # s_t
# # func --> alpha (var)
# #      --> gamma (var)
# #      --> u_0 (constant)
# #      --> s_0 (constant)
# #      --> t (non-diff var)

# # Generate the function vector needed for
# # optimization of the data
# f = lambda x, y: cos(x) + sin(y)
# h = lambda x, y: x + y
# function_vector = [f, h]


# jp_object = JacobianProduct(function_vector)


# # Actual code
# f = lambda x,y: sin(x) + sin(y)
# h = lambda f: sin(f)
# g = lambda h, m: h + m

# combined = lambda x, y, m: g(h(f(x, y)), m)

# jp = JacobianProduct([combined])
# jp.partial(wrt=0, inputs=[[1, 2, 3], 0, 0]) #wrt refers to first variable for diff





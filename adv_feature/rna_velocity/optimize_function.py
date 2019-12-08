#!/usr/bin/env python


# Performs optimization of the RNA velocity
# equation

import numpy as np
import random



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
	for i in len(vector1):
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
data = np.load("norm_filtered_cells.pickle")
num_cells = data.shape()[2]
num_genes = data.shape()[1]


# Randomize the time values
time_cell = range(num_cells)
time_cell_random = random.shuffle(time_cell)
initial_cell_index = time_cell_random.index(0)


# Randomize the alpha and gamma values
# for each gene
alpha_vals = [random.random() for i in range(num_cells)]
gamma_vals = [random.random() for i in range(num_cells)]


# Get the indices of the cells based on
# ordered temporal ordering
##########
# CHECK!!!! I think this should work
##########
order_cell_index = range(num_cells)[time_cell_random]



# Create the function vector
function_vector_unspliced = []
for i in range(len(order_cell_index) - 1):
	curr_index = order_cell_index[i]
	future_index = order_cell_index[i+1]

	# Curr index
	alpha = alpha_vals[curr_index]
	gamma = gamma_vals[curr_index]
	t = time_cell_random[curr_index]

	# Future index
	t = time_cell_random[future_index]


	calc_predicted_future_state(present_cell, currstate, velocity, delta_t)


	# Get the distance values for each gene

	distance_splice = calc_euclidian_distance
	distance_unspliced = 

	distance_total = distance_splice + distance_unspliced

	# Add each distance value for each gene to
	# the vector.
	function_vector_unspliced.append(distance_total)





=======

# Overall loss function
# func --> loss func of each pair of cells in time

# Loss func of each pair of cells
# func --> predicted future state of cell from current cell (variable)
#      --> actual future state of cell (constant from raw data)

# Predicted future state of cell
# func --> current state of cell
#      --> velocity of cell
#      --> time difference between cell

# velocity of cell
# func --> alpha
#      --> gamma
#      --> u_t
#      --> s_t

# u_t
# func --> alpha (var)
#      --> u_0 (const)
#      --> t (non-diff var)

# s_t
# func --> alpha (var)
#      --> gamma (var)
#      --> u_0 (constant)
#      --> s_0 (constant)
#      --> t (non-diff var)

# Generate the function vector needed for
# optimization of the data
f = lambda x, y: cos(x) + sin(y)
h = lambda x, y: x + y
function_vector = [f, h]


jp_object = JacobianProduct(function_vector)
=======
jp_object = JacobianProduct(function_vector)


# Actual code
f = lambda x,y: sin(x) + sin(y)
h = lambda f: sin(f)
g = lambda h, m: h + m

combined = lambda x, y, m: g(h(f(x, y)), m)

jp = JacobianProduct([combined])
jp.partial(wrt=0, inputs=[[1, 2, 3], 0, 0]) #wrt refers to first variable for diff





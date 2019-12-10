
# Performs optimization of the RNA velocity
# equation

import numpy as np
import random
import sys
sys.path.append('../../')
from genericdiff import *

from functions import calc_u as u_t
from functions import calc_s as s_t



# Read data in
data = np.load("processed_data/norm_filtered_cells.scaled.pickle", allow_pickle=True)
num_cells = data.shape[2]
num_genes = data.shape[1]


# Randomize the time values (Time values are in per 10^6 scale)
time_cell = [ x / 1000000 for x in range(num_cells)]

random.seed(1234)

# Shuffle the time values between cells
random.shuffle(time_cell)

# Get index sorted from smallest to largest
idx = np.argsort(time_cell)

# initial_cell_index = time_cell.index(0)
initial_cell_index = idx[0]


# Randomize the alpha and gamma values
# for each gene
alpha_vals = [random.random() for i in range(num_genes)]
gamma_vals = [random.random() for i in range(num_genes)]



# Euclidean distance lambda function
euclidean_distance = lambda u_t, s_t, u_t_actual, s_t_actual: sqrt((u_t - u_t_actual)**2 + (s_t - s_t_actual)**2)


# Now combine them into final function that makes explicit what are variables (these can be your differentiating variables of interest but also your variable inputs):
combined = lambda alpha, gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual:\
euclidean_distance(u_t(alpha, u_0, t_curr), s_t(alpha, gamma, u_0, s_0, t_curr), u_t_actual, s_t_actual)


# Then make a jacobian product class
jp_object = JacobianProduct([combined])



# for i in range(num_genes):
curr_gene_idx = 110
curr_cell_index = 180

s_0 = data[0][curr_gene_idx][initial_cell_index]
u_0 = data[1][curr_gene_idx][initial_cell_index]
alpha = alpha_vals[curr_gene_idx]
gamma = gamma_vals[curr_gene_idx]
# t_curr = time_cell[curr_cell_index]
# u_t_actual = data[0][curr_gene_idx][curr_cell_index]
# s_t_actual = data[1][curr_gene_idx][curr_cell_index]

t_curr = time_cell
u_t_actual = data[0][curr_gene_idx]
s_t_actual = data[1][curr_gene_idx]



#this will loop through each input in inputs from 0 to length(alpha). Note that all input vectors need to be the same length.
# jp_matrix = jp_object.jacobian_product(inputs)
# print("initial:", gamma)
# jp_matrix = jp_object.partial(wrt=1, inputs=inputs)
# print(jp_matrix)

# jp_matrix = jp_object.partial(wrt=0, inputs=inputs)
# print(jp_matrix)

# jp_matrix = jp_object.partial(wrt=4, inputs=inputs)
# print(jp_matrix)



###########
# Optimization
###########


def calc_total_loss_and_der_across_cells(alpha, gamma, u_0, s_0, \
	t_curr_allcells, u_t_actual_allcells, s_t_actual_allcells, wrt=1):
	'''
	Calculate the loss and derivative
	'''

	total_cells = len(t_curr_allcells)
	loss_der_wrt_all_cells = np.empty(total_cells)
	loss_val_all_cells = np.empty(total_cells)
	
	# Loop through each cell and calculate the loss
	for i in range(len(t_curr_allcells)):
		t_curr = t_curr_allcells[i]
		u_t_actual = u_t_actual_allcells[i]
		s_t_actual = s_t_actual_allcells[i]


		# Define the input for the loss function
		inputs = [alpha, gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual]
		jp_matrix = jp_object.partial(wrt=wrt, inputs=inputs)


		# print(jp_matrix)

		# Get the loss function value, and derivative given the inputs
		loss_der_wrt = jp_matrix[0][0][0] # wrt is the index of variable of interest, alpha is 0, gamma is 1
		loss_val = jp_matrix[1][0][0] # Might to change this reference for updated code

		print(loss_val, loss_der_wrt)

		# Store the loss function and derivatives for each cell
		loss_der_wrt_all_cells[i] = loss_der_wrt
		loss_val_all_cells[i] = loss_val

	loss_sum = np.sum(loss_val_all_cells) / total_cells
	loss_der_sum = np.sum(loss_der_wrt_all_cells) / total_cells

	print("losssum", loss_sum)
	
	return loss_sum, loss_der_sum



def optimize_gamma(alpha, gamma, u_0, s_0, t_curr_allcells, u_t_actual_allcells, \
	s_t_actual_allcells, learning_rate = 1000000000000000):
	'''
	Function to optimize the gamma value
	across all cells
	'''

	loss_val_sum, loss_der_gamma_sum = calc_total_loss_and_der_across_cells(alpha, gamma, u_0, s_0, \
	t_curr_allcells, u_t_actual_allcells, s_t_actual_allcells, wrt=1)


	curr_gamma = gamma
	iterations = 0
	iterations_cutoff = 200
	previous_error = 1000000000
	print("initial gamma:", gamma)


	while True and iterations < iterations_cutoff:
		new_gamma = curr_gamma - learning_rate * float(loss_val_sum / loss_der_gamma_sum)
		print("gamma:", new_gamma)

		# We reoptimize for gamma if the number becomes negative
		# by randomly selecting a new gamma for optimzation
		if new_gamma <= 0 :
			new_gamma = random.random()


		loss_val_sum, loss_der_gamma_sum = calc_total_loss_and_der_across_cells(alpha, new_gamma, u_0, s_0, \
		t_curr_allcells, u_t_actual_allcells, s_t_actual_allcells, wrt=1)

		print(loss_val_sum, loss_der_gamma_sum)

		curr_gamma = new_gamma

		if(abs(loss_val_sum - previous_error) < 10 **(-20)):
			break

		previous_error = loss_val_sum
		iterations += 1

	return curr_gamma



def optimize_alpha(alpha, gamma, u_0, s_0, t_curr_allcells, u_t_actual_allcells, \
	s_t_actual_allcells, learning_rate = 100000):
	'''
	Function to optimize the alpha value
	across all cells
	'''

	loss_val_sum, loss_der_alpha_sum = calc_total_loss_and_der_across_cells(alpha, gamma, u_0, s_0, \
	t_curr_allcells, u_t_actual_allcells, s_t_actual_allcells, wrt=0)


	curr_alpha = alpha
	iterations = 0
	iterations_cutoff = 200
	previous_error = 1000000000
	print("initial alpha:", curr_alpha)


	while True and iterations < iterations_cutoff:
		new_alpha = curr_alpha - learning_rate * float(loss_val_sum / loss_der_alpha_sum)
		print("alpha:", new_alpha)

		# We reoptimize for gamma if the number becomes negative
		# by randomly selecting a new alpha for optimzation
		if new_alpha <= 0 :
			new_alpha = random.random()


		loss_val_sum, loss_der_alpha_sum = calc_total_loss_and_der_across_cells(new_alpha, gamma, u_0, s_0, \
		t_curr_allcells, u_t_actual_allcells, s_t_actual_allcells, wrt=0)

		print(loss_val_sum, loss_der_alpha_sum)

		curr_alpha = new_alpha

		if(abs(loss_val_sum - previous_error) < 10 **(-20)):
			break

		previous_error = loss_val_sum
		iterations += 1

	return curr_alpha



# optimize_gamma(alpha, gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual)

new_alpha = alpha
while True:
	# Alternating optimization between alpha and gamma
	new_gamma = optimize_gamma(new_alpha, gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual)
	new_alpha = optimize_alpha(alpha, new_gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual)



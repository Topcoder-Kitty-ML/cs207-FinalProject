#!/usr/bin/env python


# Performs optimization of the RNA velocity
# equation

import numpy as np
import random
import sys
sys.path.append('../../code/')
from autodiff_module import *
from generic_diff import *
from vector_jacobian import *

from functions import calc_u as u_t
from functions import calc_s as s_t



# Read data in
data = np.load("processed_data/norm_filtered_cells.scaled.pickle", allow_pickle=True)
# data = np.load("processed_data/norm_filtered_cells.pickle")
num_cells = data.shape[2]
num_genes = data.shape[1]


# Randomize the time values (Time values are in per 10^6 scale)
time_cell = [ x / 1000000 for x in range(num_cells)]

random.seed(1234)

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




euclidean_distance = lambda u_t, s_t, u_t_actual, s_t_actual: sqrt((u_t - u_t_actual)**2 + (s_t - s_t_actual)**2)
# where u_t is a function defined above,
# where s_t is a function defined above,
# u_t_actual is a data point, 
# s_t_actual is a data point

# Now combine them into final function that makes explicit what are variables (these can be your differentiating variables of interest but also your variable inputs):
combined = lambda alpha, gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual:\
euclidean_distance(u_t(alpha, u_0, t_curr), s_t(alpha, gamma, u_0, s_0, t_curr), u_t_actual, s_t_actual)



# combined = lambda alpha, gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual: alpha ** 2



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


# for i in range(num_genes):
curr_gene_idx = 110
curr_cell_index = 180

s_0 = data[0][curr_gene_idx][initial_cell_index]
u_0 = data[1][curr_gene_idx][initial_cell_index]
alpha = alpha_vals[curr_gene_idx]
gamma = gamma_vals[curr_gene_idx]
t_curr = [time_cell[curr_cell_index]]
u_t_actual = [data[0][curr_gene_idx][curr_cell_index]]
s_t_actual = [data[1][curr_gene_idx][curr_cell_index]]


# t_curr = time_cell
# u_t_actual = data[0][curr_gene_idx]
# s_t_actual = data[1][curr_gene_idx]



# alpha = list of alpha values
# gamma = list of gamma values
# u_0 = list of u 0 values
# s_0 = list of s 0 values
# t_curr = list of t curr values
# u_t_actual = list of u_t_actual values
# s_t_actual = list of s_t_actual values
# inputs = [alpha, gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual] # in the same order in which we defined the python variables in the combined function


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
		# print(i)
		t_curr = t_curr_allcells[i]
		u_t_actual = u_t_actual_allcells[i]
		s_t_actual = s_t_actual_allcells[i]


		# Define the input for the loss function
		inputs = [alpha, gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual]
		# print(inputs)
		jp_matrix = jp_object.partial(wrt=wrt, inputs=inputs)


		# print(jp_matrix)

		# Get the loss function value, and derivative given the inputs
		loss_der_wrt = jp_matrix[0][0][0] # wrt is the index of variable of interest, alpha is 0, gamma is 1
		loss_val = jp_matrix[1][0][0] # Might to change this reference for updated code

		# print(loss_val, loss_der_wrt)

		# Store the loss function and derivatives for each cell
		loss_der_wrt_all_cells[i] = loss_der_wrt
		loss_val_all_cells[i] = loss_val

		# print("der for cell:", loss_der_wrt)

	loss_sum = np.sum(loss_val_all_cells) / total_cells
	loss_der_sum = np.sum(loss_der_wrt_all_cells) / total_cells

	print(alpha, loss_sum, loss_der_sum)
	# print("losssum", loss_sum)
	# print("losssum der", loss_der_sum)
	
	return loss_sum, loss_der_sum


def optimize_gamma(alpha, gamma, u_0, s_0, t_curr_allcells, u_t_actual_allcells, \
	s_t_actual_allcells, learning_rate = 0.000000000000001):
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
		# new_gamma = curr_gamma - learning_rate * float(loss_val_sum / loss_der_gamma_sum)
		# print("der", loss_der_gamma_sum)
		new_gamma = curr_gamma - learning_rate * loss_der_gamma_sum

		# print("gamma:", new_gamma)

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
	s_t_actual_allcells, learning_rate = 0.1):
	'''
	Function to optimize the alpha value
	across all cells
	'''

	loss_val_sum, loss_der_alpha_sum = calc_total_loss_and_der_across_cells(alpha, gamma, u_0, s_0, \
	t_curr_allcells, u_t_actual_allcells, s_t_actual_allcells, wrt=0)


	curr_alpha = alpha
	iterations = 0
	iterations_cutoff = 2000
	previous_error = 1000000000
	print("initial alpha:", curr_alpha)


	while True and iterations < iterations_cutoff:
		# new_alpha = curr_alpha - learning_rate * float(loss_val_sum / loss_der_alpha_sum)
		# new_alpha = curr_alpha - float(loss_val_sum / loss_der_alpha_sum)
		new_alpha = curr_alpha - learning_rate * loss_der_alpha_sum
		diff = new_alpha - curr_alpha
		# print("diff:", diff)
		# print("alpha:", new_alpha)

		# We reoptimize for gamma if the number becomes negative
		# by randomly selecting a new alpha for optimzation
		# if new_alpha <= 0 :
		# 	new_alpha = random.random()


		loss_val_sum, loss_der_alpha_sum = calc_total_loss_and_der_across_cells(new_alpha, gamma, u_0, s_0, \
		t_curr_allcells, u_t_actual_allcells, s_t_actual_allcells, wrt=0)

		# print("----")
		# print(loss_val_sum, loss_der_alpha_sum)

		curr_alpha = new_alpha

		# if(abs(loss_val_sum - previous_error) < 10 **(-20)):
		# 	break

		if abs(loss_der_alpha_sum) < 0.0001:
			break

		previous_error = loss_val_sum
		iterations += 1

	# print("apple")

	return curr_alpha



# optimize_gamma(alpha, gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual)

new_alpha = alpha
# while True:
# 	# new_gamma = optimize_gamma(alpha, gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual)
# 	new_alpha = optimize_alpha(new_alpha, gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual)

######################
######################
######################
######################
optimize_alpha(new_alpha, gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual)

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
curr_cell_index = 189

s_0 = data[0][curr_gene_idx][initial_cell_index]
u_0 = data[1][curr_gene_idx][initial_cell_index]
alpha = alpha_vals[curr_gene_idx]
gamma = gamma_vals[curr_gene_idx]
t_curr = time_cell[curr_cell_index]
u_t_actual = data[0][curr_gene_idx][curr_cell_index]
s_t_actual = data[1][curr_gene_idx][curr_cell_index]


# alpha = list of alpha values
# gamma = list of gamma values
# u_0 = list of u 0 values
# s_0 = list of s 0 values
# t_curr = list of t curr values
# u_t_actual = list of u_t_actual values
# s_t_actual = list of s_t_actual values
inputs = [alpha, gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual] # in the same order in which we defined the python variables in the combined function


#this will loop through each input in inputs from 0 to length(alpha). Note that all input vectors need to be the same length.
# jp_matrix = jp_object.jacobian_product(inputs)
print("initial:", gamma)
jp_matrix = jp_object.partial(wrt=1, inputs=inputs)
print(jp_matrix)

jp_matrix = jp_object.partial(wrt=0, inputs=inputs)
print(jp_matrix)

jp_matrix = jp_object.partial(wrt=4, inputs=inputs)
print(jp_matrix)



###########
# Optimization
###########


der_gamma = jp_matrix[0][0][0]
val = jp_matrix[1][0][0]

# learning_rate = 10000000000


learning_rate = 10000000
curr_gamma = gamma
# print("apple")
iterations = 0
iterations_cutoff = 200
while True and iterations < iterations_cutoff:
	new_gamma = curr_gamma - learning_rate * float(val / der_gamma)
	print("gamma:", new_gamma)

	# We reoptimize for gamma if the number becomes negative
	# by randomly selecting a new gamma for optimzation
	if new_gamma <= 0 :
		new_gamma = random.random()


	inputs = [alpha, new_gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual]

	jp_matrix = jp_object.partial(wrt=1, inputs=inputs)
	print(jp_matrix)

	# jp_matrix = jp_object.partial(wrt=0, inputs=inputs)
	# print(jp_matrix)

	der = jp_matrix[0][0][0]
	val = jp_matrix[1][0][0]
	curr_gamma = new_gamma

	iterations += 1





######################
######################
######################
######################


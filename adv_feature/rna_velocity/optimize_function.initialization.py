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
# print(data.shape) # type x genes x cells
num_cells = data.shape[2]
num_genes = data.shape[1]


# Randomize the time values (Time values are in per 10^6 scale)
# time_cell = [ x / 1000000 for x in range(num_cells)]
time_cell = [ x / 100000000000000 for x in range(num_cells)]




# Randomize the alpha and gamma values
# for each gene (Initialization)
random.seed(1234)
alpha_vals = [random.random() for i in range(num_genes)]
gamma_vals = [random.random() for i in range(num_genes)]



# Swap function 
def swapPositions(list, pos1, pos2): 
	  
	list[pos1], list[pos2] = list[pos2], list[pos1] 
	return list


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

def calc_norm_euclidian_distance(vector1, vector2):
	'''
	Calculate the euclidean distance between
	two input vectors. This implementation
	allows us to calculate the derivative of this
	function
	'''

	norm_dist = calc_euclidian_distance(vector1, vector2).val / len(vector1)

	return norm_dist



def change_initial_and_randomize():
	'''
	We select each of the cells in turn as the
	initial cells, and randomize the rest of the
	cells.
	'''
	cell_idx = list(range(num_cells))
	cell_time_vals = []
	for i in range(num_cells):
	# for i in range(2):
		# print(i)
		# cell_idx_rest = [element for i, element in enumerate(vector) if i not in to_exclude]

		# Shuffle the time values between cells
		random.shuffle(time_cell)

		# Get index sorted from smallest to largest
		idx = np.argsort(time_cell)


		# Swap the time zero element to the "i-th" index.
		# i.e. if we want the first element to be timepoint
		# zero, we swap the element with timepoint zero with
		# the first element
		initial_cell_index = idx[0] # index of the cell with time stated as zero
		time_cell_copy = time_cell.copy()
		time_cell_new = swapPositions(time_cell_copy, i, initial_cell_index) # we swap the positions here

		# print(time_cell_new)
		cell_time_vals.append(time_cell_new)

	return cell_time_vals




def optimization_function(data, alpha_vals, gamma_vals, time_cell):

	dist_all_gene = []
	idx = np.argsort(time_cell)
	initial_cell_index = idx[0]


	for curr_gene_idx in range(num_genes):
		# print(curr_gene_idx)
		# Do this for a single gene first
		# curr_gene_idx = 104

		s_0 = data[0][curr_gene_idx][initial_cell_index]
		u_0 = data[1][curr_gene_idx][initial_cell_index]


		unspliced_vals_predicted = []
		spliced_vals_predicted = []
		unspliced_vals_actual = []
		spliced_vals_actual = []
		for i in range(len(idx)):
			# print(i)
			curr_index = idx[i]
			# print(curr_index)

			# Curr index
			alpha = alpha_vals[curr_gene_idx]
			gamma = gamma_vals[curr_gene_idx]
			t_curr = time_cell[curr_index]

			# Predicted values based on equations
			u_t_pred = u_t(alpha, u_0, t_curr)
			s_t_pred = s_t(alpha, gamma, u_0, s_0, t_curr)

			# Actual state at t
			u_t_actual = data[0][curr_gene_idx][curr_index]
			s_t_actual = data[1][curr_gene_idx][curr_index]
			# print(u_t, s_t)
			# print(u_t_actual, s_t_actual)

			unspliced_vals_predicted.append(u_t_pred)
			spliced_vals_predicted.append(s_t_pred)
			unspliced_vals_actual.append(u_t_actual)
			spliced_vals_actual.append(s_t_actual)


		# Combine the list
		vals_predicted = unspliced_vals_predicted + spliced_vals_predicted
		vals_actual = unspliced_vals_actual + spliced_vals_actual


		# print(len(vals_predicted ))

		# Calculate the distance per data point for each gene
		dist_gene = calc_norm_euclidian_distance(vals_predicted, vals_actual)
		dist_all_gene.append(dist_gene)

	# Calculate the average distance across all genes
	total_dist_all_gene = np.sum(dist_all_gene) / num_genes

	return total_dist_all_gene



time_cells_all_cell_initial = change_initial_and_randomize()

for i in range(num_cells):
	print(i)
	print("dist is:", optimization_function(data, alpha_vals, gamma_vals, time_cells_all_cell_initial[i]))






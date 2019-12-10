#!/usr/bin/env python

import numpy as np
import random
import sys
sys.path.append('../')
from genericdiff import *
from rnavelocity.functions import calc_u as u_t
from rnavelocity.functions import calc_s as s_t



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




def optimization_function(data, alpha_vals, gamma_vals, time_cell, idx, num_genes):
	'''
	Calculate the 
	'''
	dist_all_gene = []
	# idx = np.argsort(time_cell)
	initial_cell_index = idx[0]


	for curr_gene_idx in range(num_genes):
		# Do this for a single gene
		s_0 = data[0][curr_gene_idx][initial_cell_index]
		u_0 = data[1][curr_gene_idx][initial_cell_index]


		unspliced_vals_predicted = []
		spliced_vals_predicted = []
		unspliced_vals_actual = []
		spliced_vals_actual = []

		# Calculate across all cells
		for i in range(len(idx)):
			curr_index = idx[i]

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


			# Append the data to a list
			unspliced_vals_predicted.append(u_t_pred)
			spliced_vals_predicted.append(s_t_pred)
			unspliced_vals_actual.append(u_t_actual)
			spliced_vals_actual.append(s_t_actual)


		# Combine the list
		vals_predicted = unspliced_vals_predicted + spliced_vals_predicted
		vals_actual = unspliced_vals_actual + spliced_vals_actual



		# Calculate the distance per data point for each gene
		dist_gene = calc_norm_euclidian_distance(vals_predicted, vals_actual)
		dist_all_gene.append(dist_gene)

	# Calculate the average distance across all genes
	total_dist_all_gene = np.sum(dist_all_gene) / num_genes

	return total_dist_all_gene


def decide_optimal_start(input_pickle_file="processed_data/norm_filtered_cells.scaled.pickle", \
	initial_cellorder_file="output/cell_order.txt",\
	final_cellorder_file="output/cell_order.final.txt"):
	'''
	Determine which cell gives rise to
	the lowest error and should thus be
	used as the starting cell.
	'''

	# Read data in
	data = np.load(input_pickle_file, allow_pickle=True)
	# print(data.shape) # type x genes x cells
	num_cells = data.shape[2]
	num_genes = data.shape[1]


	f = open(initial_cellorder_file, "r")
	for line in f:
		order = line.strip().split(",")
	f.close()

	order = [int(float(i)) for i in order] 


	# Initialize the time values
	time_cell = [ x / 1000000 for x in range(num_cells)]



	# Randomize the alpha and gamma values
	# for each gene (Initialization)
	random.seed(1234)
	alpha_vals = [random.random() for i in range(num_genes)]
	gamma_vals = [random.random() for i in range(num_genes)]


	error_left_initial = optimization_function(data, alpha_vals, gamma_vals, time_cell, order, num_genes)
	error_right_initial = optimization_function(data, alpha_vals, gamma_vals, time_cell, order[::-1], num_genes)

	# For left as initial cell
	print("Error with left as start:", error_left_initial)

	# For right as initial cell
	print("Error with right as start:", error_right_initial)


	# Open file for writing
	output = open(final_cellorder_file, "w")

	# Original order (if error starting from left is smaller)
	if error_left_initial < error_right_initial:
		output.write(",".join(map(str, order)))
		output.close()

	# Reverse order (if error on other side is smaller)
	else:
		output.write(",".join(map(str, order[::-1])))
		output.close()


if __name__ == "__main__":
	decide_optimal_start(input_pickle_file="processed_data/norm_filtered_cells.scaled.pickle", \
		initial_cellorder_file="output/cell_order.txt",\
		final_cellorder_file="output/cell_order.final.txt")



#!/usr/bin/env python

from time_sort import *
from optimize_parameters import *

class RNAOptimize:
	'''
	'''
	def __init__(self, pickle_file = "processed_data/norm_filtered_cells.scaled.pickle", \
		output_cellorder_file = "output/cell_order.txt", \
		output_cellorder_final_file = "output/cell_order.final.txt",
		final_parameter_output_file = "output/optimized_gene_parameters.txt",
		num_processes = 4):
		'''
		Performs the overall optization on the input pickle
		file on run.
		'''

		time_sort(array_pickle_file = pickle_file, \
			output_cellorder_file = output_cellorder_file, \
			output_cellorder_final_file = output_cellorder_final_file)


		overall_optimization(input_pickle_file=pickle_file, \
			cell_order_file=output_cellorder_final_file, \
			output_parameter_file=final_parameter_output_file, \
			num_processes=num_processes)


	def get_sequence(self):
		'''
		Read the final sequence from the final
		order file
		'''
		pass


	def plot_top_alpha_gamma(self):
		'''
		Plot the 
		'''
		pass


	def plot_expression(self):
		pass


	def get_alpha_gamma(self):
		'''
		Get the alpha and gamma values
		as a list from the input files
		'''
		pass






	# # Read data in
	# data = np.load("processed_data/norm_filtered_cells.scaled.pickle", allow_pickle=True)
	# # print(data.shape) # type x genes x cells
	# num_cells = data.shape[2]
	# num_genes = data.shape[1]
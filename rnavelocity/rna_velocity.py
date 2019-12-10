#!/usr/bin/env python

from time_sort import *
from optimize_parameters import *

class RNAOptimize:
	'''
	Optimize for alpha, gamma and time, given input data
	of single cell RNA-seq expression values
	'''
	def __init__(self, input_pickle_file = "processed_data/norm_filtered_cells.scaled.pickle", \
		output_cellorder_file = "output/cell_order.txt", \
		output_cellorder_final_file = "output/cell_order.final.txt",
		final_parameter_output_file = "output/optimized_gene_parameters.txt",
		num_processes = 4, cached=False):
		'''
		Performs the overall optization on the input pickle
		file which carries the expression of the spliced and
		unspliced RNA species.

		By default cached is set to true as the optimization takes
		a long time. Thus, we cached it by default.
		'''
		self.output_cellorder_final_file = output_cellorder_final_file
		self.final_parameter_output_file = final_parameter_output_file

		if not cached:
			time_sort(array_pickle_file = input_pickle_file, \
				output_cellorder_file = output_cellorder_file, \
				output_cellorder_final_file = output_cellorder_final_file)


			overall_optimization(input_pickle_file=input_pickle_file, \
				cell_order_file=output_cellorder_final_file, \
				output_parameter_file=final_parameter_output_file, \
				num_processes=num_processes)


	def get_sequence(self):
		'''
		Read the final sequence from the final
		order file
		'''

		f = open(self.output_cellorder_final_file, "r")
		for line in f:
			order = line.strip().split(",")
		f.close()
		idx = [int(float(i)) for i in order]
		
		return idx


	def get_parameters(self):
		'''
		Get the alpha and gamma parameters
		column 1: gene index
		column 2: alpha parameter for gene
		column 3: gamma parameter for gene
		'''
		file = open(self.final_parameter_output_file, "r")
		data = []
		for line in file:
			data.append(line.strip().split("\t"))
			
		data_np = np.array(data)

		return data_np

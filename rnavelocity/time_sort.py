#!/usr/bin/python

from generate_minimum_spanning_tree import *
from initialization import *

def time_sort(array_pickle_file = "processed_data/norm_filtered_cells.scaled.pickle",\
	output_cellorder_file = "output/cell_order.txt", \
	output_cellorder_final_file = "output/cell_order.final.txt"):
	'''
	Generate the order of the cells.
	Pickle file is a n x m x o matrix where,
	n : spliced and unspliced dimension (spliced = 0, unspliced = 1)
	m : each is a gene
	o : each is a cell
	'''

	# Generate the tree from the data
	generate_tree_from_data(\
	input_file = array_pickle_file,\
	output_file = output_cellorder_file)


	# Decide on the optimal starting point and
	# generate a final cell order file that will
	# be used for optimization
	decide_optimal_start(input_pickle_file=array_pickle_file, \
	initial_cellorder_file=output_cellorder_file, \
	final_cellorder_file=output_cellorder_final_file)


if __name__ == "__main__":
	time_sort()
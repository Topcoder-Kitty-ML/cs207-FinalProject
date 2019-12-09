#!/usr/bin/env python


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



# Calculate the euclidean distance between
# the cells
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

	norm_dist = calc_euclidian_distance(vector1, vector2) / len(vector1)

	return norm_dist




# Generates a tree of the cells using a greedy
# approach

def calc_pairwise_similarity(all_cells):
	'''
	Calculate the pairwise similarity
	of the cells
	'''

	# all_cells[0]
	num_cells = 10

	dist_result = []

	for i in range(num_cells):
		# print(i)
		for j in range(i+1,num_cells):
			dist = calc_norm_euclidian_distance(all_cells[0,:,i], all_cells[0,:,j])
			result = (i, j, dist)
			dist_result.append(result)

	return(dist_result)


# def convert_distance_to_tree(distance_matrix):
# 	'''
# 	Convert a distance matrix into a minimum
# 	spanning tree
# 	'''




all_dist = calc_pairwise_similarity(data)
all_dist = np.array(all_dist)
# print(all_dist)

all_dist_sorted = all_dist[all_dist[:,2].argsort()]
print(all_dist_sorted)
# print(all_dist[:,2].argsort())

for i in range(all_dist_sorted.shape[0]):
	print(i)


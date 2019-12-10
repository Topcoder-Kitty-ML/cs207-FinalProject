#!/usr/bin/env python


import numpy as np
import random
import sys
sys.path.append('../../')
from genericdiff import *

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

	num_cells = all_cells.shape[2]
	# num_cells = 100

	dist_result = []

	for i in range(num_cells):
		# print(i)
		for j in range(i+1,num_cells):
			dist = calc_norm_euclidian_distance(all_cells[0,:,i], all_cells[0,:,j])
			result = (i, j, dist)
			dist_result.append(result)

	return(dist_result)





def prune_node(data, node_value):
	'''
	Remove rows with node in all rows
	'''
	idx_left = data[:,0] == node_value
	idx_right = data[:,1] == node_value

	idx_keep = np.logical_not(idx_left + idx_right)

	data_new = data[idx_keep]

	return data_new



all_dist = calc_pairwise_similarity(data)
all_dist = np.array(all_dist)
# print(all_dist)

all_dist_sorted = all_dist[all_dist[:,2].argsort()]
# print(all_dist_sorted)
# print(all_dist[:,2].argsort())


# def find_smallest_dist


left_node = all_dist_sorted[0,0]
right_node = all_dist_sorted[0,1]
final_order = [left_node, right_node]
# print(final_order)


# Delete first row
all_dist_sorted = np.delete(all_dist_sorted, 0, axis=0)


while all_dist_sorted.shape[0]:
	node_prune = -1
	# print(all_dist_sorted)
	for i in range(all_dist_sorted.shape[0]):
		if left_node == all_dist_sorted[i,0] and right_node == all_dist_sorted[i,1]:
			next
		if left_node == all_dist_sorted[i,1] and right_node == all_dist_sorted[i,0]:
			next

		if left_node == all_dist_sorted[i,0]:
			node_to_link = all_dist_sorted[i,1]
			node_prune = left_node
			final_order.insert(0, node_to_link)
			left_node= node_to_link
			break

		elif left_node == all_dist_sorted[i,1]:
			node_to_link = all_dist_sorted[i,0]
			node_prune = left_node
			final_order.insert(0, node_to_link)
			left_node= node_to_link
			break

		elif right_node == all_dist_sorted[i,0]:
			node_to_link = all_dist_sorted[i,1]
			node_prune = right_node
			final_order.append(node_to_link)
			right_node= node_to_link
			break

		elif right_node == all_dist_sorted[i,0]:
			node_to_link = all_dist_sorted[i,1]
			node_prune = right_node
			final_order.append(node_to_link)
			right_node= node_to_link
			break


	all_dist_sorted = prune_node(all_dist_sorted, node_prune)
	# print(final_order)


# print(all_dist_sorted[:,0] == 0)

f = open("cell_order.txt", "w")
f.write(",".join(map(str, final_order)))


# print(prune_node(all_dist_sorted, 2))



# Performs optimization of the RNA velocity
# equation

import numpy as np
import random
import sys
sys.path.append('../../')
from genericdiff import *
from multiprocessing import Pool

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

# # Get index sorted from smallest to largest
# idx = np.argsort(time_cell)

f = open("cell_order.txt", "r")
for line in f:
	order = line.strip().split(",")
f.close()
idx = [int(float(i)) for i in order]

# Reverse it to start from the end
idx = idx[::-1]

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
		jp_matrix_der = jp_object.partial_ders(wrt=wrt, inputs=inputs)
		jp_matrix_val = jp_object.partial_vals(wrt=wrt, inputs=inputs)


		# Get the loss function value, and derivative given the inputs
		loss_der_wrt = jp_matrix_der[0][0] # wrt is the index of variable of interest, alpha is 0, gamma is 1
		loss_val = jp_matrix_val[0][0] 

		# print(loss_val, loss_der_wrt)

		# Store the loss function and derivatives for each cell
		loss_der_wrt_all_cells[i] = loss_der_wrt
		loss_val_all_cells[i] = loss_val

	loss_sum = np.sum(loss_val_all_cells) / total_cells
	loss_der_sum = np.sum(loss_der_wrt_all_cells) / total_cells

	
	return loss_sum, loss_der_sum



def optimize_gamma(alpha, gamma, u_0, s_0, t_curr_allcells, u_t_actual_allcells, \
	s_t_actual_allcells, learning_rate = 0.0001):
	'''
	Function to optimize the gamma value
	across all cells
	'''

	loss_val_sum, loss_der_gamma_sum = calc_total_loss_and_der_across_cells(alpha, gamma, u_0, s_0, \
	t_curr_allcells, u_t_actual_allcells, s_t_actual_allcells, wrt=1)


	curr_gamma = gamma
	iterations = 0
	iterations_cutoff = 30


	while True and iterations < iterations_cutoff:
		new_gamma = curr_gamma - learning_rate * float(loss_val_sum / loss_der_gamma_sum) # Newton root finding
		# new_gamma = curr_gamma - learning_rate * loss_der_gamma_sum # Gradient descent
		# print("gamma:", new_gamma)

		# We reoptimize for gamma if the number becomes negative
		# by randomly selecting a new gamma for optimzation
		if new_gamma <= 0 :
			new_gamma = random.random()


		loss_val_sum, loss_der_gamma_sum = calc_total_loss_and_der_across_cells(alpha, new_gamma, u_0, s_0, \
		t_curr_allcells, u_t_actual_allcells, s_t_actual_allcells, wrt=1)

		# print(loss_val_sum, loss_der_gamma_sum)

		curr_gamma = new_gamma

		if(abs(loss_der_gamma_sum) < 10 **(-8)):
			break

		iterations += 1

	return curr_gamma



def optimize_alpha(alpha, gamma, u_0, s_0, t_curr_allcells, u_t_actual_allcells, \
	s_t_actual_allcells, learning_rate = 0.0001):
	'''
	Function to optimize the alpha value
	across all cells
	'''

	loss_val_sum, loss_der_alpha_sum = calc_total_loss_and_der_across_cells(alpha, gamma, u_0, s_0, \
	t_curr_allcells, u_t_actual_allcells, s_t_actual_allcells, wrt=0)


	curr_alpha = alpha
	iterations = 0
	iterations_cutoff = 30


	while True and iterations < iterations_cutoff:
		new_alpha = curr_alpha - learning_rate * float(loss_val_sum / loss_der_alpha_sum) # newton root finding
		# new_alpha = curr_alpha - learning_rate * loss_der_alpha_sum # gradient descent

		# We reoptimize for gamma if the number becomes negative
		# by randomly selecting a new alpha for optimzation
		if new_alpha <= 0 :
			new_alpha = random.random()


		loss_val_sum, loss_der_alpha_sum = calc_total_loss_and_der_across_cells(new_alpha, gamma, u_0, s_0, \
		t_curr_allcells, u_t_actual_allcells, s_t_actual_allcells, wrt=0)

		curr_alpha = new_alpha

		if(abs(loss_der_alpha_sum) < 10 **(-8)):
			break

		previous_error = loss_val_sum
		iterations += 1

	return curr_alpha



def optimize_gene(curr_gene_idx):
	# for i in range(num_genes):
	# curr_gene_idx = 220
	# curr_cell_index = 180

	try:
		iterations = 0
		iterations_cutoff = 2
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


		new_alpha = alpha
		new_gamma = gamma
		while True and iterations < iterations_cutoff:
			# Alternating optimization between alpha and gamma
			print(iterations)
			new_gamma = optimize_gamma(new_alpha, new_gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual)
			new_alpha = optimize_alpha(new_alpha, new_gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual)
			
			iterations += 1


		return curr_gene_idx, new_alpha, new_gamma

	except:
		# Return NA if there's an error during the run
		return curr_gene_idx, "NA", "NA"


# print(optimize_gene(1))

pool = Pool(processes = 3)
# result = pool.map(optimize_gene, range(2))
result = pool.map(optimize_gene, range(num_genes))


output = open("optimized_gene_parameters.txt", "w")
for result_line in result:
	output.write("\t".join(map(str, result_line)) + "\n")
	print(result_line)
output.close()


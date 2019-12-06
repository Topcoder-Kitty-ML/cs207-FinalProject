#!/usr/bin/env python


# Performs optimization of the RNA velocity
# equation



def calc_euclidian_distance(vector1, vector2):
	'''
	Calculate the euclidean distance between
	two input vectors
	'''
	pass


def calc_loss_func(present_cell, future_cell):
	'''
	Calculate the loss function between the
	present cell and a future cell. We assume
	that the state of a future cell can be predicted
	based on the current cell 
	'''

	time_diff = future_cell.time - present_cell.time
	predicted_future_cell = calc_predicted_future_state(present_cell.velocity, time_diff)

	loss = calc_euclidian_distance(future_cell, predicted_future_cell)

	return loss


def calc_predicted_future_state(present_cell, currstate, velocity, delta_t):
	'''
	Calculate the predicted future state
	of the cell based on the current state,
	the velocity and the timestep, delta_t

	Here, we assume that the future state of
	a cell can be approximated by its current
	state, plus the velocity component multiplied
	by the delta_t.
	'''

	future_state = currstate + velocity * delta_t

	return future_state


def sort_cells_by_ascending_time(multiple_cells):
	pass



def calc_overall_loss_func(all_cells):
	'''
	Calculate the overall loss function
	'''

	# Sort all the cells by time
	sorted_cells = sort_cells_by_ascending_time(multiple_cells)

	total_loss = 0

	for i in range(len(sorted_cells) - 1):
		present_cell = sorted_cells[i]
		future_cell = sorted_cells[i+1]
		curr_loss = calc_loss_func(present_cell, future_cell)

		total_loss += curr_loss


	return total_loss



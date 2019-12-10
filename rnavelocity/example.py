from rnavelocity.rna_velocity import *

# We set cached as true since it is going to take a long time to
# rerun the optimization
opt = RNAOptimize(input_pickle_file = "processed_data/norm_filtered_cells.scaled.pickle", \
	num_processes = 4, cached=True)

print("The order of the cells in time in sequential order is:")
print(opt.get_sequence())


print("===========================")
print("===========================")

print("The parameters are:")
print(opt.get_parameters())

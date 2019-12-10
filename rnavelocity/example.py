from rna_velocity import *

opt = RNAOptimize(pickle_file = "processed_data/norm_filtered_cells.scaled.pickle", num_processes = 4)

opt.get_sequence()

opt.plot_alpha_gamma()

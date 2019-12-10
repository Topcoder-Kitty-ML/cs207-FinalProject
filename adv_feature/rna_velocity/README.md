# Overview of RNA Velocity


## Overview
In an organism, cells gradually grow and develop from parental cells, to give rise to daughter cells. For instance, following fertilization of an egg, this single cell gradually grows and multiply to first give rise to precursor daughter cells (e.g. stem cells), which further grow and multiply to give rise to "granddaughter cells" like muscles, skin, brain, heart, liver, pancreas cells, etc. (Figure)

Single-cell RNA sequencing has emerged as a powerful technology for tracking these developmental changes, by enabling measurements of gene expression to be made on each and every one of these single cells. However, during single-cell RNA sequencing, each of these parental and daughter cells are mixed up. Thus, it becomes incredible difficult to distinguish which of this cells came first and are the "parents", and which of the other cells arose later on during development and are the "daughters".

To resolve this, a recently published and highly cited publication by Manno et al in Nature (cite) proposed the use of pre-cursor molecules, in tandem with their corresponding products to establish which of these cells are the "parents", and which of them are the "daughters". Briefly, a cell can be thought of as a mixture of a multitude of biological reactions, consisting of "reactants" and "products". Thus, when a "parent" cell is transitioning to become a "daughter" cell, the parental cell will express more of the reactant and less of the product, while the "daughter" cell will express less of the reactant and more of the product (Figure). Notably, using this simple logic, we can in principle infer which cell is the "parent", and which is the "daughter" via measurements of the reactants and products in these cells.

In the paper by Manno et al, the following differential equations were proposed to track these time related changes:

(equations 3 and 4 from the paper) $\alpha$

This give rise to the following equations:

(equations 5 and 6 from the paper)

where:
u - reactants (unspliced RNA)
s - products (spliced RNA)
t - time
α, γ - rate constants describing the reaction

Notably, u and s are values we can readily obtain from the single-cell RNA-sequencing experiments while α, γ, and t remains unknown parameters which we need to estimate from the data. Specifically, we are especially interested in the values of t which will enable us to infer which cell came earlier and is the "parental" cell, and which cells came later and are the "daughter" cells. Further, it should be noted that measurements of u and s are made typically made across thousands of cells, and across 20,000 genes.

To find an optimal arrangement for the cells in time, we propose a Markov chain where each of these cells can be individually arranged into a "parent" --> "daughter" chain.  (Figure)

To optimize for the optimal state in this model, we propose the following loss function for optimization:

(loss function)

Briefly, the loss function was defined as above because the future state of the cell can be approximated as the current "velocity" of the cell multiplied by the timestep difference between the current and future state. Thus, when the cells are arranged in an optimal sequential order, the above function would be minimized.

To obtain the optimal solution, we need to calculate the optimal α, γ, and t values. To this end, we will be performing gradient descent using our KittyDiffy package to optimize the function with respect to α and γ first. Subsequent to that, we will perform optimization for the best t values. Overall, we will perform these two steps in turn via alternating optimization to optimize for the target function. In the end, the final t values should provide an intuitive inference of which cell is the "parental" cell, and which is the "daughter" cell


# Data Pre-processing
To generate 


As the data is initially stored in the ".loom" format which requires a customized python library, we extracted and dumped the data into a ".pickle" object which is more readily readable across different platforms. To do so, we applied the code "extract_data.py", which extracts both the counts of unspliced reads (reactants), and spliced reads (products) from the original data structure. These data which are represented as two matrices of the same dimensions were dumped into the "hgForebrainGlut.spliced.pickle" and "hgForebrainGlut.unspliced.pickle" files.

# Data cleaning and normalization
The matrices representing the reactants (unspliced RNA) and products (spliced RNA) are extremely sparse in nature because (1) some genes within the cells are not expressed, and (2) single-cell RNA-sequencing typically is only able to subsample a fraction of the genes present within the cell. Noting this, most elements within this matrix is zero, causing the matrix to be extremely sparse. With this, most genes (columns in the matrix) will not provide much useful information in helping us determine which cells are the parental cells, and which are the daughter cells.

We expect that genes which show a significant level of counts within each cell to provide meaningful information for inference of the parental or daughter nature of each cells. To address this, we removed genes (columns) which showed only a very low count of reads within the data for both the 'spliced' and 'unspliced' data. As such, we selected for genes which showed at least a 

This was done using the 


# Optimization of alpha, gamma, and pseudotime



## Optimization of alpha and gamma


## Optimization of pseudotime





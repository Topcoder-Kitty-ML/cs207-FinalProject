#!/usr/bin/env python


import numpy as np
import loompy

ds = loompy.connect("hgForebrainGlut.loom")

spliced_layer = ds.layers["spliced"][:,:]
unspliced_layer = ds.layers["unspliced"][:,:]

spliced_layer.dump("hgForebrainGlut.spliced.pickle")
unspliced_layer.dump("hgForebrainGlut.unspliced.pickle")


# Dumpy gene names
gene_name = ds.ra.Gene
gene_name.dump("gene_name.pickle")

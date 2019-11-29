#!/usr/bin/python

from autodiff_module import *

x_val = 2
x = autodiff(x_val)

f = cos(x) ** 2
print(f.val, f.der)

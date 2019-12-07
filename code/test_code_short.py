#!/usr/bin/python

from autodiff_module import *

x = Var(2)
# y = Var(3)
y = 3

print(x.val)
print(x.der)

z = x + y
print(z.val)
print(z.der) 


print("=====")

z = y + x
print(z.val)
print(z.der) 



#############
print("------")

z = x - y
print(z.val)
print(z.der) 

z = y - x
print(z.val)
print(z.der) 

#############


print("------")

z = x * y
print(z.val)
print(z.der) 

z = y * x
print(z.val)
print(z.der) 

#############


print("------")

z = x / y
print(z.val)
print(z.der) 

z = y / x
print(z.val)
print(z.der) 


#############


print("------")

z = x ** y
print(z.val)
print(z.der) 

z = y ** x
print(z.val)
print(z.der) 

print("------")


z = -x
print(z.val)
print(z.der) 

print("------")
print(x < y)


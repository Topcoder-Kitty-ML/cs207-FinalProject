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

x = Var(2)
# y = Var(3)
y = 3

def test_GenerifDiff_lt:
    f = GenericDiff(1, 0)
    h = 2
    assert (f.der < h.der)

def test_GenerifDiff_gt:
    f = GenericDiff(1, 0)
    h = 2
    assert (f.der > h.der)

def test_GenerifDiff_eq():
    f = GenericDiff(1, 0)
    h = 2
    assert (f.der == h.der)
 
def test_GenerifDiff_ne:
    f = GenericDiff(1, 0)
    h = 2
    assert (f.der != h.der)

def test_GenerifDiff_le:
    f = GenericDiff(1, 0)
    h = 2
    assert (f.der <= h.der)

def test_GenerifDiff_ge:
    f = GenericDiff(1, 0)
    h = 2
    assert (f.der >= h.der)
    
   
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
print(x > y)
print(x <= y)
print(x >= y)
print(x == y)
print(x != y)









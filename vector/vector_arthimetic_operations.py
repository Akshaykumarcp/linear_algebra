import numpy as np

# create vector using numpy
# 1D array is the vector 
# create python list and convert into array
x = [1,2,3]
vector = np.array(x)
# array([1, 2, 3])

vector.ndim
# 1 --> 1D

vector.shape
# (3,) --> 1D array

# ARTHIMETIC OPERATIONS ON VECTORS {element wise operation}

# Addition

# create "a" 1D vector between 10 to 50 with size = 5
# vector in theory, array in pratical representation
a = np.random.randint(10,50,size=5)
# print a --> array([29, 10, 30, 21, 41])

# create "b" 1D vector between 25 to 75 with size = 5
b = np.random.randint(20,75,size=5)
# print b --> array([28, 54, 22, 54, 71])

# vection addition
c = a + b
# print c --> array([ 57,  64,  52,  75, 112])

# vection subtraction
d = a - b
# print d --> array([  1, -44,   8, -33, -30])

# vection multiplication
e = a * b
# print e --> array([ 812,  540,  660, 1134, 2911])

# vection division
f = a / b
# print f --> array([1.03571429, 0.18518519, 1.36363636, 0.38888889, 0.57746479])

# other operations can be performed respectively as above




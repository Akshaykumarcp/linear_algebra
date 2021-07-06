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

# create "a" 1D vector between 10 to 50 with size = 5
# vector in theory, array in pratical representation
a = np.random.randint(10,50,size=5)
# print a --> array([29, 10, 30, 21, 41])

# create "b" 1D vector between 25 to 75 with size = 5
b = np.random.randint(20,75,size=5)
# print b --> array([28, 54, 22, 54, 71])




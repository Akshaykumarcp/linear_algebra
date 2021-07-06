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
# print a --> array([10, 33, 28, 29, 32])

# create "b" 1D vector between 25 to 75 with size = 5
b = np.random.randint(20,75,size=5)
# print b --> array([72, 32, 50, 30, 59])

# vection dot product (element wise multiplication and summation)
# when 2 vector are dot producted, outcome is scalar
# can do using numpy in built function "dot"

vector_dot_product = a.dot(b)
# print vector_dot_product --> 5934

# LETS UNDERSTAND

x = np.arange(5,10) # array([5, 6, 7, 8, 9])
y = np.arange(5) # array([0, 1, 2, 3, 4])

# vector dot product working for x and y
# 0+6+14+24+36 = 80

vector_dot_product = x.dot(y) 
# vector dot product of x and y --> 80




import numpy as np

# MATRIX ADDITION
# dim of two matrices must match 

np.random.seed(0)

matrix1 = np.random.randint(1,100,(5,4))

matrix2 = np.random.randint(1,100,(5,4))

matrix1 + matrix2

# what happens when matrix dim doesn't match !!

matrix3 = np.arange(1,3)

matrix2 + matrix3

# ValueError: operands could not be broadcast together with shapes (5,4) (2,)

# MATRIX SUBTRACTION

matrix1 - matrix2

# MATRIX DIVISION

matrix1/matrix2

# MATRIX MULTIPLICATION

# 1. hadamard product
# 2. dot or matrix matrix product

# 1. hadamard product --> element or position wise multiplication

hadamard_matrix1 = np.random.randint(1,10,(2,2))
hadamard_matrix2 = np.random.randint(1,10,(2,2))

hadamard_matrix1 * hadamard_matrix2

# 2. dot or matrix matrix product --> multiply 1st row with 1st column, 1st row with 2nd column and so on

dot_matrix1 = np.random.randint(1,10,(2,2))
dot_matrix2 = np.random.randint(1,10,(2,2))

np.matmul(dot_matrix1,dot_matrix2)

# alternate to matmul is "@" and "dot" function

dot_matrix1 @ dot_matrix2

dot_matrix1.dot(dot_matrix2)

# MATRIX VECTOR MULTIPLICATION --> important for machine learning

'''
how ?

dataset is divided into independent and dependent features

suppose independent feature set is 4 X 3 --> X
suppose dependent feature set is 4 X 1 --> y

multiplication is not possible between two matrices as number of columns in 
independent feature does not match the rows in dependent feature

in order to get the dependent feature, have to multiple with unknown vector (W, weight vector) to get
dependent feature

NOTE: is the core logic of ML algorithms

'''

matrix1 = np.random.randint(10,100,(4,4)) # X

matrix2 = np.arange(2,6) # y

output_vector = matrix1.dot(matrix2) # W

# MATRIX SCALAR MULTIPLICATION

2 * matrix1

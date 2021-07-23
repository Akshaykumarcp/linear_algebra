import numpy as np

# SQUARE MATRIX --> number of rows is equal to number of columns

matrix1 = np.random.randint(1,10,(4,4))

matrix1.shape

# SYMMETRIC MATRIX --> type of square matrix where top right triangle is same as bottom left triangle based on principle diagonal elements

# https://stackoverflow.com/questions/10806790/generating-symmetric-matrices-in-numpy/27331415
N = 4
b = np.random.random_integers(-2000,2000,size=(N,N))
symmetric_matrix = (b + b.T)/2

symmetric_matrix.shape

# TRIANGULAR MATRIX --> is a square matrix and top OR bottom elements are zero based on principle diagonal element

# top elements are zero
np.triu(matrix1)

# bottom elements are zero
np.tril(matrix1)

# DIAGONAL MATRIX --> is a square matrix and top AND bottom elements are zero based on principle diagonal  element

diagonal_matrix = np.array([[1,0,0],[0,2,0],[0,0,3]])

# IDENTITY MATRIX --> type of diagonal matrix, principle diagonal will be equal to one 

np.eye(4)

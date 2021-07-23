import numpy as np

# TRANSPOSE OF MATRIX --> convert from rows to columns and columns to rows

matrix = np.random.randint(10,100,(4,2))
""" array([[19, 11],
       [25, 83],
       [30, 63],
       [51, 76]])
 """

transpose_matrix = matrix.T
""" 
array([[19, 25, 30, 51],
       [11, 83, 63, 76]]) """

# DETERMINANT OF MATRIX --> volume of the matrix

matrix = np.random.randint(10,100,(4,4))
""" 
array([[59, 68, 57, 92],
       [48, 50, 36, 63],
       [30, 52, 45, 32],
       [62, 66, 97, 65]])
       """

from numpy.linalg import det

det_matrix = det(matrix)
# -912991.9999999997

# RANK OF THE MATRIX --> estimate of linearly independent rows or columns

vector = np.array([1,2,3])

np.linalg.matrix_rank(vector)
# 1

matrix = np.random.randint(10,100,(4,4))
np.linalg.matrix_rank(matrix)
# 4
'''

Vector Norm - Finding length of vector

Many ways to find length of the vector:

1. L1 Norm - Lasso regression (a.k.a Taxicab Norm or Manhattan Norm)
2. L2 Norm - Ridge regression (a.k.a Eucledian Norm)
3. p Norm
4. Vector Max Norm

Norm Equation: https://image.slidesharecdn.com/02linearalgebra-171229202748/95/02-linear-algebra-15-638.jpg?cb=1514579308

'''

'''

how to find length of a vector ?
- draw a triangle to the vector and apply pythagoras theorem i,e sqrt of a2 + b2 = c

what if vector is in 3D ?
- sqrt of a2 + b2 + c2 = d

this process of knowing the length of vector is known as L2 Norm.

'''

# L2 norm implementation
import numpy as np
x = np.array([2,3,4])
y = np.array([3,4])

# length of vector y can be found using 
# norm function using linear algebra module
from numpy.linalg import norm
length_of_y = norm(y) # by default L2 form
# print length_of_y --> 5.0

# length of vector y can be found using 
# norm function using linear algebra module
length_of_x = norm(x) # by default L2 form
# print length_of_x --> 5.385164807134504

# lets verify length of vector x by manually calculating:
np.sqrt((4+9+16))
# 5.385164807134504

# L2 Norm of the vector i,e Ridge regression is used for regularization technique in Machine learning

'''
L1 Norm

vector --> [-1,2,3,-4]

take absolute value of each component and summazation i,e

1 + 2 + 3 + 4 = 10, is known as L1 Norm

'''

# L1 norm implementation
 
x = np.array([-1,2,3,-4])

l1_norm = norm(x,ord = 1) # ord = 1 --> find L1 norm of the vector
# print l1_norm --> 10.0

'''
p norm

- generalized form
- p = 2 , L2 norm
- p = 1, L1 norm

'''

# p norm implementation

z = np.array([-1,2,3,-4])
#p=1
p1 = norm(z,1)
# print p1 --> 10.0

#p=2
p2 = norm(z,2)
# print p2 --> 5.477225575051661

#p=3
p3 = norm(z,3) # take cube on each component, summation & take cube root of sum
# print p3 --> 4.641588833612778

# in summary, based on p value, squaring and root varies

'''
Vector Max Norm

- return max value in vector
'''

# implementation of vector max norm

x = np.random.randint(0,1000,10)
# x --> array([357, 460, 303, 200, 845, 617,  69, 870, 818, 840])

# we can use np.max but crux is how can we use/prove with the norm equation
# we get vector max norm when p = infinity
from math import inf
max_norm = norm(x,ord=inf)
# max_norm --> 870.0

'''
SUMMARY:

- L1 norm can be calculated by sum of absolute values of the vector
- L2 norm can be calculated by square root of the sum of the squared vector values
- Max norm can be calculated by finding maximum vector value

'''




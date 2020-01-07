import numpy as np
# 1. Make an array immutable (read-only).
x = np.zeros(10)
x.flags.writeable = False
# x[0] = 1 ### uncomment this to try and write to x, will produce ValueError: assignment destination is read-only

# 2. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates.
x = np.random.random([10,2]) #[rows, columns]
A,B = x[:,0], x[:,1] #i = row, j = column, [:,0] slices all rows and column 0, [:,1] slices all rows, column 1
R = np.sqrt(A**2 + B**2)
T = np.arctan2(B,A)
print(R)
print(T)
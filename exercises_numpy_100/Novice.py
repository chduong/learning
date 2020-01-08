# Numpy Novice Exercises
import numpy as np

print('1. Create a 8x8 matrix and fill it with a checkerboard pattern.')
m = np.zeros([8, 8], dtype = int)
m[1: :2, : :2] = 1 #adds 1 starting with the second column, first row, all the way through the matrix.
m[ : :2,1: :2] = 1 #adds 1 starting with the first column, second row, all the way through the matrix.
print(m)

#%%
print('2. Create a 10x10 array with random values and find the minimum and maximum values.')

m = np.random.random([10, 10])
m_min, m_max = m.min(), m.max()
print('m_min =', m_min, 'm_max =', m_max)

#%%
print('3. Create a checkerboard 8x8 matrix using the tile function.')
m = np.tile(np.array([[0, 1], [1, 0]]), (4, 4)) # last parameter (4, 4) is the number of repetitions along an axis in (x, y)
print(m)

#%%
print('4. Normalize a 5x5 random matrix (between 0 and 1).')
m = np.random.random([5, 5])
m_min, m_max = m.min(), m.max()
m_norm = (m - m_min) / (m_max - m_min) # normalized data equation: x_new = (x - x_min) / (x_max - x_min)

print('m =', m)
print('m_norm =', m_norm)

#%%
print('5. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).')
m = np.dot(np.ones([5, 3]), np.ones([3, 2])) #np.dot is the dot product of 2 matrices, 5x3 and 3x2, resulting in a 5x2 matrix.
print(m)

#%%
print('6. Create a 5x5 matrix with row values ranging from 0 to 4.')
m = np.zeros([5, 5])
m += np.arange(0, 5)
print(m)

#%%
print('7. Create a vector of size 10 with values ranging from 0 to 1, both excluded.')
m = np.linspace(0, 1, 12, endpoint=True)[1:-1] #endpoint=True by default, includes the last point (1) in this case and then slices 0 and 1 out of the vector
print(m)

#%%
print('8. Create a random vector of size 10 and sort it.')
m = np.random.random(10)
m.sort()
# explicitly: m = m.sort()
print(m)

#%%
print('9. Consider two random array A anb B, check if they are equal.')
A = np.random.randint(0, 2, 5) # parameters are: low, high=None (default), size=None (default), dtype='l'
B = np.random.randint(0, 2, 5)
print(A)
print(B)
equal = np.allclose(A, B) #parameters are: array1, array2, relative tolerance, absolute tolerance
print(equal)

#%%
print('10. Create a random vector of size 30 and find the mean value.')
x = np.random.random(30)
print('matrix =', x)
mean = x.mean()
print('mean =', mean)
print('1. Import the numpy package under the name np.')
import numpy as np

#%%
print('2. Print the numpy version and the configuration.')
print(np.__version__)
np.__config__.show()

#%%
print('3. Create a null vector of size 10.')
x = np.zeros(10)
print(x)

#%%
print('4. Create a null vector of size 10 but the fifth value which is 1.')
x = np.zeros(10)
x[4] = 1
print(x)

#%%
print('5. Create a vector with values ranging from 10 to 49.')
x = np.arange(10, 50)
print(x)

#%%
print('6. Create a 3x3 matrix with values ranging from 0 to 8.')
x = np.arange(0, 9).reshape(3, 3)
print(x)

#%%
print('7. Find indices of non-zero elements from [1,2,0,0,4,0].')
x = [1, 2, 0, 0, 4, 0]
nonzero_x = np.nonzero(x)
print('indices for nonzero elements of x =', nonzero_x)

#%%
print('8. Create a 3x3 identity matrix.')
x = np.eye(3) # (N, M=None, k=0, dtype=<class 'float'>, order='C')[source] where N = the number of rows in the output, specified as 3 here.
print(x)

#%%
print('9. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal.')
x = np.diag(1 + np.arange(0, 4), k = -1) # 1 + np.arange(4) is needed to start at 1-4 rather than 0-3. k = the diagonal in question. The default is 0 (on the diagonal). Use k>0 for diagonals above the main diagonal, and k<0 for diagonals below the main diagonal.
print(x)

#%%
print('10. Create a 3x3x3 array with random values.')
x = np.random.random([3, 3, 3])
print(x)

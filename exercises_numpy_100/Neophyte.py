# 1. Import the numpy package under the name np.
import numpy as np

# 2. Print the numpy version and the configuration.
print(np.__version__)
np.__config__.show()

# 3. Create a null vector of size 10.
x = np.zeros(10)
print(x)

# 4. Create a null vector of size 10 but the fifth value which is 1.
x = np.zeros(10)
x[4] = 1
print(x)

# 5. Create a vector with values ranging from 10 to 49.
x = np.arange(10, 50)
print(x)

# 6. Create a 5x5 matrix with row values ranging from 0 to 4.
x = np.zeros([5,5])
x += np.arange(5)
print (x)

# 7. Create a vector of size 10 with values ranging from 0 to 1, both excluded.
x = np.linspace(0, 1, 12, endpoint=True)[1:-1]
print(x)

# 8. Create a random vector of size 10 and sort it.
x = np.random.random(10)
x.sort()
print(x)

# 9. Consider two random array A anb B, check if they are equal.
A = np.random.randint(0, 2, 5) # parameters are: low, high=None (default), size=None (default), dtype='l'
B = np.random.randint(0, 2, 5)
print(A)
print(B)
equal = np.allclose(A, B) #parameters are: array1, array2, relative tolerance, absolute tolerance
print(equal)

# 10. Create a random vector of size 30 and find the mean value.
x = np.random.random(30)
print(x)
mean = x.mean()
print(mean)
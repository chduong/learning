import numpy as np
print('1. Make an array immutable (read-only).')
x = np.zeros(10)
x.flags.writeable = False
# x[0] = 1 ### uncomment this to try and write to x, will produce ValueError: assignment destination is read-only

#%%
print('2. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates.')
# Polar coordinates require taking x, y and converting to r and angle phi.
m = np.random.random([10,2]) #[rows, columns]
x, y = m[:,0], m[:,1] #i = row, j = column, [:,0] slices all rows and column 0, [:,1] slices all rows, column 1

r = np.sqrt(x**2 + y**2) # converts Cartesians to find hypotenuse in Pythagoras' Theorem
phi = np.arctan2(y,x) #arctan2 uses 2 inputs (y,x)
# phi2 = np.arctan(y/x) #arctan uses 1 argument (#)

polar = np.array([r, phi]).T
print('r, phi=', polar)

print('Polar to Cartesian Coordinates:')
# Use Cosine function for x. Cosine function: cos(phi) = x/r
x = np.cos(phi)*r

# Use Sine function for y. Sine function: sin(phi) = y/r
y = np.sin(phi)*r

cartesian = np.array([x, y]).T # 'T' transposes row to column
print('x, y =', cartesian)

#%%
print('3. Create random vector of size 10 and replace the maximum value by 0')
m = np.random.random(10)
# print(np.max(m))
m[m.argmax()] = 0
# print(np.max(m))
print(m)

#%%
print('4. Create a structured array with x and y coordinates covering the [0,1]x[0,1] area.')
m = np.zeros([5, 5], [('x', float), ('y', float)])
m['x'], m['y'] = np.meshgrid(np.linspace(0, 1, 5),
                             np.linspace(0, 1, 5)) #meshgrid evaluates a function on a grid, in this case the function 'linspace' for linear spacing from 0 to 1 in 5 steps

print(m)

#%%
print('5. Print the minimum and maximum representable value for each numpy scalar type.')
intdtype = [np.int8, np.int32, np.int64]
for dtype in intdtype:
    print(dtype, 'i min =', np.iinfo(dtype).min) #np.iinfo gives machine limits of the argument, different from np.info which gives info on the function, class or module.
    print(dtype, 'i max =', np.iinfo(dtype).max)
for dtype in [np.float32, np.float64]:
    print(dtype, 'f min =', np.finfo(dtype).min)
    print(dtype, 'f max =', np.finfo(dtype).max)
    print(dtype, 'f eps =', np.finfo(dtype).eps) # eps = machine epsilon, gives an upper bound on the relative error due to rounding in floating point arithmetic.

#%%
print('6. Create a structured array representing a position (x,y) and a color (r,g,b).')
m = np.zeros(5, [('position', [('x', float, 1),
                                ('y', float, 1)]),
                  ('color',    [('r', float, 1),
                                ('g', float, 1),
                                ('b', float, 1)])])
# prints (x, y), (r, g, b) 1D array. Extend to 2D array by changing 5 to [5, 5]
print(m)

#%%
print('7. Consider a random vector with shape (100,2) representing coordinates, find point by point distances.')
m = np.random.random([5, 2]) #to keep things small, working with 5 x 2 matrix instead of 100 x 2.
x, y = np.atleast_2d(m[:, 0]), np.atleast_2d(m[:, 1]) #mp.atleast_2d views inputs of at least 2D arrays.
distance = np.sqrt((x-x.T)**2 + (y-y.T)**2) #distance equation, d = sqrt((x2-x1)^2 + (y2-y1)^2)
print('numpy distance =', distance)

# Faster SciPy Solution:
import scipy
from scipy import spatial
distance2 = scipy.spatial.distance.cdist(m, m)
print('scipy distance =', distance2)

#%%
print('8. Generate a generic 2D Gaussian-like array.')
x, y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
distance = np.sqrt(x*x + y*y)
sigma, mu = 1.0, 0.0 #standard normal distribution defines sigma and mu as 1.0 and 0.0 respectively.
p_x = (1/(sigma * np.sqrt(2 * np.pi)) * np.exp(- ( (distance - mu)**2 / (2.0 * sigma**2) ) ))
print(p_x)

#%%
print('9. Consider the vector [1, 2, 3, 4, 5], how to build a new vector with 3 consecutive zeros interleaved between each value?')
m = np.arange(1, 6, 1) #(start, stop, steps)
n = 3
print(len(m))
m0 = np.zeros(len(m) + (len(m)-1) * n) #builds an array with zeros that are the same length as m0, the array with elements m with 0 0 0 interleaved between. the -1 is needed or else you'll have trailing zeros after the last element of m.
print(m0)

m0[::n + 1] = m # slices through m0 and inserts m in steps of n + 1

print(m0)

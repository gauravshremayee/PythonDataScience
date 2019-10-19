#!/usr/bin/python
import numpy as np
grid = np.arange(1, 10).reshape((3, 3)) 
print(grid)

x = np.array([1, 2, 3]) # row vector via reshape
x.reshape((1, 3))

print (x[np.newaxis, :])


x.reshape((3, 1))
print ( x[:, np.newaxis])


grid = np.array([[1, 2, 3],
                [4, 5, 6]])

print (grid)
# concatenate along the first axis 
np.concatenate([grid, grid])

print (grid)


np.concatenate([grid, grid], axis=1)

print (grid)

x = np.arange(9)
print(np.split(x, 3))

print(np.split(x,[3,7]))

print (np.arange(5))

print (np.arange(1, 6))
#divide each element by each element of other array 
print(np.arange(5)/np.arange(1,6))

print (x)
#[0 1 2 3 4 5 6 7 8]
#Add 2 to each element 
print (np.add(x, 2))
#[ 2  3  4  5  6  7  8  9 10]



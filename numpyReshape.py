#!/usr/bin/python
import numpy as np
#reshape in 3*3 matrix
#2*2 wont work as there are 9 elements ,so accomodating in 2*2 would be too less space for 9 elements

print (np.arange(5))
print (np.arange(1, 6))
print(np.arange(5)/np.arange(1,6))

#[0 1 2 3 4]
#[1 2 3 4 5]
#[0.         0.5        0.66666667 0.75       0.8       ]
grid = np.arange(1, 10).reshape((3, 3)) 
print(grid)
#output
#[[1 2 3]
# [4 5 6]
# [7 8 9]]

x = np.array([1, 2, 3]) # row vector via reshape
x.reshape((1, 3))

print (x[np.newaxis, :])

# output [[1 2 3]]

# column vector via reshape 

x.reshape((3, 1))
print ( x[:, np.newaxis])

#output 
#[[1]
#[2]
#[3]]



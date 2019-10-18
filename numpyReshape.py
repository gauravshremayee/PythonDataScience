#!/usr/bin/python
import numpy as np
#reshape in 3*3 matrix
#2*2 wont work as there are 9 elements ,so accomodating in 2*2 would be too less space for 9 elements
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



#!/usr/bin/python
import numpy as np
#reshape in 3*3 matrix
#2*2 wont work as there are 9 elements ,so accomodating in 2*2 would be too less space for 9 elements
grid = np.arange(1, 10).reshape((3, 3)) 
print(grid)



#!/usr/bin/python
import numpy as np
#array1
x = np.array([1, 2, 3])
#array2
y = np.array([3, 2, 1])
np.concatenate([x, y])

#concat more than two array 
z = [99, 99, 99] 
print(np.concatenate([x, y, z]))


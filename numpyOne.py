import numpy as np
np.random.seed(0) # seed for reproducibility
array1 = np.random.randint(10, size=6) # One-dimensional array
array2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array
array3 = np.random.randint(10, size=(3, 4, 5)) # Three-dimensional array

print(array1)
print(array2)
print(array3)

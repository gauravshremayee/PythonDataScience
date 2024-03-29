import numpy as np
#numpy.ones(shape, dtype=None, order='C')
#Shape of the new array, e.g., (2, 3) or 2.
#In below example one dimensional shape is present 
print ("np.ones()")
print (np.ones(5))

#numpy.array(object, dtype=None, copy=True, order='K', subok=, ndmin=0)

np.array([[1, 2], [3, 4]])
#array([[1, 2],
#      [3, 4]])
#[1,1,1,1,1]
print(np.array([1, 2, 3], ndmin=2))
#array([[1, 2, 3]])
print (np.array([1, 2, 3], dtype=complex))

#array([ 1.+0.j,  2.+0.j,  3.+0.j])
#
Creating an array from sub-classes:

print(np.array(np.mat('1 2; 3 4'))
    
#array([[1, 2],
#       [3, 4]])
np.random.seed(0) # seed for reproducibility
array1 = np.random.randint(10, size=6) # One-dimensional array
array2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array
array3 = np.random.randint(10, size=(3, 4, 5)) # Three-dimensional array

print(array1)
print(array2)
print(array3)


print("Third row first olumn data:")
print(array2[2,0])



[5 0 3 3 7 9]


[[3 5 2 4]
 [7 6 8 8]
 [1 6 7 7]]



[[[8 1 5 9 8]
  [9 4 3 0 3]
  [5 0 2 3 8]
  [1 3 3 3 7]]

 [[0 1 9 9 0]
  [4 7 3 2 7]
  [2 0 0 4 5]
  [5 6 8 4 1]]

 [[4 9 8 1 1]
  [7 9 9 3 6]
  [7 2 0 3 5]
  [9 4 4 6 4]]]

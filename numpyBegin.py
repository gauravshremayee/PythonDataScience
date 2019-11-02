import numpy as np

# numpy.ones(shape, dtype=None, order='C')
# Shape of the new array, e.g., (2, 3) or 2.
# In below example one dimensional shape is present
print("np.ones()")
#
print(np.ones(5))

#1 1 1 1 1
# numpy.array(object, dtype=None, copy=True, order='K', subok=, ndmin=0)

print(np.array([[1, 2], [3, 4]]))
# array([[1, 2],
#      [3, 4]])
# [1,1,1,1,1]
print(np.array([1, 2, 3,4], ndmin=1))

print(np.array(range(12), dtype="float", ndmin=2))
# array([[1, 2, 3]])

print("Print from 0 to 9")
print (np.arange(10))

print("After Reshaping print 0 to 5 in 2*3 Matrix")
print(np.arange(9).reshape(3,3))

print(np.arange(6).sum()/5)

print(np.arange(6).max())

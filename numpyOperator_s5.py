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

print ("Array is :")

print(x)

print ("Sum of all elements in array is ",np.sum(x))

#Array is :
#[0 1 2 3 4 5 6 7 8]
#Sum of all elements in array is  36
#divide each element by each element of other array 
print(np.arange(5)/np.arange(1,6))

print (x)
#[0 1 2 3 4 5 6 7 8]
#Add 2 to each element 
print (np.add(x, 2))
#[ 2  3  4  5  6  7  8  9 10]


print (np.subtract(x,2))
#[-2 -1  0  1  2  3  4  5  6]
x = np.array([-2, -1, 0, 1, 2])
print (abs(x))
#array([2, 1, 0, 1, 2])

theta = np.linspace(0, np.pi, 3)

print (theta)

#Now we can compute some trigonometric functions on these values:
print("theta = ", theta) print("sin(theta) = ", np.sin(theta)) print("cos(theta) = ", np.cos(theta)) print("tan(theta) = ", np.tan(theta))
#theta      =  [ 0.          1.57079633  3.14159265]
#sin(theta) =  [  0.00000000e+00   1.00000000e+00   1.22464680e-16]
#cos(theta) =  [  1.00000000e+00   6.12323400e-17  -1.00000000e+00]
#tan(theta) =  [  0.00000000e+00   1.63312394e+16  -1.22464680e-16]

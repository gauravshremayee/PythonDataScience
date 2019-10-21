#!/usr/bin/python
import numpy as np
grid = np.arange(1, 10).reshape((3, 3)) 
print(grid)

x = np.array([1, 2, 3]) # row vector via reshape
x.reshape((1, 3))

print (x[np.newaxis, :])


x.reshape((3, 1))

print(x<3)
#[ True  True False ]


np.any(x > 8)
#Out[18]: True
np.any(x < 0)
#False
#Are all values less than 10? 
np.all(x < 10)
#True
np.all(x == 6)
#Out[21]: False
  
  
  
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

#reshape the array

y=np.reshape(x,(3,3))

print("After reshape ")

print(y)

print ("min and max of array is:")

print ( np.min(x), np.max(x)) 

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

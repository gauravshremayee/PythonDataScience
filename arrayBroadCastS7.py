#Broadcasting is simply a set of rules for applying binary ufuncs (addition, subtraction, multiplication, etc.) 
import numpy as np
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
a+b
#Out[2]: array([5, 6, 7])

#Broadcasting allows these types of binary operations to be performed on arrays of dif‐ ferent sizes—for example, we can just as easily add a scalar (think of it as a zero- dimensional array) to an array:


#a+5
Out[3]: array([5, 6, 7])

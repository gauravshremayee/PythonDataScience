import numpy as np
X=np.arange(12)
Y=X.reshape(3,4)

print(Y)

#Combined Indexing 
# 2,2 2nd row 2nd column is 10 and so on
print(Y[2, [2, 0, 1]])

#[[ 0  1  2  3]
#[ 4  5  6  7]
#[ 8  9 10 11]]
#[10  8  9]

import numpy as np
from matplotlib import pyplot as plt

data = np.array([
    [1, 2],
    [2, 3],
    [3, 6],
])


x, y = data.T
plt.scatter(x,y)
#plt.plot(x, y)
plt.plot(x, y, label='linear graph')
#x = [value1, value2, value3,....]
n=[1,2,2,3,4,4,5,5,5,5,5,5,5,5,5]
print (n)
plt.hist(n, bins = 4)

# Add a legend
plt.legend(loc='upper left', frameon=False)
plt.show()

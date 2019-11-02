# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
#linspace (start ,stop, numberofpoints)
#below start at 0 and stop at 10 and there will be 100 co-ordinates
x = np.linspace(0, 12, 5)

#x=np.linspace([1,2,3,4],10)
#print all the co-ordinates

print (x)
#y=mx+c

#np.linspace(start = 0, stop = 100, num = 5, dtype = int)
# Plot the data
plt.plot(x, x, label='linear graph')
# Add a legend
plt.legend(loc='upper left', frameon=False)
# Show the plot
plt.show()


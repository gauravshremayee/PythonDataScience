import numpy as np 
import pandas as pd
import random
# use Pandas to extract rainfall inches as a NumPy array

	
rainfall = pd.read_csv('rainfall.csv')['PRCP'].values

print ("Rainfall is ",rainfall) 
inches = rainfall / 254 # 1/10mm -> inches

print(inches.shape)


import matplotlib.pyplot as plt
import seaborn; seaborn.set() # set plot styles
plt.hist(inches, 40);

#!/usr/bin/python
import numpy as np
import pandas as pd

df=pd.read_csv("data.csv");

#print column A 

print(df['A'])

#print column A and B

print (df[['A','B']])

#print 2nd Row


print("2nd row")
print(df.iloc[2])


#row 0, all columns
print(df.loc[0, :])

#row 1 all columns

print(df.loc[1,:])

#print("Row 3 column A")

print(df.loc[3,'A'])


#row 0 1 2 and Column C

#print(df.loc[[0,1,2],'B'])

#Sum of all elements column B
#Sum each column
#df.sum(axis=0) 

#sum each row
#df.sum(axis=1)


print("Column Row")
print(df.sum(axis=0))

print("Sum Row")
print(df.sum(axis=1))



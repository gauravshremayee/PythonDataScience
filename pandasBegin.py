#!/usr/bin/python

import pandas as pd

list=[1,2,3,4]
df=pd.Series(list)

print (df)


#disable index

df=pd.Series(list)

print ("Without index")
print (df)

dict={'a':1,'b':2,'c':3}

df=pd.Series(dict)

print ("Dictionary df")

print (df)


dp=df.to_csv("dict.csv")


df=pd.DataFrame(list)
#print in 2 D format 
print ("Dictionary Dataframe df")

print (df)

#By default the keys of the dict become the DataFrame columns:


dict1={'id1':123 , 'id2' : 345 , 'id3' : 567 }

df=pd.DataFrame(dict ,dict1)

print ("Multiple Dictionary")

print(df)

data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
pd.DataFrame.from_dict(data)

#Specify orient='index' to create the DataFrame using dictionary keys as rows:

data = {'row_1': [3, 2, 1, 0], 'row_2': ['a', 'b', 'c', 'd']}
print(pd.DataFrame.from_dict(data, orient='index'))
data = {'row_1': [3, 2, 1, 0], 'row_2': ['a', 'b', 'c', 'd']}
print(pd.DataFrame.from_dict(data, orient='index'))




#multiple

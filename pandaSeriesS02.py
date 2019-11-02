import pandas as pd
#A Pandas Series is a one-dimensional array of indexed data
#And Dataframe is 2-D data 
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print ( data)

print (data.index)

print (data.values)

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                            index=['a', 'b', 'c', 'd'])
                            
                           
                           
                           
#a    0.25
#b    0.50
#c    0.75
#d    1.00
#dtype: float64

print (data['b'])
#0.50

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                            index=[2, 5, 3, 7])
print (data)

print (data[5])
#0.5

population_dict = {'California': 38332521,
                               'Texas': 26448193,
                               'New York': 19651127,
                               'Florida': 19552860,
                               'Illinois': 12882135}
population = pd.Series(population_dict)
print (population)
            
print (population['California'])
            
pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2])
#Out[17]: 3 c 2a
#dtype: object

area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
                 'Florida': 170312, 'Illinois': 149995}
                 
area = pd.Series(area_dict)
print (area)
#            population    area
#California    38332521  423967
#Texas         26448193  695662
#New York      19651127  141297
#Florida       19552860  170312
#Illinois      12882135  149995
State Area
states = pd.DataFrame({'population': population,
                                   'area': area})
print (states)


#Out[18]: California    423967
#        Florida       170312
#         Illinois      149995
#         New York      141297
#         Texas         695662
#         dtype: int64

print ("State Area")
print (states.area)
print ( states['area'])

California    423967
Texas         695662
New York      141297
Florida       170312
Illinois      149995
Name: area, dtype: int64
California    423967
Texas         695662
New York      141297
Florida       170312
Illinois      149995
Name: area, dtype: int64

states['sum']=states['area']+states['population']

print (states)

#            population    area       sum
#California    38332521  423967  38756488
#Texas         26448193  695662  27143855
#New York      19651127  141297  19792424
#Florida       19552860  170312  19723172
#Illinois      12882135  149995  13032130

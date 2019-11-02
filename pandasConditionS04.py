# Import modules
import pandas as pd
import numpy as np

# Create a dataframe
raw_data = {'first_name': ['Jason', 'Molly', np.nan, np.nan, np.nan], 
        'nationality': ['USA', 'USA', 'France', 'UK', 'UK'], 
        'age': [42, 52, 36, 24, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'nationality', 'age'])
df

# Create variable with TRUE if nationality is USA
american = df['nationality'] == "USA"

# Create variable with TRUE if age is greater than 50
elderly = df['age'] > 50

# Select all cases where nationality is USA and age is greater than 50
df[american & elderly]


# Select all cases where the first name is not missing and nationality is USA 
df[df['first_name'].notnull() & (df['nationality'] == "USA")]



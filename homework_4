import numpy as np
#import pandas
import pandas as pd

### Solution exercise 1
# function that takes array and returns sorted indices
def ret_indices(score):
    if isinstance(score, np. ndarray):
        #score = np.array([103, 1502, 6230, 3, 1682, 5241, 4532])
        # sort the numpy array
        sorted_score = np.sort(score)
        # create np array for indices 
        indices_final = np.empty(shape=[0], dtype=np.float64)

        for item in sorted_score:
            #get indices of elements in score array
            indices = np.where(score==item) # this returns a tuple
            # access only indices from tuple
            indices_final = np.append(indices_final,indices[0], axis=None)
            
        return indices_final
    else:
        print('Sorry not a numpy array')

print(ret_indices(score = np.array([103, 1502, 6230, 3, 1682, 5241, 4532])))


### Solutions for exercise 2
# TASK 1
#read in from url -> get url by clicking raw in github
df = pd.read_csv('https://raw.githubusercontent.com/WHPAN0108/BHT-DataScience-S23/main/python-DS/country.csv')
print(df)

# TASK 2
# Display descriptive statistics for the numerical column (count, mean, std, min, 25%, 50%, 75%, max)
print(df.describe())

# TASK 3
# Show the last 4 rows of the dataframe
print(df.tail(4))

# TASK 4 
# Show all the rows of countries that have the EURO
print(df.loc[df['Currency'] == 'EUR'])

# TASK 5
# Show only name and Currency in a new data frame
temp_dataframe = df.filter(['Name','Currency'], axis=1)
print(temp_dataframe)

# TASK 6
# Show only the rows/countries that have more than 2000 GDP
print(df.loc[df['GDP'] > 2000])

# TASK 7
# Select all countries where with inhabitants between 50 and 150 Mio
new_df = df[(df['Population'].between(50000000, 150000000))]
print(new_df['Name']) # only show countries

# TASK 8 
# Calculate the GDP average (ignore the missing value)
df_avg = df['GDP'].mean()
print('Average of GDP is : ' + str(df_avg))

# TASK 9
# Calculate the GDP average (missing value treated as 0)
df8 = df.fillna(0) # fill nan with 0
#now calculate average again
df8avg = df8['GDP'].mean() 
print('Average of GDP is : ' + str(df8avg))

# TASK 10
# Calculate the population density (population/area)  of all countries and add as new column
df["Pop. Density"] = df["Population"] / df["Area"]
print(df)

# TASK 11
# Sort by country name alphabetically
df = df.sort_values('Name')
print(df)

# TASK 12
# Create a new data frame from the original where the area is changed: all countries with > 1000000 get BIG and <= 1000000 get SMALL in the cell replaced!
df_copy = df.copy()
df_copy.loc[df['Area'] > 1000000, 'Area'] = 'BIG'
df_copy.loc[df['Area'] <= 1000000, 'Area'] = 'SMALL'
print(df_copy)


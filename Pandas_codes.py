import pandas as pd

# Create a Pandas Series

data = [1, 2, 3, 4, 5]

series = pd.Series(data)

# Create a Pandas DataFrame

data = {

    'Name': ['Alice', 'Bob', 'Charlie'],

    'Age': [24, 27, 22]

}

df = pd.DataFrame(data)

print("\nPandas DataFrame:")

print(df)


###########################
print("###########################")
###########################

import pandas as pd

# Sample data

data = {

    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],

    'Age': [24, 27, 22, 32, 29],

    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

}

# Creating DataFrame

df = pd.DataFrame(data)

# Selecting multiple rows by index

print("\nSelecting rows with index 1 and 3:")

print(df.iloc[[1, 3]])

###########################
print("###########################")
###########################

import pandas as pd

import numpy as np

# Sample data with missing values

data = {

    'A': [1, 2, np.nan, 4, 5],

    'B': [np.nan, 10, 20, np.nan, 50],

    'C': ['foo', 'bar', 'baz', 'qux', 'quux']

}

df = pd.DataFrame(data)

# Display the DataFrame with missing values

print("Original DataFrame:")

print(df)

# Fill missing values with a specific value, e.g., 0

df_filled = df.fillna(0)

# Display the DataFrame after filling missing values

print("\nDataFrame after filling missing values with 0:")

print(df_filled)

###########################
print("###########################")
###########################

import pandas as pd

# Creating two small DataFrames

df1 = pd.DataFrame({

    'key': ['A', 'B', 'C', 'D'],

    'value1': [1, 2, 3, 4]

})

df2 = pd.DataFrame({

    'key': ['B', 'D', 'E', 'F'],

    'value2': ['foo', 'bar', 'baz', 'qux']

})

# Performing an inner join on 'key'

inner_join = pd.merge(df1, df2, on='key', how='inner')

print("Inner Join:")

print(inner_join)

# Performing a left join on 'key'

left_join = pd.merge(df1, df2, on='key', how='left')

print("\nLeft Join:")

print(left_join)

###########################
print("###########################")
###########################

import pandas as pd

import matplotlib.pyplot as plt

# Create a sample DataFrame

data = {

    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],

    'Age': [24, 27, 22, 32, 29],

    'Score': [85, 72, 88, 95, 78]

}

df = pd.DataFrame(data)

# Plotting a bar chart

df.plot(kind='bar', x='Name', y='Score', legend=None)

plt.xlabel('Name')

plt.ylabel('Score')

plt.title('Student Scores')

plt.show()
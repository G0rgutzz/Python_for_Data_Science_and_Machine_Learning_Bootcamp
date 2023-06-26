import pandas as pd
import numpy as np
from numpy.random import randn

a = np.random.seed(101)
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])  # data series, rows, columns
print(df)
print(df['W'])  # selecting column
print(df[['W', 'Z']])  # 2 brackets required for the 2 or more columns
df['new'] = df['W'] + df['Y']
print(df)
print(df.drop('new', axis=1))  # removing columns, it is not removing columns from original series
print(df.drop('new', axis=1, inplace=True))  # inplace allows to remove columns from original series
print(df)
print(df.drop('E', axis=0))  # drops rows
print(df.loc['A'])  # selecting rows
print(df.iloc[2])  # returns the row based on it's index location
print(df.loc['C', 'Z'])  # specific result based on the column and row
print(df.loc[['A', 'B'], ['W', 'Y']])

# part 2
booldf = df > 0
print(df[booldf])  # prints nan on the values that doesn't meet the criteria
print(df['W'] > 0)
print(df[df['W'] > 0])  # returns rows where the criteria is true
print(df[df['Z'] < 0])
resultdf = df[df['W'] > 0]
print(resultdf['X'])  # returns the column from the modified df variable
print(df[df['W'] > 0]['X'])  # same as above, it's possible to show more columns as in 9th line
""" the same as above but in the steps
boolser = df['W'] > 0
result = df[boolser]
mycols = ['Y', 'X']
print(result[mycols])"""
# more conditions than 1
print(df[(df['W'] > 0) & (df['Y'] > 1)])  # use & instead of and - and can't work on series of boolean values
print(df[(df['W'] > 0) | (df['Y'] > 1)])  # use | instead of or - same as above

# index
print(df.reset_index())  # index is shown as a column, actual index is numerical
newindex = 'CA NY WY OR CO'.split()  # splits index
print(newindex)
df['States'] = newindex
print(df)
# setting index name
print(df.set_index('States'))
print(df)

# part 3
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))  # creates a list from two arrays
hier_index = pd.MultiIndex.from_tuples(hier_index)  # shows list in form of array, created from the method above
print(hier_index)
df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])  # constructing multi level index data frame
print(df)
print(df.loc['G1'].loc[1])  # prints only G1 index and then sub index 1
df.index.names = ['Groups', 'Numbers']  # labels outside index as groups, and inside as numbers
print(df)
print(df.loc['G1'].loc[2]['A'])
print(df.xs('G1'))  # cross section of rows and columns, it can skip or go inside multi level index
print(df.xs(1, level='Numbers'))  # skips entirely outside index and shows everything with number 1



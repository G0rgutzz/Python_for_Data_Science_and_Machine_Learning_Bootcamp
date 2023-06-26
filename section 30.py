import pandas as pd
import numpy as np
from numpy.random import randn

d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)
print(df)

# dropna - dropping missing values
print(df.dropna(axis=1))  # automatically drops any row with missing values, some for columns, when axis=1
print(df.dropna(thresh=1))  # thresh is value that sets max amount of non nan items per row,
# 1 means row need to have at least 1 normal value, 2 means 2 non nan values etc

# replacing missing values
print(df.fillna(value='a'))  # value= allows to fill in missing values with given argument
print(df['A'].fillna(value=df['A'].mean()))  # sets nan value to mean of the column A


# groupby
data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}
df = pd.DataFrame(data)
print(df)
group1 = df.groupby('Company')
print(group1.mean(numeric_only=True))  # required to work in future versions
print(group1.sum(numeric_only=True).loc['FB'])  # sums up sales made by FB
print(df.groupby('Company').sum(numeric_only=True).loc['FB'])  # faster way to do it
print(df.groupby('Company').count())  # counts the number of instances of each segment
print(df.groupby('Company').max())  # returns the person with the highiest sales from each company, same for min
print(df.groupby('Company').describe())  # shows a lot of informations - st dev, mean, max, min, percentiles etc
# transpose() switches columns with rows

# merging, joining and concatenaiting
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'], 'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'], 'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'], 'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'], 'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])
print(df1)
print(df2)
print(df3)
print(pd.concat([df1, df2, df3]))  # used to concatenate DataFrames,
# dimensions of the frames should match along the axis
print(pd.concat([df1, df2, df3], axis=1))  # concatenating along columns, instead of rows

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

# merge function
print(pd.merge(left, right, how='inner', on='key'))  # merging as in SQL, default is by 'inner',
# on= indicates which column will be used to merge data frames
# concatenating would return twice 'key' column, while merge is merging left and right on it,

# more complicated examples

left1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'], 'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3']})

right1 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'], 'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']})

print(pd.merge(left1, right1, on=['key1', 'key2']))
print(pd.merge(left1, right1, how='outer', on=['key1', 'key2']))
print(pd.merge(left1, right1, how='right', on=['key1', 'key2']))
print(pd.merge(left1, right1, how='left', on=['key1', 'key2']))
# right: use only keys from right frame, similar to a SQL right outer join; preserve key order.
# outer: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically.
# inner: use intersection of keys from both frames, similar to a SQL inner join; preserve the order of the left keys.
# cross: creates the cartesian product from both frames, preserves the order of the left keys
# left: use only keys from left frame, similar to a SQL left outer join; preserve key order.

# joining - join dataframes at the index instead of a column as in merge
left2 = pd.DataFrame({'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']}, index=['K0', 'K1', 'K2'])
right2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'], 'D': ['D0', 'D2', 'D3']}, index=['K0', 'K2', 'K3'])
print(left2.join(right2))
print(right2.join(left2))  # how= can be used in the same way as with merge

# operations
df4 = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'jkl']})
print(df4.head())
print(df4['col2'].unique())  # returns unique values
print(df4['col2'].nunique())  # returns amount of unique values
print(df4['col2'].value_counts())  # returns how many times each value appears
print(df4[(df4['col1'] > 2) & (df4['col2'] < 500)])

# apply


def times2(x):
    return x*2


print(df4['col1'].apply(times2))  # applies function times2 to the col1 in df4
print(df4['col3'].apply(len))  # measures length of each string
print(df4['col2'].apply(lambda x: x*2))  # same as above without defining function
# removing the column
'''print(df4.drop('col1', axis=1, inplace=True)) - drops the column (axis=1) or row (axis=0), action is permanent
'''
# sorting values in df4
print(df4.sort_values('col2'))

# finding null values
print(df4.isnull())
'''df5 = pd.DataFrame({'col1': [1, 2, 3, np.nan], 'col2': [np.nan, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']})
print(df5.head())'''

# pivot table
data1 = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'], 'B': ['one', 'one', 'two', 'two', 'one', 'one'],
         'C': ['x', 'y', 'x', 'y', 'x', 'y'], 'D': [1, 3, 2, 5, 4, 1]}

df5 = pd.DataFrame(data1)
print(df5, '\n')
print(df5.pivot_table(values='D', index=['A', 'B'], columns=['C']))



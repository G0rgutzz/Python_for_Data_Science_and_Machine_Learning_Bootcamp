import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('911.csv')
print(df['zip'].value_counts().head(5))
print(df['twp'].value_counts().head(5))
print(df['title'].nunique())
# x = df['title'].iloc[0].split(':')[0]
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])
print(df['Reason'].value_counts().head(1))  # number 1 reason for 911 calls
# print(df.info())
print(type(df['timeStamp'].iloc[0]))  # it is object, so not a number, iloc and type required to specify it
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)
# print(df['Hour'])
# print(df['Month'])
# print(df['Day of Week'])
dmap = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)
# print(df)
# sns.countplot(x='Day of Week', data=df, hue='Reason')  # countplot with hue based of Reason
# sns.countplot(x='Reason', data=df)
# sns.countplot(x='Month', data=df, hue='Reason')  # months are missing some values
byMonth = df.groupby('Month').count()
# byMonth['lat'].plot()
# sns.lmplot(x='Month', y='twp', data=byMonth.reset_index(),)
df['Date'] = df['timeStamp'].apply(lambda t: t.date())  # () required to work
# print(df.info())
# sns.countplot(data=df, x=df['Date'], color='blue')
# traffic calls
'''
df[df['Reason'] == 'Traffic'].groupby('Date').count()['lat'].plot()
plt.title('Traffic')
# fire calls
df[df['Reason'] == 'Fire'].groupby('Date').count()['lat'].plot()
plt.title('Fire')
# EMS calls
df[df['Reason'] == 'EMS'].groupby('Date').count()['lat'].plot()
plt.title('EMS')
'''
# heatmaps
dfhour = df.groupby(by=['Day of Week', 'Hour']).count()['Reason'].unstack()
dfmonth = df.groupby(by=['Day of Week', 'Month']).count()['Reason'].unstack()
# sns.heatmap(dfhour)
# sns.heatmap(dfmonth)
# sns.clustermap(dfhour)
# sns.clustermap(dfmonth)
# plt.legend()
plt.tight_layout()
plt.show()

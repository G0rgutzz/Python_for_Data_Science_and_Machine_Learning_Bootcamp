import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df1 = pd.read_csv('df1', index_col=0)
df2 = pd.read_csv('df2')
sns.set_style('darkgrid')
# df1['A'].hist(bins=30, color='red')  # automatically creates histogram from the data
# df1['A'].plot(kind='hist', bins=30)  # same as above
# df1['A'].plot.hist()  # same as above
# df2.plot.area(alpha=0.6)  # area plot
# df2.plot.bar()  # it can be show as stacked by stacked=True
# df1['A'].plot.hist(bins=50)
# df1.plot.line(x=df1.index, y='B')  # df1.index doesn't work - it shows that index is not in column
# sns.lineplot(x=df1.index, y='B', data=df1)  # same as above, but works
# df1.plot.scatter(x='A', y='B', size=df1['C']*20, color='C', cmap='coolwarm')
# df2.plot.box()
df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
# df.plot.hexbin(x='a', y='b', gridsize=200, cmap='rainbow')  # hexplot, similar to scatter, but points are in hex
df2['a'].plot.kde()  # density is the same as kde
plt.tight_layout()
plt.show()

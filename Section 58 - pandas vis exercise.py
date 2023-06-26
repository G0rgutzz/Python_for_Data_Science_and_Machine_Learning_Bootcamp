import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df3 = pd.read_csv('df3')
sns.set_style('darkgrid')
plt.style.use('ggplot')
df3.plot.scatter(x='b', y='a', figsize=(12, 6), color='red', size=80)
# df3['a'].plot.hist()
# df3['a'].hist(bins=50, color='red', alpha=0.6)
# df3[['a', 'b']].plot.box()
# df3['d'].plot.kde(linewidth=3, linestyle='dashed')
# df3[0:30].plot.area().legend(loc=6, bbox_to_anchor=(1, 0.5))  # shows rows from 0 to 30
plt.show()

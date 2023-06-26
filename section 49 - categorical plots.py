import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

tips = sns.load_dataset('tips')
# print(tips.head())
# sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)  # deafult function is mean()
# sns.countplot(x='sex', data=tips)  # traces number of occurences
# sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')  #
# sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)  # shows kde of the actual plot
# sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex')
# jitter adds random noise to see what points are stuck on each other
# sns.violinplot(x='day', y='total_bill', data=tips)
# sns.swarmplot(x='day', y='total_bill', data=tips, color='black')
# stripplot but points are adjsuted so they don't overlap
# possible to stack violin and swarm plots together one on top of another, to show more info
# sns.catplot(x='day', y='total_bill', data=tips, kind='bar')  # used to be factorplot
# plt.tight_layout()
# plt.show()

# matrix plots
flights = sns.load_dataset('flights')  # number of passengers in the given month od the year
tc = tips.corr(numeric_only=True)
# sns.heatmap(tc, annot=True, cmap='coolwarm')  # annot shows values, cmap allows for different colors
fp = flights.pivot_table(index='month', columns='year', values='passengers')
# sns.heatmap(fp, cmap='magma', linecolor='white', linewidths=1)
# sns.clustermap(fp, standard_scale=1)  # clusters information to show which arguments are similar to each other
# plt.tight_layout()
# plt.show()

# grids
iris = sns.load_dataset('iris')
# sns.pairplot(iris)  # creates plots of for pairs of every variable
# g = sns.PairGrid(iris)
# g.map(plt.scatter)  # makes every chart scatter plot
# g.map_diag(sns.histplot)  # plots on the diagonal
# g.map_upper(plt.scatter)  # plots on the upper part of the diagonal
# g.map_lower(sns.kdeplot)  # plots on the lower part of the diagonal
# h = sns.FacetGrid(tips, col='time', row='smoker')
# h.map(sns.histplot, 'total_bill', kde=True)  # name of the plot, number of req data points
# plt.tight_layout()
# plt.show()

# regression plots
# sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o', 'v'], scatter_kws={'s': 50})
# scatter_kws - dictionary with number of variables for the plot (size, position, colour of the markers etc
# sns.lmplot(x='total_bill', y='tip', data=tips, col='day', row='time', hue='sex',
#           aspect=0.6)

# plt.tight_layout()
# plt.show()

# style and color
# sns.set_style('whitegrid')  # set style of the background
# white, darkgrid, ticks, whitegrid
# sns.despine()  # removes axis on the top and right, left=True and bottom=True removes rest
# plt.figure(figsize=(12, 6))
# sns.set_context('poster', font_scale=3)
# sns.countplot(x='sex', data=tips)
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='seismic')  # matplotlib colormap in google
plt.tight_layout()
plt.show()

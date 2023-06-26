import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
tc = titanic.corr(numeric_only=True)
# print(titanic.head())
# sns.jointplot(x='fare', y='age', data=titanic)
# sns.displot(titanic['fare'], bins=30, color='red')
# sns.boxplot(x='class', y='age', data=titanic, palette='rainbow')
# sns.swarmplot(x='class', y='age', data=titanic, palette='magma', size=3)
# sns.countplot(x='sex', data=titanic)
# sns.heatmap(tc, annot=False, cmap='coolwarm')
# plt.title('titanic.corr')
h = sns.FacetGrid(titanic, col='sex')
h.map(sns.histplot, 'age', kde=False)
plt.tight_layout()
plt.show()

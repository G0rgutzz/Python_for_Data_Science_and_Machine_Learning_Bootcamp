import pandas as pd
import numpy as np
import cufflinks as cf
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True)
cf.go_offline()

df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
print(df.head())
df2 = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Values': [32, 43, 50]})
# df.iplot(kind='scatter', x='A', y='B')  # doesn't work in pycharm

# fig = px.line(df, x=df.index, y=df.columns)
# fig.add_scatter(x=df.index, y=df['B'])
# fig.add_scatter(x=df.index, y=df['C'])
# fig.add_scatter(x=df.index, y=df['D'])  # works the same way as above but it's longer
# fig = px.scatter(df, x='A', y='B', size=100)
# fig = px.bar(df2, x='Category', y='Values')
# fig = px.bar(df.std())  # I can use functions as a variables, columns are assigned automatically
# fig = px.box(df)
df3 = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 20, 30, 20, 10], 'z': [500, 400, 300, 200, 100]})
# fig = go.Figure(data=[go.Surface(z=df3.values, colorscale='Earth')])  # surface plot
# colors: Blackbody,Bluered,Blues,Cividis,Earth,Electric,Greens,Greys,Hot,
# Jet,Picnic,Portl and,Rainbow,RdBu,Reds,Viridis,YlGnBu,YlOrRd.
# fig = px.histogram(df, nbins=50)
# fig = px.line(df[['A', 'B']])  # spread plot to do, so far it's only line
# fig = px.scatter(df, x=df.index, y=df.columns)  # bubble plot, doesn't work so far
# fig = go.Figure(data=[go.Scatter(x=df['A'], y=df['B'], mode='markers', marker_size=df['C'].abs()*100)])
# bubble that works
fig = px.scatter_matrix(df)  # creates matrix of plots for every value in the data frame
fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01), title='random',
                  )
fig.update_traces(marker_line_width=1, marker_line_color="black")  # borderline
# autosize=False, width=500, height=500, margin=dict(l=65, r=50, b=65, t=90)
fig.show(renderer="browser")






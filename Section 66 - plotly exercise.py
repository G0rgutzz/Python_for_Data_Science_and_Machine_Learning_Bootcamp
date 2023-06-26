import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('2014_World_Power_Consumption')
# print(df.head())  # power consumption is in WH, not KWH
data = dict(type='choropleth', colorscale='YlOrRd', locations=df['Country'], text=df['Text'],
            locationmode='country names', z=df['Power Consumption KWH'],
            colorbar={'title': 'TWH'},
            )
layout = dict(title='2014 World Power Consumption',
              geo=dict(showframe=False, projection={'type': 'mercator'}))
# fig = go.Figure(data=[data], layout=layout)
df1 = pd.read_csv('2012_Election_Data')
print(df1.info())

data1 = dict(type='choropleth', colorscale='YlOrRd', locations=df1['State Abv'], text=df1['State'],
             locationmode='USA-states', z=df1['Voting-Age Population (VAP)'],
             colorbar={'title': 'Number of people'},)
layout1 = dict(title='2012 Election Voting',
               geo=dict(scope='usa', showlakes=True, lakecolor='rgb(85,173,240)'))
fig = go.Figure(data=[data1], layout=layout1)
fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01), title='USA states')
fig.update_traces(marker_line_width=1, marker_line_color="black")  # borderline
fig.show()

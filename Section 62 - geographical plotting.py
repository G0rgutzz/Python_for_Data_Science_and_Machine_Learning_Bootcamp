import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import pandas as pd

data = dict(type='choropleth', locations=['AZ', 'CA', 'NY'], locationmode='USA-states',
            colorscale='Portland', text=['text1', 'text2', 'text3'], z=[1.0, 2.0, 3.0],
            colorbar={'title': 'colors'})
layout = dict(geo={'scope': 'usa'})
# fig = go.Figure(data=[data], layout=layout)
df = pd.read_csv('2011_US_AGRI_Exports')
data1 = dict(type='choropleth', colorscale='YlOrRd', locations=df['code'], text=df['text'],
             locationmode='USA-states', z=df['total exports'], colorbar={'title': 'Millions USD'},
             marker=dict(line=dict(color='rgb(255, 255, 255)', width=2)))
layout1 = dict(title='2011 US Agriculture Exports by state',
               geo=dict(scope='usa', showlakes=True, lakecolor='rgb(85,173,240)'))
# fig = go.Figure(data=[data1], layout=layout1)
df1 = pd.read_csv('2014_World_GDP')
data2 = dict(type='choropleth', colorscale='YlOrRd', locations=df1['CODE'], text=df1['COUNTRY'],
             z=df1['GDP (BILLIONS)'], colorbar={'title': 'GDP in Billions USD'},
             )
layout2 = dict(title='2014 Global GDP',
               geo=dict(showframe=False, projection={'type': 'mercator'}))
fig = go.Figure(data=[data2], layout=layout2)
fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01), title='USA states',
                  margin=dict(l=50, r=30, t=30, b=30))
# fig.update_traces(marker_line_width=1, marker_line_color="black")  # borderline
fig.show()

import pandas as pd
from sqlalchemy import create_engine

# reading and writing from csv file
a = pd.read_csv('example')
print(a)
a.to_csv('My_output', index=False)
b = pd.read_csv('My_output')

# reading and writing from excel file
c = pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1').set_index([' '])
print(c)

c.to_excel('Excel1.xlsx', sheet_name='Sheet1')

# reading from html

d = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
print(d)
d[0].to_excel('Excel3.xlsx', sheet_name="Sheet1")
''' it doesn't work
engine = create_engine('sqlite:///:memory:')
a.to_sql('my_table', engine)
e = pd.read_sql('my_table', con=engine)
print(e)'''

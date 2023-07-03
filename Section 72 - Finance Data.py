from pandas_datareader import data, wb, Options
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)

'''
aapl = Options('aapl', 'yahoo')
data1 = aapl.get_call_data()
print(data1)

f = data.DataReader('BAC', 'iex', start, end)
print(f)  doesn't work
'''

# Bank of America
BAC = data.DataReader('BAC', 'yahoo', start, end)
print(BAC)
# asdf
'''
# CitiGroup
C = data.DataReader("C", 'yahoo', start, end)

# Goldman Sachs
GS = data.DataReader("GS", 'yahoo', start, end)

# JPMorgan Chase
JPM = data.DataReader("JPM", 'yahoo', start, end)

# Morgan Stanley
MS = data.DataReader("MS", 'yahoo', start, end)

# Wells Fargo
WFC = data.DataReader("WFC", 'yahoo', start, end)
'''
# plt.show()

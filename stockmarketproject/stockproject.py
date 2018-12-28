import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import pandas_datareader
import datetime
import pandas_datareader.data as web

start = datetime.datetime(2012,1,1)
end = datetime.datetime(2017,1,1)

tesla = web.DataReader('TSLA', 'google', start, end)

ford = web.DataReader('F', 'google', start, end)

gm = web.DataReader('GM', 'google', start, end)

tesla['Open'].plot(label='Test', figsize=(12,8),title='Opening Prices')
gm['Open'].plot(label='GM')
ford['Open'].plot(label='Ford')
plt.legend()


tesla['Volume'].plot(label='Test', figsize=(12,8),title='Volume Traded')
gm['Volume'].plot(label='GM')
ford['Volume'].plot(label='Ford')
plt.legend()

ford['Volume'].argmax()

ford['Open'].plot(figsize=(20,6))
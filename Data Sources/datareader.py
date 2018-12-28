import pandas_datareader.data as web
import datetime
start = datetime.datetime(2015,1,1)
end = datetime.datetime(2017,1,1)
Facebook = web.DataReader('FB','google',start,end)
facebook.head()

from pandas_datareader. data import import Option
fb_options = Options('FB', 'google')

options_df = fb_options.get_options_data(expiry=fb_options.expiry_data(0))
import pandas_datareader.data as web
import pandas as pd  # for storing and manipulating the data we get back
import datetime as dt  # for dealing with times


def get_bars(symbol, interval='1h'):
    root_url = 'https://api.binance.com/api/v1/klines'
    url = root_url + '?symbol=' + symbol + '&interval=' + interval
    data = json.loads(requests.get(url).text)
    df = pd.DataFrame(data)
    df.columns = ['open_time',
                  'o', 'h', 'l', 'c', 'v',
                  'close_time', 'qav', 'num_trades',
                  'taker_base_vol', 'taker_quote_vol', 'ignore']
    df.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in df.close_time]
    return df


steemeth = get_bars('STEEMETH')
ethusdt = get_bars('ETHUSDT')
steemusdt = steemeth['c'].astype('float') * ethusdt['c'].astype('float')

steemusdt.plot(figsize=(16, 9))
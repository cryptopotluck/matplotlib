from binance.client import Client
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime
import keys
client = Client(keys.APIKey, keys.SecretKey)



# fetch 1 minute klines for the last day up until now
klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1HOUR, "1 day ago UTC")



times = []
for d in klines:
    times.append(d[0])


count = 0
timesreadable =[]
while (count < len(times)-1):
    count = count + 1
    readable = time.ctime(times[count])
    #print(readable)
    timesreadable.append([readable])

print()
print(timesreadable)
print()
print()
print()
print(klines)


#trades = client.get_historical_trades(symbol='BNBBTC')[0]['time']
#trades2 = client.get_historical_trades(symbol='BNBBTC')

#readable = time.ctime(1540023060000)
#print(readable)
#print(readable)
#print(trades2)

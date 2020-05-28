# Bollinger-Band

Gather the daily prices for Apple over the period 2015-2018

```python

import pandas as pd

import pandas_datareader.data as web

import matplotlib.pyplot as plt

from datetime import datetime

start = datetime(2015, 1, 1)
end = datetime(2018, 1, 1)

Symbols = ['AAPL']


df = pd.DataFrame()


for sym in Symbols:
    df[sym] = web.DataReader(sym,'iex', start, end)['open']
rolling =df.rolling(window = 21)  

rollingMean =rolling.mean()
std = rolling.std()

upperBand = rollingMean+std*2
lowerBand = rollingMean-std*2


plt.plot(df)
plt.plot(upperBand)
plt.plot(lowerBand)
plt.show()
```

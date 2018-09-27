
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import statsmodels.api as sm
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
start = datetime(2015, 2, 9)
end = datetime(2017, 5, 24)

Symbols = ['SPY','MSFT','AMZN']

data = pd.DataFrame()

for sym in Symbols:
    data[sym] = web.DataReader(sym,'iex', start, end)['open']

res = sm.OLS(data['SPY'],data[['MSFT','AMZN']]).fit()
print(res.summary())
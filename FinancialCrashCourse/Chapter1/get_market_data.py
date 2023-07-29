import numpy as np
import pandas as pd
import pandas_datareader.data as data
import datetime as dt
import matplotlib.pyplot as plt

ticker = 'TSLA'

data_source = 'yahoo'
start = dt.datetime(2018, 1 ,1)
end = dt.datetime.today()
df= data.DataReader(ticker, data_source, start, end)

#print(df.tail(10))

df['Log_Ret'] = np.log(df['Close'] / df['Close'].shift(1))
df['Volatility']= (df['Log_Ret'].rolling(window=252).std()) * np.sqrt(252)
print(df.tail(10))

plt.plot(df['Close'], df['Log_Ret'])
plt.show()
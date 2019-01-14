import datetime as dt
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd
import pandas_datareader.data as data

ticker = 'USDTRY=X'

df = pd.read_csv('{}.csv'.format(ticker), parse_dates=True, index_col=0)

df['200ma'] = df['Adj Close'].rolling(window=200, min_periods=0).mean()
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
df['50ma'] = df['Adj Close'].rolling(window=50, min_periods=0).mean()
df['15ma'] = df['Adj Close'].rolling(window=15, min_periods=0).mean()
df['10ma'] = df['Adj Close'].rolling(window=10, min_periods=0).mean()
df['5ma'] = df['Adj Close'].rolling(window=5, min_periods=0).mean()

print('TICKER:',ticker)
print(df.tail(5))
df.tail(250).to_csv('{}_analysis.csv'.format(ticker))

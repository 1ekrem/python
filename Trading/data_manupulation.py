import datetime as dt
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd
import pandas_datareader.data as data

style.use('ggplot')

ticker = 'AAPL'

df = pd.read_csv('stock_dfs/{}.csv'.format(ticker), parse_dates=True, index_col=0)

# Let's create a new column - 100, 50, 10, 5 Moving Averages
# min_perios=0 --> Does not require any date to start.
x100 = df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
x50 = df['50ma'] = df['Adj Close'].rolling(window=50, min_periods=0).mean()
x10 = df['10ma'] = df['Adj Close'].rolling(window=10, min_periods=0).mean()
x5 = df['5ma'] = df['Adj Close'].rolling(window=5, min_periods=0).mean()

ax1 = plt.subplot2grid((6,1),(0,0), rowspan=5, colspan=1)
#sharex will go aling with box charts when zoom in.
ax2 = plt.subplot2grid((6,1),(5,0), rowspan=1, colspan=1, sharex=ax1)


ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

print('Ticker:', ticker)
print(df.tail(10))

d100= x100[-1]
d50= x50[-1]
d10= x10[-1]
d5= x5[-1]


if  d10 > d100:
    print("10 day is above 100 day")
if d10 > d50:
    print("10 day is above 50 day")
if d10 > d5:
    print("10 day is above 5 day")

if d5 > d100:
    print("5 day is above 100 day")

if d5 > d50:
    print("5 day is above 50 day")
else:
    print('50 day is above 5 day-->','Delta: ', d5 - d50)
if d5 > d10:
    print("5 day is above 10 day")



#plt.show()

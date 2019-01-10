import datetime as dt
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd
import pandas_datareader.data as data

style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

# Let's create a new column - 100, 50, 10, 5 Moving Averages
# min_perios=0 --> Does not require any date to start.
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
df['50ma'] = df['Adj Close'].rolling(window=50, min_periods=0).mean()
df['10ma'] = df['Adj Close'].rolling(window=10, min_periods=0).mean()
df['5ma'] = df['Adj Close'].rolling(window=5, min_periods=0).mean()

ax1 = plt.subplot2grid((6,1),(0,0), rowspan=5, colspan=1)
#sharex will go aling with box charts when zoom in.
ax2 = plt.subplot2grid((6,1),(5,0), rowspan=1, colspan=1, sharex=ax1)


ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

print(df.tail())

plt.show()

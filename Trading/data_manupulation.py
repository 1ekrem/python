import datetime as dt
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd
import pandas_datareader.data as data

#ticker = 'V'
ticker = input(str("Enter ticker: "))

df = pd.read_csv('{}.csv'.format(ticker), parse_dates=True, index_col=0)

df['200ma'] = df['Close'].rolling(window=200, min_periods=0).mean()

#RSI
delta = df['Close'].diff()
window = 14
up_days = delta.copy()
up_days[delta<=0]=0.0
down_days = abs(delta.copy())
down_days[delta>0]=0.0
RS_up = up_days.rolling(window).mean()
RS_down = down_days.rolling(window).mean()
rsi= 100-100/(1+RS_up/RS_down)
df['RSI']=rsi

#CCI
# ndays=20
# TP = (df['High'] + df['Low'] + df['Close']) / 3 
# CCI = pd.Series((TP - df.rolling(TP, ndays).mean())) / (0.015*df.rolling_std(TP, ndays)), name = 'CCI') 
# dataCCI = df.join(CCI) 
# df['CCI-20']=dataCCI

print('TICKER:',ticker)
print(df.tail(5))
#df.tail(250).to_csv('{}_analysis.csv'.format(ticker))

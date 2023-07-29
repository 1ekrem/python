import datetime as dt
# import matplotlib.pyplot as plt 
# from matplotlib import style
import pandas as pd
import pandas_datareader.data as data
import os
import ta
import openpyxl
import numpy as np
import datetime
import sqlalchemy
import pyodbc
import startegies
import yfinance as yf

from ta import add_all_ta_features
from ta.utils import dropna

ticker = input(str("Enter ticker: "))
#ticker = 'FB'

today = dt.datetime.today()

last_year_today = today - dt.timedelta(days=365)
print(today, last_year_today)

data_source = 'yahoo'
start = last_year_today
#end = dt.datetime(2022, 2 ,14)
end = today
# df= data.DataReader(ticker, data_source, start, end)
df = yf.download(ticker, start, end)
#df.to_csv('C:\\PythonClass\\ta-ticker\\{}.csv'.format(ticker))
#print("Stock prices of {} is pulled!".format(ticker))
#df = pd.read_csv('C:\\PythonClass\\ta-ticker\\{}.csv'.format(ticker), parse_dates=True, index_col=0)
df['200ma'] = df['Adj Close'].rolling(window=200, min_periods=0).mean()
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
df['50ma'] = df['Adj Close'].rolling(window=50, min_periods=0).mean()
df['20ma'] = df['Adj Close'].rolling(window=20, min_periods=0).mean()
df['10ma'] = df['Adj Close'].rolling(window=10, min_periods=0).mean()
df['5ma'] = df['Adj Close'].rolling(window=5, min_periods=0).mean()

print("Moving Averages are created!")

"""Calculate RSI - Relative Strenght Index"""
delta = df['Close'].diff()
window = 14
up_days = delta.copy()
up_days[delta<=0]=0.0
down_days = abs(delta.copy())
down_days[delta>0]=0.0
RS_up = up_days.rolling(window).mean()
RS_down = down_days.rolling(window).mean()
rsi= 100-100/(1+RS_up/RS_down)
# df['RSISensitive']=rsi
df['RSIST'] = rsi.astype('float')
#print("Relative Strenght Index of 14 is created!")

# """Calculate CCI - Commodity Channel Index"""
# ndays=21
# TP = (df['High'] + df['Low'] + df['Close']) / 3 
# df['CCI'] = pd.Series((TP - TP.rolling(ndays).mean()) / (0.014 * TP.rolling(ndays).std()),name = 'CCI')
# df['CCI'] = df['CCI'].astype('float')

#print("Commodity Channel Index of 21 is created!")

""" VOLUME INDICATORS """
df['moneyIndexFlow'] = ta.volume.money_flow_index(df['High'],df['Low'],df['Close'],df['Volume'])
df['volumePriceTrend'] = ta.volume.volume_price_trend(df['Close'],df['Volume'])
df['VWAP'] = ta.volume.volume_weighted_average_price(df['High'],df['Low'],df['Close'],df['Volume'])
df['MarketPressure'] = ta.volume.force_index(df['Close'],df['Volume'])/100


""" MOMENTUM INDICATORS """
df['RSI'] = ta.momentum.rsi(df['Close'])
df['AwesomeOscillator'] = ta.momentum.awesome_oscillator(df['High'],df['Low'])
df['RateOfChageINC'] = ta.momentum.roc(df['Close'])

""" VOLATILITY INDICATORS """
df['BBLowerValue'] = ta.volatility.bollinger_hband(df['Close'])
df['BBUpper'] = ta.volatility.bollinger_hband_indicator(df['Close'])

df['BBLowerValue'] = ta.volatility.bollinger_lband(df['Close'])
df['BBLower'] = ta.volatility.bollinger_lband_indicator(df['Close'])

df['BBPercentage'] = ta.volatility.bollinger_pband(df['Close'])
df['BBWidth'] = ta.volatility.bollinger_wband(df['Close'])

""" TREND INDICATORS """
df['BearishVortex'] = ta.trend.vortex_indicator_neg(df['High'],df['Low'],df['Close'])
df['BullishVortex'] = ta.trend.vortex_indicator_pos(df['High'],df['Low'],df['Close'])
df['DownTrend'] = ta.trend.psar_down_indicator(df['High'],df['Low'],df['Close'])
df['UpTrend'] = ta.trend.psar_up_indicator(df['High'],df['Low'],df['Close'])
df['ADXIndicator']=ta.trend.adx(df['High'],df['Low'],df['Close'], window=14)
df['CCI'] = ta.trend.cci(df['High'],df['Low'],df['Close'], window=20)

""" EXPONENTIAL MOVING AVERAGE """
# ema9 = ta.trend.EMAIndicator(df['Close'],9)
# #df['9EMA'] = ta.add_momentum_ta(df['High'],df['Low'],df['Close'],df['Volume'])
df['9EMA'] = ta.trend.ema_indicator(df['Close'],window=9)


"""Additional Info"""
df['Ticker'] = ticker
df['RunTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

"""Exponentail Moving Average"""

""" Calculated Signals """
#df.loc[df['VWAP'] > df['Close'], 'VWAP-Status'] = 'Above'
#df.loc[df['VWAP'] < df['Close'], 'VWAP-Status'] = 'Below'
df['VWAPStatus2'] = np.where(df['VWAP'] > df['Close'], 'Above', 'Below')
df['BuyLT'] = np.where((df['5ma'] < df['10ma']) & (df['5ma'] < df['20ma']) & (df['10ma'] < df['20ma']) & (df['RSI'] < 35), 'BUY', '-')
df['BuyST'] = np.where((df['5ma'] < df['10ma']) & (df['5ma'] < df['20ma']) & (df['10ma'] < df['20ma']) & (df['RSIST'] < 35), 'BUY', '-')
df['Sell'] = np.where((df['5ma'] > df['10ma']) & (df['10ma'] > df['20ma']) & (df['RSI'] > 75), 'SELL', '-')
#df['InConsolidation'] = startegies.is_consolidation(df['Close'],2.5)


df['Adj_Close']= df['Adj Close']

dataset = df[['High'
           ,'Low'
           ,'Open'
           ,'Close'
           ,'Adj_Close'
           ,'RSIST'
           ,'CCI'
           ,'moneyIndexFlow'
           ,'VWAP'
           ,'RSI'
           ,'BBUpper'
           ,'BBLower'
           ,'BBPercentage'
           ,'BBWidth'
           ,'DownTrend'
           ,'UpTrend'
           ,'VWAPStatus2'
           ,'Ticker'
           ,'Close'
           ,'BuyLT'
           #,'BUYS2'
           ,'Sell'
           ,'9EMA'
           ,'ADXIndicator'
        #    ,'InConsolidation'
           ]]

## Console Printing Set
consoleDataset = df[['High'
           ,'Low'
           ,'Open'
           ,'RSIST'
           ,'CCI'
           ,'moneyIndexFlow'
           ,'volumePriceTrend'
           ,'VWAP'
           ,'MarketPressure'
           ,'RSI'
           ,'BBPercentage'
           ,'BBWidth'
           ,'DownTrend'
           ,'UpTrend'
           ,'VWAPStatus2'
           ,'Ticker'
           ,'Close'
           ,'BuyLT'
           ,'BuyST'
           ,'Sell'
           ,'9EMA'
           ,'ADXIndicator'
        #    ,'InConsolidation'
           ]]

print(consoleDataset.tail(20))

consoleDataset.to_excel("C:\\Users\\ekrem\\Desktop\\Trade Analysis\\{}.xlsx".format(ticker))
print("file is ready")

# todayD = dt.datetime.today().strftime('%Y-%m-%d')
# df['date'] = todayD

# textFileDataset = df[[
#            'Ticker'
#            ,'Close'
#            ,'BuyLT'
#            ,'Sell'
#            ,'date'
#            ]]

# textFileDataset.tail(1).to_csv("{}.txt".format(todayD))
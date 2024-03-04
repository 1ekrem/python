import yfinance as yf
import datetime
from pushover import pushNotificationSender

# # Define the stock symbol and the date range
# symbol = input("Enter Ticker: ")  # Change this to the desired stock symbol
# start_date = datetime.datetime.now() - datetime.timedelta(days=5)  # 7 days ago
# end_date = datetime.datetime.now()

# # Download the stock data
# data = yf.download(symbol, start=start_date, end=end_date, interval="1m")

# # Print the data
# print(data)


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
import yfinance as yf

from ta import add_all_ta_features
from ta.utils import dropna

# ticker = input(str("Enter ticker: "))
#ticker = 'FB'


def bulkRunner(ticker):
    today = dt.datetime.today()
    data_source = 'yahoo'
    # start = dt.datetime(today.year -1, today.month -1 ,1)
    #end = dt.datetime(2022, 2 ,14)
    end = today
    start = datetime.datetime.now() - datetime.timedelta(days=5)  # 7 days ago
    end = datetime.datetime.now()
    try:
        df= yf.download(ticker, start, end, progress=False, interval="1m")
    except IndexError:
        pass
    
    # Create Moving Averages 
    df['200ma'] = df['Adj Close'].rolling(window=200, min_periods=0).mean()
    df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
    df['50ma'] = df['Adj Close'].rolling(window=50, min_periods=0).mean()
    df['20ma'] = df['Adj Close'].rolling(window=20, min_periods=0).mean()
    df['10ma'] = df['Adj Close'].rolling(window=10, min_periods=0).mean()
    df['5ma'] = df['Adj Close'].rolling(window=5, min_periods=0).mean()

    # Calculate RSI - Relative Strenght Index
    delta = df['Close'].diff()
    window = 14
    up_days = delta.copy()
    up_days[delta<=0]=0.0
    down_days = abs(delta.copy())
    down_days[delta>0]=0.0
    RS_up = up_days.rolling(window).mean()
    RS_down = down_days.rolling(window).mean()
    rsi= 100-100/(1+RS_up/RS_down)
    df['RSIST'] = rsi.astype('float')

    # VOLUME INDICATORS
    df['moneyIndexFlow'] = ta.volume.money_flow_index(df['High'],df['Low'],df['Close'],df['Volume'])
    df['volumePriceTrend'] = round(ta.volume.volume_price_trend(df['Close'],df['Volume']),2)
    df['VWAP'] = ta.volume.volume_weighted_average_price(df['High'],df['Low'],df['Close'],df['Volume'])
    df['MarketPressure'] = round(ta.volume.force_index(df['Close'],df['Volume'])/100,2)


    # MOMENTUM INDICATORS
    df['RSI'] = ta.momentum.rsi(df['Close'])
    df['AwesomeOscillator'] = ta.momentum.awesome_oscillator(df['High'],df['Low'])
    df['RateOfChageINC'] = ta.momentum.roc(df['Close'])
    #df['StochRSI'] = ta.StochRSIIndicator(df['Close'])

    # VOLATILITY INDICATORS
    df['BBLowerValue'] = ta.volatility.bollinger_hband(df['Close'])
    df['BBUpper'] = ta.volatility.bollinger_hband_indicator(df['Close'])

    df['BBLowerValue'] = ta.volatility.bollinger_lband(df['Close'])
    df['BBLower'] = ta.volatility.bollinger_lband_indicator(df['Close'])

    df['BBPercentage'] = ta.volatility.bollinger_pband(df['Close'])
    df['BBWidth'] = ta.volatility.bollinger_wband(df['Close'])

    # TREND INDICATORS
    df['BearishVortex'] = ta.trend.vortex_indicator_neg(df['High'],df['Low'],df['Close'])
    df['BullishVortex'] = ta.trend.vortex_indicator_pos(df['High'],df['Low'],df['Close'])
    df['DownTrend'] = ta.trend.psar_down_indicator(df['High'],df['Low'],df['Close'])
    df['UpTrend'] = ta.trend.psar_up_indicator(df['High'],df['Low'],df['Close'])
    df['CCI'] = ta.trend.cci(df['High'],df['Low'],df['Close'], window=20)

    # EXPONENTIAL MOVING AVERAGE
    df['9EMA'] = ta.trend.ema_indicator(df['Close'],window=9)

    # Additional Info
    df['Ticker'] = ticker
    # df['RunTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    df['Adj_Close'] = df['Adj Close']
    df['VWAPStatus'] = np.where(df['VWAP'] > df['Close'], 'WVAP > Price', 'Price > WVAP')


    #Signals
    # df['BuyLT'] = np.where((df['5ma'] < df['10ma']) & (df['5ma'] < df['20ma']) & (df['10ma'] < df['20ma']) & (df['RSI'] < 35), 'BUY', '-')
    df['Buy'] = np.where((df['5ma'] < df['10ma']) & (df['5ma'] < df['20ma']) & (df['10ma'] < df['20ma']) & (df['RSIST'] < 35), 'BUY', '-')
    df['Sell'] = np.where((df['5ma'] > df['10ma']) & (df['10ma'] > df['20ma']) & (df['RSI'] > 75), 'SELL', '-')

    

    ## Console Printing Set
    consoleDataset = df[['High'
            ,'Low'
            ,'Open'
            ,'RSIST'
            ,'CCI'
            ,'moneyIndexFlow'
            ,'MarketPressure'
            ,'volumePriceTrend'
            ,'RSI'
            ,'VWAPStatus'
            ,'Ticker'
            ,'Close'
            ,'Buy'
            ,'Sell'
            ]]
    
    # print(consoleDataset)
    
    # consoleDataset.to_csv("{}_OneMin_Test.csv".format(ticker))

    #consoleDataset = consoleDataset.tail(1)


    for index, column in consoleDataset.iterrows():
        if (column['Buy'] == 'BUY'):
            print(ticker,":", "BUY")
            return ("0DTE Flow:",ticker,"BUY")
        
        elif (column['Sell'] == 'SELL'):
            print(ticker,":", "SELL")
            return ("0DTE Flow:",ticker,"SELL")
    else: pass

result = bulkRunner("SPY")
if result is not None:
        pushNotificationSender(result)
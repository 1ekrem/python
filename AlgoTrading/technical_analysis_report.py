import datetime as dt
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd
import pandas_datareader.data as data
import os
import ta
import openpyxl
import numpy as np
from pandas_datareader._utils import RemoteDataError
import yfinance as yf
# import datetime

#ticker = input(str("Enter ticker: "))
#ticker = 'CCIV'



def technical_analysis_report(ticker):
    global df
    try:
        data_source = 'yahoo'
        start = dt.datetime(2018, 1 ,1)
        end = dt.datetime.today()
        ##df= data.DataReader(ticker, data_source, start, end)
        df = yf.download(ticker, start, end)
    except KeyError:
        pass
    
    except RemoteDataError:
        print("{} not found".format(ticker))
        pass
    #df.to_csv('C:\\PythonClass\\ta-ticker\\{}.csv'.format(ticker))
    #print("Stock prices of {} is pulled!".format(ticker))
    #df = pd.read_csv('C:\\PythonClass\\ta-ticker\\{}.csv'.format(ticker), parse_dates=True, index_col=0)
    df['200ma'] = df['Adj Close'].rolling(window=200, min_periods=0).mean()
    df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
    df['50ma'] = df['Adj Close'].rolling(window=50, min_periods=0).mean()
    df['20ma'] = df['Adj Close'].rolling(window=20, min_periods=0).mean()
    df['10ma'] = df['Adj Close'].rolling(window=10, min_periods=0).mean()
    df['5ma'] = df['Adj Close'].rolling(window=5, min_periods=0).mean()

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
    df['RSISensitive']=rsi
    df['RSISensitive'] = df['RSISensitive'].astype('float')
    #print("Relative Strenght Index of 14 is created!")

    """Calculate CCI - Commodity Channel Index"""
    ndays=21
    TP = (df['High'] + df['Low'] + df['Close']) / 3 
    df['CCI'] = pd.Series((TP - TP.rolling(ndays).mean()) / (0.014 * TP.rolling(ndays).std()),name = 'CCI')
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
    df['BB-Upper'] = ta.volatility.bollinger_hband_indicator(df['Close'])

    df['BBLowerValue'] = ta.volatility.bollinger_lband(df['Close'])
    df['BB-Lower'] = ta.volatility.bollinger_lband_indicator(df['Close'])

    df['BBPercentage'] = ta.volatility.bollinger_pband(df['Close'])
    df['BBWidth'] = ta.volatility.bollinger_wband(df['Close'])

    """ TREND INDICATORS """
    df['BearishVortex'] = ta.trend.vortex_indicator_neg(df['High'],df['Low'],df['Close'])
    df['BullishVortex'] = ta.trend.vortex_indicator_pos(df['High'],df['Low'],df['Close'])
    df['DownTrend'] = ta.trend.psar_down_indicator(df['High'],df['Low'],df['Close'])
    df['UpTrend'] = ta.trend.psar_up_indicator(df['High'],df['Low'],df['Close'])

    """Additional Info"""
    df['Ticker'] = ticker
    df['RunTime'] = dt.datetime.now().strftime("%Y-%m-%d %H:%M")

    """ Calculated Technicals """
    #df.loc[df['VWAP'] > df['Close'], 'VWAP-Status'] = 'Above'
    #df.loc[df['VWAP'] < df['Close'], 'VWAP-Status'] = 'Below'
    df['VWAP-Status-2'] = np.where(df['VWAP'] > df['Close'], 'Above', 'Below')
    df['BUY'] = np.where((df['5ma'] < df['10ma']) & (df['5ma'] < df['20ma']) & (df['10ma'] < df['20ma']) & (df['RSI'] < 35), 'BUY', '-')
    df['SELL'] = np.where((df['5ma'] > df['10ma']) & (df['5ma'] > df['20ma']) & (df['10ma'] > df['20ma']) & (df['RSI'] > 70), 'SELL', '-')

    dataset = df[['High'
               ,'Low'
               ,'Open'
               ,'Close'
               ,'Adj Close'
               ,'RSISensitive'
               ,'CCI'
               ,'moneyIndexFlow'
               ,'VWAP'
               ,'RSI'
               ,'BB-Lower'
               ,'BB-Upper'
               ,'BBPercentage'
               ,'BBWidth'
               ,'DownTrend'
               ,'UpTrend'
               ,'VWAP-Status-2'
               ,'Ticker'
               ,'Close'
               ,'BUY'
               ,'SELL'
               ]]
    

    dataset.tail(250).to_excel('C:\\Users\\ekrem\\Desktop\\Trade Analysis\\{}_New-TA-analysis.xlsx'.format(ticker))
    print("Technical Analysis Report of {} is ready!".format(ticker))

    todayD = dt.datetime.today().strftime('%Y-%m-%d')

    textFileDataset = df[['Ticker','Close','BUY','SELL','RunTime']]

    textFileDataset.tail(1).to_csv("C:\\PythonClass\\AlgoTrading\\marketRunSummary\\Market-Run-Summary-{}.txt".format(todayD), mode = 'a')
import yfinance as yf
import datetime
from pushover import pushNotificationSender
import datetime as dt
import pandas as pd
import pandas_datareader.data as data
import os
import ta
import openpyxl
import numpy as np
from ta import add_all_ta_features
from ta.utils import dropna
from oneMinOptionsFinder import ODTE_Options_Finder
import antLab_indicators as ant


def antLab_1min_prices_analysis(ticker):
    today = dt.datetime.today()
    data_source = 'yahoo'
    # start = dt.datetime(today.year -1, today.month -1 ,1)
    #end = dt.datetime(2022, 2 ,14)
    end = today
    start = datetime.datetime.now() - datetime.timedelta(days=7)  # 7 days ago
    end = datetime.datetime.now()
    try:
        df= yf.download(ticker, start, end, progress=False, show_errors=False, interval="1m")
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
    # df['DownTrend'] = ta.trend.psar_down_indicator(df['High'],df['Low'],df['Close'])
    # df['UpTrend'] = ta.trend.psar_up_indicator(df['High'],df['Low'],df['Close'])
    df['CCI'] = ta.trend.cci(df['High'],df['Low'],df['Close'], window=20)

    # EXPONENTIAL MOVING AVERAGE
    df['4EMA'] = ta.trend.ema_indicator(df['Close'],window=4)
    df['9EMA'] = ta.trend.ema_indicator(df['Close'],window=9)

    df['EMA_Validation'] = ant.ema_validation(df)

    df['EMA_Distance'] = ant.ema_distance(df)

    # Additional Info
    df['Ticker'] = ticker
    # df['RunTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    df['Adj_Close'] = df['Adj Close']
    df['VWAPStatus'] = np.where(df['VWAP'] > df['Close'], 'WVAP > Price', 'Price > WVAP')

    # Calculate the Maximum RateOfChageINC
    max_roc_inc = df['RateOfChageINC'].max()

    #Candle Sizes
    body_size = abs(df['Close'] - df['Open'])
    lower_wick = abs(df['Low'] - np.minimum(df['Open'], df['Close']))
    upper_wick = abs(np.maximum(df['Open'], df['Close']) - df['High'])

    #Additional Calculations
    df['ma200delta'] = round(((df['Close'] - df['200ma'])/ df['200ma']), 2)


    #Signals
    # df['BuyLT'] = np.where((df['5ma'] < df['10ma']) & (df['5ma'] < df['20ma']) & (df['10ma'] < df['20ma']) & (df['RSI'] < 35), 'BUY', '-')
    df['Buy'] = np.where((df['5ma'] < df['10ma']) & (df['5ma'] < df['20ma']) & (df['10ma'] < df['20ma']) & (df['RSI'] < 35), 'BUY', '-')

    # df['Sell'] = np.where((df['5ma'] > df['10ma']) & (df['10ma'] > df['20ma']) & (df['RSI'] > 75), 'SELL', '-')
    df['Sell'] = np.where(
                            (df['5ma'] > df['10ma']) & (df['10ma'] > df['20ma']) &
                                ((df['RateOfChageINC'] > (0.65 * max_roc_inc)) | (df['RSI'] > 70)), 'SELL', '-')

    #TEST SINGALS
    df['Buy-V2'] = np.where((df['5ma'] < df['10ma']) & (df['5ma'] < df['20ma']) & (df['10ma'] < df['20ma']) &
                            (lower_wick > body_size) &
                            (df['RSI'] < 35), 'BUY', '-') 
           
    df['Sell-V2'] = np.where(
                            (df['5ma'] > df['10ma']) & (df['10ma'] > df['20ma']) &
                                (upper_wick > body_size) &
                                ((df['RateOfChageINC'] > (0.65 * max_roc_inc)) | (df['RSI'] > 70)), 'SELL', '-')
    
    # TEST SIGNALS
   # TEST SIGNALS
    df['TradeSignal'] = np.where(
        ((df['5ma'] < df['10ma']) & (df['5ma'] < df['20ma']) & (df['10ma'] < df['20ma']) & (lower_wick > body_size) & (df['RSI'] < 35)),
        'BUY', "-"
    )

    df['TradeSignal'] = np.where(
        ((df['5ma'] > df['10ma']) & (df['10ma'] > df['20ma']) & (upper_wick > body_size) & ((df['RateOfChageINC'] > (0.65 * max_roc_inc)) | (df['RSI'] > 70))),
        'SELL', df['TradeSignal']
    )

    ## Console Printing Set
    consoleDataset = df[['High'
            ,'Low'
            ,'Open'
            ,'Volume'
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
            ,'Buy-V2'
            ,'Sell'
            ,'Sell-V2'
            ,'TradeSignal'
            ,'EMA_Validation'
            ,'EMA_Distance'
            # ,'RateOfChageINC'
            ]]
    
    # print(consoleDataset)
    
    #Store analysis in csv file
    # consoleDataset.to_csv("EQ-Analysis\\{}_OneMinPrices_Test.csv".format(ticker))
    # consoleDataset.to_csv("EQ-Analysis\\{}_OneMinPrices_{}.csv".format(ticker, end.strftime('%Y%m%d_%H%M')), index=True)

    # print("Analysis File Created")

    #Get the latest index
    # consoleDataset = consoleDataset.tail(1)
    # print(consoleDataset)

    # Filter the latest index data to validate if there is a signal
    for index, column in consoleDataset.iterrows():
        if (column['Buy'] == 'BUY'):
            # pushNotificationSender(ODTE_Options_Finder(ticker=ticker, contractType='Call'))
            result = (f"Ticker: {column['Ticker']}\n"
                        f"Flow: 0DTE\n"
                        f"Trade Signal: {column['Buy']}\n"                               
                        f"Trade Signal: {column['Sell']}\n"
                        f"Volume Profile Signal: {column['TradeSignal']}\n"
                        f"EMA Validation: {column['EMA_Validation']}\n"
                        f"EMA Distance: {column['EMA_Distance']}\n"
                        f"Price: {column['Close']}\n")
            return result
        
        elif (column['Sell'] == 'SELL'):
            # pushNotificationSender(ODTE_Options_Finder(ticker=ticker, contractType='Put'))
            result = (f"Ticker: {column['Ticker']}\n"
                        f"Flow: 0DTE\n"                               
                        f"Trade Signal: {column['Buy']}\n"                               
                        f"Trade Signal: {column['Sell']}\n"
                        f"Volume Profile Signal: {column['TradeSignal']}\n"
                        f"EMA Validation: {column['EMA_Validation']}\n"
                        f"EMA Distance: {column['EMA_Distance']}\n"
                        f"Price: {column['Close']}\n")
            return result
        else: pass

result = antLab_1min_prices_analysis("QQQ")
if result is not None:
    pushNotificationSender(result)
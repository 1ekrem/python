import yfinance as yf
import datetime
from pushover import pushNotificationSender
import datetime as dt
import pandas as pd
import pandas_datareader.data as data
import ta
import numpy as np
from ta import add_all_ta_features
from ta.utils import dropna
from antLab_indicators import *
import antLab_indicators as ant
import matplotlib as plt
import antLab_plotting as plot


def antLab_1hour_prices_analysis(ticker):
    today = dt.datetime.today()
    data_source = 'yahoo'
    # start = dt.datetime(today.year -1, today.month -1 ,1)
    #end = dt.datetime(2022, 2 ,14)
    end = today
    start = datetime.datetime.now() - datetime.timedelta(days=29)  # 7 days ago
    end = datetime.datetime.now()

    # start = "2023-12-20"
    # end = "2024-01-01"

    try:
        df= yf.download(ticker, start, end, progress=False, interval="1h")
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

    df['rsi_sens'] = rsi_sensitive(df)

    # VOLUME INDICATORS
    df['moneyIndexFlow'] = ta.volume.money_flow_index(df['High'],df['Low'],df['Close'],df['Volume'])
    df['volumePriceTrend'] = round(ta.volume.volume_price_trend(df['Close'],df['Volume']),2)
    df['VWAP'] = ta.volume.volume_weighted_average_price(df['High'],df['Low'],df['Close'],df['Volume'])
    df['MarketPressure'] = round(ta.volume.force_index(df['Close'],df['Volume'])/100,2)
    

    # Exponential Moving Average
    df['Volume_EMA10'] = ta.trend.ema_indicator(df['Volume'],window=10)
    df['Volume_EMA20'] = ta.trend.ema_indicator(df['Volume'],window=20)

    # Calculate VWAP distance to equity price 
    df['VWAP_Ratio'] = round(abs((df['VWAP'] - df['Close']) / df['Close']),2)
    df['VWAP_Ratio_2'] = wvap_ratio(df)


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

    # df['ATR'] = ta.volatility.average_true_range(df['High'],df['Low'],df['Close'], window=14)


    # TREND INDICATORS
    df['BearishVortex'] = ta.trend.vortex_indicator_neg(df['High'],df['Low'],df['Close'])
    df['BullishVortex'] = ta.trend.vortex_indicator_pos(df['High'],df['Low'],df['Close'])
    df['CCI'] = ta.trend.cci(df['High'],df['Low'],df['Close'], window=20)

    # EXPONENTIAL MOVING AVERAGE
    df['4EMA'] = ta.trend.ema_indicator(df['Close'],window=4)
    df['9EMA'] = ta.trend.ema_indicator(df['Close'],window=9)
    df['EMA_Validation'] = ant.ema_validation(df)
    df['EMA_Distance'] = ant.ema_distance(df)/100

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
                            (df['RSIST'] < 35), 'BUY', '-') 
           
    df['Sell-V2'] = np.where(
                            (df['5ma'] > df['10ma']) & (df['10ma'] > df['20ma']) &
                                (upper_wick > body_size) &
                                ((df['RateOfChageINC'] > (0.65 * max_roc_inc)) | (df['RSI'] > 75)), 'SELL', '-')
    
    df['TradeSignal'] = np.where(
        ((df['5ma'] < df['10ma']) & (df['5ma'] < df['20ma']) & (df['10ma'] < df['20ma']) & (lower_wick > body_size) & (df['RSI'] < 35)),
        'BUY', "-"
    )

    df['TradeSignal'] = np.where(
        ((df['5ma'] > df['10ma']) & (df['10ma'] > df['20ma']) & (upper_wick > body_size) & ((df['RateOfChageINC'] > (0.65 * max_roc_inc)) | (df['RSI'] > 70))),
        'SELL', df['TradeSignal']
    )
    
    df['MA_TradeSignal'] = ant.trade_signal_moving_averages(df,0.65,max_roc_inc)
    df['VPF_TradeSignal'] = ant.trade_signal_volume_profile(df, lower_wick, body_size, upper_wick, max_roc_inc, 0.65)
    df['EMA_TradeSignal'] = ant.trade_signa_exponential_moving_averages(df, 10)


    dataset = df[['High'
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
            ,'TradeSignal'
            # ,'MA_TradeSignal'
            ,'VPF_TradeSignal'
            ,'EMA_TradeSignal'
            ,'EMA_Validation'
            ,'EMA_Distance'
            ,'EMA_TradeSignal'
            ,'Volume_EMA10'
            ,'Volume_EMA20'
            # ,'ATR'
            ]]

    # Drop rows with invalid values
    # dataset = dataset.dropna() 

    # Exclude rows with "-" in 'BuyLT' or 'Sell'
    # dataset = dataset[(dataset['Buy-V2'] != '-') |
    #                 #    (dataset['Sell'] != '-') |
    #                    (dataset['Sell'] != '-')]

    # dataset = dataset[(dataset['TradeSignal'] != '-')]

    #Store analysis in csv file
    # dataset.to_csv("EQ-Analysis\\{}_OneHour_Test.csv".format(ticker))
    # dataset.to_csv("EQ-Analysis\\{}_Dev_OneHourPrices_{}.csv".format(ticker, end.strftime('%Y%m%d_%H%M')), index=True)

    # print(dataset.tail(3))

    #Get the latest index
    dataset = dataset.tail(1)

    #Filter the latest index data to validate if there is a signal
    # for index, column in dataset.iterrows():
    #     if (column['Buy'] == 'BUY'):
    #         print(ticker,":", "BUY", round(column['Close'],2))
    #         return ("0DTE Flow:",ticker,"BUY : ", round(column['Close'],2))
    #     elif (column['Sell'] == 'SELL'):
    #         print(ticker,":", "SELL", round(column['Close'],2))
    #         return ("0DTE Flow:",ticker,"SELL : ",  round(column['Close'],2))
    # else: pass

    for index, column in dataset.iterrows():
        if (column['TradeSignal'] == 'BUY'):
            print("${}".format(ticker),":", "BUY","- Price:",round(column['Close'],2))
            # return ("BUY")
        elif (column['TradeSignal'] == 'SELL'):
            print("${}".format(ticker),":", "SELL","- Price:",round(column['Close'],2))
            # print("$",ticker,":", "SELL")
            # return ("SELL")
    else: pass

    plot.antlab_plotting(df,ticker)

antLab_1hour_prices_analysis(input("Enter Ticker: "))

# result = bulkRunner("SPY")
# if result is not None:
#     pushNotificationSender(result)
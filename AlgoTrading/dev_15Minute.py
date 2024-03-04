import yfinance as yf
import datetime
from pushover import pushNotificationSender
import datetime as dt
import ta
import numpy as np
from ta import add_all_ta_features
from ta.utils import dropna
from oneMinOptionsFinder import ODTE_Options_Finder
from antLab_strategies import *
from antLab_indicators import *
import matplotlib.pyplot as plt
import antLab_plotting as plot


def antLab_15min_prices_analysis(ticker):
    today = dt.datetime.today()
    data_source = 'yahoo'
    # start = dt.datetime(today.year -1, today.month -1 ,1)
    #end = dt.datetime(2022, 2 ,14)
    end = today
    start = datetime.datetime.now() - datetime.timedelta(days=30)  # 7 days ago
    end = datetime.datetime.now()
    try:
        df= yf.download(ticker, start, end, progress=False, interval="15m")
        if df.empty:
            # print(f"Empty DataFrame for {ticker}")
            return None
    except IndexError:
        pass
    
    # Create Moving Averages 
    df['200ma'] = df['Adj Close'].rolling(window=200, min_periods=0).mean()
    df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
    df['50ma'] = df['Adj Close'].rolling(window=50, min_periods=0).mean()
    df['20ma'] = df['Adj Close'].rolling(window=20, min_periods=0).mean()
    df['10ma'] = df['Adj Close'].rolling(window=10, min_periods=0).mean()
    df['5ma'] = df['Adj Close'].rolling(window=5, min_periods=0).mean()

    # VOLUME INDICATORS
    df['moneyIndexFlow'] = ta.volume.money_flow_index(df['High'],df['Low'],df['Close'],df['Volume'])
    df['volumePriceTrend'] = round(ta.volume.volume_price_trend(df['Close'],df['Volume']),2)
    df['VWAP'] = ta.volume.volume_weighted_average_price(df['High'],df['Low'],df['Close'],df['Volume'])
    df['MarketPressure'] = round(ta.volume.force_index(df['Close'],df['Volume'])/100,2)

    # Create Moving Averages 
    df['Vol200ma']  = df['Volume'].rolling(window=200, min_periods=0).mean()
    df['Vol100ma']  = df['Volume'].rolling(window=100, min_periods=0).mean()
    df['Vol50ma']   = df['Volume'].rolling(window=50, min_periods=0).mean()
    df['Vol20ma']   = df['Volume'].rolling(window=20, min_periods=0).mean()
    df['Vol10ma']   = df['Volume'].rolling(window=10, min_periods=0).mean()
    df['Vol9ma']    = df['Volume'].rolling(window=9, min_periods=0).mean()
    df['Vol5ma']    = df['Volume'].rolling(window=5, min_periods=0).mean()
    df['Vol4ma']    = df['Volume'].rolling(window=4, min_periods=0).mean()

    df['volume_validation'] = np.where((df['Vol10ma'] > df['Vol20ma']), 'Volume_Increasing', 'Steady')
    df['volume_width'] = round((df['Vol10ma'] - df['Vol20ma'])/ df['Vol20ma'],2)

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
    df['4EMA'] = ta.trend.ema_indicator(df['Close'],window=4)
    df['9EMA'] = ta.trend.ema_indicator(df['Close'],window=9)

    df['EMA_Validation'] = ema_validation(df)
    df['EMA_Distance'] = ema_distance(df)/100



    # Additional Info
    df['Ticker'] = ticker
    # df['RunTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    df['Adj_Close'] = df['Adj Close']
    df['VWAPStatus'] = np.where(df['VWAP'] > df['Close'], 'WVAP > Price', 'Price > WVAP')
    df['GoldenZone'] = fib_retracement_test(df)

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
                            (df['RSI'] < 35), 'BUY', '-') 
           
    df['Sell-V2'] = np.where(
                            (df['5ma'] > df['10ma']) & (df['10ma'] > df['20ma']) &
                                (upper_wick > body_size) &
                                ((df['RateOfChageINC'] > (0.65 * max_roc_inc)) | (df['RSI'] > 70)), 'SELL', '-')
    
    df['TradeSignal'] = trade_signal_moving_averages(df, max_roc_inc, 0.65)
    df['VPF_TradeSignal'] = trade_signal_volume_profile(df,lower_wick,body_size, upper_wick, max_roc_inc, 0.65)

    df['EMA_Distance'] = ema_distance(df)/100
    df['EMA_TradeSignal'] = trade_signa_exponential_moving_averages(df, 10)


    ## Console Printing Set
    consoleDataset = df[['High'
            ,'Low'
            ,'Open'
            # ,'RSIST'
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
            ,'VPF_TradeSignal'
            ,'EMA_TradeSignal'
            ,'volume_validation'
            ,'volume_width'
            ]]
    
    plot.antlab_plotting(df, ticker)
    
    # print(consoleDataset.tail(5))
    
    #Store analysis in csv file
    # consoleDataset.to_csv("EQ-Analysis\\{}_15Min_Test.csv".format(ticker))
    # consoleDataset.to_csv("EQ-Analysis\\{}_Dev_15MinPrices_{}.csv".format(ticker, end.strftime('%Y%m%d_%H%M')), index=True)
    # print("Analysis File Created")



    consoleDataset = consoleDataset.tail(1)
    # consoleDataset = consoleDataset[(consoleDataset['TradeSignal'] != '-')]
    # print(consoleDataset['TradeSignal'])
    # return consoleDataset['TradeSignal']
    # for index, column in consoleDataset.iterrows():
    #     if (column['TradeSignal'] == 'BUY'):
    #         print("$",ticker,":", "BUY")
    #         # return ("BUY")
    #     elif (column['TradeSignal'] == 'SELL'):
    #         print("$",ticker,":", "SELL")
    #         # return ("SELL")
    # else: pass

    for index, column in consoleDataset.iterrows():
        if (column['VPF_TradeSignal'] == 'BUY'):
            print("${}".format(ticker),":", "BUY","- Price:",round(column['Close'],2))
            # return ("BUY")
        elif (column['VPF_TradeSignal'] == 'SELL'):
            print("${}".format(ticker),":", "SELL","- Price:",round(column['Close'],2))
            # print("$",ticker,":", "SELL")
            # return ("SELL")
    else: pass


antLab_15min_prices_analysis("BABA")

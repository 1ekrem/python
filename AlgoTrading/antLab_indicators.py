import yfinance as yf
import datetime
import pandas as pd
import ta
import openpyxl
import numpy as np


def buy_signal(df):
    return np.where((df['5ma'] < df['10ma']) & (df['5ma'] < df['20ma']) & (df['10ma'] < df['20ma']) & (df['RSI'] < 35), 'BUY', '-')

def sell_signal(df, max_roc_inc, rate_of_change_treshold):
    return np.where(
                    (df['5ma'] > df['10ma']) & (df['10ma'] > df['20ma']) &
                        ((df['RateOfChageINC'] > (rate_of_change_treshold * max_roc_inc)) |
                         (df['RSI'] > 70)), 'SELL', '-')

def trade_signal_moving_averages(df,rate_of_change_treshold,max_roc_inc):
    buy_condition = ((df['5ma'] < df['10ma']) & (df['5ma'] < df['20ma']) & (df['10ma'] < df['20ma']) & (df['RSI'] < 35))

    sell_condition = ((df['5ma'] > df['10ma']) & 
                      (df['10ma'] > df['20ma']) &
                        ((df['RateOfChageINC'] > (rate_of_change_treshold * max_roc_inc)) |
                         (df['RSI'] > 70)))
    
    ma_TradeSignal = np.where(buy_condition, 'BUY', '-')
    ma_TradeSignal = np.where(sell_condition, 'SELL', ma_TradeSignal)

    return ma_TradeSignal 

def buy_signal_volume_profile (df, lower_wick, body_size):
    return np.where((df['5ma'] < df['10ma']) &
                            (df['5ma'] < df['20ma']) &
                            (df['10ma'] < df['20ma']) &
                            (lower_wick > body_size) &
                            (df['RSI'] < 35), 'BUY', '-') 

def sell_signal_volume_profile (df, upper_wick, body_size, max_roc_inc, rate_of_change_treshold):
    return np.where(
                    (df['5ma'] > df['10ma']) &
                    (df['10ma'] > df['20ma']) &
                    (upper_wick > body_size) &
                    ((df['RateOfChageINC'] > (rate_of_change_treshold * max_roc_inc)) | (df['RSI'] > 70)), 'SELL', '-')
    

def trade_signal_volume_profile(df, lower_wick, body_size, upper_wick, max_roc_inc, rate_of_change_threshold):
    buy_condition = (
        (df['5ma'] < df['10ma']) & 
        (df['5ma'] < df['20ma']) & 
        (df['10ma'] < df['20ma']) & 
        (lower_wick > body_size) & 
        (df['RSI'] < 35)
    )

    sell_condition = (
        (df['5ma'] > df['10ma']) & 
        (df['10ma'] > df['20ma']) & 
        (upper_wick > body_size) & 
        ((df['RateOfChageINC'] > (0.65 * max_roc_inc)) | (df['RSI'] > 70))
    )
    
    vpf_TradeSignal = np.where(buy_condition, 'BUY', '-')
    vpf_TradeSignal = np.where(sell_condition, 'SELL', vpf_TradeSignal)

    return vpf_TradeSignal


def in_consolidation(df, percentange):
    
    last_15days = df[-45:]
    
    max_price = last_15days['Close'].max()
    min_price = last_15days['Close'].min()
    
    custom_threshold = 1- (percentange / 100)
    if min_price > (max_price * custom_threshold):
        return True
    
def consolidation_range(df):
    last_15days = df[-15:]

    max_price = round(last_15days['Close'].max(),2)
    min_price = round(last_15days['Close'].min(),2)

    # print(max_price, min_price)

    delta_perc = round((max_price - min_price) / min_price,2)

    return delta_perc

def internal_bar_strength(df):
    close = df['Close'] - df['Low']
    high = df['High'] - df['Low']

    ibs = round((close / high) * 100, 2)

    return ibs


def rsi_sensitive(df):
    delta = df['Close'].diff()

    window = 14

    up_days = delta.copy()
    up_days[delta<=0]=0.0

    down_days = abs(delta.copy())
    down_days[delta>0]=0.0

    RS_up = up_days.rolling(window).mean()
    RS_down = down_days.rolling(window).mean()

    rsi = 100-100/(1+RS_up/RS_down)
    rsi = rsi.astype('float')

    return rsi

def simple_moving_average(df, window):
    sma = df['Close'].rolling(window=window, min_periods=0).mean()

    return sma

def wvap_ratio(df):
    vwap_ratio = round(abs((df['VWAP']-  df['Close']) / df['Close']),2)
    
    return vwap_ratio


def longterm_trend_identifier(df):
    all_time_low_for_selected_period = df['Close'].min()

    trend = np.where(df['Close'] > all_time_low_for_selected_period, 'Uptrending', 'Downtrending')

    return trend

def shortterm_trend_identifier(df,rsi_window):
    last_5days = df[-20:]
    all_time_high_for_selected_period = last_5days.max()

    rsi_average = last_5days['RSI'].rolling(window=rsi_window, min_periods=0).mean()

    # trend = np.where(df['Close'] > all_time_high_for_selected_period & df['RSI'] > rsi_average , 'Uptrending', 'Downtrending')
    trend = np.where((last_5days['Close'] > all_time_high_for_selected_period) & (last_5days['RSI'] > 50), 'Uptrending', 'Downtrending')

    return trend

def ath_trend_ratio(df):
    all_time_high_for_selected_period = df['Close'].max()

    ratio_from_ath = round((all_time_high_for_selected_period - df['Close'])/df['Close'], 2)*100

    return ratio_from_ath

def atl_trend_ratio(df):
    all_time_low_for_selected_period = df['Close'].min()

    ratio_from_atl = round((df['Close'] - all_time_low_for_selected_period)/df['Close'], 2)*100

    return ratio_from_atl

def ema_validation(df):
    """4EMA and 9EMA must exist in your dataframe to execute this function"""
    ema_validation = np.where(df['4EMA'] > df['9EMA'], "4EMA_Higher", "9EMA_Higher")
    
    return ema_validation

def ema_distance(df):
    """4EMA and 9EMA must exist in your dataframe to execute this function"""
    ema_distance = round(((df['4EMA'] - df['9EMA']) / df['4EMA'])*100000,2)

    return ema_distance

def pull_back_identifier(df, pullback_rate):
    pullback_rate = pullback_rate / 100

    # Create a new column for the highest price in the last rolling 20 days
    df['Highest_Price_20D'] = df['High'].rolling(window=20).max()

    # Compare if the latest price is 7 percent less than the current rolling price
    latest_price = df['Close'].iloc[-1]  # Get the latest closing price
    rolling_price = df['Highest_Price_20D'].iloc[-1] * (1-pullback_rate)  # 7% less than the current rolling price

    if latest_price < rolling_price:
        True
    else:
        False
    
def trade_signa_exponential_moving_averages(df, ema_distance_range):
    ema_distance_range = ema_distance_range / 100

    # Calculate the top 10% positive and negative values
    top_10_percent_positive = df['EMA_Distance'].quantile(0.9)
    top_10_percent_negative = df['EMA_Distance'].quantile(0.1)

    # Generate sell and buy signals
    sell_condition = df['EMA_Distance'] >= top_10_percent_positive
    buy_condition = df['EMA_Distance'] <= top_10_percent_negative

    ema_TradeSignal = np.where(buy_condition, 'BUY', '-')
    ema_TradeSignal = np.where(sell_condition, 'SELL', ema_TradeSignal)

    return ema_TradeSignal
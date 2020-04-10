import datetime as dt
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd
import pandas_datareader.data as data
import os

ticker = input(str("Enter ticker: "))

def get_stock_prices():
    data_source = 'yahoo'
    start = dt.datetime(2018, 1 ,1)
    end = dt.datetime.today()
    df= data.DataReader(ticker, data_source, start, end)
    df.to_csv('C:\\PythonClass\\ta-ticker\\{}.csv'.format(ticker))
    print("Stock prices of {} is pulled!".format(ticker))

def tech_analysis():
    df = pd.read_csv('C:\\PythonClass\\ta-ticker\\{}.csv'.format(ticker), parse_dates=True, index_col=0)
    df['200ma'] = df['Adj Close'].rolling(window=200, min_periods=0).mean()
    df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
    df['50ma'] = df['Adj Close'].rolling(window=50, min_periods=0).mean()
    df['20ma'] = df['Adj Close'].rolling(window=20, min_periods=0).mean()
    df['10ma'] = df['Adj Close'].rolling(window=10, min_periods=0).mean()
    df['5ma'] = df['Adj Close'].rolling(window=5, min_periods=0).mean()
    print("Moving Averages are created!")
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
    print("Relative Strenght Index of 14 is created!")
    #CCI
    ndays=21
    TP = (df['High'] + df['Low'] + df['Close']) / 3 
    df['CCI'] = pd.Series((TP - TP.rolling(ndays).mean()) / (0.014 * TP.rolling(ndays).std()),name = 'CCI')
    print("Commodity Channel Index of 21 is created!")
    #Save analysis file and remove the historic data
    df.tail(250).to_excel('C:\\PythonClass\\ta-ticker\\{}_SMAanalysis.xlsx'.format(ticker))
    os.remove('C:\\PythonClass\\ta-ticker\\{}.csv'.format(ticker))
    print("NOTE: Stock prices data file is removed!")

get_stock_prices()
tech_analysis()

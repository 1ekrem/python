import datetime as dt
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd
import pandas_datareader.data as data
import os

ticker = input(str("Enter ticker: "))

def get_stock_prices():
    data_source = 'yahoo'
    start = dt.datetime(2017, 1 ,1)
    end = dt.datetime(2020, 1 ,12)
    df= data.DataReader(ticker, data_source, start, end)
    df.to_csv('C:\\PythonClass\\ta-ticker\\{}.csv'.format(ticker))
    print("Stock prices of {} is pulled!".format(ticker))

def tech_analysis():
    df = pd.read_csv('C:\\PythonClass\\ta-ticker\\{}.csv'.format(ticker), parse_dates=True, index_col=0)
    df['200ma'] = df['Adj Close'].rolling(window=200, min_periods=0).mean()
    df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
    df['50ma'] = df['Adj Close'].rolling(window=50, min_periods=0).mean()
    df['15ma'] = df['Adj Close'].rolling(window=15, min_periods=0).mean()
    df['10ma'] = df['Adj Close'].rolling(window=10, min_periods=0).mean()
    df['5ma'] = df['Adj Close'].rolling(window=5, min_periods=0).mean()
    df.tail(250).to_excel('C:\\PythonClass\\ta-ticker\\{}_SMAanalysis.xlsx'.format(ticker))
    print("Moving Averages are created!")
    os.remove('C:\\PythonClass\\ta-ticker\\{}.csv'.format(ticker))
    print("NOTE: Stock prices data file is removed!")

get_stock_prices()
tech_analysis()

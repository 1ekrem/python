import datetime as dt
from matplotlib.pyplot import ticklabel_format
import pandas as pd
import pandas_datareader.data as data
from pandas_datareader._utils import RemoteDataError
import os
import ta
import numpy as np
import datetime
#from startegies import in_consolidation
import startegies
import yfinance as yf


from ta import add_all_ta_features
from ta.utils import dropna

# global df

# def data_request(ticker):
#     try:
#         today = dt.datetime.today()
#         data_source = 'yahoo'
#         start = dt.datetime(today.year -1, today.month -1 ,1)
#         end = today
#         df= data.DataReader(ticker, data_source, start, end)
#     except KeyError:
#         pass
    
#     except RemoteDataError:
#         print("{} not found".format(ticker))

def breakout_finder(ticker, perc):
    global df
    try:
        today = dt.datetime.today()
        last_year_today = today - dt.timedelta(days=365)
        data_source = 'yahoo'
        start = last_year_today
        end = today
        df = yf.download(ticker, start, end, progress = False)
    except KeyError:
        pass
    
    except RemoteDataError:
        print("{} not found".format(ticker))

    if startegies.in_consolidation(df, percentange=perc):
        print("{} in consolidation".format(ticker))
    else:
        pass
        print("{} Consolidation Range:".format(ticker), startegies.consolidation_range(df))
        #print("{} skipped".format(ticker))
        
def golden_zone_finder(ticker):
    global df
    try:
        today = dt.datetime.today()
        last_year_today = today - dt.timedelta(days=365)
        data_source = 'yahoo'
        start = last_year_today
        end = today
        df = yf.download(ticker, start, end, progress = False)
    except KeyError:
        pass
    
    except RemoteDataError:
        print("{} not found".format(ticker))

    if startegies.fib_retracement(df):
        print("{} in Golden Zone".format(ticker))
    else:
        pass
        #print("{} GZ skipped".format(ticker))
        
   
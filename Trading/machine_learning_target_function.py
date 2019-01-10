'''
Machine Learning Buy & Sell signal 2
'''

import numpy as np 
import pandas as pd 
import pickle

def process_data_for_labels(ticker):
    hm_days = 7 # Number of days taken under decision
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, hm_days+1):
        print(i)
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker])/df[ticker]  #When you shift things negatively, future data goes up 
    
    df.fillna(0, inplace=True)
    return tickers, df

#Target Function
def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement = 0.02 # If stock price changes 2%, we'll have a notification
    for col in cols:
        if col > requirement:
            return 1
        if col < -requirement:
            return -1
    return 0
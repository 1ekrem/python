'''
Machine Learning Buy & Sell signal 1 
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

process_data_for_labels("XOM")
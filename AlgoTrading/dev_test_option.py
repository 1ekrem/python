import pandas as pd
import numpy as np
import yfinance as yf
import sys


yf.debug_mode()
print('run')
print(sys.version)
ticker = 'AMD'

tk = yf.Ticker(ticker)
print(tk)
    
    # Get Equity Price
ticker_yahoo = yf.Ticker(ticker)
data = ticker_yahoo.history()
last_quote = (data.tail(1)['Close'].iloc[0])

    # Expiration dates
exps = tk.options

    # Get options for each expiration
options = pd.DataFrame()
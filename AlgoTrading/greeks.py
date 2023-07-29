from wallstreet import Stock, Put, Call
from datetime import date
from datetime import datetime
import pandas as pd
import numpy as np
import yfinance as yf
import datetime

this_year = str(date.today().year)

ticker = 'PLTR'
tk = yf.Ticker(ticker)

# Get Equity Price
ticker_yahoo = yf.Ticker(ticker)
data = ticker_yahoo.history()
last_quote = (data.tail(1)['Close'].iloc[0])

    
# Expiration dates
exps = tk.options

# Get greeks


# Get options for each expiration
options = pd.DataFrame()
for e in exps:
    # Show me option of this year
    if e[:4] == this_year:
        print(e)
        opt = tk.option_chain(e)
        opt = pd.DataFrame().append(opt.calls).append(opt.puts)
        opt['expirationDate'] = e
        options = options.append(opt, ignore_index=True)

options['CALL'] = options['contractSymbol'].str[4:].apply(lambda x: "C" in x)

print(options)

        
options.to_excel('C:\\Users\\ekrem\\Desktop\\Option Chain Analysis\\{}_Option_Analysis-2.xlsx'.format(ticker))



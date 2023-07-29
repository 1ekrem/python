
import yfinance as yf
import datetime as dt
from SPX import SPX
from NDX import NDX
from NDX100 import NDX100

def consolidationRangeFinder (ticker):
    today = dt.datetime.today()
    last_year_today = today - dt.timedelta(days=365)
    data_source = 'yahoo'
    start = last_year_today
    end = today
    df = yf.download(ticker, start, end, progress=False)
            
    last_15days = df[-20:]

    max_price = round(last_15days['Close'].max(),2)
    min_price = round(last_15days['Close'].min(),2)

    delta_perc = round((max_price - min_price) / min_price,2)
    
    if delta_perc <0.03:
        print(ticker)
    

for ticker in SPX:
    consolidationRangeFinder(ticker)

    



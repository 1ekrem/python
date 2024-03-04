import datetime as dt
import pandas as pd
import yfinance as yf


def pull_market_data(ticker):
    try:
        today = dt.datetime.today()
        start = dt.datetime(today.year - 1, today.month - 1, 1)
        end = today
        data_source = 'yahoo'
        df = yf.download(ticker, start, end, progress=False, show_errors=False, interval="1d")

        if df.empty:
            print(f"Empty DataFrame for {ticker}")
            return None

        return df
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None
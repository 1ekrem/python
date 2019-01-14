import pandas_datareader.data as web
import datetime as dt

ticker = 'DEXJPUS'

start = dt.datetime(2017, 1 ,1)
end = dt.datetime(2020, 1 ,12)

df = web.get_data_fred(ticker, start, end)

print(df.tail(5))
import datetime as dt
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd
import pandas_datareader.data as data


ticker = 'TRYUSD=X'

data_source = 'yahoo'
start = dt.datetime(2017, 1 ,1)
end = dt.datetime(2020, 1 ,12)

df= data.DataReader(ticker, data_source, start, end)

#Store data into csv or xl
df.to_csv('{}.csv'.format(ticker))

print(df.tail(5))

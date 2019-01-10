import datetime as dt
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd
import pandas_datareader.data as data

style.use('ggplot')

ticker = 'TSLA'
data_source = 'yahoo'
start = dt.datetime(2018, 1 ,1)
end = dt.datetime(2019, 1 ,10)

df= data.DataReader(ticker, data_source, start, end)

#Store data into csv or xl
df.to_csv('tsla.csv')

print(df.tail(25))

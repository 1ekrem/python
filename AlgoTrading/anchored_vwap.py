import pandas as pd
import numpy as np
import yfinance as yf
import pandas_ta  as ta

# set anchor date
anchored_date = pd.to_datetime('2023-10-27')

data = yf.download("AMD", start="2023-10-20", end="2023-12-21")
df = pd.DataFrame(data)

print(df.columns)

df1 = df.ta.vwap(anchor = "D")
df14 = pd.concat([df, df1],axis=1)

# I create a column 'typical_price', it should be identical with 'VWAP_D'
df14['typical_price'] = (df14['High'] + df14['Low'] + df14['Close'])/3
tpp_d = ((df14['High'] + df14['Low'] + df14['Close'])*df14['Volume'])/3


df14['anchored_VWAP'] = tpp_d.where(df14.index >= anchored_date).groupby(df14.index >= anchored_date).cumsum()/df14['Volume'].where(df14.index >= anchored_date).groupby(df14.index >= anchored_date).cumsum()

dataset = df14[['High'
            ,'Low'
            ,'Open'
            ,'Close'
            ,'Volume'
            ,'anchored_VWAP'
            ]]

print(dataset.tail(20))
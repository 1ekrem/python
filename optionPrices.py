from yahoo_fin import options
from yahoo_fin import stock_info
import os
import datetime as dt
from pandas_datareader import DataReader



ticker = "AAPL"
data_source = options.get_options_chain(ticker)


print(options.get_options_chain(ticker))

#print(chain["puts"].head(1))

#most_active = stock_info.get_day_most_active()


#df = stock_info.get_day_most_active()
#df.to_csv('C:\\PythonClass\\ta-ticker\\{}MostActive.csv'.format(dt.today()))
#
#p_stock = stock_info.get_live_price("AAPL")
#print(p_stock)
#
#financials = stock_info.get_financials("AAPL",True,False)
#print(financials)

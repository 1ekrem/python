import pyodbc
import pandas
import pandas as pd
import numpy as np
import yfinance as yf
import datetime
from datetime import date
import pyodbc

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
        opt = tk.option_chain(e)
        opt = pd.DataFrame().append(opt.calls).append(opt.puts)
        opt['expirationDate'] = e
        options = options.append(opt, ignore_index=True)

# Bizarre error in yfinance that gives the wrong expiration date
# Add 1 day to get the correct expiration date
#options['expirationDate'] = pd.to_datetime(options['expirationDate']) #+ datetime.timedelta(days = 1)

#Calculate days to expire 
options['dte'] = ((pd.to_datetime(options['expirationDate']) - datetime.datetime.today()).dt.days)
 
# Boolean column if the option is a CALL
options['CALL'] = options['contractSymbol'].str[4:].apply(lambda x: "C" in x)

# Show ticker
options['EquityTicker'] = ticker

# Add Equity Price
options['EquityPrice'] = last_quote

# Calculate breakeven equity price
options['BreakevenPrice'] = (last_quote - options['ask'])

# Calculate percentage payout per contract
options['PercentagePayout'] = ((options['ask'] / last_quote)*100)
#options['PutPercentagePayout'] = (((options['ask'] / options['strike'])/options['strike'])*100)

# Add Contract Price Details
options[['bid', 'ask', 'strike']] = options[['bid', 'ask', 'strike']].apply(pd.to_numeric)
#options['PercentagePayout'] = options['PercentagePayout'].apply(pd.to_numeric)

# Calculate the midpoint of the bid-ask
#options['mark'] = (options['bid'] + options['ask']) / 2 

# Create dataset2
dataset2 = options[['contractSymbol', 'strike' ,'bid','ask','change','percentChange','volume','openInterest','impliedVolatility','expirationDate','dte','EquityPrice','BreakevenPrice','PercentagePayout']]

dataset2.fillna({
                'percentChange': '0',
                'volume': '0',
                'openInterest': '0'}, inplace = True)

dataset2.to_excel('C:\\Users\\ekrem\\Desktop\\Option Chain Analysis\\2\\{}_Option_Analysis-2.xlsx'.format(ticker))


#data = pandas.read_csv (r'C:/Users/ekrem/Documents/Database File Upload/test_2.csv')
#df = pandas.DataFrame(data,columns = ['Ticker', 'PutRatio', 'CallRatio', 'Date'])


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-UTF7GAF\SQLEXPRESS;'
                      'Database=Trading;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()


cursor.execute('CREATE TABLE option_test (contractSymbol varchar(255), strike decimal(6, 2), bid decimal(6, 2),ask decimal(6, 2), change float(2), percentChange float(2),  volume int, openInterest int, impliedVolatility decimal(6, 2),expirationDate date ,dte int, EquityPrice decimal(6, 2),BreakevenPrice decimal(6, 2), PercentagePayout decimal(6, 2))')

conn.commit()

for row in dataset2.itertuples():
    cursor.execute('''
                INSERT INTO [Trading].[dbo].[option_test] (contractSymbol, strike, bid, ask, change, percentChange, volume, openInterest, impliedVolatility, expirationDate, dte, EquityPrice, BreakevenPrice, PercentagePayout )
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                '''
                ,row.contractSymbol 
                ,row.strike
                ,row.bid
                ,row.ask
                ,row.change
                ,row.percentChange
                ,row.volume
                ,row.openInterest
                ,row.impliedVolatility 
                ,row.expirationDate
                ,row.dte
                ,row.EquityPrice 
                ,row.BreakevenPrice 
                ,row.PercentagePayout
                )
conn.commit()
print("Data Insert is completed")
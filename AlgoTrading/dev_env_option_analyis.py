import pandas as pd
import numpy as np
import yfinance as yf
import datetime
from datetime import date
from datetime import datetime as dt
import pyodbc

this_year = str(date.today().year)

ticker = input('Please enter the ticket: ')
tk = yf.Ticker(ticker)

# Get Equity Price
ticker_yahoo = yf.Ticker(ticker)
data = ticker_yahoo.history()
last_quote = (data.tail(1)['Close'].iloc[0])
    
# Expiration dates
exps = tk.options

# Get options for each expiration
options = pd.DataFrame()
for e in exps:
    # Show me option of this year
    #if e[:4] == this_year:
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
#options['CALL'] = options['contractSymbol'].str[4:].apply(lambda x: "C" in x)
options['ContractType']= options['contractSymbol'].str[4:].apply(lambda x: "Call" if "C" in x else "Put")

# Show ticker
options['Ticker'] = ticker

# Add Equity Price
options['EquityPrice'] = last_quote

# Calculate breakeven equity price
options['BreakevenPrice'] = (last_quote - options['ask']) 

# Calculate Covered Call Payoff percentage per contract
#options['CoveredCallPayoff'] = np.where((options['ContractType'] == 'Call'), ((options['bid'] / last_quote)), '0').astype(float)

# Calculate Selling Put Payoff percentage per contract
#options['SellingPutPayoff'] = np.where((options['ContractType'] == 'Put'), ((options['bid'] / last_quote)), '0').astype(float)

# 0DTE Contrancts
# options['CoveredCallPayoff'] = np.where(options['dte'] == '1')

options['TotalOIValue'] = (options['openInterest'] * options['strike'] * 100).fillna(0).astype(int)
 
#Run Timestamp
options['RunTime'] = dt.now().strftime("%Y-%m-%d %H:%M")

# Add Contract Price Details
options[['bid', 'ask', 'strike']] = options[['bid', 'ask', 'strike']].astype(float)

options['percentChange'] = (options['percentChange']/100).fillna(0)



# Create dataset2
dataset2 = options[['contractSymbol'
                    ,'strike'
                    ,'bid'
                    ,'ask'
                    ,'lastPrice'
                    ,'change'
                    ,'percentChange'
                    ,'volume'
                    ,'openInterest'
                    ,'impliedVolatility'
                    ,'inTheMoney'
                    ,'expirationDate'
                    ,'dte'
                    ,'ContractType'
                    ,'Ticker'
                    ,'EquityPrice'
                    ,'BreakevenPrice'
                    ,'TotalOIValue'
                    ,'RunTime'
                    ]]

dataset2 = dataset2[(dataset2['CoveredCallPayoff'] >= 0.02) & (dataset2['CoveredCallPayoff'] < 0.10)]

print(dataset2.tail(15))


# Save the dataset
dataset2.to_excel('C:\\Users\\ekrem\\Desktop\\Option Chain Analysis\\{}_Option_Analysis.xlsx'.format(ticker))

# Print confirmation message
#print("Option chain file of {} is generated!\n".format(ticker))

# Insert into Database

# create temporary dateset
#sql_dataset = pd.DataFrame(data,columns = ['contractSymbol','strike','bid','ask','change','percentChange','volume','openInterest','impliedVolatility','inTheMoney','expirationDate','dte','CALL','EquityTicker','EquityPrice','BreakevenPrice','PercentagePayout'])


#Save dataset2
#dataset2.to_excel('C:\\Users\\ekrem\\Desktop\\Option Chain Analysis\\2\\{}_Option_Analysis-2.xlsx'.format(ticker))


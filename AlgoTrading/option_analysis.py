import pandas as pd
import numpy as np
import yfinance as yf
import datetime
from datetime import date
from datetime import datetime as dt

def options_chain(ticker):
    
    # Get today's year value
    this_year = str(date.today().year)
    
    # Initiate the process
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
        if e[:4] == this_year:
            opt = tk.option_chain(e)
            opt = pd.DataFrame().append(opt.calls).append(opt.puts)
            opt['expirationDate'] = e
            options = options.append(opt, ignore_index=True)

    # Bizarre error in yfinance that gives the wrong expiration date -- Not anymore 1/20/2020
    # Add 1 day to get the correct expiration date
    #options['expirationDate'] = pd.to_datetime(options['expirationDate'])
    
    
    #Calculate days to expire 
    options['dte'] = ((pd.to_datetime(options['expirationDate']) - datetime.datetime.today()).dt.days)
     
    # Boolean column if the option is a CALL
    options['ContractType']= options['contractSymbol'].str[4:].apply(lambda x: "Call" if "C" in x else "Put")
    
    # Show ticker
    options['Ticker'] = ticker

    # Add Equity Price
    options['EquityPrice'] = last_quote

    # Calculate breakeven equity price
    options['BreakevenPrice'] = (last_quote - options['ask'])

    # Calculate Covered Call Payoff percentage per contract
    options['CoveredCallPayoff'] = np.where((options['ContractType'] == 'Call'), ((options['bid'] / last_quote)), '0').astype(float)

    # Calculate Selling Put Payoff percentage per contract
    options['SellingPutPayoff'] = np.where((options['ContractType'] == 'Put'), ((options['bid'] / last_quote)), '0').astype(float)

    # Calculate Total Value of All open interest
    options['TotalOIValue'] = (options['openInterest'] * options['ask'] * 100).fillna(0).astype(int)

    # Add Contract Price Details
    options[['bid', 'ask', 'strike']] = options[['bid', 'ask', 'strike']].apply(pd.to_numeric)
   
    # Modify Percentage Change
    options['percentChange'] = (options['percentChange']/100).fillna(0)
    
    #Run Timestamp
    options['RunTime'] = dt.now().strftime("%Y-%m-%d %H:%M")
   
    # Drop unnecessary and meaningless columns
    #options = options.drop(columns = ['contractSize', 'currency'])
    
    # Create dataset2
    options = options[['contractSymbol'
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
                        ,'CoveredCallPayoff'
                        ,'SellingPutPayoff'
                        ,'TotalOIValue'
                        ,'RunTime'
                        ]]
    
    # Filter By Profitibility
    # options = options[((options['SellingPutPayoff'] >= 0.02) & (options['SellingPutPayoff'] < 0.04)) 
                                #   | (options['CoveredCallPayoff'] >= 0.02) & (options['CoveredCallPayoff'] < 0.04)]
    # Save the dataset
    options.to_excel('C:\\Users\\ekrem\\Desktop\\Option Chain Analysis\\{}_Option_Analysis.xlsx'.format(ticker))

    print("Option chain file of {} is generated!\n".format(ticker))
    return options

#\OneDrive\
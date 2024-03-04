import pandas as pd
import numpy as np
import yfinance as yf
import datetime
from datetime import date
from datetime import datetime as dt
from pushover import pushNotificationSender

def beautify_options_data(ODTE_Options_Finder):
    beautified_data = []
    for index, row in ODTE_Options_Finder.iterrows():
        beautified_data.append(f"contractSymbol: {row['contractSymbol']}\n"
                               f"Ticker: {row['Ticker']}\n"
                               f"Strike: {row['strike']}\n"
                               f"Contract Type: {row['ContractType']}\n"
                               f"Bid: {row['bid']}\n"
                               f"Ask: {row['ask']}\n"
                               f"Equity Price: {row['EquityPrice']}\n"
                               f"Expiration Date: {row['expirationDate']}\n"
                               f"IV AVG By Expiry: {row['ivAVGByExpiry']}\n"
                               f"P/C Ratio By Expiry: {row['PCRbyExpiry']}")

    return ''.join(beautified_data)

def ODTE_Options_Finder(ticker, contractType):
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
            
            # Set Expiration Date
            opt['expirationDate'] = e

            # Calculate Implied Volatility By Expiry
            opt['ivAVGByExpiry'] = round(opt['impliedVolatility'].mean(), 4)

            # Contract Type
            opt['optContractType'] = opt['contractSymbol'].str[4:].apply(lambda x: "Call" if "C" in x else "Put")
            
            # Calculate Put/Call Ratio By Expiry
            optcallChain = opt.loc[opt['optContractType'] == 'Call']
            optputChain = opt.loc[opt['optContractType'] == 'Put']
            opt['PCRbyExpiry'] = round((optputChain["volume"].sum() / optcallChain["volume"].sum()), 2)
            options = options.append(opt, ignore_index=True)

    # Bizarre error in yfinance that gives the wrong expiration date -- Not anymore 1/20/2020
    # Add 1 day to get the correct expiration date
    # options['expirationDate'] = pd.to_datetime(options['expirationDate'])
    
    # Calculate days to expire 
    options['dte'] = ((pd.to_datetime(options['expirationDate']) - datetime.datetime.today()).dt.days)
     
    # Boolean column if the option is a CALL
    options['ContractType'] = options['contractSymbol'].str[4:].apply(lambda x: "Call" if "C" in x else "Put")
    
    # Show ticker
    options['Ticker'] = ticker

    # Add Equity Price
    options['EquityPrice'] = round(last_quote, 2)

    # Calculate breakeven equity price
    options['BreakevenPrice'] = (last_quote - options['ask'])

    # Calculate Covered Call Payoff percentage per contract
    options['CoveredCallPremPayoff'] = np.round(np.where((options['ContractType'] == 'Call'), ((options['bid'] / last_quote)), '0').astype(float), 2)
    options['ITMCoveredCallPayoff'] = np.round(np.where((options['ContractType'] == 'Call'), ((options['bid'] + (options['strike'] - last_quote)) / last_quote), '0').astype(float), 2)

    # Calculate Selling Put Payoff percentage per contract
    options['SellingPutPayoff'] = np.round(np.where((options['ContractType'] == 'Put'), ((options['bid'] / last_quote)), '0').astype(float), 2)

    # Calculate Total Value of All open interest
    options['TotalOIValue'] = (options['openInterest'] * options['ask'] * 100).fillna(0).astype(int)

    # Add Contract Price Details
    options[['bid', 'ask', 'strike']] = options[['bid', 'ask', 'strike']].apply(pd.to_numeric)

    # Round to 2 decimal points
    options[['impliedVolatility', 'ask', 'strike']] = round(options[['impliedVolatility', 'ask', 'strike']], 2)

    # Get Implied Volatility Average
    options['ivAVG'] = round(options['impliedVolatility'].mean(), 4)

    # Modify Percentage Change
    options['percentChange'] = round((options['percentChange'] / 100).fillna(0), 2)
    
    # Calculate P/C Ratio
    callChain = options.loc[options['ContractType'] == 'Call']
    putChain = options.loc[options['ContractType'] == 'Put']
    options['PCR'] = round((putChain["volume"].sum() / callChain["volume"].sum()), 2)

    # Calculate Strike Diff
    options['StrikeDiffRatio'] = (options['strike'] - last_quote) / options['strike']

    # Run Timestamp
    options['RunTime'] = dt.now().strftime("%Y-%m-%d %H:%M")
    
    options_short = options[['contractSymbol'
                            ,'strike'
                            ,'bid'
                            ,'ask'
                            ,'volume'
                            ,'openInterest'
                            ,'impliedVolatility'
                            ,'PCRbyExpiry'
                            ,'StrikeDiffRatio'
                            ,'ivAVGByExpiry'                       
                            ,'expirationDate'
                            ,'ContractType'
                            ,'Ticker'
                            ,'EquityPrice'
                            ]]    

    # Filter Earliest DTE and Strike
    earliest_expiry_date = options['expirationDate'].min()

    # Filter for the specified contract type and where the strike is greater than the current equity price
    otm_options = options[(options['expirationDate'] == earliest_expiry_date) &
                          (options['ContractType'] == contractType) &
                          (options['inTheMoney'] == False) &
                          ((options['strike'] > last_quote) & (options['ContractType'] == 'Call') |
                            (options['strike'] < last_quote) & (options['ContractType'] == 'Put'))]

    # Check if there are any out-of-the-money options
    if not otm_options.empty:
        # Sort by strike and get the first OTM contract
        if contractType == 'Put':
            otm_options = otm_options.sort_values(by='strike', ascending=False).head(1)
        elif contractType == 'Call':
            otm_options = otm_options.sort_values(by='strike').head(1)
    else:
        print("No out-of-the-money options found.")

    return beautify_options_data(otm_options)

# pushNotificationSender(ODTE_Options_Finder('SPY', 'Call'))


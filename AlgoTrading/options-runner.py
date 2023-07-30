import pandas as pd
import numpy as np
import yfinance as yf
import datetime
from datetime import date
from datetime import datetime as dt
import maxPain

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
            
            #Set Expiration Date
            opt['expirationDate'] = e

            #Calculate Implied Volatility By Expiry
            opt['ivAVGByExpiry'] = round(opt['impliedVolatility'].mean(),4)

            #Contract Type
            opt['optContractType']= opt['contractSymbol'].str[4:].apply(lambda x: "Call" if "C" in x else "Put")
            
            #Calculate Put/Call Ratio By Expiry
            optcallChain = opt.loc[opt['optContractType'] == 'Call']
            optputChain = opt.loc[opt['optContractType'] == 'Put']
            opt['PCRbyExpiry'] = round((optputChain["volume"].sum() / optcallChain["volume"].sum()),2)
            options = options.append(opt, ignore_index=True)

            #Calcaulate Max Pain
            # strikes = opt(['strike']).values.tolist()
            # losses = [maxPain.total_loss_on_strike(opt, strike[0]) for strike in strikes] 
            
            # # max pain min loss to option writers/sellers at strike price
            # flat_strikes = [item for sublist in strikes for item in sublist]
            # point = losses.index(min(losses))
            # max_pain = flat_strikes[point]

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
    options['EquityPrice'] = round(last_quote,2)

    # Calculate breakeven equity price
    options['BreakevenPrice'] = (last_quote - options['ask'])

    # Calculate Covered Call Payoff percentage per contract
    options['CoveredCallPremPayoff'] = np.round(np.where((options['ContractType'] == 'Call'), ((options['bid'] / last_quote)), '0').astype(float),2)
    options['ITMCoveredCallPayoff'] = np.round(np.where((options['ContractType'] == 'Call'), ((options['bid'] + (options['strike'] - last_quote)) / last_quote ), '0').astype(float),2)

    # Calculate Selling Put Payoff percentage per contract
    options['SellingPutPayoff'] = np.round(np.where((options['ContractType'] == 'Put'), ((options['bid'] / last_quote)), '0').astype(float),2)

    # Calculate Total Value of All open interest
    options['TotalOIValue'] = (options['openInterest'] * options['ask'] * 100).fillna(0).astype(int)

    # Add Contract Price Details
    options[['bid', 'ask', 'strike']] = options[['bid', 'ask', 'strike']].apply(pd.to_numeric)

    # Round to 2 decimal points
    options[['impliedVolatility', 'ask', 'strike']] = round(options[['impliedVolatility', 'ask', 'strike']],2)

    # Get Implied Volitility Average
    options['ivAVG'] = round(options['impliedVolatility'].mean(),4)

    # Modify Percentage Change
    options['percentChange'] = round((options['percentChange']/100).fillna(0),2)
    
    # Calculate P/C Ratio
    callChain = options.loc[options['ContractType'] == 'Call']
    putChain = options.loc[options['ContractType'] == 'Put']
    options['PCR'] = round((putChain["volume"].sum() / callChain["volume"].sum()),2)

    # Calculate Strike Diff
    options['StrikeDiffRatio'] = (options['strike'] - last_quote) / options['strike']



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
                        ,'PCR'
                        ,'PCRbyExpiry'
                        ,'StrikeDiffRatio'
                        ,'ivAVG'
                        ,'ivAVGByExpiry'
                        ,'inTheMoney'
                        ,'expirationDate'
                        ,'dte'
                        ,'ContractType'
                        ,'Ticker'
                        ,'EquityPrice'
                        ,'BreakevenPrice'
                        ,'CoveredCallPremPayoff'
                        ,'ITMCoveredCallPayoff'
                        ,'SellingPutPayoff'
                        ,'TotalOIValue'
                        ,'RunTime'
                        ]]
    # Save the dataset
    # options.to_excel('C:\\Users\\Ekrem.Ersayin\\Documents\\pythonwork\\OptionsSummary\\{}_Option_Analysis.xlsx'.format(ticker))


    print("Option chain file of {} is generated!\n".format(ticker))

    options_short = options[['contractSymbol'
                            ,'strike'
                            ,'bid'
                            ,'ask'
                            ,'lastPrice'
                            ,'change'
                            ,'percentChange'
                            ,'volume'
                            ,'openInterest'
                            ,'impliedVolatility'
                            ,'PCR'
                            ,'PCRbyExpiry'
                            ,'StrikeDiffRatio'
                            ,'ivAVG'
                            ,'ivAVGByExpiry'                       
                            ,'inTheMoney'
                            ,'expirationDate'
                            ,'dte'
                            ,'ContractType'
                            ,'Ticker'
                            ,'EquityPrice'
                            ,'CoveredCallPremPayoff'
                            ,'ITMCoveredCallPayoff'
                            ,'SellingPutPayoff'
                            ]]    
    
    # #Filter out deep in the moneyC
    options_short = options_short[
        ((options_short['StrikeDiffRatio'] > (-0.025)) & (options_short['StrikeDiffRatio'] < 0.08))]

    # #Filter for 2% - 4% 
    # options_short = options_short[
    #     ((options_short['SellingPutPayoff'] >= 0.02) & (options_short['SellingPutPayoff'] < 0.1)) | 
    #     ((options_short['CoveredCallPremPayoff'] >= 0.03) & (options_short['CoveredCallPremPayoff'] < 0.08) & (options_short['dte'] < 31)) |
    #     ((options_short['ITMCoveredCallPayoff'] >= 0.03) & (options_short['ITMCoveredCallPayoff'] < 0.08) & (options_short['dte'] < 31))
    #     ]
    
    # print(options_short)   
    options_short.to_excel('C:\\Users\\ekrem\\Desktop\\Option Chain Analysis\\{}_Option_Analysis.xlsx'.format(ticker))

    return options


print(options_chain(input("Enter ticker: ")).tail(10))

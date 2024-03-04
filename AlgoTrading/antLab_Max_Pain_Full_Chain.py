'''
FILE: OptionsMaxPainCalc.py
'''
import pandas as pd
import yfinance as yf
import datetime
import matplotlib.pyplot as plt


def options_chain(tk, expiry):
    # Get options exp
    options = pd.DataFrame()
    opt = tk.option_chain(expiry.strip())
    opt = pd.DataFrame().append(opt.calls).append(opt.puts)
    opt['expirationDate'] = expiry
    options = options.append(opt, ignore_index=True)
    
    # Add 1 day to get the correct expiration date
    options['expirationDate'] = pd.to_datetime(options['expirationDate']) + datetime.timedelta(days = 1)
    options['dte'] = (options['expirationDate'] - datetime.datetime.today()).dt.days / 365
    
    # Boolean column if the option is a CALL
    options['CALL'] = options['contractSymbol'].str[4:].apply(lambda x: "C" in x)
    
    options[['bid', 'ask', 'strike','impliedVolatility']] = options[['bid', 'ask', 'strike','impliedVolatility']].apply(pd.to_numeric)
    
    # Drop unnecessary and meaningless columns
    options = options.drop(columns = ['contractSize', 'currency', 'change', 'percentChange', 'lastTradeDate', 'lastPrice'
                                      , 'contractSymbol', 'bid', 'ask', 'inTheMoney', 'dte'])
    
    return options
    
def total_loss_on_strike(chain, expiry_price):
    '''
    Get's the total loss at the given strike price
    '''    
    # call options with strike price below the expiry price -> loss for option writers
    callChain = chain.loc[chain['CALL'] == True]
    callChain = callChain.dropna()       
    in_money_calls = callChain[callChain['strike'] < expiry_price][["openInterest", "strike"]]
    in_money_calls["CLoss"] = (expiry_price - in_money_calls['strike'])*in_money_calls["openInterest"]

    # get puts n drop null values
    putChain = chain.loc[chain['CALL'] == False]
    putChain = putChain.dropna()    
    
    # put options with strike price above the expiry price -> loss for option writers
    in_money_puts = putChain[putChain['strike'] > expiry_price][["openInterest", "strike"]]
    in_money_puts["PLoss"] = (in_money_puts['strike'] - expiry_price)*in_money_puts["openInterest"]
    total_loss = in_money_calls["CLoss"].sum() + in_money_puts["PLoss"].sum()

    return total_loss


def main():
    '''
    Get's the symbol and expiry date n plot the data
    '''
    symbol = input("Enter the Symbol: " )
    tk = yf.Ticker(symbol)
    expiries = tk.options
    for expiry in expiries:
        chain = options_chain(tk, expiry)
        
        strikes = chain.get(['strike']).values.tolist()
        losses = [total_loss_on_strike(chain, strike[0]) for strike in strikes] 
        
        # max pain min loss to option writers/sellers at strike price
        flat_strikes = [item for sublist in strikes for item in sublist]
        point = losses.index(min(losses))
        max_pain = flat_strikes[point]
        buffer = 3
        bufferHigh = max_pain + (max_pain * (buffer/100))
        bufferLow = max_pain - (max_pain * (buffer/100))
        # print(f"Expiry: {expiry}")
        # print(f"Maximum Pain: {bufferLow} < {max_pain} < {bufferHigh}")
        
        # calc put to call ratio
        callChain = chain.loc[chain['CALL'] == True]
        putChain = chain.loc[chain['CALL'] == False]
        pcr = putChain["volume"].sum() / callChain["volume"].sum()
        putAvgIV = putChain['impliedVolatility'].mean()
        callAvgIV = callChain['impliedVolatility'].mean()
        avgIV = (putAvgIV + callAvgIV)/2
        # print(callAvgIV)
        # print("Put to call ratio:", round(pcr,2))
        # print()

        print(f"EXP: {expiry}", "||",
              f"MP: {bufferLow} < {max_pain} < {bufferHigh}", "||",
              f"PCR:", round(pcr,2), "||", 
              f"AvG IV:", round(avgIV,2)
            )

# if __name__ == "__main__":
#     main()
        

main()

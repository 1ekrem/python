# https://medium.com/@rajsingh.tarun/automate-option-chain-analysis-in-python-tips-for-successful-option-trading-4682bfede2bb

import requests
import pandas as pd
import numpy as np
from scipy.stats import norm
from bs4 import BeautifulSoup

def scrape_options_chain(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}/options?p={ticker}"
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    calls = soup.find_all('table')[0]
    puts = soup.find_all('table')[1]
    calls_df = pd.read_html(str(calls))[0]
    puts_df = pd.read_html(str(puts))[0]
    calls_df = calls_df.loc[:, ['Contract Name', 'Last Trade Date', 'Strike', 'Last Price', 'Bid', 'Ask', 'Change', 'Percent Change', 'Volume', 'Open Interest', 'Implied Volatility']]
    puts_df = puts_df.loc[:, ['Contract Name', 'Last Trade Date', 'Strike', 'Last Price', 'Bid', 'Ask', 'Change', 'Percent Change', 'Volume', 'Open Interest', 'Implied Volatility']]
    calls_df['Type'] = 'call'
    puts_df['Type'] = 'put'
    options_df = pd.concat([calls_df, puts_df])
    options_df = options_df.reset_index(drop=True)
    return options_df

def black_scholes(S, K, T, r, sigma, option='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option == 'call':
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)


def analyze_options_chain(options_df):
    df = options_df.copy()
    df = df[df['Implied Volatility'].notnull()]
    df['Implied Volatility'] = df['Implied Volatility'].str.strip('%').astype(float) / 100
    df['Last Trade Date'] = pd.to_datetime(df['Last Trade Date'])
    df = df.sort_values('Strike')
    df['Theoretical Price'] = df.apply(lambda row: black_scholes(df['Last Price'][0], row['Strike'], 
                                      (row['Last Trade Date'] - df['Last Trade Date'][0]).days / 365, 
                                      0.02, row['Implied Volatility'], option='call'), axis=1)
    df['Profit/Loss if Expired'] = df.apply(lambda row: (row['Theoretical Price'] - row['Ask']) 
                                            if row['Type'] == 'call' else (row['Bid'] - row['Theoretical Price']), axis=1)
    df['Probability of Profit'] = df.apply(lambda row: norm.cdf((row['Theoretical Price'] - 
                                            df['Last Price'][0]) / (row['Implied Volatility'] * 
                                            np.sqrt((row['Last Trade Date'] - df['Last Trade Date'][0]).days / 365))), axis=1)
    return df



ticker = 'AAPL'
options_df = scrape_options_chain(ticker)
analyzed_options_df = analyze_options_chain(options_df)
print(analyzed_options_df.head())



# Contract Name Last Trade Date  Strike  Last Price   Bid   Ask  Change  \
# 0  AAPL220318C00065000      2023-03-04    65.0        0.02  0.00  0.05    0.00   
# 1  AAPL220318C00070000      2023-03-03    70.0        0.01  0.00  0.05   -0.03   
# 2  AAPL220318C00075000      2023-03-04    75.0        0.01  0.00  0.05   -0.03   
# 3  AAPL220318C00080000      2023-03-04    80.0        0.01  0.00  0.05   -0.04   
# 4  AAPL220318C00085000      2023-03-03    85.0        0.01  0.00  0.05   -0.04 

# Percent Change  Volume  Open Interest  Implied Volatility  Type  \
# 0        0.00e+00       3              0               0.245  call   
# 1       -7.59e-01     114             34               0.210  call   
# 2       -7.59e-01      54            101               0.185  call   
# 3       -7.14e-01      27            145               0.168  call   
# 4       -7.14e-01      56            187               0.154  call   
#    Theoretical Price  Profit/Loss if Expired  Probability of Profit  
# 0               2.60                    0.00                   0.54  
# 1               3.59                    3.54                   0.39  
# 2               4.63                    4.58                   0.35  
# 3               5.73                    5.68                   0.32  
# 4               6.86                    6.81                   0.30  
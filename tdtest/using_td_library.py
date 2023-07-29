from tda import auth, client
from tda_config import CONSUMER_KEY, REDIRECT_URI, JSON_PATH
import json
import pprint
from ekrem import ACCOUNT_NUMBER
import datetime
import pandas as pd
from pandas.io.json import json_normalize
import itertools
import flatten_json

try:
    c = auth.client_from_token_file(JSON_PATH, CONSUMER_KEY)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome() as driver:
        c = auth.client_from_login_flow(
            driver, CONSUMER_KEY, REDIRECT_URI, JSON_PATH)

#r = c.get_price_history('AAPL',
#        period_type=client.Client.PriceHistory.PeriodType.YEAR,
#        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
#        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
#        frequency=client.Client.PriceHistory.Frequency.DAILY)
#assert r.status_code == 200, r.raise_for_status()
#print(json.dumps(r.json(), indent=4))

#response = c.get_quote('BA')

# response = c.search_instruments(['AAPL', 'AMD'], c.Instrument.Projection.FUNDAMENTAL)
# print(json.dumps(response.json(), indent=4))

allresponse = c.get_option_chain('PLTR', contract_type= None)
allResponseData = allresponse.json()
df = pd.DataFrame(allResponseData)



x = flatten_json.flatten(allresponse)

 
x = pd.json_normalize(allresponse['callExpDateMap']['2021-11-12:6']['27.0'])
x = pd.json_normalize(allresponse)
print(x)

# for word in df["callExpDateMap"]:
#         for each in word:
#             if each == "29.0":
#                 print(df[word])

# print(df["theoreticalOptionValue"])


# response = c.get_option_chain('PLTR', contract_type= c.Options.ContractType.CALL, strike='35')
#response = (response['callExpDateMap']['2021-11-12:6'])
# opt_ch = response.json()

# # opt_ch = opt_ch['symbol'] ['underlyingPrice'] [0]
# df = pd.DataFrame(opt_ch)
# df.to_excel('C:\\Users\\ekrem\\Desktop\\Option Chain Analysis\\test.xlsx')
#print("done")
# print(df["underlyingprice"])
 


# print(json.dumps(response.json(), indent=4))

# expiration_dates = []
# strike_temp = []
# strikePrices_temp = []

# # Get Expiration Dates and Create temp table to retrieve Strike prices
# for key, value in responsedump['callExpDateMap'].items():
#     expiration_dates.append(key)
#     strike_temp.append(value)

# # Get Strike Prices
# for calldate in strike_temp:
#     for key, value in calldate.items():
#         strikePrices_temp.append(key)


# # Remove duplicates from the strike prices
# strikePrices = []
# [strikePrices.append(single) for single in strikePrices_temp if single not in strikePrices]
# print(strikePrices)
# print(expiration_dates)


# x = flatten_json.flatten(responsedump)

 
# x = pd.json_normalize(responsedump['callExpDateMap']['2021-03-26:6']['27.0'])
# x = pd.json_normalize(responsedump)
#print(x)

# HOW TO LOOP NESTED DICTIONARIES?
#print(callExpDates)

#Create a dataset
# df = pd.DataFrame(x)

# # Fix Date Format
# df['tradeTimeInLong'] = pd.to_datetime(df['tradeTimeInLong'], unit='ms')
# df['quoteTimeInLong'] = pd.to_datetime(df['quoteTimeInLong'], unit='ms')
# df['expirationDate'] = pd.to_datetime(df['expirationDate'], unit='ms')
# df['lastTradingDay'] = pd.to_datetime(df['lastTradingDay'], unit='ms')

# # Add Ticker, EquityPrice, Volatility Ratio to Dataset
# symbol = responsedump['symbol']
# underlyingPrice = responsedump['underlyingPrice']
# volatility = responsedump['volatility']

# df['symbol'] = symbol
# df['equityPrice'] = underlyingPrice
# df['stockVolatility'] = volatility

# # Store data in excel
# df.to_excel('C:\\Users\\ekrem\\Desktop\\Option Chain Analysis\\PLTR_TDAPI_Option_Analysis.xlsx')
# print("Loaded")





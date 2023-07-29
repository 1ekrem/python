from tda import auth, client
from config import CONSUMER_KEY, REDIRECT_URI, JSON_PATH
import json
import pprint
from ekrem import ACCOUNT_NUMBER
import datetime
import pandas as pd
from pandas.io.json import json_normalize
import pprint

try:
    c = auth.client_from_token_file(JSON_PATH, CONSUMER_KEY)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome() as driver:
        c = auth.client_from_login_flow(
            driver, CONSUMER_KEY, REDIRECT_URI, JSON_PATH)



response = c.get_option_chain('SPY')
data = response.json()
# print(data)

putCall= ['callExpDateMap','putExpDateMap']
dset = []
for i in putCall:
    child_data = data[i]
    del data [i]
    for expiration_date, price_data in child_data.items():
        expiration_date, day_remaining = expiration_date.split(':')
        for price, details in price_data.items():
                for detail in details:
                    print({
                        'underlyingPrice' : data['underlyingPrice'],
                        'strikePrice' : detail['strikePrice'], 
                        'symbol': detail['symbol'],
                        'description' : detail['description'],
                        'openInterest' : detail['openInterest'],
                        'totalVolume' : detail['totalVolume'],
                        'putCall' : detail['putCall'],
                        'bid' : detail['bid'],
                        'ask' : detail['ask'],
                        'lowPrice' : detail['lowPrice'],
                        'highPrice' : detail['highPrice'],
                        'daysToExpiration' : detail['daysToExpiration'],
                        'percentChange' : detail['percentChange'],
                        'volatility' : detail['volatility'],
                        'delta' : detail['delta'],
                        'gamma' : detail['gamma'],
                        'theta' : detail['theta'],
                        'inTheMoney' : detail['inTheMoney']
                    })
                    dset.append({
                        'ticker' : data['symbol'],
                        'ContractCode': detail['symbol'],
                        'description' : detail['description'],
                        'underlyingPrice' : data['underlyingPrice'],
                        'strikePrice' : detail['strikePrice'], 
                        'openInterest' : detail['openInterest'],
                        'totalVolume' : detail['totalVolume'],
                        'putCall' : detail['putCall'],
                        'bid' : detail['bid'],
                        'ask' : detail['ask'],
                        'lowPrice' : detail['lowPrice'],
                        'highPrice' : detail['highPrice'],
                        'daysToExpiration' : detail['daysToExpiration'],
                        'percentChange' : detail['percentChange'],
                        'volatility' : detail['volatility'],
                        'delta' : detail['delta'],
                        'gamma' : detail['gamma'],
                        'theta' : detail['theta'],
                        'inTheMoney' : detail['inTheMoney']
                    })
                    
df = pd.DataFrame(dset)
df.to_excel("{}-tda.xlsx".format(data['symbol']))


print(df)


# Get priceHistory
# priceHistory = c.get_price_history(symbol="PLTR")
# pprint.pprint(priceHistory.json())


# r = c.get_price_history('AAPL',
#        period_type=client.Client.PriceHistory.PeriodType.YEAR,
#        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
#        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
#        frequency=client.Client.PriceHistory.Frequency.DAILY)
# assert r.status_code == 200, r.raise_for_status()
# print(json.dumps(r.json(), indent=4))

# response = c.get_quote("BA")
# print(response.json())

#response = c.search_instruments(['AAPL', 'AMD'], c.Instrument.Projection.FUNDAMENTAL)
# print(json.dumps(response.json(), indent=4))



# x = pd.json_normalize(data['callExpDateMap'])
# print(x)

# child_data = data[]

# for field in data.items():
#     print(field)
#     #row = field[symbol][status]
#     #rows.append(row)

# data = pd.DataFrame(rows)

# print(data)
#print(json.dumps(response.json(), indent=4))

# Positions and Order an Account
# orders_and_positions = c.get_account(account_id=ACCOUNT_NUMBER)
# pprint.pprint(orders_and_positions.json())





# for key, value in responsedump['callExpDateMap'].items():
#     print(key)

# # Create a dataset
# df = pd.DataFrame(x)
# datesonly = df['tradeTimeInLong']
# print(datesonly)

# # Fix Date Format
# df['tradeTimeInLong'] = pd.to_datetime(df['tradeTimeInLong'], unit='ms')
# df['quoteTimeInLong'] = pd.to_datetime(df['quoteTimeInLong'], unit='ms')
# df['expirationDate'] = pd.to_datetime(df['expirationDate'], unit='ms')
# df['lastTradingDay'] = pd.to_datetime(df['lastTradingDay'], unit='ms')

# # Get Ticker and add to 
# symbol = responsedump['symbol']
# underlyingPrice = responsedump['underlyingPrice']
# volatility = responsedump['volatility']

# df['symbol'] = symbol


# # Store data in excel
#df.to_excel('C:\\Users\\ekrem\\Desktop\\Option Chain Analysis\\PLTR_TDAPI_Option_Analysis.xlsx')

# Call by specific time frame
# start_date = datetime.datetime.strptime('2021-02-01', '%Y-%M-%d').date()
# end_date = datetime.datetime.strptime('2021-02-31', '%Y-%M-%d').date()

# # Get data in STR
# response = c.get_option_chain('PLTR', contract_type= c.Options.ContractType.CALL, strike='35')
# responsedump = json.dumps(response.json(), indent=4)
# # print(type(responsedump))



# # Convert it to Dictionary
# dictresponse = json.loads(responsedump)
# # print(type(dictresponse))

# print(dictresponse['callExpDateMap'])

# Dump data into a JSON file
# location = 'C://PythonClass//tdtest//'
# filename = 'test'
# extention = '.json'
# fullpath = location+filename+extention

# with open(fullpath, 'w') as file_object:
#     json.dump(responsedump, file_object)
# print('DUMPED')
from ast import Import
from tda import auth, client
#from tda.orders import EquityOrderBuilder, Duration, Session
import json
import config
import datetime
import ekrem

# authenticate
try:
    c = auth.client_from_token_file(config.JSON_PATH, config.CONSUMER_KEY)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome() as driver:
        c = auth.client_from_login_flow(
            driver, config.CONSUMER_KEY, config.REDIRECT_URI, config.JSON_PATH)

# get price history for a symbol
r = c.get_price_history('AAPL',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)

#print(json.dumps(r.json(), indent=4))

# get a stock quote
response = c.get_quote('AAPL')

#print(response.json())


#Positions and Order an Account
orders_and_positions = c.get_account(account_id=ekrem.ACCOUNT_NUMBER)
print(orders_and_positions.json())


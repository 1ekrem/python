import requests
import key as apikey
import pprint

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=N7I0AUJQV0JQ2WX1'
r = requests.get(url)
data = r.json()

pprint.pprint(data)
import requests
import csv
from alphaVentageKey import keyValue
from datetime import date

CSV_URL = 'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=keyValue'
todayDate = date.today()

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    print(my_list)
    
    USMarketTickers = "C:\\PythonClass\\AlgoTrading\\Alphavantage\\USMarketTickers\\USMarketTicker-{}.csv".format(todayDate)
    with open (USMarketTickers, 'w') as list_file:
        for row in my_list:
            row = row[0]
            list_file.write(str(row) + '\n')
            # print(row)
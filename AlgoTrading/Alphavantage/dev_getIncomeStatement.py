import requests
from alphaVentageKey import keyValue
import json

ticker = input("Enter Ticker: ")
url = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={}&apikey=keyValue'.format(ticker)
r = requests.get(url)
data = r.json()

# print(data)

quarterly_reports = data.get('quarterlyReports', [])
# print(data)

# Get Latest Report
filtered_data = quarterly_reports[0]

for report in quarterly_reports:
    if report.get('fiscalDateEnding') > filtered_data.get('fiscalDateEnding'):
        filtered_data = report

# print(filtered_data)

# # Get Latest Report Option 2
# latest_report = max(quarterly_reports, key=lambda report: report.get('fiscalDateEnding'))

# print(latest_report)

# Filter data by fiscalDateEnding field
# filtered_data = [item for item in quarterly_reports if item.get('fiscalDateEnding') == '2023-03-31']
#print(filtered_data)

# # Extract required fields from filtered data and show values in millions
filtered_data_extracted = {'fiscalDateEnding': filtered_data.get('fiscalDateEnding'),
                            'reportedCurrency' : filtered_data.get('reportedCurrency'),
                            'totalRevenue' : filtered_data.get('totalRevenue'),
                            'costOfRevenue' : filtered_data.get('costOfRevenue'),                            
                            'operatingIncome': filtered_data.get('operatingIncome'),
                            'interestAndDebtExpense' : filtered_data.get('interestAndDebtExpense'),
                            'commonStockSharesOutstanding' : filtered_data.get('commonStockSharesOutstanding'),
                            'OperatingMargin' : round(float(filtered_data.get('operatingIncome')) / (float(filtered_data.get('totalRevenue'))),2),
                            'ProfitMargin' : round(float(filtered_data.get('netIncome')) / (float(filtered_data.get('totalRevenue'))),2),
                            'CostMargin' : round(float(filtered_data.get('costOfRevenue')) / (float(filtered_data.get('totalRevenue'))),2)                                                        
                            }
                           
formatted_data = json.dumps(filtered_data_extracted, indent=4)

if filtered_data_extracted.get('CostMargin') < 0.25: 
    print(formatted_data)

# Fields to Capture
    #totalRevenue
    #costOfRevenue
    #operatingIncome
    #interestAndDebtExpense
    #netIncome
    #commonStockSharesOutstanding



#Calculate Operating Margin
    #(operatingIncome/totalRevenue) / 100

#Calculate Profit Margin
    #(netIncome/totalRevenue) / 100

#Calculate Cost Margin
    #(costOfRevenue/totalRevenue) / 100
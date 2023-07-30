import requests
import json
from alphaVentageKey import keyValue

ticker = input("Enter Your Ticker: ")
url = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={}&apikey=keyValue'.format(ticker)
r = requests.get(url)
# print(url)
data = r.json()

# Get the 'quarterlyReports' field from the response
quarterly_reports = data.get('quarterlyReports', [])
print(quarterly_reports)

# Get Latest Report
# latest_report = quarterly_reports[0]

# for report in quarterly_reports:
#     if report.get('fiscalDateEnding') > latest_report.get('fiscalDateEnding'):
#         latest_report = report


# # Get Latest Report Option 2
# latest_report = max(quarterly_reports, key=lambda report: report.get('fiscalDateEnding'))

# print(latest_report)


# Filter data by fiscalDateEnding field
# filtered_data = [item for item in quarterly_reports if item.get('fiscalDateEnding') == '2023-03-31']

# # Extract required fields from filtered data and show values in millions
filtered_data_extracted = [{'fiscalDateEnding': item.get('fiscalDateEnding'),
                            'reportedCurrency' : item.get('reportedCurrency'),
                            'cashAndCashEquivalents': float(item.get('cashAndCashEquivalentsAtCarryingValue'))/1000000,
                            'totalLiabilities' : float(item.get('totalLiabilities'))/1000000,
                            # 'currentDebt' : float(item.get('currentDebt'))/1000000,
                            'shortTermDebt' : item.get('shortTermDebt')
                            }
                           for item in filtered_data]


# # Beautify JSON filtered data
formatted_data = json.dumps(filtered_data_extracted, indent=4)

# # Print the formatted data
# print(formatted_data)
import requests
import json
from alphaVentageKey import keyValue
from pushover import pushNotificationSender

ticker = input("Enter Your Ticker: ")
url = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={}&apikey=keyValue'.format(ticker)
r = requests.get(url)
# print(url)
data = r.json()

# Get the 'quarterlyReports' field from the response
quarterly_reports = data.get('quarterlyReports', [])
# print(quarterly_reports)

# Get Latest Report
filtered_data = quarterly_reports[0]

for report in quarterly_reports:
    if report.get('fiscalDateEnding') > filtered_data.get('fiscalDateEnding'):
        filtered_data = report

print(filtered_data)


# # Get Latest Report Option 2
# latest_report = max(quarterly_reports, key=lambda report: report.get('fiscalDateEnding'))

# print(latest_report)


# Filter data by fiscalDateEnding field
# filtered_data = [item for item in quarterly_reports if item.get('fiscalDateEnding') == '2023-03-31']

# Convert relevant values to numeric types
# short_term_debt = float(filtered_data.get('shortTermDebt', 0))
short_long_term_debt_total = float(filtered_data.get('shortLongTermDebtTotal', 0))
total_assets = float(filtered_data.get('totalAssets', 1))  # Avoid division by zero

# Calculate Ratios
debt_to_equity_ratio = round(((short_long_term_debt_total) / (total_assets + float(filtered_data.get('totalLiabilities', 0))))*100,2)

# # Extract required fields from filtered data and show values in millions
filtered_data_extracted = {'ticker': ticker,
                           'statementType': 'Balance Sheet',                           
                            'fiscalDateEnding': filtered_data.get('fiscalDateEnding'),
                            'reportedCurrency' : filtered_data.get('reportedCurrency'),
                            'cashAndCashEquivalents': float(filtered_data.get('cashAndCashEquivalentsAtCarryingValue',0)),
                            'totalAssets' : float(filtered_data.get('totalAssets')),                            
                            'totalLiabilities' : float(filtered_data.get('totalLiabilities')),
                            'currentDebt' : filtered_data.get('currentDebt'),
                            'shortTermDebt' : filtered_data.get('shortTermDebt'),
                            'commonStockSharesOutstanding' : filtered_data.get('commonStockSharesOutstanding'),
                            'debtToEquityRatio' : debt_to_equity_ratio
                            }


# # Beautify JSON filtered data
formatted_data = json.dumps(filtered_data_extracted, indent=4)
print(formatted_data)
pushNotificationSender(formatted_data)


# # Print if currentDebt is None
# if filtered_data_extracted['currentDebt'] == 'None':
#     print(formatted_data)
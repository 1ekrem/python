import FundamentalAnalysis as fa
import env_var
import datetime 

"""Time"""
#now = datetime.datetime.now()
#dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#
period_var = 'Quarter'

"""STATEMENTS"""

# Get Cashflow
def get_cashflow_statement(ticker, period_val=period_var):
    cf_statement = fa.cash_flow_statement(ticker,env_var.api_key,period=period_var)
    cf_statement.to_csv("C:\\Users\\ekrem\\Desktop\\Trade Analysis\\Financials\\{}_cf_statement.csv".format(ticker))
    print("{} Cash Flow Statement is ready.".format(ticker))

# Get Balance Sheet
def get_balance_sheet_statement(ticker, period_val="quarter"):
    balance_sheet = fa.balance_sheet_statement(ticker=ticker, api_key=env_var.api_key, period=period_var)
    balance_sheet.to_csv("C:\\Users\\ekrem\\Desktop\\Trade Analysis\\Financials\\{}_balance_sheet.csv".format(ticker))
    print("{} Balance Sheet is ready.".format(ticker))
    
# Get Key Metrics
def get_key_metrics(ticker, period_val=period_var):
    key_metric_data = fa.key_metrics(ticker,env_var.api_key,period=period_val)
    key_metric_data.to_csv("C:\\Users\\ekrem\\Desktop\\Trade Analysis\\Financials\\{}_key_metrics.csv".format(ticker))
    print("{} Key Metrics statement is ready.".format(ticker))
    
# Get Financial Statement Yearly Growth
def get_financial_statement_growth(ticker, period_val=period_var):
    financial_statement_growth = fa.financial_statement_growth(ticker=ticker, api_key=env_var.api_key, period=period_val)
    financial_statement_growth.to_csv("C:\\Users\\ekrem\\Desktop\\Trade Analysis\\Financials\\{}{}{}_financial_statement_growth.csv".format(ticker," ",period_var))
    print("{}{}{} Financial Growth Statement is ready.".format(ticker," ", period_var))
    
def get_discounted_cash_flow_statement(ticker, period_val=period_var):
    discounted_cash_flow_statement = fa.discounted_cash_flow(ticker=ticker, api_key=env_var.api_key, period=period_val)
    discounted_cash_flow_statement.to_csv("C:\\Users\\ekrem\\Desktop\\Trade Analysis\\Financials\\{}_discounted_cash_flow_statement.csv".format(ticker))
    print("{} Discounted Cash flow Statement is ready.".format(ticker))

def run_financial_reports(ticker):
    #get_balance_sheet_statement(ticker) 
    #get_cashflow_statement(ticker)
    #get_discounted_cash_flow_statement(ticker)
    #get_financial_statement_growth(ticker)
    get_key_metrics(ticker)
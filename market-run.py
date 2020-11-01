from taReportSector import get_stock_prices, tech_analysis, createAnalysis
"""Group of functions that generate daily buy/sell signals for listed tickers"""

growth = ['AMD', 'NVDA', 'BA', 'TSLA']
financial = ['BAC','C','GS','JPM','MS']
bluechip = ['WMT','MSFT','NFLX','ROKU']

for ticker in bluechip:
    get_stock_prices(ticker)
    tech_analysis(ticker)
    createAnalysis(ticker)
    print("Report is generated for {}! Please check your Desktop - Trade Analysis folder".format(ticker))

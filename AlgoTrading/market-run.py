from taReportSector import get_stock_prices, tech_analysis, createAnalysis
from option_analysis import options_chain
from pandas_datareader._utils import RemoteDataError
from financial_reports import run_financial_reports
from technical_analysis_report import technical_analysis_report
from breakoutFinder import breakout_finder, golden_zone_finder
from startegies import in_consolidation, consolidation_range
from SPX import SPX
from NDX import NDX
from NDX100 import NDX100

"""Group of functions that generate daily buy/sell signals for listed tickers"""

bluechip = ['WMT','MSFT','AAPL','BA', 'AMZN','FB', 'GOOGL', 'NVDA']
financial = ['BAC','C','GS','JPM','MS', 'WFC']
airlines = ['AAL', 'BA','JBLU','SAVE','UAL', 'LUV', 'DAL']
ev_car_manufacturers = ['TSLA','LCID','NIO', 'GE', 'F', 'RIVN']
social_media = ['FB','TWTR','SNAP','PINS']
semiconductor = ['LRCX', 'AMAT','TSM','MU','INTC','AMD','NVDA','MRVL']
crypto = ['COIN', 'MARA', 'HUT']
chinese = ['BABA', 'NIO', 'BIDU', 'PDD', 'JD']

single = ['^SPX']
etailer = ['AMZN','BABA', 'SHOP','DENEME']  

#Daily
daily_analysis = ['LCID','F','M','VXX','NIO','PLTR','SOFI','TWTR','HOOD','PYPL']
daily_option_test = ['NIO','BABA','AAPL', 'NVDA', 'TWTR']
fin_viz_daily = ['F','AAPL','NIO','AMD','BAC', 'SQ']

march_week_2 = ['SPY', 'UVXY', 'QQQ', 'AMD', 'AAL', 'XOM', 'GDX', 'MU', 'MRVL', 'RIVN', 'SQ']
Agricultural = ['MOS', 'CF' , 'NTR', 'CTVA', 'FMC', 'PDD']

positions = ['PDD', 'GM']

goldenList=[]

for ticker in NDX100:
    #breakout_finder(ticker, 2.5)
    golden_zone_finder(ticker)
    #technical_analysis_report(ticker)
    #options_chain(ticker)
    #run_financial_reports(ticker)
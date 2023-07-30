import yfinance as yf

ticker = yf.Ticker(input("Enter Ticker: "))

# show financials:
# - income statement
ticker.info
import yfinance as yf
import pandas as pd

# Define the ticker symbol and timeframe
ticker = "AAPL"
start_date = "2022-01-01"
end_date = "2022-12-31"

# Fetch the historical stock data using yfinance
data = yf.download(ticker, start=start_date, end=end_date)

# Calculate the volume divergence
data["Volume_ROC"] = data["Volume"].pct_change()

# Find the dates with volume divergence
divergence_dates = data[data["Volume_ROC"] != 0].index

# Print the dates with volume divergence
print("Dates with Volume Divergence:")
print(divergence_dates)

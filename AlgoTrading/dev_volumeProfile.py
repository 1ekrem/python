import yfinance as yf
import pandas as pd

def get_stock_data(symbol, start_date, end_date):
    # Download historical data
    data = yf.download(symbol, start=start_date, end=end_date, interval='1d')
    return data

def group_volume_by_price(data):
    # Round the 'Close' prices and group by the rounded prices
    data['Rounded_Price'] = data['Close'].round(0)
    grouped_data = data.groupby('Rounded_Price')['Volume'].sum().reset_index()
    return grouped_data

def display_top_prices(grouped_data, n=10):
    # Display the top n prices with the highest volume
    top_prices = grouped_data.nlargest(n, 'Volume')
    print(top_prices)

if __name__ == "__main__":
    # Replace 'AAPL' with the desired stock symbol
    stock_symbol = 'BABA'
    
    # Set the start and end dates for the data
    start_date = '2022-11-01'
    end_date = '2023-12-11'
    
    # Get stock data
    stock_data = get_stock_data(stock_symbol, start_date, end_date)
    
    # Group volume by rounded price
    grouped_data = group_volume_by_price(stock_data)
    
    # Display the top 10 prices with the highest volume
    display_top_prices(grouped_data, n=10)

import pandas as pd
from pandas_datareader.data import Options

def download_option_chain(ticker):
    try:
        # Create an Options object for the specified stock symbol using Alpha Vantage
        options = Options(ticker, 'av')

        # Get the option chain data
        option_chain = options.get_all_data()

        # Print the DataFrame
        print(option_chain)

        # Save the DataFrame to a CSV file
        file_path = f"{ticker}_option_chain.csv"
        option_chain.to_csv(file_path)

        print(f"\nOption chain data for {ticker} downloaded successfully. Saved to {file_path}")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Prompt the user to enter a stock symbol
    stock_symbol = input("Enter stock symbol: ").upper()

    # Download and print the option chain data
    download_option_chain(stock_symbol)

import yfinance as yf

yf.Tickers()

def get_most_active_tickers():
    # Get the S&P 500 ticker symbols
    sp500_tickers = yf.Tickers()

    for tickers in sp500_tickers:
        print(tickers)
    # Initialize an empty dictionary to store ticker symbols and their volumes
    volumes = {}

    # # Iterate through each ticker in the S&P 500
    # for ticker in sp500_tickers:
    #     # Fetch historical data for the past day
    #     hist_data = ticker.history(period="1d")

    #     # Calculate the total trading volume for the day
    #     total_volume = hist_data["Volume"].sum()

    #     # Store the ticker symbol and its total volume in the dictionary
    #     volumes[ticker.ticker] = total_volume

    # # Sort the tickers based on their trading volumes in descending order
    # sorted_tickers = sorted(volumes.items(), key=lambda x: x[1], reverse=True)

    # # Print the top N most active tickers
    # top_n = 10  # You can adjust this number based on your preference
    # print(f"Top {top_n} most active tickers:")
    # for i in range(top_n):
    #     print(f"{i + 1}. {sorted_tickers[i][0]} - Volume: {sorted_tickers[i][1]}")

if __name__ == "__main__":
    get_most_active_tickers()
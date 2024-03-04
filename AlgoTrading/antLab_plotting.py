import matplotlib.pyplot as plt

def antlab_plotting(df, ticker):

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'], label='Close Price', color='black')
    # plt.plot(df.index, df['10ma'], label='10-Day MA', color='blue')
    # plt.plot(df.index, df['20ma'], label='20-Day MA', color='red')
    plt.plot(df.index, df['50ma'], label='50-Day MA', color='green')
    # plt.plot(df.index, df['ATR'], label='ATR', color='yellow')
    plt.scatter(df.index[df['VPF_TradeSignal'] == 'BUY'], df['Close'][df['VPF_TradeSignal'] == 'BUY'], label='Buy Signal', marker='^', color='green', lw=3)
    plt.scatter(df.index[df['VPF_TradeSignal'] == 'SELL'], df['Close'][df['VPF_TradeSignal'] == 'SELL'], label='Sell Signal', marker='v', color='red', lw=3)
    plt.title('Analysis of {}'.format(ticker))
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()
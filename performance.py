import matplotlib.pyplot as plt 

def plot_closing_price(symbol, df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Close'], label=f'{symbol} Closing Prices')
    plt.title(f'Closing Prices of {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    plt.grid(True)
    plt.show()

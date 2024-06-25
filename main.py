from fetch import download_historical_data
import matplotlib.pyplot as plt 
from performance import plot_closing_price
import datetime

# Parameters
symbol = 'RELIANCE.NS'
start_date = '2024-06-01'
end_date = datetime.datetime.today().strftime('%Y-%m-%d')

timeframe = '1d'  # '1wk', '1mo'  ... in case we want weekly and monthly data

# Fetch data
df = download_historical_data(symbol, start_date, end_date, timeframe)

print(df) # .......... we can print it too to view

plot_closing_price(symbol, df)
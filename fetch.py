import yfinance as yf
import pandas as pd

def download_historical_data(symbol, start_date, end_date, timeframe='1d'):
    
    data = yf.download(symbol, start=start_date, end=end_date, interval=timeframe)
    return data

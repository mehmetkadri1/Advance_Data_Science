import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)


stock_data_tesla=yf.Ticker('TSLA')

tesla_data=stock_data_tesla.history(period='max')
tesla_data.reset_index(inplace=True)
tesla_data.head()
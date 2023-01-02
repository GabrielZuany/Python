from api_key import api_key
import requests
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
import numpy as np
import mplcursors as mpc


plt.style.use('ggplot')

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=IBM&interval=15min&apikey={api_key}&datatype=csv"

response = requests.get(url)
csv_text = response.text

data = pd.read_csv(StringIO(csv_text))

data['timestamp'] = pd.to_datetime(data['timestamp'])
dates = data['timestamp']

price_adj_close = data['adjusted close']
price_adj_close = np.array(price_adj_close, dtype=float)

price_open = data['open']
price_open = np.array(price_open, dtype=float)

interval_a = 0
interval_b = 24 #last 24 months
date_interval = dates[interval_a:interval_b]
close_price_interval = price_adj_close[interval_a:interval_b]
price_open_interval = price_open[interval_a:interval_b]
close_interval_mean = close_price_interval.mean()
open_interval_mean = price_open_interval.mean()

plt.plot_date(date_interval, close_price_interval, linewidth=0.7, linestyle='solid', label='IBM Close Price', marker='.', color='g') #plot the last n months
plt.plot_date(date_interval, price_open_interval, linewidth=0.7, linestyle='solid', label='IBM Open Price', marker='.', color='b') #plot the last n months

plt.gcf().autofmt_xdate() #rotate data label axis
plt.axhline(close_interval_mean, color='g', linewidth=0.5, label='Avg Close Line')
plt.axhline(open_interval_mean, color='b', linewidth=0.5, label='Avg Open Line')

plt.fill_between(date_interval, close_price_interval, price_open_interval, where=(close_price_interval > price_open_interval), interpolate=True, color='b', alpha=0.25, label='Above Open Price')

plt.fill_between(date_interval, close_price_interval, price_open_interval, where=(close_price_interval < price_open_interval), interpolate=True, alpha=0.25, color='r', label='Below Open Price')


plt.title('IBM Stock')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

mpc.cursor(hover=2)

plt.tight_layout()
plt.show()
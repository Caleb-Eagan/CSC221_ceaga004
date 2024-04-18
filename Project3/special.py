# gamestop stock graph

import yfinance as yf
import matplotlib.pyplot as plt

ticker_symbol = 'GME'
start_date = '2018-01-01'
end_date = '2024-01-01'
stock_data = yf.download(ticker_symbol, start_date, end_date)

fix, ax = plt.subplots(figsize=(10,6), dpi=128)
ax.set_title("Gamestop Stock Prices", fontsize=24)
ax.set_xlabel("Time", fontsize=14)
ax.set_ylabel("Stock Price at Close", fontsize=14)

ax.plot(stock_data['Close'], color='Blue', linewidth=2, label='Close')
#ax.plot(stock_data['Open'], color='Red', linewidth=2, label='Open')

plt.legend(fontsize=12)

plt.show()
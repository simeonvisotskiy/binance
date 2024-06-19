import os
from binance.client import Client
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

client = Client(api_key, api_secret)

start_time = datetime(2024, 1, 1)

end_time = datetime.now()

start_str = start_time.strftime("%d %b %Y %H:%M:%S")
end_str = end_time.strftime("%d %b %Y %H:%M:%S")

klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, start_str, end_str)

data = pd.DataFrame(klines, columns=[
    'timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume',
    'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
])

data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')

data['close'] = data['close'].astype(float)

plt.figure(figsize=(10, 5))
plt.plot(data['timestamp'], data['close'], label='BTC/USDT Closing Price')
plt.xlabel('Time')
plt.ylabel('Price (USDT)')
plt.title('BTC/USDT Closing Prices from January 1, 2024 to Today')
plt.legend()
plt.grid(True)
plt.show()

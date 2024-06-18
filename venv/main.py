import os
from binance.client import Client

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

client = Client(api_key, api_secret)

account_info = client.get_account()

for balance in account_info['balances']:
    asset = balance['asset']
    free = balance['free']
    locked = balance['locked']
    if float(free) > 0 or float(locked) > 0:
        print(f"{asset}: Free={free}, Locked={locked}")

btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
print(f"Current BTC price: {btc_price['price']}")
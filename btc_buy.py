import ccxt
import time

exchange = ccxt.binance({
    'apiKey': 'your_api_key',
    'secret': 'your_api_secret',
})

symbol = 'BTC/USDT'
amount = 0.001 
interval = 3600

while True:
    try:
        ticker = exchange.fetch_ticker(symbol)
        price = ticker['last']
        print(f"Current price: {price}")

        order = exchange.create_market_buy_order(symbol, amount)
        print(f"Bought {amount} BTC at {price}")

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(interval)

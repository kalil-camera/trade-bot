import ccxt
import time

# Configure the exchange
exchange = ccxt.binance({
    'apiKey': 'your_api_key',
    'secret': 'your_api_secret',
})

symbol = 'BTC/USDT'
amount = 0.001  # BTC to buy
interval = 3600  # Buy every hour

while True:
    try:
        # Fetch the latest price
        ticker = exchange.fetch_ticker(symbol)
        price = ticker['last']
        print(f"Current price: {price}")

        # Place a market buy order
        order = exchange.create_market_buy_order(symbol, amount)
        print(f"Bought {amount} BTC at {price}")

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(interval)

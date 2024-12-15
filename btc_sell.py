import ccxt
import time

# Configure the exchange
exchange = ccxt.binance({
    'apiKey': 'your_api_key',
    'secret': 'your_api_secret',
})

symbol = 'BTC/USDT'
amount = 0.001  # BTC to sell
take_profit_price = 35000  # Example: sell if price hits $35,000
stop_loss_price = 20000    # Example: sell if price drops below $20,000
check_interval = 60  # Check market price every 60 seconds

while True:
    try:
        # Fetch the latest price
        ticker = exchange.fetch_ticker(symbol)
        current_price = ticker['last']
        print(f"Current price: {current_price}")

        # Check for take profit condition
        if current_price >= take_profit_price:
            print(f"Target hit! Selling {amount} BTC at {current_price}")
            order = exchange.create_market_sell_order(symbol, amount)
            print(f"Order executed: {order}")
            break

        # Check for stop loss condition
        elif current_price <= stop_loss_price:
            print(f"Stop loss triggered! Selling {amount} BTC at {current_price}")
            order = exchange.create_market_sell_order(symbol, amount)
            print(f"Order executed: {order}")
            break

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(check_interval)

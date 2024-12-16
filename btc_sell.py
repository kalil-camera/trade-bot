import ccxt
import time

exchange = ccxt.binance({
    'apiKey': 'your_api_key',
    'secret': 'your_api_secret',
})

symbol = 'BTC/BRL'
amount = 0.001  
take_profit_price = 35000 
stop_loss_price = 20000    
check_interval = 60  

while True:
    try:
        ticker = exchange.fetch_ticker(symbol)
        current_price = ticker['last']
        print(f"Current price: {current_price}")

        if current_price >= take_profit_price:
            print(f"Selling {amount} BTC at {current_price}")
            order = exchange.create_market_sell_order(symbol, amount)
            print(f"Order executed: {order}")
            break

        elif current_price <= stop_loss_price:
            print(f"Stop loss trigger: Selling {amount} BTC at {current_price}")
            order = exchange.create_market_sell_order(symbol, amount)
            print(f"Order executed: {order}")
            break

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(check_interval)

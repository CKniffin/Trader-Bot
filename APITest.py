import gdax

pc = gdax.PublicClient()
last_trades = pc.get_product_trades('ETH-USD')
ticker = pc.get_product_ticker('ETH-USD')
prods = pc.get_products()
odbook = pc.get_product_order_book('ETH-USD',level=3)
asks = odbook['asks']
bids = odbook['bids']
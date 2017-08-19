import gdax
from getAsksBids import getAsks, getBids

pc = gdax.PublicClient()
last_trades = pc.get_product_trades('ETH-USD')
ticker = pc.get_product_ticker('ETH-USD')
prods = pc.get_products()
odbook = pc.get_product_order_book('ETH-USD',level=3)
asks1 = odbook['asks']
bids1 = odbook['bids']
asks = getAsks(pc,'ETH-USD')
bids = getBids(pc,'ETH-USD')

1+1
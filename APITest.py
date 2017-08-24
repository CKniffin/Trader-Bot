import gdax
import iso8601
import datetime
from getAsksBids import getAsks, getBids
from getHistory import getHistory

pc = gdax.PublicClient()
last_trades = pc.get_product_trades('ETH-USD')
ticker = pc.get_product_ticker('ETH-USD')
prods = pc.get_products()
hist  = getHistory(pc,5,10,'ETH-USD')
asks = getAsks(pc,'ETH-USD')
bids = getBids(pc,'ETH-USD')

1+1
import gdax
from getAsksBids import getAsks, getBids
from getHistory import getHistory
from getPriceRatios import getPriceRatios

pc = gdax.PublicClient()
last_trades = pc.get_product_trades('ETH-USD')
ticker = pc.get_product_ticker('ETH-USD')
prods = pc.get_products()
hist  = getHistory(pc,5,10,'ETH-USD')
asks = getAsks(pc,'ETH-USD')
bids = getBids(pc,'ETH-USD')
price_ratios = getPriceRatios(pc)
f = open('key.txt','r')

key = f.readline()
key = key[:-1]
secret = f.readline()
pw  = raw_input('Enter GDAX password')


authclient = gdax.AuthenticatedClient(key,secret,pw,'https://api-public.sandbox.gdax.com')
sell = authclient.sell(size='1',price='50000',side='sell',product_id='BTC-USD')
buy = authclient.buy(size='1',price='50',side='buy',product_id='BTC-USD')


1+1
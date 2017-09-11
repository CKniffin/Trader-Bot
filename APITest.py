import gdax
from getAsksBids import getAsks, getBids
from getHistory import getHistory
from getPriceRatios import getPriceRatios
from getLearningData import getLearningData
import datetime

pc = gdax.PublicClient()
last_trades = pc.get_product_trades('ETH-USD')
ticker = pc.get_product_ticker('ETH-USD')
endTime = datetime.datetime.strptime('Sep 6 2017 12:15PM', '%b %d %Y %I:%M%p')
delta = 15*300
startTime = endTime - datetime.timedelta(minutes=delta)
hist = getHistory(pc,startTime,endTime,900,'ETH-USD')
asks = getAsks(pc,'ETH-USD')
bids = getBids(pc,'ETH-USD')
price_ratios = getPriceRatios(pc)
startTime = datetime.datetime.strptime('Aug 30 2017 12:15PM', '%b %d %Y %I:%M%p')
decimation = 15 * 300
getLearningData(pc,'ETH-USD',startTime,decimation)

f = open('key.txt','r')
key = f.readline()
key = key[:-1]
secret = f.readline()
pw  = raw_input('Enter GDAX password')

authclient = gdax.AuthenticatedClient(key,secret,pw,'https://api-public.sandbox.gdax.com')
sell = authclient.sell(size='1',price='50000',side='sell',product_id='BTC-USD')
buy = authclient.buy(size='1',price='50',side='buy',product_id='BTC-USD')

import numpy as np
# Returns list of current asks with volume
def getAsks(pc,prod):
    # Get order book from GDAX
    order_book = pc.get_product_order_book(prod, level=3)
    # Get asks from order book
    asks = order_book['asks']
    # Create output list
    asksOut = [[float(asks[0][0]),float(asks[0][1])]]
    # Traverse asks, group listings with same price and append to list
    for i in range(1,len(asks)):
        if float(asks[i][0]) == asksOut[-1][0]:
            asksOut[-1][1] += float(asks[i][1])
        else:
            asksOut.append([float(asks[i][0]),float(asks[i][1])])
    # Output as numpy matrix
    return np.matrix(asksOut)

# Returns list of current bids with volume
def getBids(pc,prod):
    # Get order book from GDAX
    order_book = pc.get_product_order_book(prod, level=3)
    # Get bids from order book
    bids = order_book['bids']
    # Create output list
    bidsOut = [[float(bids[0][0]),float(bids[0][1])]]
    # Travers bids, group listings with same price and append to list
    for i in range(1, len(bids)):
        if float(bids[i][0]) == bidsOut[-1][0]:
            bidsOut[-1][1] += float(bids[i][1])
        else:
            bidsOut.append([float(bids[i][0]), float(bids[i][1])])
    # Output as numpy matrix
    return np.matrix(bidsOut)
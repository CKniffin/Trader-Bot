def getAsks(pc,prod):
    order_book = pc.get_product_order_book(prod, level=3)
    asks = order_book['asks']
    asksOut = [[float(asks[0][0]),float(asks[0][1])]]
    for i in range(1,len(asks)):
        if float(asks[i][0]) == asksOut[-1][0]:
            asksOut[-1][1] += float(asks[i][1])
        else:
            asksOut.append([float(asks[i][0]),float(asks[i][1])])
    return asksOut

def getBids(pc,prod):
    order_book = pc.get_product_order_book(prod, level=3)
    bids = order_book['bids']
    bidsOut = [[float(bids[0][0]),float(bids[0][1])]]
    for i in range(1, len(bids)):
        if float(bids[i][0]) == bidsOut[-1][0]:
            bidsOut[-1][1] += float(bids[i][1])
        else:
            bidsOut.append([float(bids[i][0]), float(bids[i][1])])
    return bidsOut
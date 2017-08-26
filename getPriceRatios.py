def getPriceRatios(pc):
    prods = pc.get_products()
    # Create list for results
    priceRatioToBTC = []
    # Get BTC-USD and BTC-EUR price as comparison base
    priceBTCtoUSD = pc.get_product_trades('BTC-USD')
    priceBTCtoUSD = float(priceBTCtoUSD[-1]['price'])
    priceBTCtoEUR = pc.get_product_trades('BTC-EUR')
    priceBTCtoEUR = float(priceBTCtoEUR[-1]['price'])
    for i in range(len(prods)):
        if prods[i]['base_currency'] != 'BTC':
            if prods[i]['quote_currency'] != 'BTC':
                if prods[i]['quote_currency'] == 'USD':
                    priceInBase= pc.get_product_trades(prods[i]['id'])
                    priceInBTC = pc.get_product_trades(prods[i]['base_currency']+'-'+'BTC')
                    priceUSD   = float(priceInBTC[-1]['price'])*priceBTCtoUSD*1/float(priceInBase[-1]['price'])
                    priceRatioToBTC.append([prods[i]['id'], priceUSD])
                else:
                    priceInBase= pc.get_product_trades(prods[i]['id'])
                    priceInBTC = pc.get_product_trades(prods[i]['base_currency']+'-'+'BTC')
                    priceEUR   = float(priceInBTC[-1]['price'])*priceBTCtoEUR*1/float(priceInBase[-1]['price'])
                    priceRatioToBTC.append([prods[i]['id'], priceEUR])
    return priceRatioToBTC
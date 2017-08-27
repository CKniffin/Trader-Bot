# Returns ratio of ETH/LTC-USD/EUR to BTC-USD/EUR prices
def getPriceRatios(pc):
    prods = pc.get_products()
    # Create empty list for results
    priceRatioToBTC = []
    # Get BTC-USD and BTC-EUR price as comparison base
    priceBTCtoUSD = pc.get_product_ticker('BTC-USD')
    priceBTCtoUSD = float(priceBTCtoUSD['price'])
    priceBTCtoEUR = pc.get_product_ticker('BTC-EUR')
    priceBTCtoEUR = float(priceBTCtoEUR['price'])
    # Compute price ratios
    for i in range(len(prods)):
        if prods[i]['base_currency'] != 'BTC' and prods[i]['quote_currency'] != 'BTC':
            if prods[i]['quote_currency'] == 'USD':
                priceInBase= pc.get_product_ticker(prods[i]['id'])
                priceInBTC = pc.get_product_ticker(prods[i]['base_currency']+'-'+'BTC')
                priceUSD   = float(priceInBTC['price'])*priceBTCtoUSD*1/float(priceInBase['price'])
                priceRatioToBTC.append([prods[i]['id'], priceUSD])
            else:
                priceInBase= pc.get_product_ticker(prods[i]['id'])
                priceInBTC = pc.get_product_ticker(prods[i]['base_currency']+'-'+'BTC')
                priceEUR   = float(priceInBTC['price'])*priceBTCtoEUR*1/float(priceInBase['price'])
                priceRatioToBTC.append([prods[i]['id'], priceEUR])
    return priceRatioToBTC
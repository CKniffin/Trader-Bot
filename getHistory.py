import datetime
def getHistory(pc,delta,gran,prod):
    endTime = datetime.datetime.utcnow()
    startTime = endTime - datetime.timedelta(minutes=delta)
    hist = pc.get_product_historic_rates(prod, start=startTime, end=endTime, granularity=gran)
    startTime = hist[-1][0]
    dt = []
    close = []
    vol = []
    for i in range(len(hist)):
        dt.append(hist[i][0]-startTime)
        close.append(hist[i][4])
        vol.append(hist[i][5])
    dt.reverse()
    close.reverse()
    vol.reverse()
    return [dt,close,vol]
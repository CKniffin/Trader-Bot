import datetime
import numpy as np
# Returns historic prices and volumes for a given time and granularity
def getHistory(pc,startTime,endTime,gran,prod):
    # Current time
    # endTime = datetime.datetime.utcnow()
    # Interval start time
    # startTime = endTime - datetime.timedelta(minutes=delta)
    # Get data from GDAX
    hist = pc.get_product_historic_rates(prod, start=startTime, end=endTime, granularity=gran)
    # Time stamp of first value in list
    #startTime = hist[-1][0]
    # Create output lists
    dt = []
    open = []
    close = []
    low = []
    high = []
    vol = []
    # Traverse history data and append to lists
    for i in range(len(hist)):
        dt.append(datetime.datetime.fromtimestamp(hist[i][0]).strftime('%Y-%m-%d %H:%M:%S'))
        low.append(hist[i][1])
        high.append(hist[i][2])
        open.append(hist[i][3])
        close.append(hist[i][4])
        vol.append(hist[i][5])
    # Reverse lists for a more intuitive output
    dt.reverse()
    low.reverse()
    high.reverse()
    open.reverse()
    close.reverse()
    vol.reverse()
    # Output as numpy array
    return {'dt':dt, 'low':low, 'high':high, 'open':open, 'close':close, 'vol':vol}
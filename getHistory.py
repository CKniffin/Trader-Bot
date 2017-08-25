import datetime
import numpy as np
# Returns historic close prices and volumes for a given time and granularity
def getHistory(pc,delta,gran,prod):
    # Current time
    endTime = datetime.datetime.utcnow()
    # Interval start time
    startTime = endTime - datetime.timedelta(minutes=delta)
    # Get data from GDAX
    hist = pc.get_product_historic_rates(prod, start=startTime, end=endTime, granularity=gran)
    # Time stamp of first value in list
    startTime = hist[-1][0]
    # Create output lists
    dt = []
    close = []
    vol = []
    # Traverse history data and append to lists
    for i in range(len(hist)):
        dt.append(hist[i][0]-startTime)
        close.append(hist[i][4])
        vol.append(hist[i][5])
    # Reverse lists for a more intuitive output
    dt.reverse()
    close.reverse()
    vol.reverse()
    # Output as numpy array
    return np.matrix([dt,close,vol])
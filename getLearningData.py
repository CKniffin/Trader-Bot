from getHistory import getHistory
import datetime
import time
import numpy as np
import os

def getLearningData(pc,tradePair,startTime,decimation):
    dir_path = 'F:/Trader-Bot/'
    endTime = startTime + datetime.timedelta(minutes=decimation)
    dt = []
    low = []
    high = []
    open = []
    close = []
    vol = []

    while (endTime-datetime.datetime(1970,1,1)).total_seconds() < time.time():
        hist = getHistory(pc,startTime,endTime,900,tradePair)
        dt.extend(hist['dt'])
        low.extend(hist['low'])
        high.extend(hist['high'])
        open.extend(hist['open'])
        close.extend(hist['close'])
        vol.extend(hist['vol'])
        startTime = endTime #+ datetime.timedelta(minutes=15)
        endTime = startTime + datetime.timedelta(minutes=decimation)
        print endTime

    data = np.matrix([low,high,open,close,vol])
    data = np.transpose(data)
    saveStr = dir_path + tradePair + '_Data.npy'
    np.save(saveStr,data)
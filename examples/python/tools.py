import numpy as np

def getMovingAverage(timeseries, window):
    # cumsum = np.cumsum(np.insert(timeseries[-window:], 0, 0)) 
    # return (cumsum[-window:] - cumsum[0]) / float(window)
    return np.average(timeseries[-window::1])


def getMovingMean(timeseries, window):
    return np.mean(timeseries[-window::1])
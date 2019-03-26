import matplotlib.pylab as pylab
import pandas_datareader
import pandas as pd
import datetime
import numpy as np



def Datapull(Stock):
    try:
        df = (pandas_datareader.DataReader(Stock,'yahoo',start='01/01/2010'))
        print('Retrieved', Stock)
        time.sleep(5)
        return df
    except e:
        print ('Main Loop', str(e))
print(df)

def RSIfun(price, n=14):
    delta = price['Close'].diff()
    #-----------
    # dUp=delta[delta>0]
    # dDown=delta[delta<0]
    #
    # RolUp=RolUp.reindex_like(delta, method="ffill")
    # RolDown=RolDown.reindex_like(delta, method="ffill")
    dUp, dDown =delta.copy(),delta.copy()
    dUp[dUp<0]=0
    dDown[dDown > 0] = 0
    RolUp=pd.rolling_mean(dUp,n)
    RolDown=pd.rolling_mean(dDown,n).abs
    RS = RolUp / RolDown
    rsi= 100.0 - (100.0 / (1.0 + RS))
    return rsi

Stock='AAPL'
df=Datapull(Stock)
RSIfun(df)
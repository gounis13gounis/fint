import sim
symbol = 'BOM500003'
import numpy as np
In [2]:
df, param = sim.technical.bollinger.Bollinger(symbol=symbol).simulation(startDate='20171201', endDate='20190215')
%matplotlib notebook
sim.plotter.Plotter(data=df,symbol=symbol, param=param).plot()
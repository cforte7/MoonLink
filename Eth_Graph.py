import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick2_ohlc
import matplotlib.dates as mdates
from datetime import datetime



with open('ETH_Data.json') as EthJson:
	d = ''
	for x in EthJson:
		d = x
	EthJson.close()
	PriceFrame = pd.read_json(str(d))
cols = ['close','date','high','low','open','quoteVolume','volume', 'weightedAverage']

#Remove multiple entries for one date. Only data with Hour '00' included
for index,row in PriceFrame.iterrows():
	if str(row['date'].time())[0:2] != '00':
		PriceFrame.drop(index, inplace=True)

PriceFrame.index = pd.to_datetime(PriceFrame.date)
PriceFrame = PriceFrame.drop('date',1)


ax_list = plt.subplot2grid((6,1),(1,0), rowspan = 10)

TimeSpan = 30*3

Candle_Graph = candlestick2_ohlc(ax =ax_list, opens=PriceFrame.open[len(PriceFrame)-TimeSpan:len(PriceFrame)],
											  closes=PriceFrame.close[len(PriceFrame)-TimeSpan:len(PriceFrame)],
											  highs=PriceFrame.high[len(PriceFrame)-TimeSpan:len(PriceFrame)],
											  lows=PriceFrame.low[len(PriceFrame)-TimeSpan:len(PriceFrame)],
											  width = 1,
											  alpha = .75)
for x in Candle_Graph:
	print(x)
plt.show()
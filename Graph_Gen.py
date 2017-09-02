import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.figure import Figure
from matplotlib.finance import candlestick2_ohlc
import matplotlib.dates as mdates
from datetime import datetime

def DataUpdate():
		DataURL = 'https://poloniex.com/public?command=returnChartData&currencyPair=USDT_ETH&start=1435699200&end=9999999999&period=14400'
		DataText = requests.get(DataURL).text
		PriceFrame1 = pd.read_json(DataText)	
		return(PriceFrame1)

def DateFrameEdit(Span):
	dates = list(PriceFrame.date.values)
	for x in dates:
		x = datetime.strptime(str(x)[0:19],'%Y-%m-%dT%H:%M:%S')
	return(dates[len(PriceFrame)-Span:len(PriceFrame)])
	
def DateFormat(x,pos):
	try:
		return(pd.to_datetime(dates[int(x)]))
	except IndexError:
		return('')



def plot(TimeSpan):	
	global dates
	dates = DateFrameEdit(TimeSpan)
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1),(0,0))
	ax1.grid(True)
	Candle_Graph = candlestick2_ohlc(ax1,
									opens=PriceFrame.open[len(PriceFrame)-TimeSpan:len(PriceFrame)],
									closes=PriceFrame.close[len(PriceFrame)-TimeSpan:len(PriceFrame)],
									highs=PriceFrame.high[len(PriceFrame)-TimeSpan:len(PriceFrame)],
									lows=PriceFrame.low[len(PriceFrame)-TimeSpan:len(PriceFrame)],
									width = .5,
									alpha = .75)
	ax1.xaxis.set_major_formatter(mticker.FuncFormatter(DateFormat))
	
	fig.autofmt_xdate()
	fig.tight_layout()
	plt.xlabel('Date')
	plt.ylabel('USDT/ETH') 
	return(fig)


	


def Gen(TimeFrame):
	global PriceFrame
	PriceFrame = DataUpdate()
	return(plot(TimeFrame))


import sys
import requests
import webbrowser
import datetime
import pandas as pd
import pickle as pk
import plotly.plotly as py 
import plotly.graph_objs as go
import json
from matplotlib.finance import candlestick2_ohlc
from pathlib import Path
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QSizePolicy
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.finance import candlestick2_ohlc
import matplotlib.dates as mdates




#Main Window Class
class Example(QWidget):

	def __init__(self,parent=None):
		super().__init__() #returns the parent object of the Example Class (Qwidget)
		self.initUI()
		
	def link_click(self):
		webbrowser.open("https://coinbase.com")

	def initUI(self):      #Actual creation of the window
		self.setGeometry(500,500,600,600) #(xpos,ypos,xlen,ylen)
		self.setWindowTitle('MoonLink')  #Title Bar Text
		self.setWindowIcon(QIcon('Graphics/MoonIcon.png'))  #Picture used for the icon (ETH image in local folder)
		
		m = Graph_Canvas(self, width=5,height=4)

		QuitButton = QPushButton('Quit',self)
		QuitButton.setToolTip('Close MoonLink')
		QuitButton.resize(QuitButton.sizeHint())
		QuitButton.move(320,575)
		QuitButton.clicked.connect(QCoreApplication.instance().quit) #Command used when button is clicked, the signal from a mouse click is the 'clicked' 

		LinkButton = QPushButton('Coinbase Link',self)
		LinkButton.setToolTip('Link to Coinbase')
		LinkButton.move(450,575)
		LinkButton.clicked.connect(self.link_click)
			

#DataURL = 'https://poloniex.com/public?command=returnChartData&currencyPair=USDT_ETH&start=1435699200&end=9999999999&period=14400'
#DataText = requests.get(DataURL).text

#Offline Data test module
with open('ETH_Data.json') as EthJson:
	d = ''
	for x in EthJson:
		d = x
	EthJson.close()
	PriceFrame = pd.read_json(str(d))

#Data Functions
'''
def DataUpdate():
	DataURL = 'https://poloniex.com/public?command=returnChartData&currencyPair=USDT_ETH&start=1435699200&end=9999999999&period=14400'
	DataText = requests.get(DataURL).text
	PriceFrame = pd.read_json(DataText)
	#Columns: ['close','date','high','low','open','quoteVolume','volume', 'weightedAverage']
	'''
TimeSpan = 30





class Graph_Canvas(FigureCanvas):
	def __init__(self, parent=None, width=5, height=4, dpi=100):
		fig = Figure(figsize=(width,height),dpi=dpi)
		self.axes = fig.add_subplot(111)#subplot2grid((6,1),(1,0), rowspan = 10)
		FigureCanvas.__init__(self,fig)
		FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)
		self.setParent(parent)
		self.plot()

	def plot(self):
		for index,row in PriceFrame.iterrows():
			if str(row['date'].time())[0:2] != '00':
				PriceFrame.drop(index, inplace=True)
		Candle_Graph = candlestick2_ohlc(ax =self.axes, opens=PriceFrame.open[len(PriceFrame)-TimeSpan:len(PriceFrame)],
												      closes=PriceFrame.close[len(PriceFrame)-TimeSpan:len(PriceFrame)],
										              highs=PriceFrame.high[len(PriceFrame)-TimeSpan:len(PriceFrame)],
										              lows=PriceFrame.low[len(PriceFrame)-TimeSpan:len(PriceFrame)],
										              width = .5,
										              alpha = .75,colorup='#77d879', colordown='#db3f3f')
		
	







if __name__ == '__main__':
	#DataUpdate()

	app = QApplication(sys.argv)
	ex = Example()
	ex.show()
	sys.exit(app.exec_())


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
from PyQt5.QtGui import QIcon, QPainter, QColor, QFont
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.finance import candlestick2_ohlc
import matplotlib.dates as mdates
from Graph_Gen import Gen

#chart = Gen(60)


#Main Window Class
class Example(QWidget):

	def __init__(self,parent=None):
		super().__init__() #returns the parent object of the Example Class (Qwidget)
		self.initUI()
		
	
	def graphEvent(self,event):
		qp = QPainter()
		qp.begin(self)
		self.Gen(60)
		qp.end()

		
	def link_click(self):
		webbrowser.open("https://coinbase.com")

	def initUI(self):      #Actual creation of the window
		self.setGeometry(500,500,770,500) #(xpos,ypos,xlen,ylen)
		self.setWindowTitle('MoonLink')  #Title Bar Text
		self.setWindowIcon(QIcon('Graphics/MoonIcon.png'))  #Picture used for the icon (ETH image in local folder)
		

		QuitButton = QPushButton('Quit',self)
		QuitButton.setToolTip('Close MoonLink')
		QuitButton.resize(QuitButton.sizeHint())
		QuitButton.move(320,575)
		QuitButton.clicked.connect(QCoreApplication.instance().quit) #Command used when button is clicked, the signal from a mouse click is the 'clicked' 

		LinkButton = QPushButton('Coinbase Link',self)
		LinkButton.setToolTip('Link to Coinbase')
		LinkButton.move(650,430)
		LinkButton.clicked.connect(self.link_click)
		m = PlotCanvas(self,width=5,height=4)

class PlotCanvas(FigureCanvas):
	def __init__(self, parent=None, width=5,height=4,dpi = 100):
		fig = Gen(365)
		

		FigureCanvas.__init__(self, fig)
		self.setParent(parent)

		FigureCanvas.setSizePolicy(self,
        	QSizePolicy.Expanding,
        	QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)
		
	def DateFormat(x,pos):
		try:
			return(pd.to_datetime(dates[int(x)]))
		except IndexError:
			return('')
	

	




if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	ex.show()
	sys.exit(app.exec_())


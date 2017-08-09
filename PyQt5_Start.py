import sys
import requests
import webbrowser
import datetime
import pandas as pd
import pickle as pk
from pathlib import Path
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon




#Main Window Class
class Example(QWidget):

	def __init__(self):
		super().__init__() #returns the parent object of the Example Class (Qwidget)
		self.initUI()
	def link_click(self):
		webbrowser.open("https://coinbase.com")

	def initUI(self):      #Actual creation of the window
		self.setGeometry(300,300,400,200) #(xpos,ypos,xlen,ylen)
		self.setWindowTitle('MoonLink')  #Title Bar Text
		self.setWindowIcon(QIcon('ETH.png'))  #Picture used for the icon (ETH image in local folder)
		

		QuitButton = QPushButton('Quit',self)
		QuitButton.setToolTip('Close MoonLink')
		QuitButton.resize(QuitButton.sizeHint())
		QuitButton.move(320,175)
		QuitButton.clicked.connect(QCoreApplication.instance().quit) #Command used when button is clicked, the signal from a mouse click is the 'clicked' 

		LinkButton = QPushButton('Coinbase Link',self)
		LinkButton.setToolTip('Link to Coinbase')
		LinkButton.move(230,175)
		LinkButton.clicked.connect(self.link_click)

		UpdateButton = QPushButton('Update Data',self)
		UpdateButton.move(130,175)
		UpdateButton.clicked.connect(DataUpdate)
		self.show()


#Data Functions
def DataUpdate():
	DataURL = 'https://poloniex.com/public?command=returnChartData&currencyPair=USDT_ETH&start=1435699200&end=9999999999&period=14400'
	DataText = requests.get(DataURL).text
	PriceFrame = pd.read_json(DataText)
	PricePickle = PriceFrame.to_pickle('EthData.pkl')
	





if __name__ == '__main__':
	DataUpdate()
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())


import webbrowser
from tkinter import *
from bs4 import BeautifulSoup
import json
import requests
import time
import threading
from PIL import ImageTk, Image

class App(Frame):
	def __init__(self,parent):
		Frame.__init__(self,parent,background="#195da3")
		self.parent = parent
		self.initUI()

	def EthLink(self):
		webbrowser.open("https://coinmarketcap.com/currencies/ethereum/")

	def initUI(self):
		self.parent.title("MoonLink")
		self.pack(fill=BOTH,expand=1)
		quitButton = Button(self, text="Quit", fg = 'red', command=self.quit, font = 'Calibri')
		quitButton.place(x=10,y=100)
		EthLink = Button(self, text = "ETH Price Chart", command = self.EthLink, font = 'Calibri')
		EthLink.place(x=60,y=100)
		global sv
		sv = StringVar(self)
		l = Label(self,textvar = sv, fg = 'green', font = 'Calibri', )
		l.place(x=35,y=50)
		l_Title = Label(self, text = 'Current ETH Price', font = "Calibri")
		l_Title.place(x=15,y=30)
		im = Image.open("ETH.png").resize((50,50))
		Im = ImageTk.PhotoImage(im)
		



	def GetPrice(self):
		RetTicker = requests.get('https://poloniex.com/public?command=returnTicker').text
		RetTicker = json.loads(RetTicker)
		price = "$"+str(RetTicker['USDT_ETH']['last'][:6])
		sv.set(price)
		root.after(5000,self.GetPrice)








def main():
	global root
	root = Tk()
	root.geometry('250x300')
	app = App(root)
	root.after(20,app.GetPrice)
	root.mainloop()
#comment
	

	




if __name__ == '__main__':
	main()
	
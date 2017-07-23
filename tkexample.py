'''from tkinter import *
import requests
import json

root = Tk()
sv = StringVar()
l = Label(textvar=sv)
l.pack()
def GetPrice():
	RetTicker = requests.get('https://poloniex.com/public?command=returnTicker').text
	RetTicker = json.loads(RetTicker)
	price = str(RetTicker['USDT_ETH']['last'])
	print("Data Grabbed")
	sv.set(price)
	root.after(5000,GetPrice)

root.after(20,GetPrice)
root.mainloop()'''

from tkinter import *
import random
import time

tk = Tk()
tk.title = "Game"
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
    def draw(self):
        self.canvas.move(self.id, 0, -1)

ball = Ball(canvas, "red")

tk.mainloop()

while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
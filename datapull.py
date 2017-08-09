import requests 
import json
import pandas as pd
def DataUpdate():
	DataURL = 'https://poloniex.com/public?command=returnChartData&currencyPair=USDT_ETH&start=1435699200&end=9999999999&period=14400'
	PriceData = requests.get(DataURL).text
	PriceFrame = pd.read_json(PriceData)
	print(PriceFrame)
DataUpdate()

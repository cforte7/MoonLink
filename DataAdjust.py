import pandas as pd

new = ''
with open('Eth_Data.json') as f:
	for x in f:
		new = x

df = pd.read_json(new)

import os
import pandas as pd

from time import sleep
from lib.path import PATH

_FILE_NAME = 'transaksi.csv'

def total_price(jml_item : int, harga : int):
	"""
	Total belanja

	Parameters
	----------
	jml_item : int
		Jumlah item yang dibeli
	harga : int
		Harga per item yang dibeli
	
	Returns
	-------
	int
		Total harga per item
	"""
	return jml_item * harga

def total_order(total_price : int):
	"""
	Total belanja keseluruhan

	Parameters
	----------
	total_price : pandas dataframe
		Total harga dari semua item yang dibeli

	Returns
	-------
	int
		Total belanja keseluruhan
	"""
	# Calculate the discount
	if total_price > 200000:
		discount = '5%'
		discount_price = round(total_price * 0.05, 0)
		total_price = round(total_price - discount_price, 0)
		return( total_price, discount_price, discount)
	elif total_price > 300000:
		discount = '8%'
		discount_price = round(total_price * 0.08, 0)
		total_price = round(total_price - discount_price, 0)
		return (total_price, discount_price, discount)
	elif total_price > 500000:
		discount = '10%'
		discount_price = round(total_price * 0.1, 0)
		total_price = round(total_price - discount_price, 0)
		return (total_price, discount_prince, discount)

def clear_screen():
	sleep(2)
	os.system('cls' if os.name == 'nt' else 'clear')

def create_csv_file():
	"""
	Create a csv file
	"""
	try:
		data = pd.DataFrame(columns=['Item', 'Jumlah Item', 'Harga/item', 'Harga Total'])
		data.to_csv(os.path.join(PATH, _FILE_NAME), index=False)
	except FileExistsError:	# Create an exception if the file already exists
		print('File already exists')
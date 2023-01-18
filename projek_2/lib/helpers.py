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

def count_total_order(total_price : int):
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
	discount_price = 0
	discount = 0
	if total_price > 200000:
		discount_price, discount = count_discount(total_price, '5%')
		total_price = round(total_price - discount_price, 0)
	elif total_price > 300000:
		discount_price, discount = count_discount(total_price, '8%')
		total_price = round(total_price - discount_price, 0)
	elif total_price > 500000:
		discount_price, discount = count_discount(total_price, '10%')
		total_price = round(total_price - discount_price, 0)

	return total_price, discount_price, discount

def count_discount(total_price : int, dsc : str):
	"""
	Discount

	Parameters
	----------
	dsc : string
		Discount price format string number + string % (ex: 5%)

	Returns
	-------
	int
		Discount price
	"""
	discount = int(dsc.split('%')[0])
	discount_price = round(total_price * (discount / 100), 0)
	return discount_price, discount

def clear_screen(slp=2):
	"""
	Clear the screen
	"""
	sleep(slp)
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
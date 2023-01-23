import os
import pandas as pd

from time import sleep
from lib.path import PATH

_FILE_NAME = 'transaksi.csv'

def total_price(jml_item : int, harga : int):
	"""
	Function to calculate the total price of the item. This function
	has two parameters, `jml_item` and `harga`. The `jml_item` is the
	quantity of the item and `harga` is the price of the item.

	Parameters
	----------
	jml_item : int
		Number of item that will be bought
	harga : int
		Price of the item
	
	Returns
	-------
	int
		jml_item * harga
	"""
	return jml_item * harga

def count_total_order(total_price : int):
	"""
	Function to calculate the total price of the order. This function
	has one parameter, `total_price` which is the total price of all
	the items that will be bought. This function also has a discount
	calculation.
	- 5% discount for total price above Rp. 200.000, -
	- 8% discount for total price above Rp. 300.000, -
	- 10% discount for total price above Rp. 500.000, -

	Parameters
	----------
	total_price : int
		Total price of all the items that will be bought.
	Returns
	-------
	int
		total_price
	int
		discount_price
	int
		discount
	"""
	# Calculate the discount
	discount_price = 0
	discount = 0
	try:
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
	except TypeError:
		print('Error: Cannot calculate total order, because you do not have any item in your order.')
	

def count_discount(total_price : int, dsc : str):
	"""
	Function to calculate the discount. This function has two parameters,
	`total_price` and `dsc`. The `total_price` is the total price of all
	the items that will be bought and `dsc` is the discount price format
	string number + string % (ex: 5%).
	The discount price format string number + string % (ex: 5%), then the
	number is split between the number and the symbol `%`. Then the number
	is converted to an integer and the discount is calculated.

	Parameters
	----------
	dsc : string
		Discount price format string number + string % (ex: 5%)

	Returns
	-------
	int
		discount_price
	int
		discount
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
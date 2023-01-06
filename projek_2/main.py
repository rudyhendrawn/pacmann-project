import os
import pandas as pd

from lib import helpers
from lib.transaction import Transaction


if '__main__' == __name__:
	# Create a csv file
	helpers.create_csv_file()

	# Read the data from the csv file
	transaction = Transaction()

	# Create a loop to add items to the data
	while True:
		# Get user input
		item = input('Nama Item: ')
		jml_item = int(input('Jumlah Item: '))
		harga = int(input('Harga/item: '))
		harga_total = helpers.total_price(jml_item, harga)

		# Create a dictionary to store the data
		data = {
			'Item': item,
			'Jumlah Item': jml_item,
			'Harga/item': harga,
			'Harga Total': harga_total
		}

		# Add the data to the csv file
		transaction.add_item(data)

		# Ask the user if they want to add more items
		choice = input('Add more items? (y/n): ')
		if 'n' == choice:
			break
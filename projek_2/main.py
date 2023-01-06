import os
# import locale
import pandas as pd

from lib import helpers
from lib.transaction import Transaction

# locale = locale.setlocale(locale.LC_ALL, 'id_ID')

if '__main__' == __name__:
	# Create a csv file
	helpers.create_csv_file()

	# Read the data from the csv file
	transaction = Transaction()

	# Create a dictionary to store the data before it is added to dataframe
	data = {
		'Item': [],
		'Jumlah Item': [],
		'Harga/item': [],
		'Harga Total': []
	}
	# Create a loop to add items to the data
	while True:
		# Get user input
		item = input('Nama Item: ')
		jml_item = int(input('Jumlah Item: '))
		harga = int(input('Harga/item: '))
		harga_total = helpers.total_price(jml_item, harga)

		data['Item'].append(item)
		data['Jumlah Item'].append(jml_item)
		data['Harga/item'].append(harga)
		data['Harga Total'].append(harga_total)

		# Ask the user if they want to add more items
		choice = input('\nAdd more items? (y/n): ')
		if 'n' == choice:
			break

	transaction.add_item(data)

	# Print the data
	print('\n')
	print(transaction.data)

	# Ask the user if they want print the total order
	choice = input('\nPrint total order? (y/n): ')
	if 'y' == choice:
		(total_order, discount_price, discount) = helpers.total_order(transaction.data['Harga Total'].sum())
		print("\nTotal: Rp.{:,}".format(transaction.data['Harga Total'].sum()))
		print("Discount: Rp.{}".format(discount))
		print("Discount Price: Rp.{:,}".format(discount_price))
		print("Total Order: Rp.{:,}".format(total_order))
		# print("Test currency: {}".format(locale.currency(total_order, grouping=True)))

	# Ask the user if they want to store the data to csv
	# choice = input('\nStore the data to csv? (y/n): ')
	# if 'y' == choice:
	# 	transaction.store_data()
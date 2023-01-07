import os
import pandas as pd

from time import sleep
from lib import helpers
from lib.transaction import Transaction

# locale = locale.setlocale(locale.LC_ALL, 'id_ID')
def input_order():
	data = {
		'Item': None,
		'Jumlah Item': None,
		'Harga/item': None,
		'Harga Total': None,
	}
	# Get user input
	data['Item'] = input("Nama Item: ")
	data['Jumlah Item'] = int(input("Jumlah Item: "))
	data['Harga/item'] = int(input("Harga/item: "))
	data['Harga Total'] = helpers.total_price(data['Jumlah Item'], data['Harga/item'])
	return data

def add_more_items(data):
	pass

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
		# Create menu
		print('Program Menu\n')
		print('1. Add item')
		print('2. Check item')
		print('3. Exit')
		# Ask the user if they are first time order
		choice = input("\nFirst time order? (y/n): ")
		if 'y' == choice:
			while True:
				# Get user input
				user_data = input_order()
				data['Item'].append(user_data['Item'])
				data['Jumlah Item'].append(user_data['Jumlah Item'])
				data['Harga/item'].append(user_data['Harga/item'])
				data['Harga Total'].append(user_data['Harga Total'])

				# Ask the user if they want to add more items
				choice = input("\nAdd more items? (y/n): ")
				if 'n' == choice:
					break
		else:
			if data is not None:
				print("You don't have item in your order. Please add some items first\n")
				user_data = input_order()
				data['Item'].append(user_data['Item'])
				data['Jumlah Item'].append(user_data['Jumlah Item'])
				data['Harga/item'].append(user_data['Harga/item'])
				data['Harga Total'].append(user_data['Harga Total'])
			else:
				print("You already have some orders\n")
				choice = input("Do you to check your previous orders? (y/n): ")
				if 'y' == choice:
					print(transaction.data)
				else:
					break
		transaction.add_item(data)
		print(transaction.data)
		sleep(2)
		os.system('cls')

				

		# while True:
		# 	# Ask the user if they want to check the data
		# 	choice = input('\nCheck the data? (y/n): ')
		# 	if 'y' == choice:
		# 		print(transaction.data)
		# 	else:
		# 		break

	# Print the data
	print('\n')
	

	# Ask the user if they want print the total order
	# choice = input('\nPrint total order? (y/n): ')
	# if 'y' == choice:
	# 	(total_order, discount_price, discount) = helpers.total_order(transaction.data['Harga Total'].sum())
	# 	print("\nTotal: Rp.{:,}".format(transaction.data['Harga Total'].sum()))
	# 	print("Discount: {}".format(discount))
	# 	print("Discount Price: Rp.{:,}".format(discount_price))
	# 	print("Total Order: Rp.{:,}".format(total_order))
		# print("Test currency: {}".format(locale.currency(total_order, grouping=True)))

	# Ask the user if they want to store the data to csv
	# choice = input('\nStore the data to csv? (y/n): ')
	# if 'y' == choice:
	# 	transaction.store_data()
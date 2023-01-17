import os
import pandas as pd

from lib import helpers
from lib.transaction import Transaction


def input_order():
	"""
	Get user input
	"""
	data = {
		'Item': None,
		'Jumlah Item': None,
		'Harga/item': None,
		'Harga Total': None,
	}
	# Get user input
	print("\n")
	data['Item'] = input("Nama Item: ")
	data['Jumlah Item'] = int(input("Jumlah Item: "))
	data['Harga/item'] = int(input("Harga/item: "))
	data['Harga Total'] = helpers.total_price(data['Jumlah Item'], data['Harga/item'])
	return data

def check_order(data : Transaction):
	"""
	Check the order
	"""
	data_viewer = data.view_data()
	if data_viewer == True:
		print("Your order is:")
		print(data_viewer)
		return True
	else:
		return False

def edit_order(data : Transaction):
	"""
	Edit the order
	"""
	choise = int(input("Choose order's number that you want to edit: "))
	print("Choose what you want to edit:")
	print("1. Item")
	print("2. Jumlah Item")
	print("3. Harga/item")
	edit_item = int(input("Choose menu (1/2/3): "))
	if edit_item == 1:
		item_name = input("Item name: ")
		data.update_item_name(choise, item_name)
	elif edit_item == 2:
		qty = int(input("Jumlah Item: "))
		data.update_item_qty(choise, qty)
	elif edit_item == 3:
		price = int(input("Harga/item: "))
		data.update_item_price(choise, price)

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
		print("Program Menu:")
		print("1. Add Item")
		print("2. Check Item")
		print("3. Edit Item")
		print("4. Reset Transaction")
		print("5. Save Transaction")
		print("6. Exit")
		choice = input("Choose menu (1/2/3/4/5/6): ")
		if '1' == choice:
			# Get user input
			while True:
				user_data = input_order()
				data['Item'].append(user_data['Item'])
				data['Jumlah Item'].append(user_data['Jumlah Item'])
				data['Harga/item'].append(user_data['Harga/item'])
				data['Harga Total'].append(user_data['Harga Total'])
				add_more_item = input("Add more items? (y/n): ")
				if 'n' == add_more_item:
					break
			transaction.add_item(data)
			helpers.clear_screen()
		elif '2' == choice:
			order = check_order(transaction)
			if order == True:
				choise = input("Do you want to edit this order? (y/n)")
				if 'y' == choise:
					edit_order(transaction)
				helpers.clear_screen()
			elif order == False:
				helpers.clear_screen()
		elif '3' == choice:
			pass
		elif '6' == choice:
			print("Thank you for ordering. See you next time\n")
			break
		else:
			print("Invalid input. Please try again\n")
			helpers.clear_screen()

		# Ask the user if they are first time order
		# choice = input("\nFirst time order? (y/n): ")
		# if 'y' == choice:
		# 	while True:
		# 		# Get user input
		# 		user_data = input_order()
		# 		data['Item'].append(user_data['Item'])
		# 		data['Jumlah Item'].append(user_data['Jumlah Item'])
		# 		data['Harga/item'].append(user_data['Harga/item'])
		# 		data['Harga Total'].append(user_data['Harga Total'])

		# 		# Ask the user if they want to add more items
		# 		choice = input("\nAdd more items? (y/n): ")
		# 		if 'n' == choice:
		# 			break
		# else:
		# 	if data is not None:
		# 		print("You don't have item in your order. Please add some items first\n")
		# 		user_data = input_order()
		# 		data['Item'].append(user_data['Item'])
		# 		data['Jumlah Item'].append(user_data['Jumlah Item'])
		# 		data['Harga/item'].append(user_data['Harga/item'])
		# 		data['Harga Total'].append(user_data['Harga Total'])
		# 	else:
		# 		print("You already have some orders\n")
		# 		choice = input("Do you to check your previous orders? (y/n): ")
		# 		if 'y' == choice:
		# 			print(transaction.data)
		# 		else:
		# 			break
		# transaction.add_item(data)
		# print(transaction.data)
		# sleep(2)
		# os.system('cls')

				

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
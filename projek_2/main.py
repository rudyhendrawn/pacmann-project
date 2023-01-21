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
	data_viewer = data.is_empty()
	if data_viewer == True:
		print("Your order is:")
		print(data_viewer)
		return True
	else:
		return False

def edit_order(data : Transaction):
	"""
	Edit the order mechanism in the main program. 
	User can choose what they want to edit, 
	whether it is the item name, quantity, or price.

	Parameters
	----------
	data : Transaction
	"""
	print("Choose what you want to edit:")
	print("1. Item")
	print("2. Number of Item")
	print("3. Price per item")
	edit_item = int(input("Type menu (1/2/3): "))
	if edit_item == 1:
		index = input("Type the order's number: ")
		item_name = input("Item name: ")
		data.update_item_name(index, item_name)
	elif edit_item == 2:
		index = input("Type the order's number: ")
		qty = int(input("Number of Item: "))
		data.update_item_qty(index, qty)
	elif edit_item == 3:
		index = input("Type the order's number: ")
		price = int(input("Price per item: "))
		data.update_item_price(index, price)

if '__main__' == __name__:
	# Read the data from the csv file
	transaction = Transaction()
	transaction.load_data()	# Nanti dihapus/komen aja setelah final push

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
		print("3. Delete Item")
		print("4. Edit Item")
		print("5. Reset Transaction")
		print("6. Save Transaction")
		print("7. Exit")
		choice = input("Type menu (1/2/3/4/5/6): ")
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
			# print(transaction['Harga Total'].sum())
			# transaction.view_data()
			trc = transaction.get_all()
			print(trc)
			total_price, discount_price, discount = helpers.count_total_order(trc['Harga Total'].sum())
			print("Total price: {}".format(total_price))
			print("Discount: {}%".format(discount))
			print("Discount price: {}".format(discount_price))
			helpers.clear_screen(slp=3)
		elif '3' == choice:
			# Search item that will be deleted
			if transaction.is_empty() == True:
				print("Your order is empty. Please add some items first")
			else:
				print("Your order is:")
				transaction.view_data()
				print("\n")
				search_item = input("search order's item that you want to delete: ")
				index_item = transaction.search_item(item_name=search_item)
				if index_item == None:
					print("Item not found")
				else:
					print("Item {} found at index: {}".format(search_item, index_item))
					transaction.delete_item(index_item)
					print("Item has been deleted")
		elif '4' == choice:
			print("Your order is:")
			transaction.view_data()
			edit_order(data=transaction)
		elif '5' == choice:
			choise_reset = input("Do you really want to reset the transaction? (y/n): ")
			if 'y' == choise_reset:
				transaction.reset_transaction()
				helpers.clear_screen()
		elif '6' == choice:
			choise_save = input("Do you really want to save the transaction? (y/n): ")
			if 'y' == choise_save:
				transaction.save_to_csv()
				helpers.clear_screen()
		elif '7' == choice:
			print("Thank you for ordering. See you next time\n")
			break
		else:
			print("Invalid input. Please try again\n")
			helpers.clear_screen()
	print('\n')
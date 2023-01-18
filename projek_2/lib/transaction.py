# Create a class that will be used to read, write, and manipulate csv data using pandas in the project
import os
import pandas as pd

from lib import helpers
from lib.path import DATA_PATH

class Transaction:
	"""
	Transaction class is used to read, write, and manipulate csv data using pandas in the project
	"""
	def __init__(self):
		"""
		Constructor
		"""
		self.data = pd.DataFrame()

	def load_data(self):
		"""
		Read the data from the csv file
		
		Returns
		-------
		pandas dataframe
		"""
		self.data = pd.read_csv(DATA_PATH)
		# return self.data

	def save_to_csv(self):
		"""
		Write the data to the csv file
		"""
		self.data.to_csv(self.data_path, index=False)

	def add_item(self, data : dict):
		"""
		Add a new item to the data
		
		Parameters
		----------
		data : dictionary

		Returns
		-------
		int
			Index of the new item
		"""
		self.data = self.data.append({
			'Item': data['Item'],
			'Jumlah Item': data['Jumlah Item'],
			'Harga/item': data['Harga/item'],
			'Harga Total': data['Harga Total']
		}, ignore_index=True)

	def add_item(self, new_data: dict):
		"""
		Add a new item to the data
		
		Parameters
		----------
		data : dictionary

		Returns
		-------
		int
			Index of the new item
		"""
		# new_data = pd.Series(new_data)
		# if self.is_empty():
		# 	self.data = pd.concat([self.data, new_data.to_frame().T], ignore_index=True)
		# else:
		data = pd.DataFrame(new_data)
		self.data = pd.concat([self.data, data], ignore_index=True)

	def update_item_name(self, index : int, item_name : str):
		"""
		Update the item name
		
		Parameters
		----------
		index : int
		item_name : str
		"""
		if self.is_empty():
			print("Your transaction is empty")
		else:
			self.data.loc[index, 'Item'] = item_name

	def update_item_qty(self, index : int, qty : int):
		"""
		Update the item quantity

		Parameters
		----------
		index : int
		qty : int
		"""
		if self.is_empty():
			print("Your transaction is empty")
		else:
			self.data.loc[index, 'Jumlah Item'] = qty

	def update_item_price(self, index : int, price : int):
		"""
		Update the item price
		
		Parameters
		----------
		index : int
		price : int
		"""
		if self.is_empty():
			print("Your transaction is empty")
		else:
			self.data.loc[index, 'Harga'] = price

	def get_all(self):
		"""
		Get all the data
		
		Returns
		-------
		pandas dataframe
		"""
		if self.is_empty():
			print("Your transaction is empty")
		else:
			return self.data

	def is_empty(self):
		"""
		Check if the data is empty
		
		Returns
		-------
		bool
		"""
		if len(self.data) == 0:
			return True
		else:
			return False

	def view_data(self):
		"""
		View the all data in stored in the object
		"""
		if self.is_empty():
			print("Your transaction is empty")
		else:
			print(self.data)

	def delete_item(self, index_item : int):
		"""
		Delete the data by index from `search_item()` method.
		
		Parameters
		----------
		name : str
		"""
		if self.is_empty():
			print("Your transaction is empty")
		else:
			# Delete the row
			self.data = self.data.drop(index_item)
			self.data.reset_index(drop=True, inplace=True)

	def search_item(self, item_name : str):
		"""
		Private method\n
		Search the data by exact name in the dataframe. If the name is not found, 
		it will return -1, otherwise it will return the index of the item.
		
		Parameters
		----------
		name : str

		Returns
		-------
		int
			-1, if the item is not found
		
		otherwise

		int
			Index of the item
		"""
		if self.is_empty():
			print("Your transaction is empty")
			return -1
		else:
			# Search in the dataframe for the item name
			try:
				index = self.data[self.data['Item'] == item_name].index[0]
			except:
				index = None
			return index

	def reset_transaction(self):
		"""
		Reset the data
		"""
		if self.is_empty():
			print("Your transaction is empty")
		else:
			self.data = pd.DataFrame(columns=['Item', 'Jumlah Item', 'Harga/item', 'Harga Total'])
# Pacmann - Python Project

Repositori projek Python course Pacmann

### Latar Belakang Permasalahan
Aplikasi ini adalah aplikasi sistem kasir berbasis console yang dibangun dengan bahasa pemrograman Python. Aplikasi ini bersifat self-service di mana user/customer supermarket/toko menginput langsung barang-barang yang dibeli beserta harga satuannya. Kemduian aplikasi akan menghitung total harga barang yang dibeli dan menampilkan struk pembayaran.

### Requirements/Objektif
- Python minimal versi 3.9
- Pandas

### Alur Program
1. User/customer pertama kali akan dihadapkan dengan tampilan menu aplikasi, diantaranya:
	- Add Item (Input Barang)
	- Check Item (Memeriksa Barang)
	- Delete Item (Menghapus Barang)
	- Edit Item (Mengedit Barang)
	- Reset Transaction (Menghapus Transaksi)
	- Save Transaction (Menyimpan Transaksi ke dalam dokumen CSV)
	- Exit (Keluar dari aplikasi)
2. User dapat memilih menu berdasarkan nomor yang tertera di depannya. Misalnya, jika user ingin memilih menu Add Item, maka user dapat mengetikkan angka 1 dan menekan tombol Enter.
3. Setelah user memilih menu, maka user akan dihadapkan dengan tampilan menu yang berbeda. Misalnya, jika user memilih menu Add Item, maka user akan dihadapkan dengan tampilan menu Add Item.

### Program Module
Terdapat 4 modul utama dalam program ini, yaitu:
1. Modul main (program utama)
	- Modul ini berisi program utama yang akan dijalankan oleh user/customer.
2. Modul helpers
	- Modul ini berisi fungsi-fungsi yang digunakan untuk membantu program utama, diantaranya:
		- fungsi `total_price()` untuk menghitung total harga barang yang dibeli
		- fungsi `total_order()` untuk menghitung total barang dan total harga barang yang dibeli.
		- fungsi `discount()` untuk menghitung diskon yang diberikan kepada user/customer berdasarkan total biaya belanja user/customer.
		- fungsi 'clear_screen()` untuk membersihkan layar terminal.
		- fungsi `create_csv_file()` untuk membuat file CSV dari transaksi user/customer.
3. Modul transaction
	- Modul ini berisi kelas `Transaction` yang digunakan untuk memproses transaksi user/customer.
	- Konstruktor kelas `Transaction` memiliki 2 parameter, yaitu:
		- `data` berupa list yang berisi daftar barang yang dibeli user/customer dengan tipe data DataFrame.
		- `data_path` berupa string yang berisi path dari file CSV yang berisi daftar barang yang dibeli user/customer.
	- Kelas `Transaction` memiliki 12 method, yaitu:
		- `load_data()` untuk memuat data dari file CSV yang berisi daftar barang yang dibeli user/customer.
		- `save_to_csv()` untuk menyimpan data ke dalam file CSV yang berisi daftar barang yang dibeli user/customer.
		- `add_item()` untuk menambahkan barang yang dibeli user/customer.
			- Parameter method ini adalah `data` berupa dictionary yang berisi nama item, jumlah item, harga item, dan harga total, yang dibeli user/customer.
		- Overloading `add_item()`, sama dengan `add_item()` sebelumnya namun data disimpan dengan tipe DataFrame.
		- `update_item_name()` untuk mengubah nama barang yang dibeli user/customer. Memiliki 2 parameter, yaitu:
			- `index` berupa integer yang berisi index dari barang yang akan diubah.
			- `item_name` berupa string yang berisi nama barang yang akan diubah.
		- `update_item_qty()` untuk mengubah jumlah barang yang dibeli user/customer. Memiliki 2 parameter, yaitu:
			- `index` berupa integer yang berisi index dari barang yang akan diubah.
			- `item_qty` berupa integer yang berisi jumlah barang yang akan diubah.
		- `update_item_price()` untuk mengubah harga barang yang dibeli user/customer. Memiliki 2 parameter, yaitu:
			- `index` berupa integer yang berisi index dari barang yang akan diubah.
			- `item_price` berupa integer yang berisi harga barang yang akan diubah.
		- `get_all()` untuk mengambil semua data barang yang dibeli user/customer.
		- `is_empty()` untuk mengecek apakah data barang yang dibeli user/customer kosong atau tidak.
		- `view_data()` untuk menampilkan data barang yang dibeli user/customer.
		- `delete_item()` untuk menghapus barang yang dibeli user/customer. Memiliki 1 parameter, yaitu:
			- `item_index` berupa integer yang berisi index dari barang yang akan dihapus.
		- `search_item()` untuk mencari barang yang dibeli user/customer. Memiliki 1 parameter, yaitu:
			- `item_name` berupa string yang berisi nama barang yang akan dicari.
		- `reset_transaction()` untuk menghapus semua data barang yang dibeli user/customer.
4. Modul path
	- Modul ini berisi 3 variabel global, yaitu:
		- `PATH`, variabel global yang berisi nilai string path dari direktori data transaksi.
		- `DATA_FILE`, variabel global yang berisi nilai string nama file CSV transaksi.
		- `DATA_PATH`, variabel global yang berisi nilai string path dari file CSV transaksi.

### Test Cases and Results
**Test 1: Input Item**
1. User memilih menu Add Item.
2. User memasukkan nama barang, jumlah barang, dan harga barang.
	- Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
	- Nama Item: Pasta Gigi, Qty: 3, Harga: 15000
Expected output:
```
Item berhasil ditambahkan!
```

**Test 2: Delete Item**
1. User memilih menu Deleted Item.
2. Sistem menampilkan barang yang telah dibeli user/customer.
3. Jika tidak ada transaksi, maka akan muncul pesan error.
```
Your order is empty. Please add some items first
```
4. Jika ada transaksi, maka user memasukkan nama barang yang ingin dihapus.
	- Nama Item: Pasta Gigi

Expected output:
```
Your order is:
<image>
search order's item that you want to delete: <input user>
Item <nama item> found at index: <nomor item>
<image>
Item has been deleted 
```
5. Jika user memasukkan nama barang yang tidak ada, maka akan muncul pesan error.
	- Nama Item: Sabun Mandi

Expected output:
```
Item not found
``` 

**Test 3: Reset Transaction**
1. User memilih menu Reset Transaction.
2. User memasukkan konfirmasi untuk menghapus transaksi.
	- Y

Expected output:
```
Your transction has been reset.
```

**Test 4: Total Transaction**


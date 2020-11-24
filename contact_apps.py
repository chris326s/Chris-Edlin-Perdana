from os import system
from datetime import datetime

def view_menu():
	system("cls")
	menu = """
	APLIKASI KONTAK KITA BERSAMA
	[A] - TAMBAH KONTAK BARU
	[B] - TAMPILKAN SEMUA KONTAK
	[C] - CARI KONTAK BERDASARKAN NAMA
	[D] - PERBARUI KONTAK
	[E] - HAPUS KONTAK
	[I] - TENTANG APLIKASI
	[Q] - KELUAR
	"""
	print(menu)

def verify_ans(char):
	char = char.upper()
	if char == "Y":
		return True
	else:
		return False

def print_header(msg):
	system("cls")
	print(msg)

def create_id_contact():
	today = datetime.now()
	year = today.year
	month = today.month
	hari = today.day
	counter = len(data_contact)+1
	id_contact = str("%4d%02d%02d-C%03d" % (year, month, hari, counter))
	return id_contact

def print_data_contact(id_contact = None, all_fields = False, hobi = True):
	if id_contact != None and all_fields == False:
		print(f"""
		-DATA DITEMUKAN-
	ID \t: {id_contact}
	Nama \t:{data_contact[id_contact]["nama"]}
	Telp \t:{data_contact[id_contact]["telp"]}
	Hobi \t:{data_contact[id_contact]["hobi"]}
			""")
	elif id_contact != None and hobi == False:
		print(f"""
		-DATA DITEMUKAN-
	ID \t: {id_contact}
	Nama \t:{data_contact[id_contact]["nama"]}
	Telp \t:{data_contact[id_contact]["telp"]}
			""")
	elif all_fields == True:
		for id_contact in data_contact:
			nama = data_contact[id_contact]["nama"]
			telp = data_contact[id_contact]["telp"]
			hobi = data_contact[id_contact]["hobi"]
			print(f"ID:{id_contact}\tNAMA:{nama}\tTELP:{telp}\tHOBI:{hobi}")

def add_to_contact():
	#Menginpun informasi / data yg kita butuhkan
	print_header("-MEMASUKKAN DAFTAR KONTAK BARU-")
	nama = input("NAMA\t:") #key dict
	telp = input("TELP\t:") #data dict di dalam dict
	hobi = input("HOBI\t:") #data dict di dalam dict

	user_ans = input("Tekan Y untuk menyimpan(Y/N) : ")

	if verify_ans(user_ans): #refactoring function
		id_contact = create_id_contact()
		print("Menyiman Data ...")
		#akses input ke data dict (dict di dalam dict)
		data_contact[id_contact] = {
			"nama" : nama,
			"telp" : telp,
			"hobi" : hobi
		}
		print("Data Tersimpan")
	else:
		print("Data batal Disimpan")
	input("Tekan ENTER untuk kembali ke MENU")


def print_contact():
	print_header("-SEMUA KONTAK-")
	if len(data_contact) == 0:
		print("<BELUM ADA KONTAK YANG DISIMPAN>")
	else:
		print_data_contact(all_fields=True)
	input("Tekan ENTER untuk kembali ke MENU")


def searching_by_name(contact):
	for id_contact in data_contact:
		if data_contact[id_contact]["nama"] == contact:
			print_data_contact(id_contact=id_contact)
			return True
	else:
		print("-DATA TIDAK DITEMUKAN-")
		return False

def get_id_contact_from_name(contact):
	for id_contact in data_contact:
		if data_contact[id_contact]["nama"] == contact:
			return id_contact

def seraching_by_id(id_contact):
	if id_contact in data_contact:
		print_data_contact(id_contact=id_contact)
		return True
	else:
		print("-DATA TIDAK DITEMUKAN-")
		return False

def find_contact():
	print_header("-CARI KONTAK-\n")
	nama = input("Nama Kontak Yang Dicari : ")
	result = searching_by_name(nama)
	input("Tekan ENTER untuk kembali ke MENU")

def delete_contact():
	print_header("-MENGHAPUS KONTAK-")
	nama = input("Masukkan Nama Kontak yang akan Dihapus : ")
	result = searching(nama)
	if result:
		respon = input(f"Yakin ingin menghapus {nama} (Y/N): ")
		if verify_ans(respon):
			del data_contact[nama]
			print("DATA telah dihapus.")

		else:
			print("DATA batal dihapus")
	input("Tekan ENTER untuk kembali ke menu utama")

def update_nama(contact):
	print(f"Nama Lama \t:{contact}")
	new_nama = input("Nama Baru\t: ")
	respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
	if verify_ans(respon):
		id_contact = get_id_contact_from_name(contact)
		data_contact[id_contact]["nama"] = new_nama
		#del data_contact[contact]
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_telp(contact):
	id_contact = get_id_contact_from_name(contact)
	print(f"Nama \t:{data_contact[id_contact]['nama']}")
	print(f"Telp Lama\t:{data_contact[id_contact]['telp']}")
	new_telp = input("Telp Baru\t: ")
	respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
	if verify_ans(respon):
		data_contact[id_contact]['telp'] = new_telp
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_hobi(contact):
	id_contact = get_id_contact_from_name(contact)
	print(f"Nama \t:{data_contact[id_contact]['nama']}")
	print(f"Hobi Lama\t:{data_contact[id_contact]['hobi']}")
	new_hobi = input("Hobi Baru\t: ")
	respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
	if verify_ans(respon):
		data_contact[id_contact]['hobi'] = new_hobi
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_contact():
	print_header("PERBARUI DATA KONTAK\n")
	nama = input("Nama Kontak yang ingin diperbarui : ")
	result = searching_by_name(nama)
	if result:
		print("Data yang ingin diperbarui : ")
		print("[1]. Nama , [2]. Telp , [3]. Hobi")
		respon = input("Pilihan : ")
		if respon == "1":
			update_nama(nama)
		elif respon == "2":
			update_telp(nama)
		elif respon == "3":
			update_hobi(nama)
	input("Tekan ENTER untuk kembali ke menu utama")



def check_input(char):
	char = char.upper()
	if char == "Q":
		return True
	elif char == "A":
		add_to_contact()
	elif char == "B":
		print_contact()
	elif char == "C":
		find_contact()
	elif char == "D":
		update_contact()
	elif char == "E":
		delete_contact()


data_contact = {
	"20201007-C001" : {
		"nama" : "Zebra",
		"telp" : "08123456789",
		"hobi" : "makan rumput"
	},
	"20201007-C002" : {
		"nama" : "Jerapah",
		"telp" : "08123456789",
		"hobi" : "makan rumput"
	}
}
stop = False


while not stop:
	view_menu()
	user_input = input("Pilihan : ")
	stop = check_input(user_input)

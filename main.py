import function as fungsi
player = []
musuh = [{
	'nama' : 'semut', 'power' : 380, 'blood' : 600, 'koin' : 150, 'lvl' : 2
},{
	'nama' : 'burung', 'power' : 420, 'blood' : 750, 'koin' : 240, 'lvl' : 3
},{
	'nama' : 'harimau', 'power' : 510, 'blood' : 950, 'koin' : 330, 'lvl' : 4
},{
	'nama' : 'monster', 'power' : 735, 'blood' : 1200, 'koin' : 500, 'lvl' : 5
}]

info_makan = [{
	'lvl' : 1, 'power' : 30, 'blood' : 100, 'koin' : 25
},{
	'lvl' : 2, 'power' : 45, 'blood' : 120, 'koin' : 45
},{
	'lvl' : 3, 'power' : 55, 'blood' : 140, 'koin' : 65
},{
	'lvl' : 4, 'power' : 75, 'blood' : 150, 'koin' : 85
},{
	'lvl' : 5, 'power' : 90, 'blood' : 175, 'koin' : 95
}]
def daftargame():
	tambah_nama = str(input("Masukkan nama monster anda : "))
	data = {
	'nama' : tambah_nama, 'power' : 200, 'blood' : 700, 'koin' : 132, 'lvl' : 1
	}
	player.append(data)
	print("\n 			Selamat datang monster ~" + player[0]['nama'] + "~")
	start_game()

def start_game():
	print("Koin = " + str(player[0]['koin']))
	print('''
-------------Menu-------------	
-   1. Lihat Info monster    -
-   2. Beri Makan	     -
-   3. Serang Selanjutnya    -
-   0. Keluar Game	     -
------------------------------
''')
	try:
		pilihan_menu1 = int(input("Pilih Menu : "))
	except:
		print('Masukkan Pilihan menu yang benar')
		start_game()

	if pilihan_menu1 == 0:
		print("Selamat Tinggal " + player[0]['nama'])
		exit()
	elif pilihan_menu1 == 1:
		fungsi.cek_info(player[0])
		start_game()
	elif pilihan_menu1 == 2:
		fungsi.beri_makan(player[0], info_makan)
		start_game()
	elif pilihan_menu1 == 3:
		fungsi.bertanding(player[0], musuh)
		start_game()


daftargame()
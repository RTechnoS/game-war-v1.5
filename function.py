import datetime as waktu
def cek_info(player):
	print('''
			----------Info----------
			   Monster : {}
			   Level : {}
			   Power : {}
			   Darah : {}
			   Koin : {}
			------------------------
'''.format(player['nama'], player['lvl'], player['power'], player['blood'], player['koin']))





def beri_makan(player, makanan):
	level_player = player['lvl']
	for i in range(0,len(makanan)):
		if makanan[i]['lvl'] == level_player:
			level_makanan = makanan[i] 
	print('Koin : ' + str(player['koin']))
	print("Harga Makanan {} koin, Dapat menambah power {}, dan dapat menambah Defanse {}".format(level_makanan['koin'], level_makanan['power'], level_makanan['blood']))
	yes_no = input("Beli makan [Y/N] : ")
	if yes_no.lower() == 'y':
		if player['koin'] >= level_makanan['koin']:
			player['koin'] = player['koin'] - level_makanan['koin'] 
			player['power'] += level_makanan['power'] 
			player['blood'] += level_makanan['blood'] 
			
			print('				Nyam.. nyam.. nyam')
			print("				BERHASIL MAKAN")
		
		else:
			print('Koin anda tidak mencukupi :)')
	else:
		print("Kembali   ")




def diserang(playernyo, lawannyo):
	playernyo['blood'] = playernyo['blood'] - lawannyo['power']
	if playernyo['blood'] <= 0:
		playernyo['blood'] = 0
		print('''
=========================================
OH Tidak Kita kalah, kita akan balas dendam
=========================================''')
	print("			ahhh darah saya tinggal {}".format(playernyo['blood']))
	




def menyerang(playernyo, lawannyo):
	lawannyo['blood'] = lawannyo['blood'] - playernyo['power']
	if lawannyo['blood'] <= 0:
		lawannyo['blood'] = 0
		print('''
=========================================
ciee ciee anda menang, selamat naik level
		Reward
	Koin = {} 
========================================='''.format(lawannyo['koin']))
	print('			Darah musuh tinggal {}'.format(lawannyo['blood']))




def bertanding(player, lawan):
	level_player = player['lvl']
	level_lawan = player['lvl'] - 1
	lawannyo = lawan[level_lawan] 
	print('''			
	Monster : {}		{}
	Power   : {}		VS	{}
	Darah   : {} 			{}

			'''.format(player['nama'],lawannyo['nama'],player['power'], lawannyo['power'],player['blood'], lawannyo['blood']))

	yes_no = input("Apakah yakin anda ingin Bertarung [Y/N] : ")
	if yes_no.lower() == 'y':
		kini = waktu.datetime.today()
		detik = kini.second
		# diserang(player, lawannyo)
		if detik % 2 == 1:
			while True:
				diserang(player, lawannyo)
				if player['blood'] <= 0:
					
					break
				
				terus1 = input("\nApakah Anda lanjut menyerang ? [Y/N]") 
				if terus1.lower() != 'y':
					break
				menyerang(player, lawannyo)
				if lawannyo['blood'] <= 0:
					player['lvl'] += 1
					player['koin'] += lawannyo['koin'] 
					break
				

				terus2 = input("\nApakah Anda lanjut menyerang ? [Y/N]") 
				if terus2.lower() != 'y':
					break

		else:
			while True:
				menyerang(player, lawannyo)
				if lawannyo['blood'] <= 0:
					
					player['lvl'] += 1
					player['koin'] += lawannyo['koin'] 
					break
				
				terus3 = input("\nApakah Anda lanjut menyerang ? [Y/N]") 
				if terus3.lower() != 'y':
					break

				diserang(player, lawannyo)
				if player['blood'] <= 0:
					break
				

				terus4 = input("\nApakah Anda lanjut menyerang ? [Y/N]") 
				if terus4.lower() != 'y':
					break
			
 
#Teknik Looping

nama_barang = ['Minyak Angin',
               'Gelas',
               'Piring',
               'Sepatu',
               'Baju',
               'Kaos Kaki',
               'Celana',
               'Topi',
               'Meja']

nama_kendaraan = ['Mobil',
                  'Motor',
                  'Kereta',
                  'Angkot',
                  'Sepeda',
                  'Becak',
                  'Dokar',
                  'Peudati']

# CONTOH 1: Perulangan Biasa
print("=" * 5, 'PERULANGAN BIASA', "=" * 5)

iterasi = 1;

for list_barang in nama_barang:
    print('No:', iterasi, '- Nama Barang : ', list_barang)
    iterasi += 1

print('\n')

# CONTOH 2: Menggunakan Enumerate
print("=" * 5, 'MENGGUNAKAN ENUMERATE', "=" * 5)

for iterasi, list_barang in enumerate(nama_barang):
    print(iterasi, ':', list_barang)
    #   Jika Menggunakan 'Enumerate' akan mengembalikan 2 buah nilai, 
    #   Yakni Indexnya dan Nilainya

print('\n')

# CONTOH 3: Menggunakan Zip
print("=" * 5, 'MENGGUNAKAN ZIP', "=" * 5)
for barang, kendaraan in zip(nama_barang, nama_kendaraan):
    print('Barang :', barang, ', dibawa menggunakan : ', kendaraan)
    # Akan mengkorespondensikan satu satu secara linier data antara 
    # data di nama_barang dan nama_kendaraan
    # jika kedua data tersebut, jumlanya tidak sama, 
    # maka data yang tidak memiliki korespondensi akan menampilkan hasil
    # kosong untuk linier nya

print('\n')

# CONTOH 4: Menggunakan Zip dengan Tipe Data Set (Sorted)
Onderdil = {'Mur', 'Rantai', 'Mono-Shock', 'Jari-Jari', 'Ban', 'Lampu', 'Gigik Tarek'}

print("=" * 5, 'MENGGUNAKAN ZIP (Dengan Data Bertipe: Set() - Sorted', "=" * 5)
for SparePart in sorted(Onderdil):
    print(SparePart, ' (Sorted)')

print('\n')

# CONTOH 5: Menggunakan Zip dengan Tipe Data Set (Not Sorted)
print("=" * 5, 'MENGGUNAKAN ZIP (Dengan Data Bertipe: Set() - Not Sorted', "=" * 5)
for SparePart in Onderdil:
    print(SparePart, ' (Not-Sorted)')

print('\n')

# CONTOH 6: Menggunakan Zip dengan Tipe Data Dictionary)
nama_kota = {'Medan' : 'Keterangan 1',
             'Banda Aceh' : 'Keterangan 2',
             'Jakarta' : 'Keterangan 3',
             'Pekanbaru' : 'Keterangan 4',
             'Bengkulu' : 'Keterangan 5',
             'Padang Sidempuan' : 'Keterangan 6',
             'Jambi' : 'Keterangan 7',
             'Lampung' : 'Keterangan 8'}

print("=" * 5, 'MENGGUNAKAN ZIP (Dengan Data Bertipe: Dictionary ', "=" * 5)
for i in nama_kota.keys():
    print(i)

print('-' * 4)

for i in nama_kota.values():
    print(i)

print('-' * 4)

for i in nama_kota.items():
    print(i)

print('-' * 4)

for i, v in nama_kota.items():
    print(i, 'Datanya =', v)

print('-' * 4)

print('\n')

# CONTOH 7: Contoh Tenik Looping Lainnya)
print("=" * 5, 'CONTOH TEKNIK LOOPING LAINNYA', "=" * 5)

for i in reversed(range(1, 10, 1)):
    print(i)

print('-' * 4)

for i in reversed(range(10, 1, 10)):
    print(i)




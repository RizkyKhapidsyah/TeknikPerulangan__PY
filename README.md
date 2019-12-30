# TeknikPerulangan__PY
Bahan Ajar Fundamental Pemrograman Python. Teknik Looping (Perulangan) Pada Pemrograman Python. Menggunakan Tipe Data List, Tuple, <code>set()</code> dan <code>Dict</code>. <br><br>

<img src="https://github.com/RizkyKhapidsyah/TeknikPerulangan__PY/blob/master/results/001.PNG"><br>
<img src="https://github.com/RizkyKhapidsyah/TeknikPerulangan__PY/blob/master/results/002.PNG"><br>
<img src="https://github.com/RizkyKhapidsyah/TeknikPerulangan__PY/blob/master/results/003.PNG"><br>
<img src="https://github.com/RizkyKhapidsyah/TeknikPerulangan__PY/blob/master/results/004.PNG"><br>
<img src="https://github.com/RizkyKhapidsyah/TeknikPerulangan__PY/blob/master/results/005.PNG"><br>
<img src="https://github.com/RizkyKhapidsyah/TeknikPerulangan__PY/blob/master/results/006.PNG"><br>
<img src="https://github.com/RizkyKhapidsyah/TeknikPerulangan__PY/blob/master/results/007.PNG"><br><br>
- Lihat <a href="https://github.com/RizkyKhapidsyah/TeknikPerulangan__PY/blob/master/TeknikPerulangan__PY.py">Source Code.</a><br><br>

-----

Perulangan dalam bahasa pemrograman berfungsi menyuruh komputer melakukan sesuatu secara berulang-ulang. Terdapat dua jenis perulangan dalam bahasa pemrograman python, yaitu perulangan dengan <code>for</code> dan <code>while</code>.

Perulangan <code>for</code> disebut counted loop (perulangan yang terhitung), sementara perulangan <code>while</code> disebut uncounted loop (perulangan yang tak terhitung). Perbedaannya adalah perulangan <code>for</code> biasanya digunakan untuk mengulangi kode yang sudah diketahui banyak perulangannya. Sementara <code>while</code> untuk perulangan yang memiliki syarat dan tidak tentu berapa banyak perulangannya.

# Perulangan <code>for</code>

Bentuk umum:

      for indek in range(banyak_perulangan):
          # jalankan kode ini
          # jalankan juga kode ini
      #kode ini tidak akan diulang karena berada di luar for

Contoh program:

      ulang = 10

      for i in range(ulang):
          print "Perulangan ke-"+str(i)

Pertama kita menentukan banyak perulangannya sebanyak 10x

      ulang = 10

Variabel <code>i</code> berfungsi untuk menampung <code>indeks</code>, dan fungsi <code>range()</code> berfungsi untuk membuat list dengan range dari 0-10. Fungsi <code>str()</code> berfungsi merubah tipe data <code>integer</code> ke <code>string</code>.

      for i in range(ulang):
          print "Perulangan ke-"+str(i)

Hasil:

<div class=highlight><pre style=color:#f8f8f2;background-color:#000000;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-bash data-lang=bash>root@rizkykhapidsyah:~$ python perulanganFor.py
Perulangan ke-0
Perulangan ke-1
Perulangan ke-2
Perulangan ke-3
Perulangan ke-4
Perulangan ke-5
Perulangan ke-6
Perulangan ke-7
Perulangan ke-8
Perulangan ke-9<span style=color:#bd93f9>7</span>
</code></pre></div></div>

Contoh lain menggunakan senarai (list):

      item = ['kopi','nasi','teh','jeruk']

      for isi in item:
          print isi

Hasil:

<div class=highlight><pre style=color:#f8f8f2;background-color:#000000;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-bash data-lang=bash>root@rizkykhapidsyah:~$ python perulanganFor.py
kopi
nasi
teh
jeruk<span style=color:#bd93f9>7</span>
</code></pre></div></div>

# Perulangan <code>while</code>

Bentuk umum:

      while(True):
          # jalankan kode ini

kode ini berada di luar perulangan <code>while</code> :

Contoh:

      jawab = 'ya'
      hitung = 0

      while(jawab == 'ya'):
          hitung += 1
          jawab = raw_input("Ulang lagi tidak? ")

      print "Total perulangan: " + str(hitung)

Atau bisa juga dengan bentuk yang seperti ini, dengan menggunakan kata kuci <code>break</code>

      jawab = 'ya'
      hitung = 0

      while(True):
          hitung += 1
          jawab = raw_input("Ulang lagi tidak? ")
          if jawab == 'tidak':
              break

      print "Total perulangan: " + str(hitung)

Pertama menentukan variabel untuk menghitung, dan menentukan kapan perulangan berhenti. kalau pengguna menjawab tidak maka perulangan akan terhenti.

      jawab = 'ya'
      hitung = 0

Melakukan perulangan dengan while, kemudian menambah satu variabel hitung setiap kali mengulang. lalu menanyakan kepada pengguna, apakah mau berhenti mengulang atau tidak?

      while(jawab == 'ya'):
        hitung += 1
        jawab = raw_input("Ulang lagi tidak? ")
      Setelah selesai mengulang, cetak berapa kali perulangan tersebut terjadi

      print "Total perulangan: " + str(hitung)

Hasil:

<div class=highlight><pre style=color:#f8f8f2;background-color:#000000;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-bash data-lang=bash>root@rizkykhapidsyah:~$ python perulanganWhile.py
Ulang lagi tidak? ya
Ulang lagi tidak? ya
Ulang lagi tidak? ya
Ulang lagi tidak? ya
Ulang lagi tidak? ya
Ulang lagi tidak? ya
Ulang lagi tidak? tidak
Total perulangan: <span style=color:#bd93f9>7</span>
</code></pre></div></div>

<br>

-----

# enumerate(iterable, start=0)

Kembalikan objek enumerasi. iterable harus berupa urutan, sebuah iterator, atau objek lain yang mendukung iterasi. The <code>__next__()</code> metode iterator dikembalikan oleh <code>enumerate()</code> mengembalikan tuple yang berisi hitungan (dari start yang bawaan ke 0) dan nilai yang diperoleh dari mengelilingi iterable.

      seasons = ['Spring', 'Summer', 'Fall', 'Winter']
      list(enumerate(seasons))
      [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
      list(enumerate(seasons, start=1))
      [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

Setara dengan:

      def enumerate(sequence, start=0):
          n = start
          for elem in sequence:
              yield n, elem
              n += 1

## Menggunakan fungsi <code>zip()</code>

Perintah <code>zip()</code> dalam bahasa pemrograman python digunakan untuk menggabungkan nilai dari dua buah iterables (misal: list,tuple) ke dalam satu iterable sehingga dapat digunakan sebagai sebuah entitas. Nilai dari hasil akhir perintah <code>zip()</code> tadi akan berisi pasangan nilai dari kedua iterables yang digabungkan.

Sintaks perintah <code>zip()<code> :

      gabungan = zip(iterableA,iterableB)

Perhatikan contoh berikut untuk lebih jelasnya :
Kita memiliki nama mahasiswa pada satu list, dan nilai ujiannya pada list yang lain. Kedua nilai tersebut ingin kita gabungkan ke dalam satu list dengan perintah <code>zip</code> seperti berikut ini.

      nama_siswa = ['Upin','Ipin','Jarjit','Meimei','Susanti','Fizi','Ehsan']
      nilai_siswa = [80,75,60,90,85,83,82]

      nama_dan_nilai = zip(nama_siswa,nilai_siswa)

      for val in nama_dan_nilai:
        print(val)

## Unzipping

Pada kasus lain kita membutuhkan proses sebaliknya, yakni melakukan ekstraksi satu jenis nilai saja dari iterable yang memiliki beberapa nilai sekaligus pada tiap elemennya. Untuk kasus ini kita menggunakan perintah <code>unzip</code> dengan sintaks seperti dibawah ini

### Perintah <code>unzip</code>

      tupleA,tupleB = zip(*iterable) 

Berikut adalah contoh untuk pemanfaatan unzip. Pelajari dan jalankan kodenya untuk lebih memahami cara kerjanya.

      kamus_en_id = [['Horse','Kuda'],['Goat','Kambing'],['Cow','Sapi'],['Buffalo','Kerbau']]

      term_en,term_id = zip(*kamus_en_id)

      print('seluruh kosakata EN:',term_en)
      print('seluruh kosakata ID:',term_id)

-----
Referensi Artikel: <a href="https://www.petanikode.com">PetaniKode</a>, <a href="https://docs.python.org">Python.org</a>, <a href="https://koding.alza.web.id">KodingAlza</a>. Thanks To: <a href="https://www.petanikode.com">PetaniKode</a>, <a href="https://docs.python.org">Python.org</a>, <a href="https://koding.alza.web.id">KodingAlza</a><br>

Referensi Source Code: <a href="https://www.youtube.com/user/faqihzamukhlish"> Kelas Terbuka </a> dan <a href="https://github.com/kelasterbuka"> Kelas Terbuka (Repository)</a>. Created by <a href="https://github.com/faqihza">Faqihza Mukhlish.</a> Thanks To: <a href="https://www.youtube.com/channel/UCRGHjysoCemh4y7tCJQs30w/about">Faqihza Mukhlish.</a><br>

-----
All Source Code is Modified.

"""

nah kali ini kita akan belajar bagaimana memanipulasi string

"""

# 1.menyambung string atau operator konkatenasi 

str1 = 'muiz '
str2 = 'zuddin'

nama_lengkap = str1 + str2

print(nama_lengkap)

"""

nah cara menggabungkan string itu tinggal kita gunakan tanda tambah

"""



# 2.menghitung panjang dari string

# nah untuk menghitung panjang string kita bisa gunakan sebuah function yang namanya leng

nama = 'muiz'
print(len(nama))


# 3 operator untuk string


# mengecheck apakah ada komponen char atau string distring

nama = 'husainnurul'
cari = "nurul"

print(cari in nama)

"""

nah jadi kita bisa mencari string didalam string

selain in kita juga bisa gunakan not in

"""

nama = 'husainnurul'
cari = "husain"

print(cari not in nama)


# 4 mengulang string

print('wk'*10)
print(10*'ha')

"""

nah kalo kita jalankan maka wknya akan diulang sebanyak 10 kali
tanpa kita menggunakan keyword for

"""


# 5 indexing

"""

nah kalo didalam python itu kita bisa memanggil index pada string tanpa mengubah dulu kedalam array
misalnya

"""

nama = 'muizzuddin'
print(nama[0])
print(nama[-1])
print(nama[-2])

"""

nah jangan lupa index dipython sama dengan javascript yaitu sama sama dimulai dari 0
kalo untuk panjang itu dimulai dari 1

nah kalo dipython kita juga bisa mengambil dari belakang 
dimulai dari -1 dan seterusnya 

kita juga bisa melakukan pemotongan pada string

"""

print(nama[0:2])

"""

0 itu kita mulai pemotongannya 
dan 2 itu akhirnya tapi yang index kedua tidak akan keambil
yang keambil adalah index sebelumnya yaitu 1

jadi 0 - 1


kita juga bisa mengambil stringnya memakai jeda

"""

print(nama[0:9:2])

"""
dari nama muizzuddin

kita ambil 0 sampai 9
tapi incrementnya 2

jadi kita ambilnya index 0 2 4 6 8
maka hasilnya akan mizdi


"""


# 6 item paling kecil


print(min(1,2,3))

"""

nah kita bisa mencari nilai terkecil menggunakan function min()
kita juga bisa melakukannya menggunakan string

jadi dibalik layar nanti tiap tiap karakter akan diubah menjadi uniqcode yang berupa angka
dan nanti akan ditampilkan mana angka yang paling kecil

setelah dapat angka yang paling kecil maka dia akan dikembalikan menjadi huruf lagi
kita coba

"""

nama = "muizzuddin"
print(min(nama))

"""

maka yang paling kecil adalah d
nah kalo hurufnya itu ada dua maka yang dikembalikan hanya satu

"""

# 7 yang peling besar

"""

nah kalo ini kebalikan dari min ya yaitu max()

"""
nama = "muizzuddin"
print(max(nama))

"""

maka dia akan mengembalikan z karena z itu yang paling besar 
nah untuk mengetahui berapa nilai angka dari z kita bisa gunakan 
sebuah function yang namanya ord()

"""

charCode = ord('z')
print(charCode)


"""

nah lalu bagaimana kalo yang kita masukkan adalah angka dan kemudian 
kita ingin mengubahnya menjadi karakter ?
kita bisa gunakan function yang namanya chr()

"""

formCodeAt = chr(90)
print(formCodeAt)

"""

maka dia akan mengubah dari angka menjadi huruf

"""


# 8 menggunakan method 

nama = 'muizzuddin'
jumlah = nama.count('i')
print(jumlah)


"""

nah kita tahu bawah python itu sama seperti javascript 
semua data entah itu variable dll kecuali function 

itu ada didalam sebuah object
nah dipython itu punya sesuatu yang dinamakan dengan method

method itu sebuah function yang ada didalam object

method count()
memiliki 1 argument yang itu dia akan mencari nilai yang ada didalam argumentnya 
ke objectnya 

disini objectnya nama dari class str
maka kalo dijalankan hasilnya 2 karena i nya ada 2

dengan menggunakan count kita juga bisa menghitung panjang string

"""


nama = 'hasan'
print(nama.count(''))

"""

kalo kita jalankan maka hasilnya 6
lah kok 6  bukannya 5 ya?

nah untuk count ini dimulai dari string kosong

kalo string kosong itu dihitung 1
ketika ada textnya 

'm' maka itu dihitung 2 

jadi kalo mau hasilnya benar kita tinggal - 1

"""
nama = 'hasan'
print(nama.count('') - 1)
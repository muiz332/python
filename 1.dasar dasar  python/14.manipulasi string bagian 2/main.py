# beberapa method pada string

# 1.merubah semua huruf ke uppercase

print('===upperCase===')
nama = 'muiz'
print(str.upper(nama))

# nah untuk method ini sama ya seperti javascript 
# kalian bisa panggil objectnya dulu kemudian panggil methodnya masukkan nilainya kedalam argumentnya 

# atau kalian bisa panggil methodnya saja

print(nama.upper())


# 2.merubah semua huruf ke loweCase

print('====lowerCase====')

nama = 'HASAN'
print(nama.lower())


# 3. pengecheckan apakah lower semua

print('=====pengecheckanlower====')
nama = 'husain'
print(nama.islower())

# dia akan mengembalikan boolean
nama = 'huSain'
print(nama.islower())

# jadi kalo ada salah satu huruf besar maka dia akan false


# 4.pengechekan upper semua

print('====pengecheckanUpper====')
nama = 'GUIDO VAN ROSSUM'
print(nama.isupper())

nama = 'BRENDAN eICH'
print(nama.isupper())


"""

kalian bisa coba satu satu beberapa method dibawah ini ya 

isalpha() = untuk mengecheck apakah semua huruf atau bukan
isalnum() = untuk mengecheck apakah string berisi huruf dan angka
isdecimal() = untuk mengecheck apakah string isinya angka saja

isspace() = untuk mengechek apakah ada string new line, tab, spasi
istitle() = untuk mengecheck semua kata diawali dengan huruf besar
capitalize() = mengubah awalan huruf dari huruf kecil menjadi besar

nah selain itu sebenarnya ada banyak banget methodnya 
silahkan kalian cari tahu sendiri ya 

"""

# 5.pengecheckan dengan awalan atau akhiran

# awalan kita gunakan method yang namanya startwith()

print('====awalan====')

nama = 'muiz zuddin'
print(nama.startswith('muiz'))

"""
ini bacanya string nama apakah dimulai dengna awalan muiz? 
nah true ya 
karena ada kata muiz diawal

"""

print('===akhiran===')

nama = 'muiz zuddin'
print(nama.endswith('in'))

"""

kalo kita jalankan maka hasilnya akan bernilai true ya 

"""


# 6.penggabungan komponen join(), split()

print('===method tentang list===')

# menggunakan join()

lis = ['m','u','i','z']
gabung = ''.join(lis)
print(gabung)

"""
nah jadi kita buat dulu sebuah variable yang namanya gabung

lalu kita bikin pemisahnya apa?
kita kasih string kosong karena saya ingin gabung tanpa adanya pemisah

''.join(lis)

lalu kita tulis titik join() nah didalam argument join() itu kita kasih listnya 

inget kalo didalam python kita tulis pemisahnya dulu kemudian join() 
nah didalam argument join itu kita kasih arraynya atau listnya 

kalo didalam javascript itu kita tulisnya 
arraynya apa lalu join() dan didalam argument join() itu kita kasih pemisahnya 
kalo string kosong nanti akan gabung 

kalo string spasi ' ' nanti akan dipisahkan dengan spasi


"""

# menggunakan split()

"""

nah sebenarnya untuk memecah string menjadi array 
didalam python itu kita bisa gunakan function list()

atau kita bisa gunakan method split()

"""

nama = 'muiz'
jadilist = list(nama)
print(jadilist)


nama = 'husain hasan'
jadilist = nama.split(' ')
print(jadilist)

"""

nah jadi kita lihat antara list() dan split()
itu memiliki perbedaan

nah kalo list apapun stringnya itu dia akan memecah tiap tiap karakter

sedangkan split() dia akan memecah dengan kalau ketemu 
karakter yang kita masukkan didalam argument splitnya 

misalnya kita punya husain hasan

maka kalo kita split dan kita masukkan argumentnya string spasi
maka dia akan memecah kalo ketemu spasi

maka hasilnya ['husain','hasan']

"""



# alokasi karakter 

# nah sebelumnya kan kita sudah belajar seperti ini 

print(5*'=' + 'alokasi karakter' + '='*5)

# nah selain itu ada cara yang lain yaitu dengan menggunakan
"""

rjust() = rata kanan
ljust() = rata kiri
center() = rata tengah

"""

kanan = 'husain'.rjust(10)
print("'"+ kanan +"'")

"""

nah maka dia akan membuat baris dengan panjang 10 karakter 
dan tulisannya akan rata kanan

"""

kiri = 'muiz'.ljust(10)
print("'"+ kiri +"'")

tengah = 'hasan'.center(11)
print("'"+tengah+"'")

"""

nah kalo kalian jalankan akan muncul hasilnya sesuai dengan methodnya 
sekarang pertanyaanya 

bisakan saya ganti spasinya menjadi karakter lain?
bisa dong 

caranya tinggal kita tambahkan argument kedua yaitu karakternya 
"""
tengah = 'hasan'.center(11, '=')
print("'"+tengah+"'")

"""

kalo kita jalankan maka dia akan berada ditengah ya 

"""

# kebalikan dari alokasi 

print('===kebalikan alokasi===')

tengah = tengah.strip('=')
print(tengah)

"""

nah kalo kita jalankan maka dia akan normal lagi

"""

kiri = kiri.strip()
print("'"+kiri+"'")
"""
nah bagaimana cara kita mengambil inputan dari user
kalo menggunakan javascript itu kita bisa pakai prompt atau confirm

nah kalo dipython itu kita gunakan sebuah function yang namanya input
contoh

"""

# nama = input('masukkan namamu: ')
# umur = input('masukkan umurmu: ')
# univ = input('masukkan univ: ')

# print('nama saya ',nama , 'saya berumur: ', umur, "saya kuliah di ", univ)

# nama = input('masukkan nama ')

# print(type(nama))

"""

nah untuk input ini data yang dimasukkan pasti bertype string
jika kita ingin mengambil intejer kita tinggal cesting saja hasil inputannya 
contoh

"""

# data_input = int(input('masukkan angka'))

# print(type(data_input))

"""

nah kalo kalian ingin inputannya berupa boolean maka 
kalian tidak bisa menginputkan true dan false

karena ketika kalian menginputkan yang false 
maka kebacanya akan true

nah kita gunakan 0 dan 1 sebagai acuan booleannya 

kan kalo 0 itu false ya dan selain 0 itu akan bernilai true

"""

dat_bol = bool(int(input('masukkan biner')))

print(dat_bol,type(dat_bol))
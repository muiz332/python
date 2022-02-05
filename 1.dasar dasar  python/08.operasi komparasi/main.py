"""

nah sekarang kita akan belajar mengenai operasi komparasi 
atau disebut juga dengan operasi perbandingan

nah hasil operasi ini nilainya boolean yaitu true dan false

operasi perbandingan

==
<
>
<=
>=
!=
is
is not


nah langsung saja kita akan membahas is dan is not

untuk is itu kita dapat membandingkan memory (variable) dan object

"""

#contoh

# a = 9

# print(a is 8)

# nah kalo saya jalankan maka tidak akan bisa 
# karena 8 itu hanya berlaku pada baris itu saja

"""

tidak bisa berlaku di baris lain atau istilahnya literal 
tapi ketika kita masukkan kedalam sebuah variable 

maka variable tersebut dapat kita panggil pada baris yang lain

jadi kalo saya tulis begini 

"""

a = 9
b = 9

print(a is b)

# apakah a adalah b? maka hasilnya true ya 


"""

nah kalo is not itu kebalikannya 
kalo nilainya sama dia akan false kalo nilainya tidak sama maka dia true

"""

c = 8
d = 6

print(c is not d)


# apakah c tidak sama dengan d? true ya 


"""

nah sebetulnya variable itu adalah boject identity
semua variable itu adalah object 

kalo saya tulis begini 


"""

print(type(c))

# <class 'int'>

"""

maka dia akan berada didalam object yang namanya class int
kalo saya panggil id dari c nya 

"""

print(id(c))

# 2156132723216

"""

maka hasilnya akan angka 
angka itu menandakan bahwa dia berada dimemorynya atau addressnya

nah si c itu adalah object 
nah kalo id itu adalah object identitasnya
kita bisa pakai id atau kita masukkan idnya kedalam hex() nanti hasilnya hexsa desimal

nah jadi kalo kita pakai is atau is not untuk membandingkan object ini 

untuk didalam python ini kalo nilainya sama itu masuk kedalam memory yang sama 
dan dia juga memiliki id yang sama 


"""
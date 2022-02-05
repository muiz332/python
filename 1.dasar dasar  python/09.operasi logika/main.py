"""

nah kita akan belajar mengenai operator logika 

macam macam opertor logika

not or and dan xor

"""

from typing import Tuple


print("====NOT====")

a = 9


print(not a == 9)
print(not a == 8)


# nah not ini dia akan membalikkan hasil
# ketika hasilnya true maka dia balikkan menjadi false
# dan ketika hasilnya false maka dia akan mengembalikan true


print("====OR====")


b = 7

print(b == 7 or b < 6)
print(b != 7 or b < 5)


"""

nah kalo or and dan xor dia membutuhkan dua kondisi atau lebih
kita check tuh apakah b sama dengan 7  true ya 

atau b lebih kecil 6 false

kalo dari dua kondisi tersebut ada yang bernilai true maka hasilnya akan true 
dan kalo kedua kondisi tersebut bernilai false maka akan mengembalikan nilai false


"""


print('====AND====')

c = 8
print(c == 8 and c < 9)
print(c == 8 and c < 7)


"""

nah kalo and itu kebalikan dari or
kalo ada salah satu kondisi yang bernilai false maka semua  hasilnya false
dan kalo semua kondisinya bernilai true maka hasilnya akan true

"""


print('====XOR====')
d = True
f = False

print(d ^ f)
d = False
f = False
print(d ^ f)

d = True
f = True
print(d ^ f)


"""

nah untuk xor ini kalo nilainya berbeda ada yang true dan ada yang false
maka dia mengembalikan nilai true

kalo semuanya bernilai false atau semuanya bernilai true maka dia akan mengembalikan nilai false


dan xor ini hanya dipakai ketika ada ada sebuah kondisi dimana kita harus mengampung hasil boolean dari kondisi kondisi kedalam sebuah variable

"""


print('====XOR contoh lagi====')

g = 9
h = 7

i = g == 9
j = h < 6

print(i ^ j)


"""

akan true jika salah satu true sisanya false

"""
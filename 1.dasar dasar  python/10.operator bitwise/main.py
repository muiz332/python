"""

nah sekarang kita akan belajar mengenai operator bitwise atau disebut juga operator binery

jadi bitwise itu adalah operasi masing masing bit

nah kalo kita bicara mengenai binary 
binery itu seperti ini 

  0  0 0  0  1  0   0   1 
   64 32 16  8  4  2   1

nah sekarang bitwise itu apa?
bitwise itu adalah operasi antara bilangan biner 

lalu gimana cara kita melakukan operator bitwise itu?
misalkan 

""" 

print('====or====')
a = 9
b = 5

# bitwise or(|)

print(a | b)

"""

nah kenapa hasilnya 13?
karena pada operator bitwise itu akan mengubah angka menjadi bilangan biner

9 = 1001
5 = 101

setelah jadi biner maka si operator bitwise itu akan menjumlahkan bilangan binernya 

1001
 101

 kalo kita pakai yang or

 anggap saja 1 itu sama dengan true kalo 0 itu false
 jadi kalo 1 ketemu 1 itu hasilnya 1 kalo 0 ketemu 1 itu hasilnya 1 dan kalo 0 ketemu 0 itu hasilnya 0

hasilnya 10101

maka kalo kita hitung

 1   1   0    1
 8   4   2    1

maka kalo kita hitung hasilnya 13



"""



print('=====and=====')


c = 3
d = 2

print(c, ' binary ', format(c,'08b'))
print(d, ' binary ', format(d,'08b'))
print(c & d, 'binary', format(c & d, '08b'))


"""

kalo kita jadi kan biner 

3 = 11
2 = 10

atau misalnya kalo kalian ingin mengubah angka menjadi biner maka
pakai function yang namanya format(angka, '08b')


"""


print('====xor====')

e = 5
f = 4

print(e,' binary ', format(e, "08b"))
print(f,' binary ', format(f, "08b"))
print(e ^ f, 'binary', format(e ^ f, '08b'))


print('====not====')

g = 6

print(g,' binary ', format(g, "08b"))

print(~g, "binary ", format(~g, '08b'))


"""

nah untuk not kalo kita punya positif 6 kalo kita gunakan not 
itu hasilnya akan menjadi -7 lah kok bisa?

-2 -1 0 1 2 3

nah kita lihat angka diatas itu cerminan antara bilangan positif dan negatif

kalo positif itu dari 0 
kalo negarif itu dari -1

makanya kalo saya punya 1 dan saya not kan 
hasilnya akan menjadi -2

seolah olah -1 itu adalah -0 nya 


"""

"""

nah selanjutnya kita akan bahas mengenai shift right dan shift left

kita bahas dulu shift right

"""

print('===>>===')

n = 9

print(n, ' binery ', format(n, "08b"))
print(n >> 2, 'binary ', format(n >> 2, '08b'))


"""

nah kalo shift right itu dia akan menggeser kekanan

jadi kalo saya punya 
9 =  00001001

maka dia akan menghilangan dua digit dari kanan
karena kita gesernya 2 kali

000010

maka hasilnya seperti itu

"""

print('=====<<====')

m = 9

print(m, ' binery ', format(m, "08b"))
print(m << 2, 'binary ', format(m << 2, '08b'))


"""

nah dia akan menggeser kekiri

9 =  00001001

maka hasilnya akan 

 00100100

 nah dia akan menambahkan 0 agar menggeser kekiri


"""

print('====kebalikan=====')


"""

nah kalo kita ingin membalikan binernya kita gunakan xor



"""

v =  0b00001001
l =  0b11111111

print(9, ' binary ', format(9, "08b"))

print(v ^ l, ' binary ', format(v ^ l, '08b'))

"""

nah maka dia akan membalik ya 
jadi kalo 1 dengan 1 itu pasti 0

kalo beda itu pasti 1

"""
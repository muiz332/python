"""

sekarang kita akan bahas salah satu jenih pada array yaitu lists

apa itu lists ?
list adalah kumpulan nilai yang tersusun, dapat diubah dan memungkinkan nilai / elementnya ada duplikat



"""

# nilai yang tersusun

"""

nah kita akan bahas dulu apa sih maksutnya nilai yang tersusun
ketika kita membuat array dengan lists maka tiap tiap nilai itu memiliki index

atau bisa disebut dengan pasangan key dan value
keynya apa? keynya index dan index itu dimulai dari 0 

nah maksutnya tersusun itu 
ketika kita memiliki misalnya 5 nilai maka tiap tiap nilai akan memiliki index dimulai dari 0

jadi nanti indexnya akan seperti ini 
0 1 2 3 4

dari 0 - 4 itukan dia urut ya jadi maksutnya tersusun itu seperti ini 
indexnya itu urut dari 0 sampai banyak element - 1

lalu bagaimana kita membuat list?
contoh misalnya saya punya variable namanya names 

"""

names = ['muiz','husain','hasan']
print(names)

"""

untuk membuat list kita membutuhkan kurung siku buka dan tutup
lalu tiap tiap nilainya kita pisahkan dengan koma 

ya seperti kita membuat array pada javascript 

"""

# dapat diubah

"""

misalkan saya punya list yang namanya angka

"""

angka = [2,1,3,5,4]
angka[1] = 'muiz'
print(angka)

"""

nah kalo kita ingin mengubah  nilai kita tinggal tuliskan ingexnya saja ya 
lalu kita assignment dengan nilainya 

"""


# memungkinkan nilai yang sama / duplikat  didalam list


angka = [1,1,1]
print(angka)


# didalam list boleh memiliki type data yang berbeda

tipe = [1,'muiz',True,2.3]
print(tipe)


# kita bisa membuat list constructor

hari = (('senin','selasa'))
print(hari)

"""

nah kita bisa membuat list menggunakan constructor 
tapi kita tidak bisa menggunakan method method yang ada pada list

"""



p = ['nama','aku','muiz','salken','oke']
print(p[0:4:2])










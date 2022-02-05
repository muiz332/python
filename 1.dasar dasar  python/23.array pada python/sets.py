"""

selanjutnya kita akan membahas type array selanjutnya yaitu set

apa itu set?
set adalah kumpulan yang tidak terurut,  tidak terindex, tidak dapat diubah dan tidak memungkinkan adanya duplikat pada nilainya 

"""


# membuat set

nama = {'muiz','zuddin'}
print(nama)

"""

jadi untuk membuat set kita harus menggunakan kurung kurawal buka dan tutup 

"""


# tidak terindex

# hari = {'senin','selasa'}
# print(hari[1])

"""

jadi kita tidak dapat menggunakan index untuk mengakses nilai yang ada didalamnya 

"""

# duplikat tidak diizinkan

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

"""

jadi seperti dijavascript ya ada tuh set
jadi set tidak dapat diduplikat 

"""


# menghitung panjang set
"""

untuk menghitung panjang set kita dapat menggunakan method len() ya

"""


# menggunakan constructor set

nama = set(('aku','aku','kamu','kamu','dia'))
print(nama)



# mengakses nilai pada set

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# menjadi nilai pada set menggunakan in
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

"""

jadi kita bisa menjadi nilai pada set menggunakan method in
seperti kita menjadi nilai pada string ya 
sama  sama menggunakan method in

"""

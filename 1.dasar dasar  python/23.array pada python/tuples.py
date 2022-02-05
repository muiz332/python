"""

nah selanjutnya kita akan belajar mengenai tuples

apa itu tuples
tuples adalah kumpulan yang kita pesan, tidak dapat diubah dan memungkinkan adanya duplikat pada nilai/elementnya 


"""

# membuat tupples

buah = ('apple', 'banana', 'watermelon')

print(buah)

# dipesan
"""

ketika kita mengatakan bahwa tuple itu dipesan maka berarti item memiliki urutan yang ditentukan dan urutan tersebut tidak dapat diubah

"""

# tidak dapat diubah

# hari = ('senin','selasa','kamis')
# hari[2] = 'rabu'
# print(hari)

"""

nah jadi kita tidak dapat mengubah nilai pada tuple ya
kalo kita jalankan maka dia akan eror 

artinya kita tidak dapat menambah mengubah dan menghapus nilai yang ada pada tuple


"""


# memungkinkan adanya duplikat


nama = ('muiz','muiz','hasan')
print(nama)


"""

nah kita bisa menambahkan nilai yang sama kedalam tuple paham ya 

"""

# membuat tuple dengan 1 nilai

namamu = ('muiz',)
print(type(namamu))

"""

kalo ingin membuat tuple yang isinya hanya 1 nilai maka kita harus menambahkan koma  
diakhir nilainya 

ketika kita tidak menambahkan koma maka kalo kita check dengan build in function dari python yang namanya type maka dia akan memunculkan str bukan tuple


"""


# membuat tuple dengan constructor

constupl = (('sekarang', 'hari', 'apa', '?'))
print(' '.join(constupl))


# kita bisa melakukan distructuring assignment / unpack pada python 


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

"""

jadi untuk unpack bisa dilakukan oleh tuple 

"""
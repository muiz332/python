"""

kali ini kita akan membahas mengenai dictionaries

apa itu dictionaries?
dictionaries adalah kumpulan yang tersusun, dapat diubah dan tidak ada anggota duplikat

"""

# membuah dictionaries

mahasiswa = {
    'nama' : 'muiz',
    'umur' : 18,
    'lulus' : False
}

print(mahasiswa['nama'])

print(mahasiswa.get('nama'))

"""

jadi kita buatnya menggunakan kurung kurawal buka dan tutup 
ya mirip ya seperti object pada javascript 

tapi untuk propertinya itu kita harus membuatnya dengan menggunakan kutip


"""

# dapat diubah
"""

artinya kita bisa menambah menghapus dan menambah nilai padda dictionaries

"""
buku = {
    'judul' : 'tuhan ada diharimu',
    'tema' : 'islami'
}
buku.update({'pembuat': 'habib husain ja\'far'})
#tanpa method
buku['harga'] = 1234
print(buku)

"""

jadi untuk menambah kita menggunakan method update
method ini memiliki 2 argument

argument yang pertama itu propertinya dan argument yang kedua itu nilainya 

"""

buku.pop('tema')
print(buku)
buku.popitem()
print(buku)

"""

untuk methodnya kalian bisa lihat diw3scholl

"""

# tidak mengizinkan duplikat

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


# untuk menghitung panjang dictionaries kita menggunakan len()


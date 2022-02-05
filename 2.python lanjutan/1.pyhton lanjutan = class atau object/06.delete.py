# delete

"""

nah kemudian kalo kalian ingin menghapus properti atau objectnya 
kalian gunakan keyword yang namanya del spasi nama object atau propertinya 

contoh 

"""

class mahasiswa:
    def __init__(this,nama,umur,jurusan):
        this.nama = nama
        this.umur = umur
        this.jurusan = jurusan



muiz = mahasiswa('muiz',18,'teknik informatika')

print(muiz.nama, muiz.umur, muiz.jurusan)

"""

akan muncul 
muiz 18 teknik informatika   

dan sekarang kita coba hapus

"""

del muiz.umur

print(muiz.umur)

"""

kalo saya print akan eror karena
class muiz tidak memiliki properti umur

untuk menghapus object 
bisa tulis

del nama objectnya 

"""


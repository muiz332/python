"""

init disini berfungsi untuk mengisi value yang berbeda
ketika properti dan methodnya sama

lalu gimana cara membuat fungsi ini didalam classnya?
seperti ini 

"""

class mahsiswa:
    def __init__(self,nama,umur,jurusan):
        self.nama = nama
        self.umur = umur
        self.jurusan = jurusan



"""

nah ketika kita menggunakan fungsi init
itu sama saja kita membuat class tapi properti nya kita
masukkan dalam function 

jadi nanti apapun yang kita masukkan kedalam function 
maka akan menjadi value dari properti tersebut

lalu untuk cara memanggilnya bagaimana?
kita panggil nama classnya diikuti dengan kurung

yang nanti dia akan mengembalikan object yang telah diisi value 
yang kalian masukkan kedalam kurungnya 


misalkan saya ingin mengisi data mahasiswa yang namanya muiz

"""


muiz = mahsiswa('nama',18, jurusan='teknik informatika')

"""

nah ketika saya ingin mengisi data muiz
maka saya tinggal panggil saja class yang namanya mahasiswa
diikuti dengan kurung buka dan tutup

dan disi dengan data mahasiswa tersebut
kalian bisa pakai keyword parameter agar kalo mengisikan datanya 
tidak harus sesuai dengan urutan parameternya 


"""

print(f"""{muiz.nama}
{muiz.umur}
{muiz.jurusan}""")

"""

kalo saya jalankan maka akan muncul seperti ini
nama
18                                            
teknik informatika 


nah lalu kenapa ketika saya ingin mengisi properti dan valuenya 
harus ada parameter self

dan pada saat mengisi valuenya 
kenapa kita harus menggunakan notasi

self.nama = nama

kenapa tidak langsung seperti ini 
nama = nama

kita akan bahas mengenai apa itu self

"""
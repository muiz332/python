"""

nah kita juga bisa menambahkan method method pada 
class tersebut

"""

class mahasiswa:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    def sapa(self):
        return f'hai nama saya {self.nama} umur saya {self.umur}'


muiz = mahasiswa('nama',18)

"""

ketika kita ingin mengakses properti yang ada didalam classnya 
dan ingin menggunakannya didalam methodnya 

maka kita kasih parameter self (sesuai dengan nama yang ada pada init)
lalu panggil propertinya apa

kalo kalian ingin memasukkan nilai pada parameter sapa 
ya tinggal kasih nama parameter lagi setelah self

"""

print(muiz.sapa())

"""

kalo saya jalankan akan muncul
hai nama saya nama umur saya 18


"""



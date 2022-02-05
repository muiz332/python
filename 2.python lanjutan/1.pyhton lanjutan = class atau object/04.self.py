# self parameter


"""

apa itu self parameter?
self parameter adalah sebuah parameter yang merepresentasikan 
class yang dibuat

maksutnya gimana?

sebelum itu kenapa kita harus menggunakan self?
kenapa tidak ditulis seperti pada saat kita membuat class biasa

pada bagian intro class
pada saat mengisi valuenya kan nulisnya begini

nama = 'muiz'

kenapa kita harus menggunakan self untuk mengisi valuenya 

misalnya ketika saya punya class yang namanya mahasiswa

"""


# class mahasiswa:
#     def __init__(self,nama,umur):
#         nama = nama
#         umur = umur


# muiz = mahasiswa('muiz',18)
# print(muiz.nama)

"""

kalo kita jalankan maka akan eror
kenapa seperti itu

karena variable nama itu hanya milik function initnya saja
bukan milik class / object mahasiswanya 

khusus untuk init tidak bisa dijadikan nama method

jadi kita butuh akses ke object yang bersangkutan 
dalam hal ini adalah mahasiswa

jadi ini sama saja dengan seperti ini 


""" 

class tes:
    nama = 'muiz'
tes.umur = 18

print(tes.umur)

"""

jadi ketika kita ingin mengisi classnya dengan 
properti baru yang berada diluar classnya 

kita bisa tulis
nama objectnya kemudian titik nama propertinya 
diisi dengan valuenya


nah sama seperti itu juga kalo kita ingin mengisi 
properti yang ada didalam fungsi init

kita masukkan ke class mahasiswa 
jadi kita butuh akses ke classnya

nah gimana cara aksesnya?
kalian bisa tulis self pada parameter pertama 
harus parameter pertama ya tidak bisa parameter selain itu

pada fungsi init
kalian bisa rubah namanya menjadi apapun

kalo didalam javascript itu this ya

isinya adalah object yang bersangkutan


"""

class mahasiswa:
    def __init__(this,nama,umur):
        # kita butuh akses ke objectnya 
        # parameter pertama itu adalah akses ke objectnya pada fungsi init

        this.nama = nama

        # ini bacanya sama saja gini
        """
        
        tes.nama = nama
        jadi kita panggil objectnya lalu titik
        nama propertinya

        lalu diisi dengan apa?
        nah disini isinya adalah sesuai dengan apa yang dimasukkan kedalam kurung pada 
        objectnya 
        """

        this.umur = umur



muiz = mahasiswa('muiz',18)

print(muiz.nama)

"""

kalo kita jalankan sama saja ya

lalu kalo misalkan kita ingin mengisi propertinya diluar 
objectnya apa bisa?

ya bisa kita coba ya 

nah sekarang objectnya itu muiz
karena kita sudah assignment muiz sebagai class mahasiswa 

"""

muiz.jurusan = 'teknik informatika'

print(muiz.jurusan)

"""

kalo kita jalankan sama ya 
jadi begitu untuk self parameter ini 



"""
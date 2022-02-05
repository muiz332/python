# membuat class

"""

nah untuk membuat class kita menggunakan keyword yang namanya

dan didalamnya ada pasangan properti dan value
dan juga kita dapat memasukkan method

untuk sintaxnya seperti ini 

class nama clasnya:
    properti = valuenya


"""

class siswa:
    nama = 'muiz'



"""

nah untuk mengakses nilai yang ada didalam class siswa
kita dapat menuliskan seperti ini 

nama classnya titik nama properti atau method yang mau diakses

"""

coba = siswa.nama
print(coba)

"""

kalo saya jalankan maka akan muncul 
muiz

nah itu kalo satu properti
gimana kalo banyak properti

"""


class tes:
    nama = 'husain'
    umur = 18
    
    def sapa():
        return f'halo nama saya {tes.nama} umur saya {tes.umur}'

print(tes.sapa())


"""

jadi seperti itu ya kalo misalnya 
kita membuat class  yang memiliki banyak properti dan method


kelihatannya ini sudah bener
tapi bagaimana kalo misalnya data nya banyak

maksutnya itukan yang saya masukkan datanya hanya seorang saja

lalu bagaimana ketika kita memiliki banyak orang 
misalnya dalam lingkup mahasiswa

tiap tiap mahasiswa itu pasti memiliki
nama kelas nim dan jurusan

ketika kita memiliki banyak data dari tiap tiap
mahasiswa maka kita tidak bisa membuat class dengan seperti itu


dan contoh class yang diatas adalah class yang paling sederhana
dan yang paling jarang digunakan direal life


tidak mungkin kita membuat class yang namanya mahasiswa
dengan tiap tiap properti yang berbeda beda pada masing masing mahasiswa

misalnya
kita buat properti yang namanya nama1 yang disi dengan muiz
nama2 yang diisi dengan hasain

kalo seperti itu apa bedanya dengan kita membuat variable tadi?


nah disitulah kita membutuhkan sebuah fungsi yang namanya __init__()


"""
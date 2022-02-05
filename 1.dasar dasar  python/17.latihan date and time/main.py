"""

nah dimateri kali ini kita akan membahas mengenai date and time ya 

untuk latihan kali ini kita akan bikin program untuk menghitung umur

cara untuk memanggil library datetime kita gunakan import

nah fungsi import kita dapat memanggil file yang terpisah
dengan cara kita tulis
import namaFile 

nanti dia akan mengembalikan object 
kalo misalnya didalam file yang dipanggil itu memiliki sebuah variable nama

kalo kita ingin memanggilnya kita tinggal tulis

import namaFile
print(namaFile.nama)

kalo kita mau mengganti nama variable dari file yang dipanggil 
kita bisa tulis begini

import namaFile as fil
print(fil.nama)

nah sekarang kita coba memanggil library datetime yang ada pada pythonya 

"""

import datetime as dateTm

hari = dateTm.date.today()
print(hari.strftime('%A'))

# atau kalian bisa tulis begini

from datetime import date
"""

artinya dari library date time saya ambil datenya saja
kalo yang atas kan ambil librarynya 

"""

hari = date.today()
print(hari.strftime('%A'))


"""

nah jadi bacanya kita panggil file namanya datetime sebagai dateTm
lalu kita buat variable hari yang isinya

file dateTm lalu kita panggil sebuah object didalamnya namanya date 
didalam object date kita panggil lagi sebuah method yang namanya today()

kalo kita jalankan maka nanti akan memunculkan tahun bulan dan tanggal sekarang


nah untuk object didalam datetime ini ada beberapa ya 
date
time
timedelta
datetime
tzinfo
timezone

nah untuk method methodnya dari sebuah object diatas kalian bisa baca documentation datetimenya ya

"""

# membuat waktu

# tanggal = dateTm.date(2003,2,16)
# print(tanggal)


# menampilkan hari
# tanggal = dateTm.date(2003,2,16)
# print(f"{tanggal:%A}")


# print('hitungUmur'.center(40,'='))

# tanggal = int(input(f"""masukkan tanggal: """))
# bulan = int(input(f"""masukkan bulan  : """))
# tahun = int(input(f"""masukkan tahun  : """))


# lahir = dateTm.date(tahun, bulan, tanggal)
# print(f"tanggal lahir anda adalah {lahir}")
# print(f"hari {lahir:%A} bulan {lahir}")

# hariIni = dateTm.date.today()

# hari = (hariIni - lahir).days
# umur = hari // 365
# bulan = hari % 365 // 30
# hari = hari % 365 % 30

# print(f"umur {umur} bulan {bulan} hari {hari}")
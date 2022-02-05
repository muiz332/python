"""

nah kali ini kita akan belajar mengenai format string

nah misalnya kita punya beberapa string seperti ini 

"""
nama = 'muiz'
umur = 18

salam = 'halo nama saya ' + nama + ' saya berumur ' + str(umur) + '\n'
print(salam)

"""

nah kalo saya jalankan maka akan muncul halo nama saya muiz
tapi problemnya kita harus menggabung gabungkan tulisan dengan variable menggunakan 
operator konkatenasi

lalu ada cara yang lebih simple gak tanpa harus menggabung gabungkan string dengan variable?

kalo didalam javascript ada yang namanya template string atau string literal
kalo didalam python itu ada yang namanya formating 


nah dengan menggunakan formating kita bisa memasukkan sebuah variable atau ekspresi kedalam string tanpa harus kita gabungkan dengan syarat menggunakan tanda kurung kurawal buka dan tutup

"""

# formating string
print('string'.center(10,'='))

nama = 'hasan'
salam = f'selamat malam {nama}\n'
print(salam)

"""

jadi sebelum kita buat formatingnya kita harus tulis dulu huruf f sebelum stringnya
kalo kita mau memasukkan sebuah variable kita tinggal bikin kurung kurawal buka dan tutup
lalu masukkan variablenya didalamnya 

nah lalu bagaimana kalo type data yang lain
kan sebelumnya kita harus mengcesting dulu ya sebelum menggabungkan kedalam string

sekarang kita coba bagaimana kalo type data yang lain

"""



# boolean

print('boolean'.center(15,'='))

nama = 'muiz'
kuliah = True
salam = f'nama saya {nama} kuliah = {kuliah} \n'
print(salam)

"""

kalo sebelumnya kita harus mengkesting dulu menjadi string 
kalo menggunakan formating itu tidak perlu ya 

"""

# float

print('intejer'.center(15,'='))

nama = 'muiz'
umur = 18.5
salam = f'halo nama saya {nama} saya berumur {umur} tahun \n'
print(salam)

# intejer

print('intejer'.center(15,'='))

nama = 'hasan'
umur = 19
salam = f'nama saya {nama} saya berumur {umur:d}\n'
print(salam)

"""

nah kalo intejer kita harus menambahkan tanda titik dua dan d
:d

setelah nama variablenya 
kalo kalian tidak kasih sebenarnya tidak apa apa 
tapi kalo kalian tambahkan :d ketika type datanya float maka akan eror

"""

# bilangan ribuan
print('ribuanAwal'.center(16,'='))
angka = 2000
tampil = f'angka = {angka} \n'
print(tampil)


"""

nah kalo kita jalankan maka akan tampil angka = 2000
biasanya kalo ribuan itu kan ada komanya ya dibelakang angka ribuannya 

harusnya 2,000
caranya kita tinggal tambahkan tanda titik dua dan koma setelah nama variablenya 

{angka:,}

"""
print('ribuanAkhir'.center(17,'='))
angka = 2000
tampil = f'angka = {angka:,} \n'
print(tampil)

"""

nah kalo kita jalankan maka akan tampil ya 2,000
kalo angkanya jutaan bagaimana? sama saja 

nanti dia akan secara otomatis menambahkan sendiri komanya 


"""

# bilangan desimal

print('desimal'.center(15,'='))

angka = 2000.56834
tampil = f'angka = {angka}'
print(tampil)

"""

nah sekarang pertanyaannya bisa gak kita menam pilkan 2 saja dibelakang koma 3 atau 1 dibealang koma ?
bisa ya 

nah kalian bisa tulis seperti ini

"""
angka = 2000.56834
tampil = f'angka = {angka:.2f}\n'
print(tampil)

"""

nah setelah variablenya kita tulis :.2f
maksutnya bagaimana?

setelah ketemu titik ambil dua digit setelah titik
dan f itu untuk foatnya ya 

maka yang tampil akan 2 digit setelah tanda titik 

"""


# leading zero

print('leading zero'.center(20,'='))

angka = 2000.56834
tampil = f'angka = {angka:.3f}'
print(tampil)

"""

nah kita kan punya 3 angka dibelang koma ya 
lalu totalnya dari depan sampai belakang itu 8 

nah kita bisa tulis angka 8 sebelum titik

"""
angka = 2000.56834
tampil = f'angka = {angka:8.3f}'
print(tampil)

"""

kalo kita tambahin 1 jadi 9 misalnya apa yang akan terjadi 

"""
angka = 2000.56834
tampil = f'angka = {angka:9.3f}'
print(tampil)

# angka = 2000.568
# angka = 2000.568
# angka =  2000.568

"""

nah maka hasilnya akan menggeser kebelankang 1 kali
lihat ada spasi didepan 2
itu berarti totalnya ada 9

nah kalo kita tambahin 0 didepan 9

"""

angka = 2000.56834
tampil = f'angka = {angka:09.3f}\n'
print(tampil)

"""
angka = 02000.568

maka dia akan mengisi tempat yang kosong itu dengan angka 0


"""

# menampilkan tanda + dan -

print('menampilkan tanda'.center(20,'='))

plus = 10
minus = -10
tampil = f"plus {plus:+d} minus {minus}"
print(tampil)

"""

nah kalo yang min itu kan langsung muncul 
kalo yang plus itu tidak muncul 
cara munculinnya kita tinggal tambahkan tanda :+d

kalo yang d itu tergantung type datanya ya 

kalo kita jalankan 

plus +10 minus -10

nah yang plus akan muncul tandanya 
kita juga bisa bikin begini 

"""

plus = 10.756
minus = -10
tampil = f"plus {plus:+.2f} minus {minus}\n"
print(tampil)



# memformat persen
print('presen'.center(19,'='))

presentase = 0.899
tampil = f'persentase {presentase:%}'
print(tampil)

"""
persentase 89.900000%

nah hasilnya akan seperti itu
lalu gimana kalo kita mau mengambil 2 angka setelah koma/
gampang saja tinggal tulis begini


"""

presentase = 0.899
tampil = f'persentase {presentase:.2%}\n'
print(tampil)

"""

kalo kita jalankan hasilnya 
persentase 89.90%

"""

# melakukan operasi aritmatika

print('operasi aritmatika'.center(30,'='))

angka = 100
tampil = f'{angka} dikali 10 hasilnya {angka * 10:,}\n'
print(tampil)

"""

seperti dijavascript ya kita bisa menambahkan sebuah ekspresi didalam formatingnya 

"""


# format angka lain binary oktal hex

print('format angka lain'.center(30,'='))

angka = 200
binary = bin(angka)
oktal = oct(angka)
hexsa = hex(angka)
print(binary)
print(oktal)
print(hexsa)
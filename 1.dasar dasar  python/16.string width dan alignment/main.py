"""

nah kali ini kita akan bahas mengenai string width dan alignment



"""
nama = 'muiz'
umur = 18
tinggi = 170.5
nomorSpatu = 42

# string

print('dataString'.center(20,'='))

dataString = f'nama saya {nama} umur {umur} tahun tinggi {tinggi} nomor sepatu {nomorSpatu}\n'
print(dataString)


# string multiline dengan menggunakan \n
print('multiline'.center(20,'='))

dataString = f'nama saya {nama} \numur {umur} tahun tinggi {tinggi} \nnomor sepatu {nomorSpatu}\n'
print(dataString)

"""

nah kita bisa melakukan multiline dengan cara  menambahkan escape karakter \n

"""


# string multiline dengan menggunakan kutip 3

print('kutip3'.center(20,'='))

data = f"""nama saya {nama}
saya berumur {umur}
tinggi saya  {tinggi}
nomor sepatu saya  {nomorSpatu}\n
"""

print(data)

# mengatur lebar


print('mengaturLebar'.center(21,'='))

data = f"""
nama saya          {nama:>5}
saya berumur       {umur}
tinggi saya        {tinggi}
nomor sepatu saya  {nomorSpatu}\n
"""

print(data)

"""

nah kita bisa melakukan rata kanan ya 
jadi kita tinggal tambahkan saja divariable yang kita mau rata kanan

kita tambahkan :>5 
nah untuk 5 ini karakter atau kata yang paling panjang disebelah kanan

kalo kalian tambahkan misalnya 10 maka dia akan menggeser kekanan lagi


"""


print(" mengatur spasi ".center(30,'='))

"""

:<12     // lebih keci, stringnya dibagian kiri dan spasinya dikanan
:>12     // lebih besar, string dibagian kanan dan spasinya dikiri
:^12    // tanda topi, stringnya ditengah dan spasinya dikiri dan kanan

"""


print('{:<12} selamat'.format('muiz'))
print('{:>12} selamat'.format('muiz'))
print('{:^12} selamat'.format('muiz'))

"""

kita atur panjangnya 12 ya 
jadi panjang 12 kalo misalkan kita mau atur yang lebih kecil

maka 12 dikurangi panjang string 
kalo mau menambahkan spasinya tinggal ganti angkanya saja 

"""
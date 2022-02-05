"""
kali ini kita akan belajar mengenai cesting type data

apa itu cesting? 
cesting adalah merubah suatu type data ketype data yang lain

kalo kita mau merubah type data itu ada yang namanya operator cesting

misalnya saya mau mengubah intejer menjadi floot

"""
print('=====intejer=====')

angka = 9

# nah untuk mengubah type data dari intejer ke float kita menggunakan sebuah function yang namanya float() 
# lalu kita masukkan argumentnya apa yang mau diubah 

ke_float = float(angka)

print(ke_float, "adalah type data ", type(ke_float))

# intejer ke string

ke_string = str(angka)
print(ke_string, "adalah type data ", type(ke_string))


# intejer ke boolean

ke_bol = bool(angka)
print(ke_bol, "adalah type data ", type(ke_bol))

# untuk boolean kalo nilainya 0 itu dia akan bernilai false





print('=====float=====')

d_float = 9.8

# nah untuk mengubah type data dari float ke intejer kita menggunakan sebuah function yang namanya float() 
# lalu kita masukkan argumentnya apa yang mau diubah 

ke_int = int(d_float)

print(ke_int, "adalah type data ", type(ke_int))

# intejer ke string

ke_string = str(d_float)
print(ke_string, "adalah type data ", type(ke_string))


# intejer ke boolean

ke_bol = bool(d_float)
print(ke_bol, "adalah type data ", type(ke_bol))

# untuk boolean kalo nilainya 0 itu dia akan bernilai false


print('=====boolean=====')

d_boolean = True

# nah untuk mengubah type data dari float ke intejer kita menggunakan sebuah function yang namanya float() 
# lalu kita masukkan argumentnya apa yang mau diubah 

ke_int = int(d_boolean)

print(ke_int, "adalah type data ", type(ke_int))

# intejer ke string

ke_string = str(d_boolean)
print(ke_string, "adalah type data ", type(ke_string))


# intejer ke boolean

ke_float = float(d_boolean)
print(ke_float, "adalah type data ", type(ke_float))





print('=====string=====')

d_string = '10'

# nah untuk mengubah type data dari string ke intejer 
#nah kalo string ke intejer maka akan eror tapi kalo stringnya hanya angka saja misalnya string 10 maka akan bisa

ke_int = int(d_string)

print(ke_int, "adalah type data ", type(ke_int))

# intejer ke string

ke_bolean = bool(d_string)
print(ke_bolean, "adalah type data ", type(ke_bolean))

# kalo ingin hasilnya menjadi false kita kosongkan saja stringnya 


# intejer ke boolean

ke_float = float(d_string)
print(ke_float, "adalah type data ", type(ke_float))

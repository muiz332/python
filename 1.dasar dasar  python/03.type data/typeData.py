"""
nah untuk type data ini ada beberapa misalkan 
yang pertama kita coba type datanya intejer

jadi saya bisa tulis begini 

"""

intejer = 10
# lalu saya tampilkan
print(intejer , "adalah type data intejer")

"""
atau kalian bisa mengechecknya 
kalo didalam javascript itu kita gunakan yang namanya typeof()

kalo dipython itu ada fungsi yang namanya type()
kita coba

"""

print(intejer, "memiliki type data ", type(intejer))


"""
nah yang selanjutnya ada type data float 
float yaitu type data angka desimal
contoh

"""

float = 1.7
print(float, "memiliki type data ", type(float))

"""
lalu ada type data yang namanya string 
yaitu type data yang isinya tulisan biasa didalam tanda kutip 

bisa kutip satu atau dua
contoh

"""

string = "muiz"
print(string, ' ini adalah type data ', type(string))

"""
dan yang terakhir adalah boolean
yaitu type data true atau false

"""

bolean = True
print(bolean, "adalah type data ", type(bolean))

bolean2 = False
print(bolean2, "adalah type data ", type(bolean2))


"""
type data khusus bilangan komplexs
contoh

"""

komplex = complex(4,4)
print(komplex, ' ini adalah type data ', type(komplex))



"""

type data dari bahasa C
karena python itu dibikin dari bahasa C maka kita bisa ambil type datanya 
nah misalnya kita mau ambil type data yang ada didalam bahasa C

caranya kita ambil dulu librarynya 
kita bisa tulis begini

"""

from ctypes import c_double

#bacanya dari ctypes kita import type data yang namanya c_double

data_c_double = c_double(10.7)
print(data_c_double, ' ini adalah type data ', type(data_c_double))
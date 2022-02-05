"""

sekarang kita akan membahas mengenai parameter dan argument

apa itu argument?
argument adalah sebuah nilai yang kita masukkan kedalam tanda kurung ketika functionnya dipanggil

misalkan saya punya function 


"""
def salam(n):
    print(n)

salam('muiz')

"""

nah ketika saya masukkan nilai yang type datanya string kedalam function pada saat function itu dipanggil 

maka itu disebutnya argument
jadi nilai yang masuk kedalam tanda kurung itu ada argument


sedangkan parameter adalah nilai yang didapat dari argument

contoh 

"""

def nama(nama):
    print(nama)

nama('hasan')

"""

jadi nilai yang ada didalam argument itu kita kirimkan keparameter 
parameter itu adalah sebuah variable yang hanya bisa diakses didalam function saja

dan nilai yang ada didalam parameter itu nanti dapat kita proses didalam function bodynya 


"""


"""

jumlah argument dan parameter itu harus sama 

kalo misalkan parameter lebih banyak daripada argument amka akan eror

kalo misalkan argumentnya lebih banyak dari pada parameter 
maka nilainya tidak akan bisa masuk kedalam function


selanjutnya kalo misalkan kalian tidak tahu berapa argument yang akan diberikan 
maka tambahkan tanda * pada parameternya 


"""


def arg(*nilai):
    print(nilai)
arg(1,'nama','aku')


"""

kalo saya print nilainya maka dia akan menjadi array yang jenisnya tuples
jadi kalo misalkan kalian ingin menggunakan method lists ya tinggil ubah saja 
menjadi list


nah kita juga bisa menambahkan default parameter ya 

"""


def nama(nama = 'tidak bernama'):
    print(nama)

nama()



"""

nah ketika anda memiliki alasan tertentu anda membuat function tanpa isi
kalian dapat menambahkan sintax pass didalam function untuk menghindari eror


dan jangan lupa function dipython juga bisa melakukan rekursif


"""




# mengisikan secara acak nilai pada argument

"""

mengisikan sesuai parameternya 
jadi kita bisa mengisikan parameternya meskipunt kita masukkan niainya tidak berurut

caranya kita assignment parameter pada saat menginputkan nilainya
contoh

"""

def indentitias(nama,alamat,umur):
    print(f'{nama} {alamat} {umur}')


indentitias(alamat = 'banyuwangi', nama='muiz',umur=18)


"""

jadi meskipun kita mengisikan datanya tidak urut 
tidak apa apa 

"""
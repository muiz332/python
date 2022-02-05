"""

dimateri kali ini kita akan belajar mengenai  pengulangan 
jadi dimateri kali ini yang kita bahas adalah mengenai for

apa itu for?
for adalah sebuah statement yang digunakan untuk mengulang suatu intruksi yang sama 


sintax

for kondisi:
    aksi



"""

# misalnya mau melooping array / list

angka = [1,2,3,4]

for i in angka:
    print(i)

"""

nah untuk looping pada python ini mirip seperti for of pada javscript

jadi variable i disini dia merepresentasikan tiap tiap nilai pada array

yang membedakan hanya untuk dipython itu pakai for in kalo dijavascript for in untuk melooping properti pada object


maka dia akan melooping sebanyak nilai /  element yang ada didalam array


"""


# menggunakan for dan range'

for i in range(5):
    print(i)
print('batas')

"""

kalo kita jalankan maka loopingnya akan dimulai dari 0 dan diakhiri dari 4
nah bagaimana kalo kita ingin memulainya dari 1

function range ini memiliki 2 paramter 
paramter 1 = dimulai dari angka berapa
parameter 2  = lingkup atau batasan loopingnya sampai berapa

"""

for i in range(2,5):
    print(i)

print('batas')

"""

maka nanti loopingnya akan dimulai dari angka 2 sampai 4

"""


# melooping string

nama = 'muiz'
for huruf in nama:
    print(huruf)

"""

nah jadi kita bisa melooping karakter atau string menggunakan for in ini ya 

nah untuk for ini hanya bisa melakukan looping pada string array 
dan angka tapi dari yang terkecil sampai terbesar

dan kalo angka incrementnya 1 jadi tiap pengulangannya nilai awalnya ditambah dengan 1

nah gimana kalo kita ingin meloopingnya dari angka terbesar ke terkecil
dan juga mengatur pengambahan / pengurangan terhadap nilai awalnya ?

nah untuk kasus seperti itu kita akan menggunakna while
jadi dimateri selanjutnya kita akan membahas mengenai while

"""
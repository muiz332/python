"""

nah sekarang kita akan masuk kedalam materi lambda

apa itu lambda?
lambda adalam sebuah small anonymous atau istilahnya function yang disimpan didalam argument

lambda hanya dapat memiliki satu exspression didalamnya 

"""

# membuat lambda

salam = lambda nama : f'selamat malam {nama}'
print(salam('muiz'))

"""

nah jadi sintaxnya 
keywordnya lambda lalu parameternya kemudian : dan kemudian expressinya 
jadi expressionya cuma satu baris ya 


"""

# lebih dari satu parameter 

siswa = lambda a,b,c : f'{a} {b} {c}'
print(siswa('muiz','husain','hasan'))



# kenapa sih kita menggunakan lambda?

"""

lambda bisa kita gunakan untuk membuat fungsi anonim didalam fungsi yang lain 
contoh

"""

def sapa (n):
    return lambda nama : f"{n} {nama}"


nama = sapa('selamat pagi')
print(nama('muiz'))

# Gunakan fungsi lambda ketika fungsi anonim diperlukan untuk waktu yang singkat
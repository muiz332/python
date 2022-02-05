# continue dan pass

"""

dimateri kali ini kita akan belajar mengeni control flow

jadi disini ada tiga ya

yaitu continue pass dan break



nah dimateri kali ini kita akan bahas mengenai continue dan pass dulu ya 
oke jadi yang paling gampang disini ada pass

kita coba dulu yang pass ya 


jadi pass itu fungsinya adalah sebagai dummy / contoh dan dia tidak akan dieksekusi

nah maksutnya gimana?
misalkan saya punya loop seperti ini 


"""

# angka = 0
# while angka < 5:
#     angka += 1

#     if angka == 3:
#         print('oke')

#     print(angka)


"""

nah ketika dia ketemu dengan angka 3 maka dia akan mengeprint 
oke

kita coba jalankan
1
2
oke
3
4
5
nah bener ya 

nah kalo misalkan printnya yang ada didalam if itu saya hilangin
otomatis statement yang ada didalam if itu kosong ya 

maka dia akan eror
untuk menangani hal tersebut kita pakai pass

jadi didalam ifnya itu kita kasih pass biar tidak error dan sebagai dummy atau contoh saja
dan dia tidak akan dijalankan

"""

angka = 0
while angka < 5:
    angka += 1

    if angka == 3:
        pass # ini tidak akan dieksekusi

    print(angka)

"""

kita coba
ketemu 3 maka masuk ke ifnya 
ada pass nih maka tidak dihalanin apa apa 

jadi begitu ya untuk pass ini 

ketika nanti kita bikin fungsi 
seperti ini 


"""

def coba():
    pass

"""

kalo kita tulis pass maka dia isinya kosong
begitu pula kalo kita nanti belajar mengenai class

"""

class mahasiswa:
    pass

"""

ya maka tidak akan terdefinisi juga
alias isinya kosong

"""
print(mahasiswa)

"""

jadi seperti itu penggunaan dari pass ini 
mudah mudahan kalian paham

"""

# continue

"""

oke sekarang gini 
kalo continue itu 

ketika kita membuat loop
maka ketka kita ketemu dengan continue maka 
dia akan melanjutkan loop berikutnya 
meskipun ada beris perintah dibawahnya 

"""

for i in range(5):
    if i == 3:
        print('oke')
        continue # meloncat ke loop selanjutnya 

    print(i)




"""

kita lihat looping diatas ya 
nah yang pertama itu ketika i nya sama dengan 3

nah ketika inya itu sama dengan 3 maka saya print oke
ketemu keyword continue

nah maka print i yang isi dari i itu adalah 3
tidak akan dijalankan 

artinya ketika ketemu dengan keyword continue 
dia akan melanjutkan looping selanjutnya 
tanpa menjalankan statement yang ada dibawah continue

nah jadi looping diatas itu seperti if else ya 
elsenya itu semua program yang ada dibawah if

tapi dengan continue kita juga bisa menskip perintah dibawahnya
dan melanjutkan loopingnya 


untuk lebih detil lagi seperti ini 

"""

for i in range(10):

    print(i)
    continue
    print('oke')


"""

nah untuk contoh looping ini 
ketika saya jalankan maka akan muncul 0-9

lalu print okenya kemana?
seperti yang sudah saya bilang tadi 

ketika ketemu dengan keyword continue
maka statement yang ada dibawah continue itu tidak akan dijalankan

dia akan mengskip statement dibawahnya dan melanjutkan loopingnya 


jadi seperti itu untuk continue ya 
mudah mudahan kalian paham

oke sampai disini tutorialnya see you next materi
keep coding stay awesome dan bay



"""
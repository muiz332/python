"""

dimateri kali ini kita akan belajar pengkondisian else if
jadi elseif ini digunakan ketika kalian memerlukan lebih dari satu kondisi

"""


# nama = input('masukkan namamu: ')

# if nama == 'muiz':
#     print('selamat pagi')
# elif nama == 'husain':
#     print(f"halo {nama}")
# else:
#     print('gak kenal')

# print('selesai')


angka1 = int(input('masukkan angka: '))
angka2 = int(input('masukkan angka lagi: '))
print('kata kunci:  kali, bagi, tambah, kurang modulus, floor devision')
operator = input('mau diapain dua angka tersebut? ')

if operator == 'tambah':
    print(angka1 + angka2)
elif operator == 'kali':
    print(angka1 * angka2)
elif operator == 'bagi':
    print(angka1 / angka2)
elif operator == 'modulus':
    print(angka1 % angka2)
elif operator == 'floor devision':
    print(angka1 // angka2)

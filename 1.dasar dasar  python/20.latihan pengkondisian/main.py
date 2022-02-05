# latihan pengkondisian 

# kalkulator sederhana 

import math 


print('kalkulator'.center(30,'='))
angka1 = float(input('masukkan angka: '))
angka2 = float(input('masukkan angka: '))
print('operator: x, /, +, -')
operator = input('masukkan operator untuk dua buah angka tersebut: ')
if angka1 % 1 == 0:
    angka1 = math.floor(angka1)

if angka2 % 1 == 0:
    angka2 = math.floor(angka2)

if operator == 'x' or operator == '*':
    print(f"{angka1} x {angka2} = {angka1 * angka2}")
elif operator == '/':
    print(f"{angka1} / {angka2} = {angka1 / angka2}")
elif operator == '+':
    print(f"{angka1} + {angka2} = {angka1 + angka2}")
elif operator == '-':
    print(f"{angka1} - {angka2} = {angka1 - angka2}")
else:
    print('masukkan operator yang benar!')

print('terima kasih')
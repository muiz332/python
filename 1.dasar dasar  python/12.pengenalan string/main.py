"""

nah kali ini kita akan belajar mengenai pengenalan string

nah lalu bagaimana cara membuat string

nah string itu adalah kumpulah karakter yang berupa text
contoh

"""

string = 'ini adalah string'
print(string)


# 1. membuat string dengan menggunakan single quote

"""

apa itu single quote? single quote itu mengunakan kutip satu


"""

string = 'menggunakan single quote'
print(string)


# 2. dengan menggunakan double quote atau kutip 2

string = "menggunakan double quote"
print(string)

print('"hallo apa kabar "')
print("'hallo apa kabar'")


# nah didalam python kita juga bisa membuat escape karakter seperti jaascript ya 

"""

\'
\"
\n LF line feed biasa gigunakan untuk mac linux
\t
\b
\\
\r  CR carrige return commodore
\r\n CRLF line feed carrige return windows

"""

print('ini adalah hari jum\'at')
print("coba \"sekarang kamu duduk\"")

print('ini adalah enter\nenter')
print('\tini adalah tab')
print('ini adalah \bbackspace')


print('ini adalah r \rini kamu')

print('coba \r\nkedua')



# string literal atau row
#contoh

print('C:\new folder')

# nah kalo kalian jalankan maka dia akan mengenter jadi akan salah
# cara mengatasinya kita tinggal tambahkan backslash lagi

print('C:\\new folder')

# itu kalo satu kalo ada banyak nah cara yang efektif adalah dengan menggunakan raw string


# menggunakan raw string

# kita tinggal tambahkan didepan dengan tanda r

print(r"C:\new folder")


# nah jadi kalian tidak perlu memikirkan tandanya  tinggal tulis saja semuanya 
# jadi kalo kalian masukkan \n \t \\ \r itu akan dianggap sebagai string



"""

nah kita juga bisa membuat multiline literal string
jadi seperti membuat komentar ya 

"""

print("""
nama :muiz 
kelas: sp1.1
jurusan: teknik informatika
""")


"""

nah selanjutnya kiga juga bisa menggabungkan miltiline dengan raw string

"""


print(r""""
nama :muiz 
kelas: sp1.1 \ stikom
jurusan: teknik informatika
""")

"""

nah maka si slashnya itu akan ditampilkan

"""
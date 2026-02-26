nama = "Budi"
umur = 90

pesan = "Nama: " + nama + ", Umur: " + str(umur)\

print(nama)
print(pesan)
print("huruf pertama nama:", nama[0])
print("huruf kedua nama:", nama[1])
print("huruf ketiga nama:", nama[2])
print("huruf pertama nama dari belakang:", nama[-1])
print("huruf kedua nama dari belakang", nama[-2])
print("huruf ketiga nama dari belakang", nama[-3])
print("panjang kalimat pesan di atas:", len(pesan))

print("\n")

nama = "Python"
print(nama[0:7])
print(nama[1:4])
print(nama[3:5])

print("\n")

nama = "Alexa D"

print(nama)
print("huruf besar semua:", nama.upper())
print("huruf kecil semua:", nama.lower())
print("huruf besar awal setiap karakter:", nama.title())
print("huruf besar awal karakter:", nama.capitalize())

print("\n")

nama1 = "Chelsea Ka"
nama2 = " Asep Jajang "

print("menghilangkan spasi/karakter kosong:", nama2.strip())
print("mengganti bagian tertentu dari:", nama1, "ke", nama1.replace("Ka", "Xhe"))
print("berapa kali text muncul:", nama1.count("C"))
print("mencari posisi text muncul:", nama1.find("Ka")) 

print("\n")

kalimat = "Baris pertama\nBaris kedua"
print("contoh spasi:", kalimat)

data = "Nama:\tAlice\nUmur:\t99"
print("contoh tab:", data)

path = "C:\\Users\\Ujang\\Documents"
print("contoh backslash:", path)

kalimat1 = "Ujang berkata \"Allow\" kepada aku"
print("contoh:", kalimat1)

kalimat2 = 'I\'m Beautiful'
print("contoh:", kalimat2)

print("\n")

nama = "Hamud"
umur = 75
kota = "Djekardah"

# f string
profil1 = f"hi, nama ak {nama}, my umur {umur}, and my kota {kota}"
print(f"contoh with f string: {profil1}")

# compare

profil2 = "hi, nama ak " + nama + ", my umur " + str(umur) + ", and my kota " + kota
print("contoh tanpa f string:", profil2)

print("\n")

# f string dapat  mengeksekusi langsung
harga = 150000
jumlah = 90

total = f"total: Rp{harga * jumlah}"
print(total)

nama = "Ujang Asep"
salam = f"Halo {nama.upper()}!"
print(salam)
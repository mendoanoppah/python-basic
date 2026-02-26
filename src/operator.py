# urutan prioritas operator
# ()
# ** (pangkat)
# *, /, //, % (perkalian, pembagian, pembagian bulat, sisa pembagian)
# +, - (penjumlahan, pengurangan)
# ==, !=, >, <, >=, <= (perbandingan)
# not (bukan)
# and (true keduanya)
# or (true salah satun)


a = 10
b = 3

print("hasil penjumlahan:", a + b) # 13
print("hasil pengurangan:", a - b) # 7
print("hasil perkalian:", a * b) # 30
print("hasil pembagian:", a / b) # 3.333
print("hasil pembagian bulat:", a // b) # 3
print("hasil sisa pembagian:", a % b) # 1
print("hasil habis dibagi:", 10 % 2) # 0

print("\n")

c = 2
d = 3

print("hasil pangkat:", c ** d) # 8

print("\n")

n = 99

print("n awal:", n) # 99

n += 1
print("n ditambah 1:", n) # 100

n -= 2
print("n dikurangi 2:", n) # 98

n *= 3
print("n dikali 3:", n) # 294

n /= 4
print("n dibagi 4:", n) # 73.5

n **= 5
print("n dipangkat 5:", n) # 2145046422.09375

n %= 6
print("n sisa pembagian 6:", n) # 0.09375

print("\n")

e = 50
f = 25

print(e > f) # True
print(e < f) # False
print(e >= f) # True
print(e <= f) # False
print(e == f) # False
print(e != f) # True

print("\n")

nama1 = "sahrujang"
nama2 = "siasep"
nama3 = "cecep kasep"
nama4 = "sahrujang"

print(nama1 == nama2) # False
print(nama1 != nama2) # True
print(nama1 == nama3) # False
print(nama1 != nama3) # True
print(nama1 == nama4) # True
print(nama1 != nama4) # False

print("\n")

umur = 39
print(umur > 30 and umur < 40) # True
print(umur < 30 or umur > 40) # False
print(not umur > 30) # False

print("\n")

nama_depan = "Ucup"
nama_belakang = "Wijaya"
print(nama_depan + " " + nama_belakang)

text = "Hello World "
print(text * 3)

bintang = "*"
print(bintang * 10)

kalimat = "aku suka makan ayam pop"
print("aku" in kalimat) # True
print("kamu" in kalimat) # False
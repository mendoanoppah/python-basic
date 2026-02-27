angka = int(input("Masukkan angka: "))

if angka > 0:
  print("Angka positif")

if angka < 0:
  print("Angka negatif")

if angka == 0:
  print("Angka nol")

print("\n")

nilai = int(input("Masukkan nilai: "))

if nilai >= 90:
  print("A")
elif nilai >= 80:
  print("B")
elif nilai >= 70:
  print("C")
elif nilai >= 60:
  print("D")
else:
  print("E")

print("\n")

umur = int(input("Masukkan umur: "))
punya_sim = str(input("Punya SIM? (ya/tidak): "))

if umur >= 17 and punya_sim == "ya":
  print("Boleh mengendarai motor")
else:
  print("Tidak boleh mengendarai motor")

print("\n")

username = str(input("Masukkan username: "))
password = str(input("Masukkan password: "))

if username == "admin":
  if password == "11111111":
    print("Login berhasil")
    print("Selamat datang admin")
  else:
    print("Username atau password salah")
else: 
  print("Username atau password salah")

print("\n")

hari = str(input("Masukan hari: ")).lower()

match hari:
  case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
    print("WEEKDAYS WAKTUNYAA KERJJAAAAAAAAAAAAAAAA")
  case "sabtu" | "minggu":
    print("HAPPY WEEEKKKNDDD YYEYY")
  case _:
    print("Input nama hari tidak valid!")

print("\n")

angkaa = int(input("Masukan angka: "))

# if-else biasa
if angkaa > 0:
  print("Hasil dari if-else biasa: Angka positif")
else:
  print("hasil dari if-else biasa: Angka negatif")

result = "Angka positif" if angkaa > 0 else "hasil dari if-else biasa: Angka negatif"
print("hasil dari operasi ternary:", result)
# Mencari password yang benar dengan batas percobaan
password_benar = "java123"
percobaan = 0
max_percobaan = 5

while percobaan < max_percobaan:
  password = str(input("Masukan password: "))
  percobaan += 1

  if password == password_benar:
    print("Login berhasil.")
    break
  else:
    print("Password salah. Sisa percobaan:", max_percobaan - percobaan)
else:
  print("Terlalu banyak percobaan gagal. Ditolak.")

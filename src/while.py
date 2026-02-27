angka = 0

while angka <= 5:
  angka += 1
  print("angka:", angka)

password = ""
while password != "123":
  password = str(input("Masukan password: "))
  if password != "123":
    print("Salah, masukan password yang benar")
print("PASSWORD BTUL")
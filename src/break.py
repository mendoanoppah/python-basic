# Mini Game tebak angka with brake

angka_rahasia = 55

while True:
  tebakan = int(input("Masukan Angka: "))

  if tebakan == angka_rahasia:
    print("Selamat, Anda berhasil menebak kodenya yey")
    break
  else:
    print("Salah tebakan, coba lagi")
# Mwncari huruf dalam kata

kata = str(input("Masukan kata: "))
huruf_dicari = str(input("Masukan huruf yang ingin dicari: "))

for huruf in kata:
  if huruf == huruf_dicari:
    print(f"Huruf {huruf_dicari}, ditemukan dalam kata.")
    break
else:
  print(f"huruf {huruf_dicari} tidak ditemukan dalam kata.")
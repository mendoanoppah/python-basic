nama = "Javascript"
for huruf in nama:
  print(huruf)

print("\n")

nama = "Typescript"
for index, huruf in enumerate(nama):
  print(index, huruf)

print("\n")

nama = input("Masukan nama: ")
for huruf in nama:
  print("-", huruf)
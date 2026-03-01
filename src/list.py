# list kosong
daftar_kosong = []

# list dengan angka
angka = [1, 2, 3, 4, 5]
print(angka)

# list dengan string
name = ["Agus", "Budi", "Joko"]
print(name)

# list campuran
campuran = ["Rayhan", 100, True, 99.9]
print(campuran)

# mengakses sebuah elemen
buah = ["apel", "jeruk", "nanas", "manggis"]
print(buah[0])
print(buah[1])
print(buah[2])
print(buah[3])

# mengubah warna with index
colors = ["red", "green", "blue"]
print(colors)
colors[1] = "purple"
print(colors)

tools = ["Obeng", "Hammer", "Screwdriver"]
print(tools)

tools.append("Chainsaw")
print(tools)

tools.remove("Obeng")
print(tools)

tools.pop()
print(tools)

del tools[0]
print(tools)

languages = ["England", "Germany", "Arabs"]
print(len(languages))

mix = tools + languages
print(mix)

for language in languages:
  print(language)

for i in range(0, len(languages)):
  print(languages[i])

if "England" in languages:
  print('Ada Bahasa "England"')
else:
  print('gk ada "England"')
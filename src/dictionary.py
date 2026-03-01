# dictionary
siswa = {
  "name": "Ucup",
  "umur": 199,
  "lahir": "Tegal" 
}
print(siswa)

print(siswa["name"])
print(siswa["umur"])
print(siswa["lahir"])

siswa["name"] = "Qila"
print(siswa)

del siswa["umur"]
print(siswa)

for key in siswa:
  print(key, ":", siswa[key])

for key, value in siswa.items():
  print(key, value)
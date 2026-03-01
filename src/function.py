# function
def say_hello():
  print("Hello World!")

say_hello()

def greetings(name):
  print(f"Hallo {name}")

greetings("mamamyo")

def hitung_luas_kotak(panjang, lebar):
  luas = panjang * lebar
  print(f"Jadi luasnya: {luas}")

hitung_luas_kotak(50, 50)

def hitung_luas_lingkaran(radius):
  pi = 3.14159
  luas = pi * radius * radius
  return luas

  

luas1 = hitung_luas_lingkaran(5)
luas2 = hitung_luas_lingkaran(10)

print(f"luas lingkaran radius 5: {luas1}")
print(f"luas lingkaran radius 10: {luas2}")
print(f"total luas: {luas1} {luas2}") 

def sapa(name, greetings="hi"):
  print(greetings, name)

sapa("Kiryu")
sapa("Alok", "hola")
sapa("Trump", "oi")

def intro(name, city, age):
  print(f"name: {name}")
  print(f"city: {city}")
  print(f"age: {age}")
  print("---")

# apropraite order
intro("Yugo", "Djirebon",67)

# nope
intro(city="Bekasie", name="Jude", age=99)

def buat_profil(name, age, kota="Djakarta", job="none"):
  print(f"=== PROFILE {name.upper()} ===")
  print(f"umur: {age} tahun")
  print(f"asalnyo: {kota}")
  print(f"job: {job}")
  print()

buat_profil("Wahyu", 99)
buat_profil("Jokok", 99, kota="Bandoeng")
buat_profil(kota="Bali", name="Dwi", age=90)
buat_profil(kota="Bali", name="Dwi", age=90, job="Java Developer")

def fungsi_test():
  x = 19 # local variable
  print(f"nilai x di dalam fungsi: {x}")

fungsi_test()
# print(x) # error is not defined

# global variable
variable_global_nama = "Andre"

def tampilkan_nama():
  print(f"nama: {variable_global_nama}")

def ubah_nama_tanpa_global_keyword():
  variable_global_nama = "Bob"
  print(f"nama: {variable_global_nama}") # jadinya membuat variable baru

def ubah_nama():
  global variable_global_nama
  variable_global_nama = "Layla" 
  print(f"setelah ubah nama: {variable_global_nama}")

print()
tampilkan_nama()
ubah_nama_tanpa_global_keyword()
ubah_nama()
tampilkan_nama()

def cetak_list(*list):
  for item in list:
    print(item)

print()
cetak_list(1, 2, 3, 4, 5, 100)

def cetak_dict(**dict):
  for key, value in dict.items():
    print(f"{key}: {value}")

print()
cetak_dict(name="Widodo", age=50, city="Garut")

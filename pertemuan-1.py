# ================================================ 
# PERTEMUAN 1: Notebook Pertama Data Science 
# ================================================ 
  
# SEL 1: Output sederhana 
print("Hello, Data Science!") 
print("Selamat datang di mata kuliah Pengantar Data Science!") 
  
# SEL 2: Variabel dan tipe data dasar 
nama       = "Mahasiswa Informatika"     # String 
angkatan   = 2024                         # Integer 
ipk        = 3.75                         # Float 
aktif      = True                         # Boolean 
  
print(f"Nama    : {nama}") 
print(f"Angkatan: {angkatan}") 
print(f"IPK     : {ipk}") 
print(f"Aktif   : {aktif}") 
  
# SEL 3: List dan perulangan 
tools = ["Python", "Google Colab", "Jupyter Notebook", "GitHub"] 
print("\nTools Data Science yang akan kita pelajari:") 
for i, tool in enumerate(tools, 1): 
    print(f"  {i}. {tool}") 
  
# SEL 4: Fungsi sederhana 
def perkenalan(nama, prodi, angkatan): 
    """Fungsi untuk menampilkan perkenalan mahasiswa.""" 
    return f"Hai! Saya {nama} dari {prodi}, angkatan {angkatan}." 
  
hasil = perkenalan("Budi Santoso", "Informatika", 2024) 
print(hasil) 
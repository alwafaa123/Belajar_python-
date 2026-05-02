class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f"Produk: {self.nama} | Harga: Rp{self.harga}"

    def __eq__(self, other):
        return self.harga == other.harga

    def __lt__(self, other):
        return self.harga < other.harga

    def __gt__(self, other):
        return self.harga > other.harga

p1 = Produk("Mouse Gaming", 250000)
p2 = Produk("Keyboard Mekanik", 750000)
p3 = Produk("Mouse Pad", 250000)

print("--- Daftar Produk ---")
print(p1)
print(p2)
print(p3)

print("\n--- Uji Perbandingan ---")
print(f"Apakah {p1.nama} harganya sama dengan {p3.nama}? {p1 == p3}")
print(f"Apakah {p1.nama} lebih murah dari {p2.nama}? {p1 < p2}")
print(f"Apakah {p2.nama} lebih mahal dari {p1.nama}? {p2 > p1}")
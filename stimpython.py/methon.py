class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        luas = self.panjang * self.lebar
        return f"Luas persegi panjang: {luas} cm²"

    def hitung_keliling(self):
        keliling = 2 * (self.panjang + self.lebar)
        return f"Keliling persegi panjang: {keliling} cm"

    @staticmethod
    def info_bangun_datar():
        return " Persegi panjang adalah bangun datar dengan dua pasang sisi sejajar."

kotak_a = PersegiPanjang(10, 5)
kotak_b = PersegiPanjang(20, 10)

print("--- Objek A ---")
print(kotak_a.hitung_luas())
print(kotak_a.hitung_keliling())

print("\n--- Objek B ---")
print(kotak_b.hitung_luas())
print(kotak_b.hitung_keliling())

print("\n--- Static Method ---")
print(PersegiPanjang.info_bangun_datar())
print(kotak_a.info_bangun_datar())
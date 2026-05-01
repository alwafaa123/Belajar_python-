
class Kamera:
    def __init__(self, merk, tipe, resolusi):
        self.merk = merk          
        self.tipe = tipe          
        self.resolusi = resolusi  
        self.is_on = False        

    def tampilkan_info(self):
        status = "Menyala" if self.is_on else "Mati"
        return f"Kamera {self.merk} ({self.tipe}) - {self.resolusi} | Status: {status}"

    def potret(self):
        if self.is_on:
            return f"[KLIK!] {self.merk} berhasil mengambil foto."
        else:
            return f"Gagal! Kamera {self.merk} harus dinyalakan dulu."

    def nyalakan(self):
        self.is_on = True
        return f"{self.merk} sekarang aktif."

kamera_pro = Kamera("Sony", "Mirrorless", "42MP")
kamera_pemula = Kamera("Canon", "DSLR", "24MP")

kamera_pro.nyalakan()

print(f"Objek 1 -> {kamera_pro.tampilkan_info()} | Aksi: {kamera_pro.potret()}")
print(f"Objek 2 -> {kamera_pemula.tampilkan_info()} | Aksi: {kamera_pemula.potret()}")
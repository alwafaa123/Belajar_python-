class Mahasiswa:
    def __init__(self, nama="", nim=""):
        self.nama = nama
        self.nim = nim


class Kampus:
    def __init__(self):
        self.mahasiswa1 = Mahasiswa("fattahul", "4526839787")
        self.mahasiswa2 = Mahasiswa("tina", "5382687389")


if __name__ == "__main__":
    kampus = Kampus()
    print(kampus.mahasiswa1.nama)
    print(kampus.mahasiswa1.nim)
    print(kampus.mahasiswa2.nama)
    print(kampus.mahasiswa2.nim)

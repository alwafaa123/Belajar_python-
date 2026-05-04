class AkunBank:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        self.__saldo = saldo_awal 

    def lihat_saldo(self):
        return f"Saldo saat ini untuk akun {self.pemilik}: Rp{self.__saldo}"

    def setor_tunai(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Berhasil setor Rp{jumlah}.")
        else:
            print("Jumlah setor harus lebih dari 0!")

    def tarik_tunai(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Berhasil tarik Rp{jumlah}.")
        else:
            print("Saldo tidak cukup atau jumlah tidak valid!")

akun_fattahul = AkunBank("Fattahul", 1000000)

print(akun_fattahul.lihat_saldo())

akun_fattahul.setor_tunai(500000)
akun_fattahul.tarik_tunai(200000)

print(akun_fattahul.lihat_saldo())
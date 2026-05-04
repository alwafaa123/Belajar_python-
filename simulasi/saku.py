class DompetDigital:
    def __init__(self, nama_pemilik, pin_rahasia, saldo_awal):
        self.nama_pemilik = nama_pemilik
        self.__id_pengguna = f"ID-{nama_pemilik.upper()}-001"
        self.__pin = pin_rahasia
        self.__saldo = saldo_awal
        
    def get_id(self):
        return f"ID Pengguna: {self.__id_pengguna}"

    def lihat_saldo(self, input_pin):
        print(f"\n--- Mencoba Melihat Saldo (Input PIN: {input_pin}) ---")
        if input_pin == self.__pin:
            return f"Verifikasi Berhasil! Saldo {self.nama_pemilik}: Rp{self.__saldo}"
        else:
            return "Verifikasi Gagal! PIN Salah. Akses Ditolak."

    def transfer_dana(self, jumlah, input_pin):
        print(f"\n--- Mencoba Transfer: Rp{jumlah} (Input PIN: {input_pin}) ---")
        if input_pin != self.__pin:
            print("Gagal: PIN yang Anda masukkan salah!")
        elif jumlah > self.__saldo:
            print(f"Gagal: Saldo tidak cukup (Saldo saat ini: Rp{self.__saldo})")
        elif jumlah <= 0:
            print("Gagal: Jumlah transfer harus lebih dari 0!")
        else:
            self.__saldo -= jumlah
            print(f"Berhasil! Transfer Rp{jumlah} sukses. Sisa saldo: Rp{self.__saldo}")
            
dompet_fattahul = DompetDigital("Fattahul", "123456", 500000)

print(dompet_fattahul.get_id())
print(dompet_fattahul.lihat_saldo("111111")) 
print(dompet_fattahul.lihat_saldo("123456")) 

dompet_fattahul.transfer_dana(600000, "123456")
dompet_fattahul.transfer_dana(200000, "123456")
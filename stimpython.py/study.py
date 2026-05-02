class pasar:
    nama = ''
    lokasi = ''
    @staticmethod
    def jam_buka() :
        print(f'pasar buka pada jam 7 pagi')   
    def jenis_barang(self) :
        print(f'pasar {self.nama} memiliki jenis barang yang lengkap {self.lokasi}')
    def pedagang(self, pdg) :
        print(f'pasar {self.nama} memiliki pedagang yang ramah {pdg}')
        
pasar1 = pasar()
pasar1.nama = 'pasar tradisional'
pasar1.lokasi = 'dekat rumah saya'
pasar1.jam_buka()
pasar1.jenis_barang()
pasar1.pedagang('pak joko')
pasar.jam_buka()

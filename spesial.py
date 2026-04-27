class dono:
    nama = ''
    anak = ''
    
    def anak_asli(self):
        print(f'Halo {self.nama}, anak anda saat ini adalah {self.anak}')
        
    def __init__(self, nama='', anak=''):
        self.nama = nama
        self.anak = anak
        print('objeck berhasil di buat')
        
    def __str__(self):
        return 'anakmu sangat pintar'
    
    def __le__(self, other):
        return self.anak == other.nama and self.anak
    
    def __eq__(self, other):
        return self.nama == other.nama and self.anak == other.anak

dono1 = dono('dimas', 'anak ke2')
dono2 = dono('nimas', 'anak ke4')
print(dono1)
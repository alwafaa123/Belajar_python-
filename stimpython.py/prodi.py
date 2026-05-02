class Prodi :
    nama = ''
    jurusan = ''
    @staticmethod
    def ruangan() :
        print(f'prodi memiliki ruangan yang nyaman')
    def matkul(self) :
        print(f'prodi {self.nama} memiliki matakuliah yang bermanfaat {self.jurusan}')
    def dosen(self, dsn) :
        print(f'prodi {self.nama} memiliki dosen yang berkualitas tinggi {dsn}')
    
prodi1 = Prodi()
prodi1.nama = 'teknik informaika'
prodi1.jurusan = 'teknik'
prodi1.ruangan()
prodi1.matkul()
prodi1.dosen('ustad wahid')

Prodi.ruangan()

        
        
        
        
    
    
    
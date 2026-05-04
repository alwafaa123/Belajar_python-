class KarakterGame:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal 


    def cek_status(self):
        return f"Karakter: {self.nama} | HP Saat Ini: {self.__hp}"
    
    def terkena_serangan(self, damage):
        print(f"--- {self.nama} diserang sebesar {damage} damage! ---")
        if damage > 0:
            self.__hp -= damage
            if self.__hp < 0:
                self.__hp = 0 
        else:
            print("Serangan tidak valid.")

    def gunakan_medkit(self, heal):
        print(f"--- {self.nama} menggunakan Medkit (+{heal} HP) ---")
        if heal > 0:
            self.__hp += heal
            if self.__hp > 100:
                self.__hp = 100
        else:
            print("Penyembuhan tidak valid.")

hero = KarakterGame("Fattahul_Warrior", 100)

print(hero.cek_status())

hero.terkena_serangan(40)
print(hero.cek_status())

hero.gunakan_medkit(20)
print(hero.cek_status())

hero.terkena_serangan(150)
print(hero.cek_status()) # HP akan tetap 0, tidak jadi -50
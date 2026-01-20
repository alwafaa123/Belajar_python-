def Sapa(nama):
    print("Halo,", nama)

Sapa("Raka")
Sapa("Dina")
buah = ["apel", "jeruk", "mangga"]

for item in buah:
    print("Saya suka", item)
    import random

angka_rahasia = random.randint(1, 10)
tebakan = 0

while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka (1-10): "))
    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Terlalu besar!")
    else:
        print("Benar! Kamu hebat!")
        
        
        
        
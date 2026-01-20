

def sapa_nama(nama): 
    print(f"Halo, {nama}!") 


sapa_nama("Budi")


pesan = "Ini adalah kode di level paling atas."
print(pesan)


def cek_usia(umur):
    if umur >= 18:
        print("Anda dewasa.") 
        usia = umur 
        print(f"Usia Anda adalah: {usia}")
    else:
        print("Anda masih di bawah umur.") 
        
cek_usia(25)
import os

# Data inventory: list of dictionaries {'nama': str, 'harga': int}
inventory = [
    {'nama': 'Apel', 'harga': 5000},
    {'nama': 'Jeruk', 'harga': 3000},
    {'nama': 'Pisang', 'harga': 2000}
]

# Keranjang belanja: list of dictionaries sama seperti inventory
keranjang = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampil_menu():
    clear_screen()
    print("=== Sistem Kasir Sederhana ===")
    print("1. Kelola Inventory")
    print("2. Belanja (Tambah ke Keranjang)")
    print("3. Lihat Keranjang")
    print("4. Cetak Struk")
    print("5. Reset Keranjang")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ")
    return pilihan

def kelola_inventory():
    while True:
        clear_screen()
        print("=== Kelola Inventory ===")
        print("1. Tambah Barang")
        print("2. Edit Barang")
        print("3. Hapus Barang")
        print("4. Lihat Inventory")
        print("5. Kembali ke Menu Utama")
        pilihan = input("Pilih (1-5): ")
        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            edit_barang()
        elif pilihan == '3':
            hapus_barang()
        elif pilihan == '4':
            lihat_inventory()
            input("Tekan Enter untuk kembali...")
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk kembali...")

def tambah_barang():
    clear_screen()
    print("=== Tambah Barang ===")
    nama = input("Nama barang: ")
    try:
        harga = int(input("Harga barang: "))
        inventory.append({'nama': nama, 'harga': harga})
        print("Barang berhasil ditambahkan!")
    except ValueError:
        print("Harga harus angka!")
    input("Tekan Enter untuk kembali...")

def edit_barang():
    lihat_inventory()
    try:
        index = int(input("Masukkan nomor barang yang ingin diedit: ")) - 1
        if 0 <= index < len(inventory):
            nama_baru = input(f"Nama baru ({inventory[index]['nama']}): ") or inventory[index]['nama']
            harga_baru = input(f"Harga baru ({inventory[index]['harga']}): ")
            if harga_baru:
                harga_baru = int(harga_baru)
            else:
                harga_baru = inventory[index]['harga']
            inventory[index] = {'nama': nama_baru, 'harga': harga_baru}
            print("Barang berhasil diedit!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Input tidak valid!")
    input("Tekan Enter untuk kembali...")

def hapus_barang():
    lihat_inventory()
    try:
        index = int(input("Masukkan nomor barang yang ingin dihapus: ")) - 1
        if 0 <= index < len(inventory):
            del inventory[index]
            print("Barang berhasil dihapus!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Input tidak valid!")
    input("Tekan Enter untuk kembali...")

def lihat_inventory():
    clear_screen()
    print("=== Inventory ===")
    if not inventory:
        print("Inventory kosong.")
    else:
        for i, item in enumerate(inventory, 1):
            print(f"{i}. {item['nama']} - Rp{item['harga']}")

def belanja():
    lihat_inventory()
    try:
        index = int(input("Masukkan nomor barang yang ingin ditambah ke keranjang: ")) - 1
        if 0 <= index < len(inventory):
            keranjang.append(inventory[index])
            print("Barang berhasil ditambahkan ke keranjang!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Input tidak valid!")
    input("Tekan Enter untuk kembali...")

def lihat_keranjang():
    clear_screen()
    print("=== Keranjang Belanja ===")
    if not keranjang:
        print("Keranjang kosong.")
    else:
        total = 0
        for i, item in enumerate(keranjang, 1):
            print(f"{i}. {item['nama']} - Rp{item['harga']}")
            total += item['harga']
        print(f"Total: Rp{total}")
    input("Tekan Enter untuk kembali...")

def cetak_struk():
    clear_screen()
    print("=== Struk Belanja ===")
    if not keranjang:
        print("Keranjang kosong, tidak ada yang dicetak.")
    else:
        total = 0
        print("Daftar Barang:")
        for item in keranjang:
            print(f"- {item['nama']}: Rp{item['harga']}")
            total += item['harga']
        print(f"Total: Rp{total}")
        print("Terima kasih telah berbelanja!")
        # Reset keranjang setelah cetak struk
        keranjang.clear()
        print("Keranjang telah dikosongkan.")
    input("Tekan Enter untuk kembali...")

def reset_keranjang():
    keranjang.clear()
    print("Keranjang berhasil dikosongkan!")
    input("Tekan Enter untuk kembali...")

# Main loop
while True:
    pilihan = tampil_menu()
    if pilihan == '1':
        kelola_inventory()
    elif pilihan == '2':
        belanja()
    elif pilihan == '3':
        lihat_keranjang()
    elif pilihan == '4':
        cetak_struk()
    elif pilihan == '5':
        reset_keranjang()
    elif pilihan == '6':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut...")
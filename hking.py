#!/usr/bin/env python3

import socket # Modul untuk operasi jaringan
import sys    # Modul untuk interaksi dengan sistem, misal argumen baris perintah
from datetime import datetime # Modul untuk mendapatkan waktu

def run_scanner():
    # --- Input Target ---
    remote_host = input("Masukkan alamat IP atau hostname target: ")

    # --- Mendapatkan informasi host ---
    try:
        # Mengubah hostname menjadi alamat IP jika yang dimasukkan adalah hostname
        ip_address = socket.gethostbyname(remote_host)
        print(f"\nMemindai host: {ip_address}")
    except socket.gaierror:
        print("Hostname tidak dapat diresolve. Mohon periksa kembali.")
        sys.exit() # Keluar jika hostname tidak valid

    # --- Menentukan Rentang Port ---
    try:
        start_port_str = input("Masukkan port awal (misal: 1): ")
        end_port_str = input("Masukkan port akhir (misal: 1024): ")

        start_port = int(start_port_str)
        end_port = int(end_port_str)

        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Rentang port tidak valid. Port harus antara 1-65535, dan port awal <= port akhir.")
            sys.exit()

    except ValueError:
        print("Input port tidak valid. Masukkan angka.")
        sys.exit()

    print("-" * 50)
    print("Waktu mulai pemindaian:", datetime.now())
    print("-" * 50)

    # --- Proses Pemindaian Port ---
    open_ports = []
    closed_ports = []
    filtered_ports = [] # Port yang tidak memberikan respon jelas

    for port in range(start_port, end_port + 1):
        try:
            # Membuat objek socket
            # AF_INET: untuk IPv4
            # SOCK_STREAM: untuk TCP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1) # Mengatur timeout 1 detik untuk koneksi

            # Mencoba koneksi ke port target
            result = s.connect_ex((ip_address, port)) # connect_ex mengembalikan kode error, bukan exception

            if result == 0: # Kode 0 berarti koneksi berhasil (port terbuka)
                service_name = "Tidak dikenal"
                try:
                    service_name = socket.getservbyport(port, 'tcp') # Mencoba mendapatkan nama layanan
                except OSError:
                    pass # Abaikan jika nama layanan tidak ditemukan
                print(f"Port {port}: Terbuka ({service_name})")
                open_ports.append(port)
            # else:
            #     # Jika ingin melihat port tertutup atau terfilter juga
            #     # print(f"Port {port}: Tertutup/Terfilter (Kode: {result})")
            #     if result == 111: # Connection refused (umumnya port tertutup)
            #         closed_ports.append(port)
            #     else: # Kode error lain (mungkin terfilter oleh firewall)
            #         filtered_ports.append(port)


            s.close() # Tutup socket setelah selesai
        except socket.error as e:
            # Menangani error jaringan (misal host tidak reachable)
            print(f"Tidak dapat terhubung ke host {ip_address}. Error: {e}")
            break # Keluar dari loop pemindaian jika ada masalah koneksi umum
        except KeyboardInterrupt:
            print("\nPemindaian dihentikan oleh pengguna.")
            sys.exit()
        except Exception as e:
            print(f"Terjadi kesalahan yang tidak terduga pada port {port}: {e}")

    print("-" * 50)
    print("Waktu selesai pemindaian:", datetime.now())
    print("-" * 50)

    print("\nHasil Ringkasan:")
    if open_ports:
        print(f"Port Terbuka ({len(open_ports)}): {', '.join(map(str, open_ports))}")
    else:
        print("Tidak ada port terbuka yang ditemukan dalam rentang yang ditentukan.")

    # print(f"Port Tertutup ({len(closed_ports)}): {', '.join(map(str, closed_ports))}")
    # print(f"Port Terfilter ({len(filtered_ports)}): {', '.join(map(str, filtered_ports))}")

if __name__ == "__main__":
    run_scanner()
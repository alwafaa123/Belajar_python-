#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║     🌍 APLIKASI KALKULATOR RADAR KECEPATAN & CUACA INDONESIA 🌍      ║
║                                                                      ║
║     Dibuat untuk Ujian - Calculator Speed Radar & Weather           ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import os
import time
from datetime import datetime
import random

# ==================== WARNA UNTUK TERMINAL ====================
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.03):
    """Menampilkan teks dengan efek ketik"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def loading_bar(duration=2):
    """Menampilkan loading bar animasi"""
    print(f"\n{Colors.CYAN}⏳ Memuat sistem...", end="")
    chars = "▓▒░"
    for _ in range(20):
        for char in chars:
            print(f"\b{char}", end="", flush=True)
            time.sleep(duration/60)
    print(f" ✓{Colors.RESET}\n")

# ==================== KALKULATOR RADAR KECEPATAN ====================
def hitung_kecapatan_radar():
    """
    Kalkulator kecepatan radar untuk Indonesia
    Menggunakan rumus fisika: v = d/t
    """
    print(f"\n{Colors.YELLOW}{'='*60}")
    print(f"  🚗 KALKULATOR KECEPATAN RADAR - INDONESIA 🚗")
    print(f"{'='*60}{Colors.RESET}\n")
    
    print(f"{Colors.CYAN}📌 Aturan Batas Kecepatan di Indonesia:")
    print(f"   • Jalan Raya: 50 km/jam")
    print(f"   • Jalan Tol: 80-100 km/jam")
    print(f"   • Zona Sekolah: 30 km/jam")
    print(f"   •awasan: 40 km/jam{Colors.RESET}\n")
    
    try:
        # Input jarak tempuh
        print(f"{Colors.GREEN}┌─ Input Data Perhitungan")
        print(f"│")
        jarak = float(input(f"│ {Colors.WHITE}Masukkan jarak tempuh (km): {Colors.YELLOW}"))
        waktu = float(input(f"│ {Colors.WHITE}Masukkan waktu tempuh (jam): {Colors.YELLOW}"))
        print(f"│")
        print(f"└{Colors.GREEN}─{Colors.RESET}")
        
        # Perhitungan
        kecepatan = jarak / waktu if waktu > 0 else 0
        
        # Tampilan hasil
        print(f"\n{Colors.CYAN}{'─'*60}")
        print(f"  📊 HASIL PERHITUNGAN")
        print(f"{'─'*60}{Colors.RESET}")
        print(f"\n  🚗 Kecepatan Rata-rata: {Colors.BOLD}{kecepatan:.2f} km/jam{Colors.RESET}")
        
        # Analisis berdasarkan batas kecepatan Indonesia
        if kecepatan > 100:
            status = f"{Colors.RED}⚠️ MELAMPAUI BATAS! (Denda: Rp 500.000 - Rp 1.000.000){Colors.RESET}"
            print(f"  📋 Status: {status}")
        elif kecepatan > 80:
            status = f"{Colors.YELLOW}⚠️ Melebihi batas jalan tol (100 km/jam){Colors.RESET}"
            print(f"  📋 Status: {status}")
        elif kecepatan > 50:
            status = f"{Colors.YELLOW}⚠️ Melebihi batas jalan raya (50 km/jam){Colors.RESET}"
            print(f"  📋 Status: {status}")
        else:
            status = f"{Colors.GREEN}✅ AMAN - Dalam batas kecepatan{Colors.RESET}"
            print(f"  📋 Status: {status}")
        
        # Konversi ke m/s
        kecepatan_ms = kecepatan * 1000 / 3600
        print(f"  🔄 Kecepatan: {kecepatan_ms:.2f} m/s")
        
        # Waktu tempuh tambahan jika melebihi batas
        if kecepatan > 50:
            waktu_lebih = (jarak / 50) - waktu
            if waktu_lebih > 0:
                print(f"  ⏱️ Waktu lebih jika sesuai batas: {waktu_lebih:.2f} jam")
        
        print(f"\n{Colors.CYAN}{'─'*60}{Colors.RESET}\n")
        
    except ValueError:
        print(f"\n{Colors.RED}❌ Error: Masukkan angka yang valid!{Colors.RESET}\n")

def kalkulator_denda_radar():
    """Kalkulator denda pelanggaran kecepatan di Indonesia"""
    print(f"\n{Colors.MAGENTA}{'='*60}")
    print(f"  💰 KALKULATOR DENDA PELANGGARAN RADAR 💰")
    print(f"{'='*60}{Colors.RESET}\n")
    
    try:
        kecepatan_terukur = float(input(f"{Colors.WHITE}Masukkan kecepatan terukur (km/jam): {Colors.YELLOW}"))
        batas_kecepatan = float(input(f"{Colors.WHITE}Masukkan batas kecepatan maksimal (km/jam): {Colors.YELLOW}"))
        
        selisih = kecepatan_terukur - batas_kecepatan
        
        print(f"\n{Colors.CYAN}{'─'*60}")
        print(f"  📋 DETAIL PELANGGARAN")
        print(f"{'─'*60}{Colors.RESET}")
        print(f"  Kecepatan Terukur: {kecepatan_terukur} km/jam")
        print(f"  Batas Kecepatan: {batas_kecepatan} km/jam")
        print(f"  Kelebihan: {selisih} km/jam")
        
        # Perhitungan denda berdasarkan UU Lalu Lintas Indonesia
        if selisih <= 0:
            denda = 0
            print(f"  💵 Denda: {Colors.GREEN}Tidak ada pelanggaran{Colors.RESET}")
        elif selisih <= 10:
            denda = 100000
            kategori = "Pelanggaran Ringan"
        elif selisih <= 20:
            denda = 250000
            kategori = "Pelanggaran Sedang"
        elif selisih <= 30:
            denda = 500000
            kategori = "Pelanggaran Berat"
        else:
            denda = 1000000
            kategori = "Pelanggaran Sangat Berat"
        
        if selisih > 0:
            print(f"  📊 Kategori: {kategori}")
            print(f"  💵 Denda: {Colors.RED}Rp {denda:,}{Colors.RESET}")
            print(f"  ⚠️ Catatan: Tilang dapat diterbitkan")
        
        print(f"\n{Colors.CYAN}{'─'*60}{Colors.RESET}\n")
        
    except ValueError:
        print(f"\n{Colors.RED}❌ Error: Masukkan angka yang valid!{Colors.RESET}\n")

# ==================== KALKULATOR CUACA INDONESIA ====================
def analisis_cuaca_indonesia():
    """Kalkulator dan analisis cuaca untuk Indonesia"""
    print(f"\n{Colors.BLUE}{'='*60}")
    print(f"  🌤️ KALKULATOR & ANALISIS CUACA INDONESIA 🌤️")
    print(f"{'='*60}{Colors.RESET}\n")
    
    print(f"{Colors.CYAN}📌 Pilih Jenis Analisis:")
    print(f"   1. Suhu & Kelembaban")
    print(f"   2. Indeks Panas (Heat Index)")
    print(f"   3. Prediksi Cuaca Sederhana")
    print(f"   4. Kategori Iklim Indonesia{Colors.RESET}\n")
    
    try:
        pilihan = int(input(f"{Colors.WHITE}Pilih menu (1-4): {Colors.YELLOW}"))
        
        if pilihan == 1:
            # Analisis Suhu & Kelembaban
            print(f"\n{Colors.GREEN}🌡️ ANALISIS SUHU & KELEMBABAN")
            print(f"{'─'*40}{Colors.RESET}")
            
            suhu = float(input(f"  Suhu (°C): "))
            kelembaban = float(input(f"  Kelembaban (%): "))
            
            # Klasifikasi suhu Indonesia
            if suhu < 20:
                kategori_suhu = "DINGIN"
                emoji = "❄️"
            elif suhu < 25:
                kategori_suhu = "SEJUK"
                emoji = "🌿"
            elif suhu < 30:
                kategori_suhu = "HANGAT"
                emoji = "☀️"
            else:
                kategori_suhu = "PANAS"
                emoji = "🔥"
            
            # Klasifikasi kelembaban
            if kelembaban < 40:
                kategori_lembap = "KERING"
            elif kelembaban < 60:
                kategori_lembap = "NYAMAN"
            elif kelembaban < 80:
                kategori_lembap = "LEMBAP"
            else:
                kategori_lembap = "SANGAT LEMBAP"
            
            print(f"\n  {emoji} Suhu: {suhu}°C - {kategori_suhu}")
            print(f"  💧 Kelembaban: {kelembaban}% - {kategori_lembap}")
            
            # Rekomendasi aktivitas
            print(f"\n{Colors.CYAN}📋 Rekomendasi:{Colors.RESET}")
            if kategori_suhu == "PANAS" and kategori_lembap == "SANGAT LEMBAP":
                print(f"  • Hindari aktivitas berat di luar ruangan")
                print(f"  • Minum air putih yang cukup")
                print(f"  • Gunakan tabir surya")
            elif kategori_suhu == "DINGIN":
                print(f"  • Kenakan pakaian hangat")
                print(f"  • Minum minuman hangat")
        
        elif pilihan == 2:
            # Heat Index Calculator
            print(f"\n{Colors.YELLOW}🌡️ KALKULATOR INDEKS PANAS (HEAT INDEX)")
            print(f"{'─'*40}{Colors.RESET}")
            
            suhu = float(input(f"  Suhu (°C): "))
            kelembaban = float(input(f"  Kelembaban (%): "))
            
            # Konversi ke Fahrenheit untuk rumus
            suhu_f = (suhu * 9/5) + 32
            
            # Rumus Heat Index (simplified)
            hi = (-8.784694) + (1.61139411 * suhu_f) + (2.338548838 * kelembaban) + \
                 (-0.14611605 * suhu_f * kelembaban) + (-0.012308094 * suhu_f**2) + \
                 (-0.0164248277778 * kelembaban**2)
            
            # Konversi kembali ke Celsius
            hi_c = (hi - 32) * 5/9
            
            print(f"\n  🌡️ Suhu Aktual: {suhu}°C")
            print(f"  💧 Kelembaban: {kelembaban}%")
            print(f"  🔥 Heat Index: {hi_c:.1f}°C")
            
            # Kategori danger level
            if hi_c < 27:
                danger = "AMAN"
                warna = Colors.GREEN
            elif hi_c < 32:
                danger = "PERHATIAN"
                warna = Colors.YELLOW
            elif hi_c < 39:
                danger = "HATI-HATI"
                warna = Colors.YELLOW
            elif hi_c < 51:
                danger = "BAHAYA"
                warna = Colors.RED
            else:
                danger = "BAHAYA EKSTREM"
                warna = Colors.RED
            
            print(f"  ⚠️ Level: {warna}{danger}{Colors.RESET}")
        
        elif pilihan == 3:
            # Prediksi Cuaca Sederhana
            print(f"\n{Colors.BLUE}🔮 PREDIKSI CUACA SEDERHANA")
            print(f"{'─'*40}{Colors.RESET}")
            
            # Simulasi prediksi berdasarkan input
            kota = input(f"  Nama Kota: ").title()
            bulan = int(input(f"  Bulan (1-12): "))
            
            # Pola cuaca Indonesia berdasarkan bulan
            if bulan in [4, 5, 6, 7, 8, 9]:
                musim = "MUSIM KEMARAU"
                cuaca = random.choice(["Cerah", "Berawan", "Hujan Ringan"])
                suhu_range = "28-35°C"
            elif bulan in [10, 11, 12, 1, 2, 3]:
                musim = "MUSIM HUJAN"
                cuaca = random.choice(["Hujan", "Berawan", "Hujan Lebat"])
                suhu_range = "24-30°C"
            else:
                musim = "PENGALIHAN"
                cuaca = "Berubah-ubah"
                suhu_range = "26-32°C"
            
            print(f"\n  📍 Kota: {kota}")
            print(f"  📅 Musim: {musim}")
            print(f"  🌤️ Prediksi Cuaca: {cuaca}")
            print(f"  🌡️ Suhu: {suhu_range}")
            print(f"  💧 Kelembaban: 70-90%")
        
        elif pilihan == 4:
            # Kategori Iklim Indonesia
            print(f"\n{Colors.MAGENTA}🗺️ KATEGORI IKLIM INDONESIA")
            print(f"{'─'*40}{Colors.RESET}")
            
            print(f"""
  Indonesia memiliki 3 tipe iklim utama:
  
  {Colors.CYAN}1. Iklim Musim (Monsoon){Colors.RESET}
     • Wilayah: Jawa, Sumatra, Kalimantan
     • Ciri: Musim kemarau (Mei-Sept) & hujan (Okt-April)
     
  {Colors.GREEN}2. Iklim Laut{Colors.RESET}
     • Wilayah: Sulawesi, Maluku, Papua
     • Ciri: Hujan sepanjang tahun
     
  {Colors.YELLOW}3. Iklim Gunung{Colors.RESET}
     • Wilayah: Dataran tinggi
     • Ciri: Suhu lebih rendah dari dataran rendah
            """)
        
        else:
            print(f"\n{Colors.RED}❌ Pilihan tidak valid!{Colors.RESET}")
        
    except ValueError:
        print(f"\n{Colors.RED}❌ Error: Masukkan angka yang valid!{Colors.RESET}")

# ==================== MENU UTAMA ====================
def tampilkan_menu():
    """Menampilkan menu utama aplikasi"""
    clear_screen()
    
    print(f"""
{Colors.CYAN}
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║     🌍 APLIKASI KALKULATOR RADAR KECEPATAN & CUACA INDONESIA 🌍  ║
║                                                                  ║
║                    📋 MENU UTAMA 📋                              ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║   🚗  1. Kalkulator Kecepatan Radar                             ║
║   💰  2. Kalkulator Denda Pelanggaran Radar                     ║
║   🌤️  3. Kalkulator & Analisis Cuaca Indonesia                  ║
║   📊  4. Semua Fitur Sekaligus                                  ║
║   ❌  5. Keluar                                                  ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
{Colors.RESET}
""")

def main():
    """Fungsi utama program"""
    loading_bar(1)
    
    while True:
        tampilkan_menu()
        
        try:
            pilihan = input(f"{Colors.WHITE}Pilih menu (1-5): {Colors.YELLOW}")
            print(Colors.RESET)
            
            if pilihan == '1':
                hitung_kecapatan_radar()
            elif pilihan == '2':
                kalkulator_denda_radar()
            elif pilihan == '3':
                analisis_cuaca_indonesia()
            elif pilihan == '4':
                print(f"\n{Colors.GREEN}📊 MENJALANKAN SEMUA FITUR...{Colors.RESET}\n")
                hitung_kecapatan_radar()
                input(f"\n{Colors.CYAN}Tekan Enter untuk melanjutkan...{Colors.RESET}")
                kalkulator_denda_radar()
                input(f"\n{Colors.CYAN}Tekan Enter untuk melanjutkan...{Colors.RESET}")
                analisis_cuaca_indonesia()
            elif pilihan == '5':
                print(f"\n{Colors.GREEN}")
                print_slow("🙏 Terima kasih telah menggunakan aplikasi ini!")
                print(f"   Dibuat dengan ❤️ untuk ujian Indonesia")
                print(f"{Colors.RESET}\n")
                break
            else:
                print(f"\n{Colors.RED}❌ Pilihan tidak valid! Silakan pilih 1-5{Colors.RESET}\n")
            
            input(f"\n{Colors.CYAN}Tekan Enter untuk melanjutkan...{Colors.RESET}")
            
        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}⚠️ Program dihentikan oleh pengguna{Colors.RESET}\n")
            break
        except Exception as e:
            print(f"\n{Colors.RED}❌ Terjadi kesalahan: {e}{Colors.RESET}\n")

# Jalankan program
if __name__ == "__main__":
    main()
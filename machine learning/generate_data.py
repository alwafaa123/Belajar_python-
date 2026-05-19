import pandas as pd
import numpy as np

# Mengatur seed agar data acak yang dihasilkan selalu konsisten dan dapat dipelajari
np.random.seed(42)
n_samples = 120

# Membuat data simulasi dengan kolom yang sesuai instruksi tugas
data = {
    'TransactionID': [f'TX{str(i).zfill(3)}' for i in range(1, n_samples + 1)],
    'AccountID': [f'ACC{str(np.random.randint(1, 30)).zfill(2)}' for _ in range(n_samples)],
    'DeviceID': [f'DEV{str(np.random.randint(1, 20)).zfill(2)}' for _ in range(n_samples)],
    'IPAddress': [f'192.168.1.{np.random.randint(1, 50)}' for _ in range(n_samples)],
    'MerchantID': [f'MCH{str(np.random.randint(1, 15)).zfill(2)}' for _ in range(n_samples)],
    'TransactionDate': pd.date_range(start='2026-01-01', periods=n_samples, freq='D').astype(str),
    'Kategori_Produk': np.random.choice(['Elektronik', 'Fashion', 'Kuliner', 'Transportasi'], n_samples),
    'Jumlah_Nominal': np.random.randint(25000, 2500000, n_samples).astype(float),
    'Durasi_Sesi': np.random.randint(2, 180, n_samples).astype(float)
}

df = pd.DataFrame(data)

# Menyisipkan Missing Values (Data Kosong) secara sengaja untuk simulasi pembersihan data (Kriteria 2)
df.loc[5, 'Jumlah_Nominal'] = np.nan
df.loc[12, 'Durasi_Sesi'] = np.nan
df.loc[45, 'Jumlah_Nominal'] = np.nan
df.loc[82, 'Durasi_Sesi'] = np.nan

# Menyisipkan Baris Duplikat secara sengaja untuk simulasi pembersihan (Kriteria 2)
duplikat_1 = df.iloc[[10]]
duplikat_2 = df.iloc[[25]]
duplikat_3 = df.iloc[[70]]
df = pd.concat([df, duplikat_1, duplikat_2, duplikat_3], ignore_index=True)

# Menyimpan ke file CSV
df.to_csv('data_transaksi.csv', index=False)
print("[SUKSES] Berkas 'data_transaksi.csv' berhasil dibuat otomatis!")
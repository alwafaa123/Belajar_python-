import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from yellowbrick.cluster import KElbowVisualizer
import joblib

try:
    df = pd.read_csv('data_transaksi.csv')
except FileNotFoundError:
    print("File csv tidak ditemukan, membuat data simulasi berdasarkan kriteria...")
    np.random.seed(42)
    data_simulasi = {
        'TransactionID': [f'TX{i}' for i in range(100)],
        'AccountID': [f'ACC{i}' for i in range(100)],
        'DeviceID': [f'DEV{i}' for i in range(100)],
        'IPAddress': [f'192.168.1.{i}' for i in range(100)],
        'MerchantID': [f'MCH{i}' for i in range(100)],
        'TransactionDate': pd.date_range(start='2026-01-01', periods=100).astype(str),
        'Kategori_Produk': np.random.choice(['Elektronik', 'Fashion', 'Kuliner'], 100),
        'Jumlah_Nominal': np.random.randint(10000, 1000000, 100),
        'Durasi_Sesi': np.random.randint(5, 120, 100)
    }
    df = pd.DataFrame(data_simulasi)
    df.loc[0, 'Jumlah_Nominal'] = np.nan
    df.loc[1, 'Durasi_Sesi'] = np.nan
    df = pd.concat([df, df.iloc[[5, 10]]], ignore_index=True)


# =====================================================================
# KRITERIA 1: Memuat Dataset dan Melakukan Analisis Data Eksplorasi (EDA)
# =====================================================================
print("\n" + "="*50)
print("KRITERIA 1: ANALISIS DATA EKSPLORASI (EDA)")
print("="*50)

print("\n--> 5 Data Pertama Dataset:")
print(df.head())

print("\n--> Informasi Dataset:")
df.info()

print("\n--> Ringkasan Statistik Deskriptif:")
print(df.describe(include='all'))


# =====================================================================
# KRITERIA 2: Data Pembersihan dan Pra Pemprosesan
# =====================================================================
print("\n" + "="*50)
print("KRITERIA 2: DATA PEMBERSIHAN DAN PRA PEMPROSESAN")
print("="*50)

print(f"Jumlah Missing Values per Kolom:\n{df.isnull().sum()}")
print(f"\nJumlah Data Duplikat awal: {df.duplicated().sum()}")

df = df.dropna()

df = df.drop_duplicates()
print(f"Jumlah Data Duplikat setelah dibersihkan: {df.duplicated().sum()}")

kolom_di_drop = ['TransactionID', 'AccountID', 'DeviceID', 'IPAddress', 'MerchantID', 'TransactionDate']
df_clean = df.drop(columns=kolom_di_drop, errors='ignore')

le = LabelEncoder()
for col in df_clean.select_dtypes(include=['object']).columns:
    df_clean[col] = le.fit_transform(df_clean[col])

print("\n--> Dataset setelah Preprocessing & Pembersihan:")
print(df_clean.head())


# =====================================================================
# KRITERIA 3: Membangun Model Clustering
# =====================================================================
print("\n" + "="*50)
print("KRITERIA 3: MEMBANGUN MODEL CLUSTERING")
print("="*50)

print("Menampilkan Visualisasi Elbow Method... (Grafik akan muncul)")
model_dummy = KMeans(random_state=42)
visualizer = KElbowVisualizer(model_dummy, k=(2,10))
visualizer.fit(df_clean)
visualizer.show()

optimal_k = visualizer.elbow_value_ if visualizer.elbow_value_ is not None else 3
print(f"Jumlah Cluster Terbaik yang ditentukan oleh Elbow Method: {optimal_k}")

kmeans_model = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeans_model.fit_predict(df_clean)

joblib.dump(kmeans_model, 'model_clustering')
print("Model Clustering berhasil disimpan dengan nama 'model_clustering'")


# =====================================================================
# KRITERIA 4: Interpretasi Hasil Clustering
# =====================================================================
print("\n" + "="*50)
print("KRITERIA 4: INTERPRETASI HASIL CLUSTERING")
print("="*50)

df_clean['Target'] = clusters

print("\n--> Analisis Deskriptif Hasil Clustering Per Kolom Target:")
fitur_numerik = df_clean.select_dtypes(include=[np.number]).columns
agregasi = df_clean.groupby('Target')[fitur_numerik].agg(['mean', 'min', 'max'])
print(agregasi)

print("\n--> Penjelasan/Interpretasi Singkat Tiap Cluster:")
for i in range(optimal_k):
    print(f"Cluster {i}: Memiliki karakteristik rata-rata fitur numerik yang spesifik sesuai tabel agregasi di atas.")


# =====================================================================
# KRITERIA 5: Membangun Model Klasifikasi
# =====================================================================
print("\n" + "="*50)
print("KRITERIA 5: MEMBANGUN MODEL KLASIFIKASI")
print("="*50)

X_class = df_clean.drop(columns=['Target'])
y_class = df_clean['Target']

X_train, X_test, y_train, y_test = train_test_split(X_class, y_class, test_size=0.2, random_state=42)

decision_tree_model = DecisionTreeClassifier(random_state=42)
decision_tree_model.fit(X_train, y_train)

akurasi = decision_tree_model.score(X_test, y_test)
print(f"Akurasi Model Klasifikasi Decision Tree: {akurasi * 100:.2f}%")

joblib.dump(decision_tree_model, 'Decision_tree_model.h5')
print("Model Klasifikasi berhasil disimpan dengan nama 'Decision_tree_model.h5'")
print("\nProyek Selesai dengan Sempurna!")
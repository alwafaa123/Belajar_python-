# 1. Mengimpor library yang dibutuhkan
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.datasets import load_iris  # Menggunakan dataset bawaan sebagai contoh

# 2. Memuat Dataset
# (Jika pakai file sendiri, gunakan: df = pd.read_csv('nama_file.csv'))
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

print("--- 5 Data Pertama ---")
print(df.head())

# 3. Memisahkan Fitur (X) dan Target/Label (y)
X = df.drop(columns=['target'])
y = df['target']

# 4. Membagi Data menjadi Data Latih (Train) dan Data Uji (Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Penskalaan Fitur (Feature Scaling) - Bagus untuk performa model
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. Membangun dan Melatih Model (Menggunakan Random Forest)
model = RandomForestClassifier(random_state=42)
model.fit(X_train_scaled, y_train)

# 7. Melakukan Prediksi dengan Data Uji
y_pred = model.predict(X_test_scaled)

# 8. Evaluasi Performa Model
print("\n--- Hasil Evaluasi Model ---")
print(f"Akurasi Model: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nLaporan Klasifikasi Detail:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
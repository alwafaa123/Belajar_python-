import matplotlib.pyplot as plt
import numpy as np

# Data contoh (misalnya, ini bisa menjadi data "volume" Anda)
# Untuk demo, kita buat data acak
num_points = 50
x = np.random.rand(num_points) * 10
y = np.random.rand(num_points) * 10
# 'volume' atau intensitas direpresentasikan oleh ukuran atau warna
s = np.random.rand(num_points) * 500 + 50 # Ukuran bintang
colors = np.random.rand(num_points) # Warna berdasarkan nilai
# Anda juga bisa menggunakan array warna eksplisit, misalnya:
# colors = ['red'] * (num_points // 2) + ['blue'] * (num_points // 2)

plt.figure(figsize=(10, 8))
scatter = plt.scatter(x, y, s=s, c=colors, marker='*', cmap='viridis', alpha=0.7)

plt.title('Grafik Titik Data Berbentuk Bintang Berwarna')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.colorbar(scatter, label='Intensitas/Nilai Volume') # Menambahkan color bar untuk menjelaskan warna
plt.grid(True)
plt.show()
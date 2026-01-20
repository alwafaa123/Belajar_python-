import matplotlib.pyplot as plt
import numpy as np

def visualize_light_performance_circle(center_x=0, center_y=0, max_radius=10, num_circles=50, color='yellow'):
    """
    Membuat visualisasi kinerja cahaya dalam bentuk lingkaran.

    Args:
        center_x (float): Koordinat X pusat cahaya.
        center_y (float): Koordinat Y pusat cahaya.
        max_radius (float): Radius maksimum lingkaran terluar.
        num_circles (int): Jumlah lingkaran konsentris yang akan digambar.
        color (str): Warna dasar cahaya (misalnya 'yellow', 'orange', 'white').
    """
    plt.figure(figsize=(8, 8))
    ax = plt.gca() # Dapatkan objek Axes saat ini

    # Buat lingkaran-lingkaran konsentris
    for i in range(num_circles, 0, -1): # Dari lingkaran terluar ke dalam
        radius = (i / num_circles) * max_radius
        
        # Hitung transparansi (alpha) atau intensitas warna
        # Semakin jauh dari pusat, semakin transparan (atau pudar)
        alpha = (i / num_circles) * 0.6 + 0.1 # Alpha dari 0.1 (paling luar) sampai 0.7 (paling dalam)
        
        # Buat lingkaran
        circle = plt.Circle((center_x, center_y), radius, color=color, alpha=alpha, fill=True, ec=None)
        ax.add_patch(circle)

    # Atur batas sumbu agar lingkaran terlihat penuh
    ax.set_xlim(center_x - max_radius * 1.1, center_x + max_radius * 1.1)
    ax.set_ylim(center_y - max_radius * 1.1, center_y + max_radius * 1.1)

    # Hapus ticks dan label sumbu agar fokus pada visualisasi
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal', adjustable='box') # Pastikan lingkaran tidak elips
    
    plt.title('Visualisasi Kinerja Cahaya (Lingkaran Memudar)')
    plt.show()

# Panggil fungsi untuk menampilkan visualisasi
# Anda bisa mengubah parameter di sini
visualize_light_performance_circle(center_x=0, center_y=0, max_radius=10, num_circles=80, color='yellow')

# Contoh lain dengan warna berbeda
# visualize_light_performance_circle(center_x=0, center_y=0, max_radius=12, num_circles=60, color='cyan')
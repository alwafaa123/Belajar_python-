# 1. Make sure you have installed the required libraries via the terminal:
# pip install fastapi uvicorn --> in your terminal

# 2. from this code
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Model Data (Struktur data yang akan diterima dari Web)
class Produk(BaseModel):
    id: int
    nama: str
    harga: float
    tersedia: bool = True

# Database sederhana di dalam memori (List)
db_produk = []

@app.get("/")
def home():
    return {"message": "Selamat datang di API Unifood Back-end"}

# Endpoint untuk mengambil semua data produk
@app.get("/produk", response_model=List[Produk])
def ambil_semua_produk():
    return db_produk

# Endpoint untuk menambahkan data baru dari web
@app.post("/produk")
def tambah_produk(item: Produk):
    db_produk.append(item)
    return {"message": f"Produk {item.nama} berhasil ditambahkan!", "data": item}

# Endpoint untuk mencari produk berdasarkan ID
@app.get("/produk/{produk_id}")
def cari_produk(produk_id: int):
    for p in db_produk:
        if p.id == produk_id:
            return p
    return {"error": "Produk tidak ditemukan"}

# 3. Cara Menjalankan
# Jalankan program dengan perintah berikut di terminal:
# uvicorn main:app --reload

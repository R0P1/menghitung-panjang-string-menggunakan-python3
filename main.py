#!/usr/bin/env python3

# Minta pengguna memasukkan teks atau string
teks = input("Masukkan teks atau string: ")

# Inisialisasi variabel panjang untuk menyimpan panjang string
panjang = 0

# Loop untuk menghitung panjang string dengan mengiterasi setiap karakter
for karakter in teks:
    panjang += 1

# Cetak panjang string
print(f"Panjang string adalah: {panjang}")

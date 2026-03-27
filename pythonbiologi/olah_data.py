import pandas as pd

# 1. Membaca file Excel
# Ganti 'data_bakteri.xlsx' sesuai nama file yang kamu simpan
try:
    df = pd.read_excel('data_bakteri.xlsx')
    print("--- Data Berhasil Dimuat ---")
    print(df)
    
    print("\n--- Analisis Singkat ---")
    # 2. Menghitung rata-rata jumlah bakteri
    rata_rata = df['Jumlah_Bakteri'].mean()
    print(f"Rata-rata populasi bakteri: {rata_rata:.2f}")

    # 3. Mencari sampel yang statusnya 'Kritis'
    kritis = df[df['Status_Kesehatan'] == 'Kritis']
    print("\n--- Sampel yang Perlu Perhatian (Kritis) ---")
    print(kritis)

except FileNotFoundError:
    print("Error: File Excel tidak ditemukan! Pastikan namanya benar.")
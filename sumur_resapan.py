# Program Perhitungan Kebutuhan Sumur Resapan 
# Rumus-rumus yang digunakan:
# Debit Puncak Limpasan (Q) = konstanta_rasional* C * I * A 
# Koefisien Limpasan Gabungan (C) = Σ(C[i] × A[i]) ÷ ΣA[i]
# Intensitas Hujan (I) = (r24 ÷ 24) × (24 ÷ t)^(2/3)
# Kedalaman Air Sumur Dibutuhkan (h_total) = [Q ÷ (F × K)] × [1 − exp(−F × K × T ÷ (π × R²))]
# Jumlah Sumur (n) = ceil(h_total/h_sumur)
import math

konstanta_rasional = 0.278
faktor_geometrik = 5.5
koef_limpasan = {
        "atap" : 0.90,
        "aspal" : 0.85,
        "beton" : 0.85,
        "paving": 0.70,
        "tanah" : 0.35,
        "taman" : 0.20,
}

def intesitas_mononobe(r24: float, durasi_jam: float):
    return (r24/24.0)*(24.0/durasi_jam) **(2.0 /3.0)

def debit (c: float, intensitas:float, luas_m2:float):
    return konstanta_rasional* c * intensitas *(luas_m2/1000000.0)

def kedalaman_sumur(q:float, k :float, jari:float, durasi_detik: float):
    f = faktor_geometrik * jari
    eksponen = f * k * durasi_detik / (math.pi*jari**2)
    return q/(f*k)*(-math.expm1(-eksponen))
    #-math.expm1(-eksponen) = 1 - exp(-eksponen)
    
def jumlah_sumur(h_total:float, h_sumur:float):
    return max(1, math.ceil(round(h_total/h_sumur,9)))
    # Fungsi max(1,jumlah_sumur) adalah untuk memastikan bahwa nilai akhir selalu minimal 1. Jika h_total sangat kecil(mendekati 0), jumlah sumur akan menjadi nol. Fungsi round adalah untuk memastikan pembagian python yang sering tidak pas, seperti pembagian yang seharusnya 3.0 malah menjadi 3.000000000004. Agar ceil(3.00000000004) tidak menjadi 4, bulatkan menjadi 3 menggunakan round.

def hitung(areas: list,durasi_jam:float,r24:float, k: float, jari: float, h_sumur: float):
    durasi_detik = durasi_jam * 3600
    i = intesitas_mononobe(r24, durasi_jam)
    q_area = []
    luas_total = 0
    for area in areas:
        c = koef_limpasan[area["tipe"]]
        luas = area["luas"]

        q_area.append(debit(c,i,luas))
        luas_total += luas

    q_total = sum(q_area)
    luas_total = sum(luas for a in areas)
    h_total = kedalaman_sumur(q_total,k, jari, durasi_detik)
    n = jumlah_sumur(h_total, h_sumur)
    return n

def main():
    durasi_jam = float(input("Masukkan durasi hujan (jam): "))
    r24 = float(input("Masukkan curah hujan R24 (mm): "))
    k = float(input("Masukkan permeabilitas tanah (K): "))
    jari = float(input("Masukkan jari-jari sumur (meter): "))
    h_sumur = float(input("Masukkan kedalaman sumur (meter); "))
    data_area = []
    while True:
        tipe = input("Masukkan tipe lahan (atau ketik 'selesai' untuk menghitung): ")
        if tipe == 'selesai':
            break
        if tipe not in koef_limpasan:
            print("Tipe lahan tidak dikenali")
            continue
        luas = float(input(f"Masukkan luas area untuk {tipe} (m2): "))
        data_area.append({"tipe": tipe, "luas":luas})
    jumlah_sumur = hitung(data_area, durasi_jam, r24, k, jari, h_sumur)
    print(f"Jumlah Sumur Resapan yang dibutuhkan adalah {jumlah_sumur} buah")
main()

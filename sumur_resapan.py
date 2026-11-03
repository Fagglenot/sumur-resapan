# Program Perhitungan Kebutuhan Sumur Resapan 
konstanta_rasional = 0.278
faktor_geometrik = 5.5
K_minimum = 2.0/ 100.0 / 3600.0
koef_limpasan = {
        "atap" : 0.90,
        "aspal" : 0.85,
        "beton" : 0.85,
        "paving": 0.70,
        "tanah" : 0.35,
        "taman" : 0.20
}

def intesitas_mononobe(r24: float, durasi_jam: float):
    return (r24/24.0)*(24.0/durasi_jam) **(2.0 /3.0)
def debit (c: float, durasi_jam: float):
    return konstanta_rasional* c * intensitas *(luas_m2/1000000.0)
def kedalaman sumur(q:float, k :float, jari:float, durasi_detik: float):
    return q/(f*k)*(-math.expm1(-eksponen))


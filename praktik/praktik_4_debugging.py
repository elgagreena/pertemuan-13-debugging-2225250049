def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)

def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None

    tertinggi = nilai[0]
    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x
    return tertinggi

nilai = [80, 60, 90, 70]

print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(60))
print("Tertinggi:", nilai_tertinggi(nilai))

print("\n=== PENGUJIAN TEST CASE ===")

print("T1 - Rata-rata:", hitung_rata_rata([80, 60, 90, 70]))
print("T2 - Rata-rata:", hitung_rata_rata([100, 80]))
print("T3 - Status 60:", status(60))
print("T4 - Status 59:", status(59))
print("T5 - Nilai tertinggi:", nilai_tertinggi([80, 60, 90, 70]))

print("\n=== BUKTI TRACING ===")

data = [80, 60, 90, 70]
total = sum(data)
jumlah_data = len(data)
rata_rata = total / jumlah_data

print("Data:", data)
print("Total:", total)
print("Jumlah data:", jumlah_data)
print("Rata-rata:", rata_rata)
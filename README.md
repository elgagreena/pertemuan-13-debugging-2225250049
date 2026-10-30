# Pertemuan 13 - Debugging dan Testing

Nama: Elga Greena Rahma Tazkia
NIM: 2225250049
Kelas: 3B

## Kasus

Program yang diuji merupakan program pengolahan nilai mahasiswa dengan tiga fungsi, yaitu menghitung rata-rata, menentukan status kelulusan, dan mencari nilai tertinggi. Pengujian dilakukan untuk menemukan kesalahan pada program, menelusuri penyebabnya, dan memperbaiki bug yang ditemukan.

## Test Case

| ID | Input            | Expected    | Actual Awal | Status |
| -- | ---------------- | ----------- | ----------- | ------ |
| T1 | [80, 60, 90, 70] | 75.0        | 60.0        | FAIL   |
| T2 | [100, 80]        | 90.0        | 36.0        | FAIL   |
| T3 | 60               | Lulus       | Tidak lulus | FAIL   |
| T4 | 59               | Tidak lulus | Tidak lulus | PASS   |
| T5 | [80, 60, 90, 70] | 90          | 0           | FAIL   |

## Bug Report

**B01 - Kesalahan Perhitungan Rata-rata**

* Gejala: Hasil rata-rata tidak sesuai dengan jumlah data.
* Lokasi: Fungsi `hitung_rata_rata()`.
* Akar penyebab: Pembagian selalu menggunakan angka 5, bukan jumlah data sebenarnya.
* Perbaikan: Mengganti pembagi dengan `len(nilai)` dan menambahkan pemeriksaan list kosong.

**B02 - Kesalahan Status Kelulusan**

* Gejala: Nilai 60 dinyatakan tidak lulus.
* Lokasi: Fungsi `status()`.
* Akar penyebab: Penggunaan operator `>` menyebabkan nilai 60 tidak memenuhi kondisi.
* Perbaikan: Mengganti operator `>` menjadi `>=`.

**B03 - Kesalahan Nilai Tertinggi**

* Gejala: Program menghasilkan nilai tertinggi 0.
* Lokasi: Fungsi `nilai_tertinggi()`.
* Akar penyebab: Variabel `tertinggi` dimulai dari 0 dan kondisi perbandingan menggunakan operator `<`.
* Perbaikan: Menginisialisasi `tertinggi` dengan data pertama dan mengganti operator `<` menjadi `>`.

Penelusuran dilakukan melalui pemeriksaan kode dan tracing perhitungan rata-rata. Hasil tracing menunjukkan total nilai 300, jumlah data 4, dan rata-rata 75.0.

## Retest

Setelah perbaikan dilakukan, seluruh test case dijalankan kembali dengan hasil berikut.

| ID | Expected    | Actual Setelah Perbaikan | Status |
| -- | ----------- | ------------------------ | ------ |
| T1 | 75.0        | 75.0                     | PASS   |
| T2 | 90.0        | 90.0                     | PASS   |
| T3 | Lulus       | Lulus                    | PASS   |
| T4 | Tidak lulus | Tidak lulus              | PASS   |
| T5 | 90          | 90                       | PASS   |

Hasil retest menunjukkan bahwa seluruh 5 test case berhasil mendapatkan hasil sesuai harapan.

## Cara Menjalankan

```bash
python3 praktik/praktik_4_debugging.py
```

## Refleksi

Teknik debugging yang paling membantu adalah tracing karena dapat membantu menelusuri proses program dan mengetahui bagian yang menyebabkan hasil tidak sesuai. Pengujian menggunakan beberapa test case juga membantu memastikan bahwa perbaikan yang dilakukan sudah benar.

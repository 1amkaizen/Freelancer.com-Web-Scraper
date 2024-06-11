# Freelancer.com-Web-Scraper
Web scraper sederhana untuk mengambil data proyek dari Freelancer.com menggunakan Python dan BeautifulSoup.

Skrip ini dirancang untuk melakukan scraping data proyek dari Freelancer.com. Data yang diambil mencakup judul proyek, durasi tersisa, status, deskripsi, tag, harga, jumlah proposal, dan lokasi proyek. Data ini kemudian disimpan dalam file Excel untuk analisis lebih lanjut.

## Fitur

- Mengambil data proyek dari halaman Freelancer.com.
- Menyimpan data dalam format file Excel.
- Mendukung pengambilan data dari beberapa halaman.

## Instalasi

1. Pastikan kamu telah menginstal Python di komputer kamu. Jika belum, kunjungi [Python's official website](https://www.python.org/) untuk mengunduh dan menginstal Python.
2. Clone repositori ini ke komputer kamu atau unduh sebagai file ZIP dan ekstrak.
3. Buka terminal atau command prompt dan navigasikan ke direktori tempat kamu menyimpan repositori ini.
4. Install library yang diperlukan dengan menjalankan perintah berikut:

```bash
pip install -r requirements.txt
```


## Penggunaan

1. Jalankan skrip `main.py` dengan menjalankan perintah berikut di terminal:

```bash
python3 main.py -p 1
```


Skrip ini akan memulai proses scraping data dari Freelancer.com. Setelah proses selesai, hasilnya akan disimpan dalam file Excel dengan nama `output.xlsx` di direktori yang sama dengan skrip.

2. Buka file `output.xlsx` menggunakan aplikasi spreadsheet seperti Microsoft Excel, LibreOffice Calc, atau Google Sheets untuk melihat dan menganalisis data proyek yang telah diambil.

## Pengaturan Tambahan

- Kamu dapat mengubah flag `-p`  untuk menentukan jumlah  halaman yang akan di-scrape. Secara default, skrip ini akan mengambil data dari semua halaman di Freelancer.com.
- Jika menggunakan flag `-p 0` itu akan menelusiru semuaa halaman,agar mendapatkan data lebih banyak.

## Catatan

- Pastikan koneksi internet kamu stabil saat menjalankan skrip ini.
- Jika kamu ingin menghentikan proses scraping sebelum selesai, cukup tekan `Ctrl + C` di terminal.





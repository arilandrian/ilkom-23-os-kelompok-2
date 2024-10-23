# Proses Menjalankan Website Menggunakan Daemon Process dengan Xampp

## 1. Pengertian Daemon Process
Daemon process adalah jenis proses latar belakang (background process) yang berjalan tanpa interaksi langsung dari pengguna. Di sistem operasi berbasis Unix atau Linux, daemon biasanya digunakan untuk menangani tugas yang berulang, seperti server jaringan, pemantauan sistem, atau layanan sistem lainnya. Daemon akan terus berjalan, siap untuk merespons permintaan tertentu, bahkan setelah pengguna logout dari sistem.

## 2. preparation
Pada metode ini saya menggunakan **Xampp** dan untuk daemon process nya menggunakan **nssm**, kemudian buatlah database dan koneksikan ke website anda

### 2.1 Menginstall Xampp
1. Download Xampp ke komputer/laptop Anda, berikut link untuk mendownload Xampp (https://sourceforge.net/projects/xampp/files/XAMPP%20Windows/8.0.30/xampp-windows-x64-8.0.30-0-VS16-installer.exe)

2. Pastikan untuk menjalankan **apache** dan **mysql**

### 2.2 Menginstall nssm
NSSM adalah alat yang memungkinkan kita menjalankan daemon process sebagai service di Windows. Ikuti langkah-langkah berikut untuk menginstal NSSM:
1. Download **NSSM** dari situs resminya: [https://nssm.cc/download].
2. Ekstrak file yang diunduh ke direktori yang mudah diakses, di proses ini saya menginstall di  `E:\asda\nssm`.

### 2.3 Membuat struktur proyek 
## 3. Struktur Proyek
Buat struktur folder proyek Anda sebagai berikut:
```
E:\asda\xamppp\htdocs\game store  
    ├── connection   
    │   └── koneksi.php
    ├── daemon
    |   └── daemon_game_purchase.php
    ├── logs 
    |   └── purchase_log.txt
    └── index.php
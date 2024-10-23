
# Proses Menjalankan Website Menggunakan Daemon Process dengan Laragon

## 1. Pendahuluan
Website yang dibangun dapat memanfaatkan **daemon process** untuk menangani tugas-tugas otomatis yang perlu berjalan di latar belakang. Daemon process dapat digunakan untuk memproses data, mengelola antrian pesanan, atau menjalankan fungsi tertentu secara berkala tanpa interaksi langsung dari pengguna. Dalam panduan ini, kita akan menggunakan **Laragon** sebagai lingkungan pengembangan.

## 2. Persiapan
Sebelum memulai, pastikan Anda telah menginstal dan mengkonfigurasi lingkungan pengembangan seperti **Laragon** dan untuk daemon processnya menggunakan **NSSM**. Pastikan juga database Anda sudah siap dan terhubung dengan benar.

### 2.1. Instalasi Laragon
1. Unduh dan instal **Laragon** dari situs resminya.
2. Jalankan Laragon dan pastikan layanan Apache dan MySQL berjalan.

### 2.2. Instalasi NSSM
NSSM adalah alat yang memungkinkan kita menjalankan daemon process sebagai service di Windows. Ikuti langkah-langkah berikut untuk menginstal NSSM:
1. Unduh **NSSM** dari situs resminya: [https://nssm.cc/download].
2. Ekstrak file yang diunduh ke direktori yang mudah diakses, misalnya `C:\nssm`.

## 3. Struktur Proyek
Buat struktur folder proyek Anda sebagai berikut:
```
C:\laragon\www\mywebsite    
    ├── connection   
    │   └── koneksi.php
    ├── daemon
    |   └── daemon_process.php
    ├── logs 
    |   └── daemon_log.txt
    └── index.php
```

## 4. Membuat Daemon Process
Dalam file `daemon_process.php`, tuliskan logika untuk mengelola tugas latar belakang, misalnya memproses pesanan. Contoh kode untuk daemon process:
```php
<?php
include('../connection/koneksi.php');

// Pastikan folder logs ada
if (!file_exists('../logs')) {
    mkdir('../logs', 0777, true);
}

while (true) {
    // Ambil pesanan yang belum diproses
    $stmt = $db->prepare("SELECT * FROM orders WHERE status = 'belum diproses'");
    $stmt->execute();
    $orders = $stmt->fetchAll();

    foreach ($orders as $order) {
        // Proses pesanan (misalnya: ubah status pesanan)
        $stmt_update = $db->prepare("UPDATE orders SET status = 'diproses' WHERE id = ?");
        $stmt_update->execute([$order['id']]);

        // Dapatkan informasi tambahan untuk log
        $customerName = isset($order['nama_pelanggan']) ? $order['nama_pelanggan'] : 'Tidak Diketahui'; // Kolom yang benar
        $tableNumber = isset($order['nomor_meja']) ? $order['nomor_meja'] : 'Tidak Diketahui'; // Kolom yang benar
        $totalPrice = isset($order['total_harga']) ? $order['total_harga'] : 0; // Kolom yang benar

        // Log aktivitas pemrosesan
        $logMessage = "Pesanan ID: ".$order['id']." | Nama Pelanggan: ".$customerName." | No Meja: ".$tableNumber." | Total Harga: Rp ".$totalPrice." | Diproses pada ".date('Y-m-d H:i:s')."\n";
        
        // Menulis log
        file_put_contents($logFile, $logMessage, FILE_APPEND);
        
        // Output ke terminal (opsional)
        echo $logMessage;
    }

    // Tunggu 10 detik sebelum memeriksa lagi
    sleep(10);
}
?>

```

## 5. Menjalankan Daemon Process dengan NSSM
NSSM digunakan untuk menjalankan `daemon_process.php` sebagai service di Windows agar proses ini tetap berjalan meskipun terminal ditutup.

### 5.1 Menambahkan Service dengan NSSM
1. Buka Command Prompt atau PowerShell sebagai Administartor.
2. Jalankan perintah berikut untuk menambah service:

```
C:\nssm\nssm.exe install PHPDaemon
```
3. Setelah menjalankan perintah tersebut, akan muncul GUI. Isi konfigurasi berikut:
- Path: arahkan ke executable PHP di Laragon, misalnya `C:\laragon\bin\php\php-7.x.x-Win32\php.exe`
- Startup directory: arahkan ke direktori proyek Anda, misalnya
`C:\laragon\www\mywebsite\daemon`
- Arguments: tambahkan daemon_process.php agar PHP menjalankan file daemon tersebut.
4. Klik Install Service

### 5.2 Menjalankan Service
Setelah service berhasil ditambahkan,jalankan service dengan perintah berikut:
`.\nssm.exe start PHPDaemon`

## 6. Memantau Log
Log aktivitas daemon process akan disimpan di `logs/daemon_log.txt`. Anda bisa membuka file ini untuk melihat pesan terkait pemrosesan pesanan yang telah dilakukan oleh daemon process.

## 7.Bukti Screenshoot Program Berhasil Berjalan
## Tampilan Start dan Stop Daemon Service (PHPDaemon)
![Bukti Screenshoot](https://drive.google.com/uc?id=1K6ckJkt3BYGZKNJAKCnLIv7nAExrwVBY)

## Tampilan Website
![Bukti Screenshoot](https://drive.google.com/uc?id=1mR39iXyg4TC7oglQ5sBKRtDO_Z2rz74L)

## Berhasil Membuat Pesanan
![Bukti Screenshoot](https://drive.google.com/uc?id=1B8SaN9RWdvFAZYK0vtVBP3tRberxKgsd)

## Daemon Process Menampilkan Log Pesanan
![Bukti Screenshoot](https://drive.google.com/uc?id=1wyQMBKwPcnvWxbeSZCQ6_L5cf_MNPtmN)
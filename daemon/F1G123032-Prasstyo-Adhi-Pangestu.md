# Proses Menjalankan Website Menggunakan Daemon Process dengan Xampp

## 1. Pengertian Daemon Process
Daemon process adalah jenis proses latar belakang (background process) yang berjalan tanpa interaksi langsung dari pengguna. Di sistem operasi berbasis Unix atau Linux, daemon biasanya digunakan untuk menangani tugas yang berulang, seperti server jaringan, pemantauan sistem, atau layanan sistem lainnya. Daemon akan terus berjalan, siap untuk merespons permintaan tertentu, bahkan setelah pengguna logout dari sistem.

## 2. preparation
Pada metode ini saya menggunakan **Xampp** dan untuk daemon process nya menggunakan **nssm**, kemudian buatlah database dan koneksikan ke website anda, di website yang saya buat adalah website untuk mengelola pembelian game

### 2.1 Menginstall Xampp
1. Download Xampp ke komputer/laptop Anda, berikut link untuk mendownload Xampp (https://sourceforge.net/projects/xampp/files/XAMPP%20Windows/8.0.30/xampp-windows-x64-8.0.30-0-VS16-installer.exe)

2. Pastikan untuk menjalankan **apache** dan **mysql**

### 2.2 Menginstall nssm
NSSM adalah alat yang memungkinkan kita menjalankan daemon process sebagai service di Windows. Ikuti langkah-langkah berikut untuk menginstal NSSM:
1. Download **NSSM** dari situs resminya: [https://nssm.cc/download].
2. Ekstrak file yang diunduh ke direktori yang mudah diakses, di proses ini saya menginstall di  `E:\asda\nssm`.

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
    └── purchase.php
    └── style.css
```

## 4. Membuat Daemon Process
Dalam file `daemon_game_purchase.php`, tuliskan logika untuk mengelola tugas latar belakang, untuk memproses pembelian game. Contoh kode untuk daemon process:
```php
<?php
include('../connection/koneksi.php');

// Pastikan folder logs ada
if (!file_exists('../logs')) {
    mkdir('../logs', 0777, true);
}

// Nama file log
$logFile = '../logs/purchase_log.txt';

while (true) {
    // Ambil pembelian yang belum diproses
    $stmt = $db->prepare("SELECT * FROM purchases WHERE status = 'belum diproses'");
    $stmt->execute();
    $purchases = $stmt->fetchAll();

    foreach ($purchases as $purchase) {
        // Proses pembelian (misalnya: ubah status pembelian)
        $stmt_update = $db->prepare("UPDATE purchases SET status = 'diproses' WHERE id = ?");
        $stmt_update->execute([$purchase['id']]);

        // Dapatkan informasi untuk log
        $gameName = isset($purchase['nama_game']) ? $purchase['nama_game'] : 'Tidak Diketahui';
        $buyerName = isset($purchase['nama_pembeli']) ? $purchase['nama_pembeli'] : 'Tidak Diketahui';
        $price = isset($purchase['harga']) ? $purchase['harga'] : 0;

        // Buat pesan log
        $logMessage = "Pembelian ID: ".$purchase['id']." | Nama Game: ".$gameName." | Nama Pembeli: ".$buyerName." | Harga: Rp ".number_format($price, 0, ',', '.')." | Diproses pada ".date('Y-m-d H:i:s')."\n";

        // Menulis log ke file
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
NSSM digunakan untuk menjalankan `daemon_game_purchase.php` sebagai service di Windows agar proses ini tetap berjalan meskipun terminal ditutup.

### 5.1 Menambahkan Service dengan NSSM
1. Buka Command Promt atau PowerShell sebagai Administartor.
2. Jalankan perintah berikut untuk menambah service:

```
E:\asda\nssm\nssm-2.24\win64\nssm.exe install DaemonPHP
```
3. Setelah menjalankan perintah tersebut, akan muncul GUI. Isi konfigurasi berikut:
- Path: arahkan ke php.exe pada folder di Xampp, misalnya `E:\asda\xamppp\php\php.exe`
- Startup directory: arahkan ke direktori proyek Anda, misalnya
`E:\asda\xamppp\htdocs\game store\daemon`
- Arguments: tambahkan daemon_game_purchase.php agar PHP menjalankan file daemon tersebut.
4. Klik Install Service

### 5.2 Menjalankan Service
Setelah service berhasil ditambahkan,jalankan service dengan perintah berikut:
`.\nssm start PHPDaemon`

## 6. Memantau Log
Log aktivitas daemon process akan disimpan di `logs/purchase_log.txt`. Anda bisa membuka file ini untuk melihat pesan terkait pemrosesan pesanan yang telah dilakukan oleh daemon process.

## 7. Hasil Screenshot Program 
## Tampilan Start Daemon menggunakan nssm
![Bukti Screenshoot](https://drive.google.com/uc?export=view&id=1gz0lC_Aa3MM3qZU_-BsWfC6dbedO1Ljw/view?usp=sharing)

## Tampilan Wesbsite Pemesanan Game
### 1. Website Pembelian
![Bukti Screenshoot](https://drive.google.com/file/d/1hEmO78vwro4p98iogaDBKEyDlqfZRLYW/view?usp=drive_link)
### 2. Tampilan daftar pembelian game
![Bukti Screenshoot](https://drive.google.com/file/d/1hEmO78vwro4p98iogaDBKEyDlqfZRLYW/view?usp=drive_link)
### 3. Pemesanan Berhasil
![Bukti Screenshoot](https://drive.google.com/file/d/1TZKI4uGi8v1FoIHwX7VfPTLgrTFULQ7K/view?usp=drive_link)

## Menampilkan log pesanan
![Bukti Screenshoot](https://drive.google.com/file/d/1fbcg0sFzSjo18AZcWye7KsVd6YqdZgtj/view?usp=drive_link)

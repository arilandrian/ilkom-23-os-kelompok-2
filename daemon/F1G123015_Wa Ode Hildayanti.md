# Proses Menjalankan Website Daftar Hadir dengan Daemon Process menggunakan Laragon

## 1. Pendahuluan
Pada kesempatan ini, kita akan membahas penggunaan proses daemon untuk menangani tugas-tugas yang berjalan di latar belakang, seperti pemrosesan data secara otomatis tanpa perlu interaksi langsung dari pengguna. Proses daemon ini akan memfasilitasi pengelolaan antrian kehadiran dan memprosesnya secara otomatis setiap beberapa detik. Pengembangan akan dilakukan dengan menggunakan Laragon sebagai server lokal, sementara daemon akan diimplementasikan menggunakan NSSM agar dapat berjalan terus-menerus sebagai layanan di Windows.

## 2. Persiapan
Sebelum memulai, pastikan software yang diperlukan Anda sudah siap, termasuk:
- **Laragon** sebagai server lokal
- **NSSM** (Non-Sucking Service Manager) sebagai tool untuk menjalankan PHP sebagai service di Windows

### 2.1. Instalasi Laragon
1. Unduh dan instal **Laragon** dari [laragon.org](https://laragon.org/download).
2. Jalankan Laragon dan pastikan layanan Apache dan MySQL aktif.

### 2.2. Instalasi NSSM
1. Unduh **NSSM** dari situs resminya [nssm.cc](https://nssm.cc/download).
2. Ekstrak file ke direktori seperti `D:\nssm`.
3. Gunakan NSSM untuk menjalankan file PHP daemon sebagai service.


## 3. Struktur Proyek
Struktur folder proyek Anda sebagai berikut:
```
C:\laragon\www\daemon-project2
├── daemon.php
├── index.php
├── daemon_log.txt
└── daemon_queue.txt
```
- **daemon.php**: Berisi file daemon untuk menjalankan proses latar belakang.
- **daemon_log.txt**: Berisi log file dari proses daemon.
- **index.php**: File untuk menangani input dari pengguna (konfirmasi kehadiran).
- **daemon_queue**: Menyimpan data antrian kehadiran.


## 4. Implementasi Daemon Process
Saya membuat contoh website dengan php, contoh kasus yang saya ambil merupakan **Website Penghitung Jumlah Pengunjung dalam suatu Website**
File `daemon.php` akan menangani pemrosesan antrian kehadiran yang dimasukkan melalui `index.php`.

### 4.1. Isi dari `index.php`
```php
<!DOCTYPE html>
<html>
<head>
    <title>Sistem Daftar Hadir Digital</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f2f5;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            width: 90%;
            max-width: 600px;
            margin: 20px;
        }
        h2, h3 {
            color: #1a73e8;
            text-align: center;
            margin-bottom: 30px;
        }
        .input-group {
            margin-bottom: 20px;
        }
        input {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 5px;
            font-size: 16px;
            transition: border-color 0.3s;
            box-sizing: border-box;
        }
        input:focus {
            border-color: #1a73e8;
            outline: none;
        }
        button {
            width: 100%;
            padding: 12px;
            background-color: #1a73e8;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #1557b0;
        }
        .success {
            color: #0f9d58;
            background: #e6f4ea;
            padding: 10px;
            border-radius: 5px;
            margin-top: 20px;
            text-align: center;
        }
        .error {
            color: #d93025;
            background: #fce8e6;
            padding: 10px;
            border-radius: 5px;
            margin-top: 20px;
            text-align: center;
        }
        .time {
            text-align: center;
            color: #5f6368;
            margin-top: 20px;
            font-size: 14px;
        }
        .attendance-list {
            margin-top: 30px;
            padding-top: 20px;
            border-top: 2px solid #e0e0e0;
        }
        .attendance-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }
        .attendance-table th,
        .attendance-table td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #e0e0e0;
        }
        .attendance-table th {
            background-color: #f8f9fa;
            color: #1a73e8;
        }
        .attendance-table tr:hover {
            background-color: #f8f9fa;
        }
        .no-data {
            text-align: center;
            color: #5f6368;
            padding: 20px;
            font-style: italic;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Daftar Hadir Digital</h2>
        <form method="POST" action="index.php">
            <div class="input-group">
                <input type="text" name="nama" placeholder="Masukkan nama Anda" required>
            </div>
            <button type="submit" name="hadir">Konfirmasi Kehadiran</button>
        </form>
        <div id="message">
        <?php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['hadir'])) {
    $nama = trim($_POST['nama']);
    $timestamp = date('Y-m-d H:i:s');
    
    // Cek apakah sudah ada entri yang sama dalam 5 detik terakhir
    $isDoubleClick = false;
    if (file_exists('daemon_log.txt')) {
        $logs = file_get_contents('daemon_log.txt');
        $lastEntry = "Kehadiran tercatat - Nama: $nama, Waktu:";
        if (strpos($logs, $lastEntry) !== false) {
            $entries = explode("\n", $logs);
            foreach ($entries as $entry) {
                if (strpos($entry, $lastEntry) !== false) {
                    $entryTime = strtotime(substr($entry, 1, 19)); // Ambil timestamp dari log
                    if (time() - $entryTime < 5) { // Cek jika entri dalam 5 detik terakhir
                        $isDoubleClick = true;
                        break;
                    }
                }
            }
        }
    }
    
    if (!$isDoubleClick) {
        $data = "$nama|$timestamp\n";
        file_put_contents('daemon_queue.txt', $data, FILE_APPEND);
        echo "<div class='success'>
                <strong>Kehadiran berhasil tercatat</strong><br>
                Nama: $nama
                <div class='time'>Waktu: $timestamp</div>
              </div>";
    } else {
        echo "<div class='error'>
                <strong>Mohon tunggu sebentar</strong><br>
                Kehadiran Anda sudah tercatat
              </div>";
    }
}
?>
        </div>

        <div class="attendance-list">
            <h3>Daftar Kehadiran Hari Ini</h3>
            <?php
            $logFile = 'daemon_log.txt';
            if (file_exists($logFile) && filesize($logFile) > 0) {
                $logs = file_get_contents($logFile);
                $entries = array_filter(explode("\n", $logs));
                
                if (!empty($entries)) {
                    echo '<table class="attendance-table">
                            <thead>
                                <tr>
                                    <th>No</th>
                                    <th>Nama</th>
                                    <th>Waktu</th>
                                </tr>
                            </thead>
                            <tbody>';
                    
                    $no = 1;
                    foreach (array_reverse($entries) as $entry) {
                        if (preg_match('/\[(.*?)\] Kehadiran tercatat - Nama: (.*?), Waktu: (.*)/', $entry, $matches)) {
                            $waktuLog = $matches[1];
                            $nama = $matches[2];
                            $waktuHadir = $matches[3];
                            
                            echo "<tr>
                                    <td>$no</td>
                                    <td>$nama</td>
                                    <td>$waktuHadir</td>
                                  </tr>";
                            $no++;
                        }
                    }
                    
                    echo '</tbody></table>';
                } else {
                    echo '<div class="no-data">Belum ada data kehadiran</div>';
                }
            } else {
                echo '<div class="no-data">Belum ada data kehadiran</div>';
            }
            ?>
        </div>
    </div>
</body>
</html>
```
### 4.1. Isi dari `daemon.php`

```php
<?php
// Fungsi untuk menulis log
function tulisLog($pesan) {
    $berkaLog = 'daemon_log.txt';
    $waktu = date('Y-m-d H:i:s');
    file_put_contents($berkaLog, "[$waktu] $pesan\n", FILE_APPEND);
}

// Fungsi untuk memproses antrian kehadiran
function prosesAntrian() {
    $berkaAntrian = 'daemon_queue.txt';
    
    if (file_exists($berkaAntrian) && filesize($berkaAntrian) > 0) {
        $data = file_get_contents($berkaAntrian);
        $baris = explode("\n", trim($data));
        
        // Kosongkan file antrian
        file_put_contents($berkaAntrian, '');
        
        foreach ($baris as $baris) {
            if (empty($baris)) continue;
            
            list($nama, $waktu) = explode('|', $baris);
            tulisLog("Kehadiran tercatat - Nama: $nama, Waktu: $waktu");
        }
    }
}

// Loop daemon
while (true) {
    prosesAntrian();
    sleep(5); // Tunggu 5 detik sebelum cek lagi
}
```

## 5. Menjalankan Daemon Process Menggunakan NSSM
NSSM digunakan untuk menjalankan daemon.php sebagai service di Windows agar proses ini tetap berjalan meskipun terminal ditutup.

### 5.1 Menambahkan Service dengan NSSM
1. Buka Command Prompt atau PowerShell sebagai Administrator.
2. Jalankan perintah berikut untuk menambah service:

```
D:\nssm-2.24\win64>nssm install DaemonAbsen
```
3. Setelah menjalankan perintah tersebut, akan muncul GUI. Isi konfigurasi berikut:
- Path: arahkan ke executable PHP di Laragon, misalnya `D:\laragon\bin\php\php-8.x.x-Win32\php.exe`
- Startup directory: arahkan ke direktori proyek Anda, misalnya
  `D:\laragon\www\daemon-project`
- Arguments: tambahkan daemon.php agar PHP menjalankan file daemon tersebut.
4. Klik Install Service

### 5.2 Menjalankan Service
Setelah service berhasil ditambahkan,jalankan service dengan perintah berikut:
`nssm start DaemonAbsen`


## 6. Memantau Log
Log aktivitas daemon process akan disimpan di `daemon_log.txt`. Anda bisa membuka file ini untuk melihat pesan terkait pemrosesan pesanan yang telah dilakukan oleh daemon process.


## 7. Menjalankan Daemon Process
1. Buka command line di Laragon.
2. Arahkan ke direktori proyek Anda:
   ```bash
   cd C:\laragon\www\daemon-project
   ```
3. Jalankan daemon process dengan perintah:
   ```bash
   php daemon.php
   ```
4. Pastikan daemon process berjalan di latar belakang dan memperbarui statistik secara otomatis.

## 7. Memantau Statistik dan Log
Data pengunjung dan statistik akan disimpan di `visitors.txt` dan `stats.json`, sedangkan log aktivitas daemon akan disimpan di `daemon.log`. Anda bisa membuka file ini untuk melihat pesan terkait aktivitas yang telah dilakukan oleh daemon process.

## 8. Bukti Screenshoot Program Berhasil Berjalan

## Tampilan Website
![Bukti Screenshoot](https://drive.google.com/uc?id=1QQlNuUlQgUvpkRPkjx5fmhNSX4BPnbbO)
## Tampilan Website Berhasil Menghitung Pengunjung
![Bukti Screenshoot](https://drive.google.com/uc?id=1QQlNuUlQgUvpkRPkjx5fmhNSX4BPnbbO)
## Daemon Process Berhasil Menampilkan Log Aktivitas
![Bukti Screenshoot](https://drive.google.com/uc?id=1-Eec5YCiVUPeHLUHWXgaDjERy2qW8gCO)
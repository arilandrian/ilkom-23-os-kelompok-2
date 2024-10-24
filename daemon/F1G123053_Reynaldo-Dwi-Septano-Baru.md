# Menjalankan Process daemon di laragon

## 1. Pengertian Daemon Process
Daemon process, seringkali disebut hanya sebagai "daemon", adalah sebuah program komputer yang berjalan di latar belakang sistem operasi tanpa memerlukan interaksi langsung dari pengguna. Daemon ini terus berjalan, menjalankan tugas-tugas tertentu secara otomatis, dan menyediakan layanan yang diperlukan oleh sistem atau aplikasi lainnya.

## 2. Pengertian Laragon
Laragon adalah sebuah lingkungan pengembangan (development environment) lokal yang populer di kalangan pengembang web. Ia menyediakan platform yang terintegrasi untuk menjalankan berbagai macam bahasa pemrograman dan server, seperti PHP, Node.js, Python, dan database seperti MySQL. Singkatnya, Laragon adalah seperti sebuah laboratorium mini bagi para pengembang untuk menguji dan mengembangkan aplikasi web mereka secara lokal sebelum di-deploy ke server yang sebenarnya.

Dalam konteks Laragon, daemon berperan sebagai "mesin" yang menggerakkan berbagai layanan yang disediakan oleh Laragon, seperti server web Apache, database MySQL, dan lain-lain.

## 3. Siapkan Lingkungan Pengembangan
1. Unduh [Laragon](https://laragon.org/download) dari situs resmi.
2. Install Laragon dan pastikan server Apache dan MySQL berjalan.

## 4. Struktur File Website
Buatlah folder website anda sebagai berikut:

```php
/login.app 
      /activity_daemon.php
      /index.php
      /logout.php
      /welcome.php
      /activity.log

```

### A. File index.php
File ini akan menampilkan form login:

```php
<!-- index.php -->
<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Ganti dengan username dan password yang diinginkan
    $username = 'reyy';
    $password = '123';

    if ($_POST['username'] == $username && $_POST['password'] == $password) {
        $_SESSION['loggedin'] = true;

        // Menyimpan aktivitas login ke new_activity.log
        file_put_contents('new_activity.log', "User '$username' logged in.");
        
        header('Location: welcome.php');
        exit;
    } else {
        $error = 'Username atau Password salah!';
    }
}
?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-container {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .login-container h2 {
            margin: 0 0 20px;
        }
        .login-container input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
        }
        .login-container button {
            width: 100%;
            padding: 10px;
            background-color: #28a745;
            color: white;
            border: none;
            cursor: pointer;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>

<div class="login-container">
    <h2>Login</h2>
    <?php if (isset($error)): ?>
        <div class="error"><?php echo $error; ?></div>
    <?php endif; ?>
    <form method="POST" action="">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
</div>

</body>
</html>

```

### B. File welcome.php
File ini akan memproses login:

```php
<!-- welcome.php -->
<?php
session_start();

if (!isset($_SESSION['loggedin'])) {
    header('Location: index.php');
    exit;
}
?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f4f8;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #333;
        }
        .container {
            text-align: center;
            background-color: #ffffff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        h1 {
            color: #4CAF50;
        }
        p {
            font-size: 18px;
        }
        a {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 15px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        a:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Selamat datang!</h1>
        <p>Anda telah berhasil login.</p>
        <a href="logout.php">Logout</a>
    </div>
</body>
</html>


```
### C. File logout.php
File ini akan berfungsi sebagai daemon yang berjalan di latar belakang.

```php
<!-- logout.php -->
<?php
session_start();

if (isset($_SESSION['loggedin'])) {
    $username = 'reyy'; // Ganti dengan variabel username jika diperlukan

    // Menyimpan aktivitas logout ke new_activity.log
    file_put_contents('new_activity.log', "User '$username' logged out.");
    
    session_destroy(); // Menghancurkan sesi
}

// Redirect ke halaman login
header('Location: index.php');
exit;
?>

```

### D. File activity_daemon.php
File ini akan menangani logout.

```php
<!-- activity.php -->
<?php
set_time_limit(0); // Biarkan skrip berjalan terus menerus

$logFile = 'activity.log';

// Fungsi untuk mencatat aktivitas
function logActivity($message) {
    global $logFile;
    $currentDateTime = date('Y-m-d H:i:s');
    file_put_contents($logFile, "[$currentDateTime] $message" . PHP_EOL, FILE_APPEND);
}

// Simulasi daemon yang akan mencatat aktivitas
while (true) {
    // Cek apakah ada aktivitas baru di log
    // Misalnya, Anda dapat menggunakan file untuk menyimpan aktivitas login/logout
    if (file_exists('new_activity.log')) {
        $activityData = file_get_contents('new_activity.log');
        if (!empty($activityData)) {
            logActivity($activityData);
            // Kosongkan file setelah dibaca
            file_put_contents('new_activity.log', '');
        }
    }
    sleep(5); // Tunggu 5 detik sebelum memeriksa lagi
}
?>

```

## 5. Menjalankan Program sebagai Daemon
Untuk menjalankan daemon.php sebagai daemon, lakukan langkah berikut:

### Buat Folder activtiy.log 
Pertama, kita perlu membuat file log di mana aktivitas pengguna akan dicatat. Anda bisa membuat file dengan nama activity.log di dalam folder web kalian.
1. Buka folder tempat kalian ingin membuat activity.log nya 
2. Buat file baru bernama activity.log.

### Menggunakan terminal
1. Buka terminal (command prompt) dan navigasikan ke folder proyek Anda:

```bash
cd C:\laragon\www\login_app

```

2. Jalankan daemon.php menggunakan PHP:

```bash
 php activity_daemon.php 


```

Dengan cara ini, daemon akan berjalan dibelakang

## 6. Pengujian
1. Buka browser dan kunjungi http://localhost/login_app/index.php.
2. Masukkan username admin dan password 123, lalu klik "Login".
3. Setelah berhasil login, daemon akan mulai mengirim file log ke activtity.log yang sudah di buat tadi
4. Untuk melihat log, buka activity.log di folder yang kalian taruh tadi.

## 7. Menghentikan Daemon
Untuk menghentikan daemon yang berjalan temukan PID-nya dan gunakan perintah kill

### Temukan PID dengan perintah:
```bash
tasklist | findstr php

```

### Setelah menemukan PID yang sesuai, gunakan perintah kill untuk menghentikan proses:
```bash
taskkill /PID <PID_NUMBER> /F

```
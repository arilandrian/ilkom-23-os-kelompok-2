# Materi Linux

## Pengantar Linux
Linux adalah sistem operasi berbasis open-source yang banyak digunakan pada server, perangkat desktop, perangkat mobile, hingga superkomputer. Linux dikenal karena keamanannya, stabilitasnya, dan fleksibilitasnya dalam berbagai kebutuhan.

## Struktur Dasar Linux

### 1. **Kernel**
Kernel adalah inti dari sistem operasi yang mengelola hardware, memori, dan proses.

### 2. **Shell**
Shell adalah antarmuka pengguna yang memungkinkan pengguna menjalankan perintah untuk berinteraksi dengan sistem operasi.
- Contoh shell: Bash, Zsh, Fish
### 3. **File System**
Linux menggunakan struktur file berbasis hierarki dengan root (`/`) sebagai direktori utama.

### 4. **Distribution (Distro)**
Distribusi Linux adalah variasi Linux yang disesuaikan untuk kebutuhan tertentu.
- Contoh distro: Ubuntu, Fedora, Debian, CentOS, Arch Linux.

## Perintah Dasar Linux

| Perintah                          | Fungsi                                    |
|-----------------------------------|------------------------------------------|
| `ls`                              | Menampilkan daftar file dan direktori    |
| `cd`                              | Berpindah direktori                      |
| `pwd`                             | Menampilkan direktori kerja saat ini     |
| `mkdir [nama_folder]`             | Membuat direktori baru                   |
| `rm [nama_file/direktori]`        | Menghapus file atau direktori            |
| `cp [sumber] [tujuan]`            | Menyalin file atau direktori             |
| `mv [sumber] [tujuan]`            | Memindahkan atau mengganti nama file     |
| `touch [nama_file]`               | Membuat file kosong baru                 |
| `cat [nama_file]`                 | Menampilkan isi file                     |
| `man [perintah]`                  | Menampilkan dokumentasi perintah         |
| `chmod`                           | Mengubah izin file atau direktori        |
| `chown`                           | Mengubah kepemilikan file atau direktori |
## Struktur File Linux

| Direktori         | Deskripsi                              |
|-------------------|----------------------------------------|
| `/`               | Root direktori                        |
| `/home`           | Direktori pengguna                    |
| `/etc`            | File konfigurasi                      |
| `/var`            | File log dan data variabel            |
| `/usr`            | Aplikasi dan utilitas sistem          |
| `/bin`            | Biner eksekusi dasar                  |
| `/dev`            | Perangkat keras                       |
| `/tmp`            | File sementara                        |
| `/proc`           | Informasi proses                      |

## Manajemen Proses
## Manajemen Proses

| Perintah                          | Fungsi                                    |
|-----------------------------------|------------------------------------------|
| `ps`                              | Menampilkan daftar proses                |
| `top`                             | Menampilkan proses secara interaktif     |
| `kill [PID]`                      | Menghentikan proses berdasarkan PID      |
| `jobs`                            | Menampilkan daftar proses latar belakang |
| `fg`                              | Mengembalikan proses ke latar depan      |
| `bg`                              | Menjalankan proses di latar belakang     |

## Manajemen Paket
Manajemen paket tergantung pada distro Linux yang digunakan:

- **Debian/Ubuntu (APT):**
  ```bash
  sudo apt update          # Memperbarui daftar paket
  sudo apt install [nama]  # Menginstal paket
  sudo apt remove [nama]   # Menghapus paket
  ```
- **Red Hat/Fedora (DNF/YUM):**
  ```bash
  sudo dnf install [nama]  # Menginstal paket
  sudo dnf remove [nama]   # Menghapus paket
  ```

- **Arch Linux (Pacman):**
  ```bash
  sudo pacman -S [nama]    # Menginstal paket
  sudo pacman -R [nama]    # Menghapus paket
  ```

## Tips dan Trik Linux

1. **Tab Completion**: Tekan `Tab` untuk melengkapi nama file atau perintah.
2. **History Command**: Gunakan `history` untuk melihat perintah yang telah dijalankan.
3. **Shortcut Keyboard**:
   - `Ctrl + C`: Menghentikan proses yang berjalan.
   - `Ctrl + Z`: Menangguhkan proses yang berjalan.
   - `Ctrl + D`: Keluar dari shell.
## Contoh Skrip Bash Sederhana
Membuat file skrip bernama `hello.sh`:
```bash
#!/bin/bash

# Skrip sederhana

echo "Hello, Linux!"
```
Jalankan skrip:
```bash
chmod +x hello.sh
./hello.sh
```

## Kesimpulan
Linux adalah sistem operasi yang kuat dan fleksibel. Dengan memahami perintah dasar dan struktur file, Anda dapat memaksimalkan penggunaan Linux untuk berbagai kebutuhan.

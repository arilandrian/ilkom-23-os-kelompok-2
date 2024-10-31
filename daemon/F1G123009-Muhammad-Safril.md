# MENJALANKAN DAEMON PROCESS DI WSL
## Deskripsi
Dokumentasi ini menjelaskan cara membuat dan menggunakan skrip untuk menjalankan dan menghentikan daemon server
## Langkah-langkah
# Disclaimer silahkan buat nama directory sesuai yang anda inginkan disini saya menggunakan nama 'coba_daemon'.
## 1. Buat directori untuk script
masuk sebagai superuser, lalu jalankan perintah
```bash
sudo mkdir -p /opt/coba_daemon
cd /opt/coba_daemon

#Buat script daemon
sudo nano coba_daemon.sh
```
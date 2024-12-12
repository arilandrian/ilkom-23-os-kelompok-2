# Materi Docker
## Pengantar Docker
Docker adalah platform containerization yang memungkinkan Anda untuk mengemas aplikasi dan semua dependensinya ke dalam sebuah container yang ringan dan portabel. Dengan Docker, Anda dapat:
- Membuat aplikasi yang dapat berjalan konsisten di berbagai lingkungan.
- Menghemat sumber daya karena container lebih ringan dibanding virtual machine.
# Konsep Dasar Docker

### 1. **Image**
Image adalah template read-only yang digunakan untuk membuat container. Sebuah image bisa berisi sistem operasi, aplikasi, dan dependensi.
- Contoh: `ubuntu:latest`, `nginx:alpine`
### 2. **Container**
Container adalah instance dari image. Container bersifat runtime dan dapat dimodifikasi selama berjalan.
- Perintah untuk membuat container dari image:
  ```bash
  docker run [OPTIONS] IMAGE_NAME[:TAG]
  ```
### 3. **Dockerfile**
Dockerfile adalah file teks yang berisi instruksi untuk membangun image secara otomatis.
- Contoh Dockerfile sederhana:
  ```dockerfile
  FROM ubuntu:latest
  RUN apt-get update && apt-get install -y python3
  CMD ["python3"]
  ```
### 4. **Docker Hub**
Docker Hub adalah repositori online tempat menyimpan dan berbagi image Docker.
- Untuk menarik (pull) image dari Docker Hub:
  ```bash
  docker pull IMAGE_NAME[:TAG]
  ```
### 5. **Volume**
Volume digunakan untuk menyimpan data agar tetap persisten, meskipun container dihentikan atau dihapus.
- Contoh perintah untuk menggunakan volume:
  ```bash
  docker run -v /host/path:/container/path IMAGE_NAME
  ```
## Perintah Dasar Docker

| Perintah                          | Deskripsi                                    |
|-----------------------------------|---------------------------------------------|
| `docker --version`                | Mengecek versi Docker yang terinstal        |
| `docker images`                   | Melihat daftar image yang tersedia          |
| `docker ps`                       | Melihat container yang sedang berjalan      |
| `docker ps -a`                    | Melihat semua container                     |
| `docker run [OPTIONS] IMAGE_NAME` | Menjalankan container dari image            |
| `docker stop CONTAINER_ID`        | Menghentikan container                      |
| `docker rm CONTAINER_ID`          | Menghapus container                         |
| `docker rmi IMAGE_ID`             | Menghapus image                             |
## Contoh Penggunaan Docker

### 1. **Menjalankan Aplikasi Web**
Menjalankan server Nginx:
```bash
docker run -d -p 8080:80 nginx
```
Akses aplikasi di browser: `http://localhost:8080`

### 2. **Membangun Image dari Dockerfile**
- Buat file `Dockerfile`:
  ```dockerfile
  FROM python:3.9-slim
  COPY app.py /app/
  CMD ["python", "/app/app.py"]
  ```
- Bangun image:
  ```bash
  docker build -t my-python-app .
  ```
- Jalankan container:
  ```bash
  docker run my-python-app
  ```
### 3. **Menggunakan Volume**
Menyimpan data dari container ke host:
```bash
docker run -v /host/data:/container/data ubuntu touch /container/data/example.txt
```

# Dasar-Dasar Docker

"""
Docker adalah platform berbasis container yang memungkinkan pengembang untuk membuat, mengemas, dan menjalankan aplikasi dengan cara yang ringan dan terisolasi. Berikut adalah beberapa konsep dasar Docker yang penting untuk dipahami:
"""

# 1. Container
print("Container adalah unit runtime yang ringan dan portabel untuk aplikasi Anda, termasuk semua dependensi (kode, runtime, libraries, dll).")
print("Contoh: Anda dapat menjalankan aplikasi Python, Node.js, atau bahkan server web seperti Nginx dalam container.")

# 2. Image
print("Image adalah template baca-saja yang digunakan untuk membuat container.")
print("Image dibangun dari Dockerfile dan bisa diunduh dari Docker Hub atau registry lain.")
print("Contoh: nginx, python, mysql.")

# 3. Dockerfile
print("Dockerfile adalah file teks berisi instruksi untuk membangun image Docker.")
print("Contoh sederhana:")
print("""
  FROM python:3.9
  WORKDIR /app
  COPY . .
  RUN pip install -r requirements.txt
  CMD [\"python\", \"app.py\"]
""")

# 4. Docker Hub
print("Docker Hub adalah registry cloud publik tempat Anda dapat mencari, mengunduh, atau mengunggah image Docker.")

# 5. Perintah Dasar Docker
print("Berikut adalah perintah-perintah dasar Docker:")

# a. Periksa Versi
os.system("docker --version")

# b. Menarik Image
print("Menarik image nginx...")
os.system("docker pull nginx")

# c. Menjalankan Container
print("Menjalankan container nginx...")
os.system("docker run -d --name my-container -p 8080:80 nginx")

# d. Melihat Container yang Berjalan
print("Melihat container yang berjalan...")
os.system("docker ps")

# e. Menghentikan dan Menghapus Container
print("Menghentikan container...")
os.system("docker stop my-container")
print("Menghapus container...")
os.system("docker rm my-container")

# f. Melihat Daftar Image
print("Melihat daftar image...")
os.system("docker images")

# g. Menghapus Image yang Tidak Digunakan
print("Menghapus image yang tidak digunakan...")
os.system("docker image prune -f")

# 6. Keuntungan Docker
print("Keuntungan Docker:")
print("- Portabilitas: Bisa dijalankan di mana saja, selama Docker terinstal.")
print("- Isolasi: Aplikasi dijalankan secara terpisah dari sistem host.")
print("- Efisiensi: Lebih ringan dibandingkan VM (Virtual Machine).")
print("- Reproduksibilitas: Memastikan aplikasi berjalan sama di lingkungan pengembangan dan produksi.")

# 7. Arsitektur Docker
print("Docker terdiri dari beberapa komponen:")
print("- Docker Engine: Mesin inti untuk membangun, menjalankan, dan mengelola container.")
print("- Docker Daemon: Proses yang berjalan di latar belakang untuk menangani container.")
print("- Docker CLI: Alat command-line untuk berinteraksi dengan Docker.")
print("- Docker Compose: Alat untuk mengelola aplikasi multi-container dengan file docker-compose.yml.")

print("Selesai! Anda telah mempelajari dasar-dasar Docker.")

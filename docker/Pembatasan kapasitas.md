# 1. Membatasi CPU
Docker memungkinkan Anda membatasi penggunaan CPU oleh container.
```bash
$ Docker run --cpus=2 my_container
```
# 2. Membatasi Memori (RAM)
Dapat menentukan batas memori maksimum yang bisa digunakan oleh container.
```bash
$ docker run --memory=512m my_container
```
Container ini hanya akan menggunakan maksimum 512 MB RAM.

# 3. Membatasi CPU dan RAM Secara Bersamaan
Gabungkan opsi --cpus dan --memory untuk membatasi keduanya.
```bash
$ docker run --cpus=1.5 --memory=1g my_container
```
Container ini akan menggunakan maksimum 1,5 core CPU dan 1 GB RAM.

# 4. Membatasi Storage (Disk Usage)
Docker mendukung pembatasan penggunaan disk menggunakan --storage-opt. Ini biasanya digunakan pada driver storage seperti devicemapper atau overlay2.
```bash
$ docker run --storage-opt size=10G my_container
```
Container ini hanya bisa menggunakan maksimum 10 GB storage.




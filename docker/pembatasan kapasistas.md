# 1. Membatasi CPU
Docker memungkinkan unutuk membatasi penggunaan CPU oleh container.
```bash
$ Docker run --cpus=2 my_container
```
Container ini hanya akan menggunakan maksimum 2 core CPU.


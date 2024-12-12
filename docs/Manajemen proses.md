### Manajemen Proses (Proses dan Thread)

#### Pengertian Proses
Proses adalah program yang sedang dieksekusi, termasuk kode program, data, dan status eksekusi. Proses merupakan unit dasar kerja dalam sistem operasi.

#### Elemen-Elemen dalam Proses
1. **Kode Program (Code Section):** Berisi instruksi-instruksi yang akan dieksekusi.
2. **Program Counter:** Menyimpan alamat instruksi berikutnya yang akan dieksekusi.
3. **Stack:** Menyimpan informasi seperti variabel lokal, panggilan fungsi, dan parameter.
4. **Heap:** Memori dinamis yang dialokasikan selama eksekusi.
5. **Data Section:** Berisi variabel global.

#### Siklus Hidup Proses
1. **New:** Proses sedang dibuat.
2. **Ready:** Proses siap untuk dijalankan tetapi sedang menunggu giliran.
3. **Running:** Proses sedang dijalankan oleh CPU.
4. **Waiting:** Proses sedang menunggu suatu kejadian, seperti I/O.
5. **Terminated:** Proses telah selesai.

#### Thread
Thread adalah unit eksekusi terkecil dalam proses. Sebuah proses dapat memiliki satu atau lebih thread yang menjalankan tugas-tugas secara independen.

#### Perbedaan Proses dan Thread
| Aspek            | Proses                                  | Thread                              |
|-------------------|-----------------------------------------|-------------------------------------|
| Definisi          | Program yang sedang dieksekusi         | Unit eksekusi dalam sebuah proses  |
| Memori           | Setiap proses memiliki memori sendiri   | Berbagi memori dalam satu proses   |
| Komunikasi       | Melalui IPC (Inter-Process Communication) | Mudah karena berbagi memori       |
| Overhead         | Lebih besar                             | Lebih kecil                        |

#### Manajemen Proses
Manajemen proses meliputi aktivitas seperti:
1. **Penjadwalan Proses:**
   - **Short-term Scheduler:** Memilih proses mana yang akan dijalankan selanjutnya oleh CPU.
   - **Medium-term Scheduler:** Mengelola proses di memori utama dan sekunder.
   - **Long-term Scheduler:** Memilih proses yang akan dimasukkan ke antrian ready.

2. **Sinkronisasi dan Komunikasi:**
   - Mengatur bagaimana proses atau thread berkomunikasi dan menyinkronkan aksi untuk menghindari kondisi balapan (race condition).

3. **Pengelolaan Deadlock:**
   - Menghindari atau mengatasi situasi di mana dua atau lebih proses saling menunggu untuk sumber daya.

#### Jenis Penjadwalan
1. **Penjadwalan Preemptive:** CPU dapat dialihkan ke proses lain sebelum proses selesai.
2. **Penjadwalan Non-Preemptive:** CPU hanya dialihkan setelah proses selesai atau memasuki keadaan waiting.

#### Thread dalam Sistem Operasi
1. **Single-Threaded:** Hanya satu thread dalam proses.
2. **Multi-Threaded:** Beberapa thread berbagi sumber daya proses untuk menjalankan tugas yang berbeda.

#### Manfaat Multi-Threading
1. Meningkatkan performa untuk tugas paralel.
2. Mempermudah pembagian tugas kompleks.
3. Meningkatkan efisiensi sumber daya.

#### Sinkronisasi Thread
- **Mutex:** Mengontrol akses thread ke sumber daya bersama.
- **Semaphore:** Mengatur jumlah thread yang dapat mengakses sumber daya secara bersamaan.
- **Barrier:** Menghentikan thread hingga semua thread mencapai titik tertentu.

#### Contoh Implementasi Thread (Pseudocode):
```python
import threading

def task():
    print("Thread berjalan")

# Membuat thread
thread1 = threading.Thread(target=task)
thread2 = threading.Thread(target=task)

# Menjalankan thread
thread1.start()
thread2.start()

# Menunggu thread selesai
thread1.join()
thread2.join()
```


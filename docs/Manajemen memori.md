### Manajemen Memori

#### Pengertian Manajemen Memori
Manajemen memori adalah fungsi sistem operasi yang bertanggung jawab untuk mengelola memori utama (RAM). Tujuan utamanya adalah untuk memastikan penggunaan memori yang efisien dan memberikan lingkungan eksekusi yang optimal bagi proses.

#### Fungsi Utama Manajemen Memori
1. **Alokasi Memori:** Menyediakan memori untuk proses yang sedang berjalan.
2. **Dealokasi Memori:** Mengembalikan memori dari proses yang telah selesai.
3. **Proteksi Memori:** Mencegah proses mengakses memori yang dialokasikan untuk proses lain.
4. **Swapping:** Memindahkan proses antara memori utama dan penyimpanan sekunder untuk efisiensi.

#### Skema Alokasi Memori
1. **Alokasi Kontigu:**
   - Memori dialokasikan secara berkelanjutan.
   - **Keuntungan:** Sederhana dan cepat.
   - **Kekurangan:** Fragmentasi internal.

2. **Alokasi Non-Kontigu:**
   - Memori dialokasikan dalam blok yang tidak bersebelahan.
   - **Keuntungan:** Mengurangi fragmentasi internal.
   - **Kekurangan:** Kompleksitas manajemen lebih tinggi.

#### Teknik Alokasi Memori
1. **Paging:**
   - Memori dibagi menjadi blok-blok kecil bernama *pages*.
   - Menghilangkan fragmentasi eksternal.

2. **Segmentation:**
   - Memori dibagi berdasarkan segmen logis seperti kode, data, dan stack.
   - Memberikan fleksibilitas tetapi rentan terhadap fragmentasi eksternal.

3. **Virtual Memory:**
   - Teknik untuk menjalankan program yang ukurannya lebih besar dari memori fisik.
   - Menggunakan disk sebagai ekstensi dari memori utama.

#### Fragmentasi
1. **Fragmentasi Internal:**
   - Terjadi ketika blok memori yang dialokasikan lebih besar dari kebutuhan proses.

2. **Fragmentasi Eksternal:**
   - Terjadi ketika terdapat ruang memori bebas tetapi tidak cukup besar untuk proses baru.

#### Swapping
Swapping adalah proses memindahkan sebagian atau seluruh proses dari memori utama ke penyimpanan sekunder dan sebaliknya.
- **Keuntungan:** Memungkinkan eksekusi proses yang tidak muat dalam memori utama.
- **Kekurangan:** Dapat meningkatkan waktu akses memori.

#### Proteksi dan Isolasi Memori
1. **Base and Limit Registers:**
   - Menentukan rentang alamat memori yang bisa diakses oleh proses.

2. **MMU (Memory Management Unit):**
   - Mengubah alamat logis menjadi alamat fisik.

#### Paging vs Segmentation
| Aspek           | Paging                          | Segmentation                     |
|------------------|--------------------------------|-----------------------------------|
| Unit Alokasi     | Pages                          | Segmen                           |
| Ukuran           | Sama untuk semua blok         | Berbeda-beda                     |
| Fragmentasi      | Mengurangi fragmentasi eksternal | Fragmentasi eksternal tetap ada |

#### Virtual Memory
Virtual memory memungkinkan proses seolah-olah memiliki akses ke memori yang lebih besar dari kapasitas fisiknya.
- **Komponen Utama:**
  - *Page Table*: Menyimpan peta antara alamat logis dan alamat fisik.
  - *Swap Space*: Ruang pada disk yang digunakan untuk menyimpan page yang tidak sedang digunakan.

#### Contoh Implementasi Paging (Pseudocode):
```python
class PageTable:
    def __init__(self):
        self.table = {}

    def map_page(self, logical_page, physical_frame):
        self.table[logical_page] = physical_frame

    def translate(self, logical_page):
        return self.table.get(logical_page, "Page Fault")

# Contoh penggunaan
page_table = PageTable()
page_table.map_page(1, 101)
print(page_table.translate(1))  # Output: 101
print(page_table.translate(2))  # Output: Page Fault
```

#### Kesimpulan
Manajemen memori adalah komponen penting dalam sistem operasi untuk memastikan penggunaan sumber daya memori yang optimal dan efisien. Dengan teknik seperti paging, segmentation, dan virtual memory, sistem operasi dapat menangani program yang kompleks dan memori yang terbatas.


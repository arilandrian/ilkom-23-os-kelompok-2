import math

# Fungsi Operasi Matematika
def tambah(a, b): return a + b
def kurang(a, b): return a - b
def kali(a, b): return a * b
def bagi(a, b): return a / b if b != 0 else "Error: Tidak bisa bagi dengan nol!"
def pangkat(a, b): return a ** b
def akar(a): return math.sqrt(a) if a >= 0 else "Error: Tidak bisa akar dari angka negatif!"
def sisa_bagi(a, b): return a % b if b != 0 else "Error: Tidak bisa bagi dengan nol!"
def faktorial(a): 
    return math.factorial(int(a)) if a >= 0 and int(a) == a else "Error: Faktorial hanya untuk bilangan bulat positif!"

# Fungsi Tampilkan Menu
def tampilkan_menu():
    print("\nKalkulator Super Lengkap")
    print("=" * 30)
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")
    print("5. Pangkat (^)")
    print("6. Akar (√)")
    print("7. Sisa Bagi (%)")
    print("8. Faktorial (!)")
    print("9. Keluar")
    print("=" * 30)

# Fungsi Kalkulator Utama
def kalkulator():
    while True:
        tampilkan_menu()
        try:
            # Meminta pilihan pengguna
            pilihan = int(input("Pilih operasi (1-9): "))
            if pilihan == 9:
                print("Terima kasih telah menggunakan Kalkulator Super!")
                break

            # Operasi dengan dua angka
            if pilihan in [1, 2, 3, 4, 5, 7]:
                a = float(input("Masukkan angka pertama: "))
                b = float(input("Masukkan angka kedua: "))
                hasil = None

                if pilihan == 1: hasil = tambah(a, b)
                elif pilihan == 2: hasil = kurang(a, b)
                elif pilihan == 3: hasil = kali(a, b)
                elif pilihan == 4: hasil = bagi(a, b)
                elif pilihan == 5: hasil = pangkat(a, b)
                elif pilihan == 7: hasil = sisa_bagi(a, b)

                print(f"Hasil: {hasil}")

            # Operasi dengan satu angka
            elif pilihan == 6:
                a = float(input("Masukkan angka: "))
                print(f"Hasil: √{a} = {akar(a)}")
            elif pilihan == 8:
                a = float(input("Masukkan angka: "))
                print(f"Hasil: {int(a)}! = {faktorial(a)}")
            else:
                print("Error: Pilihan tidak valid!")

        except ValueError:
            print("Error: Harap masukkan angka yang valid.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

# Jalankan Program
if __name__ == "__main__":
    kalkulator()

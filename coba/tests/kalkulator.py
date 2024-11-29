import math

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian dengan nol!"

def pangkat(a, b):
    return a ** b

def akar(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: Tidak bisa menghitung akar dari angka negatif!"

def sisa_bagi(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: Pembagian dengan nol!"

def faktorial(a):
    if a >= 0 and int(a) == a:
        return math.factorial(int(a))
    else:
        return "Error: Faktorial hanya berlaku untuk bilangan bulat positif!"

def kalkulator():
    while True:
        print("\nKalkulator Canggih")
        print("Pilih operasi:")
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        print("5. Pangkat")
        print("6. Akar")
        print("7. Sisa Bagi (Modulus)")
        print("8. Faktorial")
        print("9. Keluar")
        
        try:
            pilihan = int(input("Masukkan pilihan (1-9): "))
            if pilihan == 9:
                print("Terima kasih telah menggunakan kalkulator!")
                break
            
            if pilihan in [1, 2, 3, 4, 5, 7]:
                num1 = float(input("Masukkan angka pertama: "))
                num2 = float(input("Masukkan angka kedua: "))
                
                if pilihan == 1:
                    print(f"Hasil: {num1} + {num2} = {tambah(num1, num2)}")
                elif pilihan == 2:
                    print(f"Hasil: {num1} - {num2} = {kurang(num1, num2)}")
                elif pilihan == 3:
                    print(f"Hasil: {num1} * {num2} = {kali(num1, num2)}")
                elif pilihan == 4:
                    print(f"Hasil: {num1} / {num2} = {bagi(num1, num2)}")
                elif pilihan == 5:
                    print(f"Hasil: {num1} ^ {num2} = {pangkat(num1, num2)}")
                elif pilihan == 7:
                    print(f"Hasil: {num1} % {num2} = {sisa_bagi(num1, num2)}")
            
            elif pilihan == 6:
                num = float(input("Masukkan angka: "))
                print(f"Hasil: √{num} = {akar(num)}")
            
            elif pilihan == 8:
                num = float(input("Masukkan angka: "))
                print(f"Hasil: {int(num)}! = {faktorial(num)}")
            
            else:
                print("Pilihan tidak valid!")
        
        except ValueError:
            print("Input tidak valid, masukkan angka!")

if __name__ == "__main__":
    kalkulator()

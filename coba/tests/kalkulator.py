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

def kalkulator():
    print("Kalkulator Sederhana")
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    
    try:
        pilihan = int(input("Masukkan pilihan (1/2/3/4): "))
        if pilihan in [1, 2, 3, 4]:
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
        else:
            print("Pilihan tidak valid!")
    except ValueError:
        print("Input tidak valid, masukkan angka!")

if __name__ == "__main__":
    kalkulator()

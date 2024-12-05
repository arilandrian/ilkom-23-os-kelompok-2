def hitung_grade(rata_rata):
    if rata_rata >= 85:
        return 'A'
    elif rata_rata >= 70:
        return 'B'
    elif rata_rata >= 60:
        return 'C'
    elif rata_rata >= 50:
        return 'D'
    else:
        return 'E'

def main():
    nama = input("Masukkan nama mahasiswa: ")
    jumlah_mata_pelajaran = int(input("Masukkan jumlah mata pelajaran: "))
    
    total_nilai = 0
    
    for i in range(jumlah_mata_pelajaran):
        nilai = float(input(f"Masukkan nilai untuk mata pelajaran {i + 1}: "))
        total_nilai += nilai
    
    rata_rata = total_nilai / jumlah_mata_pelajaran
    grade = hitung_grade(rata_rata)
    
    print(f"\nNama Mahasiswa: {nama}")
    print(f"Rata-rata Nilai: {rata_rata:.2f}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
#include <iostream>
#include <stdexcept>

using namespace std;

void displayMenu() {
    cout << "\n=== Kalkulator Sederhana ===" << endl;
    cout << "1. Penjumlahan" << endl;
    cout << "2. Pengurangan" << endl;
    cout << "3. Perkalian" << endl;
    cout << "4. Pembagian" << endl;
    cout << "5. Keluar" << endl;
    cout << "Pilih operasi (1-5): ";
}

double add(double a, double b) {
    return a + b;
}

double subtract(double a, double b) {
    return a - b;
}

double multiply(double a, double b) {
    return a * b;
}

double divide(double a, double b) {
    if (b == 0) {
        throw invalid_argument("Error: Pembagian dengan nol tidak diperbolehkan.");
    }
    return a / b;
}

int main() {
    int choice;
    double num1, num2;

    do {
        displayMenu();
        cin >> choice;

        if (choice >= 1 && choice <= 4) {
            cout << "Masukkan dua angka: ";
            cin >> num1 >> num2;
        }

        switch (choice) {
            case 1:
                cout << "Hasil: " << add(num1, num2) << endl;
                break;
            case 2:
                cout << "Hasil: " << subtract(num1, num2) << endl;
                break;
            case 3:
                cout << "Hasil: " << multiply(num1, num2) << endl;
                break;
            case 4:
                try {
                    cout << "Hasil: " << divide(num1, num2) << endl;
                } catch (const invalid_argument& e) {
                    cout << e.what() << endl;
                }
                break;
            case 5:
                cout << "Terima kasih! Sampai jumpa." << endl;
                break;
            default:
                cout << "Pilihan tidak valid. Silakan coba lagi." << endl;
        }
    } while (choice != 5);

    return 0;
}
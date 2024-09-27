#include <iostream>

using namespace std;

void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int temp = arr[i], j = i - 1;
        while (j >= 0 && arr[j] > temp) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = temp;
    }
}

int main() {
    int n;
    cout << "Masukkan jumlah elemen: ";
    cin >> n;

    int data[n];
    cout << "Masukkan elemen data:\n";
    for (int i = 0; i < n; ++i) {
        cout << "Elemen ke-" << i + 1 << ": ";
        cin >> data[i];
    }

    cout << "Nilai awal data adalah : ";
    for (int i = 0; i < n; ++i)
        cout << data[i] << " ";
    cout << endl;

    insertionSort(data, n);

    cout << "Hasil akhir adalah : ";
    for (int i = 0; i < n; ++i)
        cout << data[i] << " ";
    cout << endl;

    return 0;
}

# **Deteksi Tepi Menggunakan Operator Roberts dan Sobel**

Repositori ini berisi implementasi manual deteksi tepi (edge detection) menggunakan **Operator Roberts** dan **Operator Sobel**, dengan memanfaatkan pustaka Python:

* `imageio`
* `numpy`
* `matplotlib`

Seluruh perhitungan dilakukan **tanpa OpenCV**, sehingga konsep deteksi tepi dapat dipahami dari dasar.

---

## **1. Struktur Proyek**

```
/
├── edge_detection_roberts_sobel.py   # Kode utama deteksi tepi
├── kucing.jpeg                       # Contoh gambar uji
└── README.md                         # Dokumentasi & analisis
```

---

## **2. Cara Menjalankan Program**

### **Install library yang dibutuhkan**

```bash
pip install numpy imageio matplotlib
```

### **Jalankan program**

```bash
python edge_detection_roberts_sobel.py kucing.jpeg
```

Jika path gambar tidak diberikan, program akan meminta input secara manual.

Program akan menampilkan:

1. Citra grayscale
2. Hasil deteksi tepi menggunakan **Roberts**
3. Hasil deteksi tepi menggunakan **Sobel**

---

## **3. Penjelasan Implementasi**

### **Operator Roberts**

Implementasi dilakukan secara manual menggunakan selisih diagonal piksel 2×2:

* `gx = I[i, j] - I[i+1, j+1]`
* `gy = I[i+1, j] - I[i, j+1]`

Nilai gradien dihitung dengan:

```
G = sqrt(gx² + gy²)
```

Hasil dinormalisasi ke rentang [0, 1].

---

### **Operator Sobel**

Operator Sobel menggunakan konvolusi 3×3 untuk mendeteksi gradien horizontal dan vertikal.

Kernel Sobel-X:

```
[-1 0 1]
[-2 0 2]
[-1 0 1]
```

Kernel Sobel-Y:

```
[-1 -2 -1]
[ 0  0  0]
[ 1  2  1]
```

Perhitungan dilakukan menggunakan fungsi konvolusi manual (`conv2d()`), lalu dihitung magnitude gradien dan dinormalisasi.

---

## **4. Analisis Perbandingan Roberts vs Sobel**

### **A. Kualitas Tepi**

* **Roberts**

  * Menghasilkan tepi yang **lebih tipis** dan **lebih tajam** pada detail kecil.
  * Namun banyak bagian tepi terlihat **putus-putus**.

* **Sobel**

  * Tepi terlihat **lebih tebal**, **jelas**, dan **lebih stabil**.
  * Kontur objek lebih mudah dikenali.

---

### **B. Sensitivitas Terhadap Noise**

* **Roberts lebih sensitif terhadap noise** karena tidak ada proses smoothing.
* **Sobel lebih tahan noise** karena kernel 3×3 memberikan efek perataan pada citra.

Pada gambar *kucing.jpeg*, Roberts menampilkan lebih banyak titik-titik kecil yang tidak diperlukan, sedangkan Sobel memberikan garis tepi yang lebih rapi.

---

### **C. Ketelitian & Stabilitas**

* **Roberts**:

  * Menangkap detail frekuensi tinggi seperti bulu halus.
  * Tetapi hasilnya kurang konsisten di area dengan kontras rendah.

* **Sobel**:

  * Lebih baik untuk mendeteksi kontur utama seperti kepala, telinga, dan badan kucing.
  * Hasil lebih cocok untuk analisis lanjutan.

---

### **D. Kesimpulan**

| Aspek              | Roberts       | Sobel                 |
| ------------------ | ------------- | --------------------- |
| Ketebalan tepi     | Tipis         | Lebih tebal & jelas   |
| Sensitivitas noise | Tinggi        | Rendah                |
| Stabilitas hasil   | Kurang stabil | Sangat stabil         |
| Performa           | Cepat         | Sedikit lebih berat   |
| Cocok untuk        | Detail kecil  | Pengolahan citra umum |

Secara umum, **Sobel memberikan hasil lebih baik untuk citra natural**, sedangkan **Roberts cocok untuk aplikasi sederhana yang butuh detail kecil**.

---

## **5. Lisensi**

Bebas digunakan untuk keperluan akademik.

---

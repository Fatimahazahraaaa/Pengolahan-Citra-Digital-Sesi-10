import sys
import imageio.v3 as imageio
import numpy as np
import matplotlib.pyplot as plt


def load_image_grayscale(path: str) -> np.ndarray:
    """Membaca citra dan mengubahnya menjadi grayscale (float64)."""
    img = imageio.imread(path)

    # Jika RGB/warna, konversi ke grayscale
    if img.ndim == 3:
        # Rumus luminance standar
        img_gray = 0.299 * img[..., 0] + 0.587 * img[..., 1] + 0.114 * img[..., 2]
    else:
        img_gray = img.astype(float)

    return img_gray.astype(float)


def roberts_edge_detection(image: np.ndarray) -> np.ndarray:
    """
    Implementasi operator Roberts (Roberts Cross).
    Menggunakan kernel 2x2 secara eksplisit (tanpa konvolusi umum).
    """
    image = image.astype(float)
    h, w = image.shape

    G = np.zeros_like(image, dtype=float)

    for i in range(h - 1):
        for j in range(w - 1):
            gx = image[i, j] - image[i + 1, j + 1]   # diagonal utama
            gy = image[i + 1, j] - image[i, j + 1]   # diagonal lain
            G[i, j] = np.sqrt(gx ** 2 + gy ** 2)

    # Normalisasi ke [0, 1]
    G = G - G.min()
    max_val = G.max()
    if max_val > 0:
        G = G / max_val

    return G


def conv2d(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """
    Konvolusi 2D sederhana (tanpa library tambahan).
    Padding: 'edge' (menjaga ukuran output sama dengan input).
    """
    image = image.astype(float)
    kh, kw = kernel.shape
    pad_h = kh // 2
    pad_w = kw // 2

    # Balik kernel (konvolusi = korelasi dengan kernel dibalik)
    kernel_flipped = np.flipud(np.fliplr(kernel))

    # Padding citra
    padded = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode="edge")

    h, w = image.shape
    output = np.zeros_like(image, dtype=float)

    for i in range(h):
        for j in range(w):
            region = padded[i:i + kh, j:j + kw]
            output[i, j] = np.sum(region * kernel_flipped)

    return output


def sobel_edge_detection(image: np.ndarray) -> np.ndarray:
    """
    Implementasi operator Sobel menggunakan konvolusi 3x3.
    Menghasilkan magnitude gradien, dinormalisasi ke [0, 1].
    """
    sobel_x = np.array(
        [
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1],
        ],
        dtype=float,
    )

    sobel_y = np.array(
        [
            [-1, -2, -1],
            [0, 0, 0],
            [1, 2, 1],
        ],
        dtype=float,
    )

    gx = conv2d(image, sobel_x)
    gy = conv2d(image, sobel_y)

    G = np.sqrt(gx ** 2 + gy ** 2)

    # Normalisasi ke [0, 1]
    G = G - G.min()
    max_val = G.max()
    if max_val > 0:
        G = G / max_val

    return G


def main():
    # Ambil path gambar dari argumen command line, kalau tidak ada minta input
    if len(sys.argv) > 1:
        img_path = sys.argv[1]
    else:
        img_path = input("Masukkan path file gambar (misal: lena.png): ").strip()

    # Load gambar grayscale
    img_gray = load_image_grayscale(img_path)

    # Deteksi tepi Roberts dan Sobel
    edges_roberts = roberts_edge_detection(img_gray)
    edges_sobel = sobel_edge_detection(img_gray)

    # Tampilkan hasil
    plt.figure(figsize=(18, 6))

    plt.subplot(1, 3, 1)
    plt.imshow(img_gray, cmap="gray")
    plt.title("Citra Grayscale")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(edges_roberts, cmap="gray")
    plt.title("Tepi - Operator Roberts")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(edges_sobel, cmap="gray")
    plt.title("Tepi - Operator Sobel")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

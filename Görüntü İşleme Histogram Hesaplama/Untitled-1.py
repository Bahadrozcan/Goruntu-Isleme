import numpy as np
import cv2
import matplotlib.pyplot as plt

def calculate_histogram(image_path):
    I = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    Hist = np.zeros(256, dtype=int)

    h, w = I.shape

    for v in range(h):
        for u in range(w):
            pixel_value = I[v, u]
            Hist[pixel_value] += 1

    return Hist

def plot_histogram(Hist):
    
    plt.bar(range(256), Hist, color='gray')
    plt.title('Gri Seviye Görüntü Histogramı')
    plt.xlabel('Piksel Değeri')
    plt.ylabel('Frekans')
    plt.show()


image_path = 'resim1.jpg'


histogram = calculate_histogram(image_path)


print("Histogram:")


# Histogramı grafik olarak çiz
plot_histogram(histogram)

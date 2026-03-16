import matplotlib.pyplot as plt
import cv2

def graphic_comparation(raw_img, depth):
    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.imshow(cv2.cvtColor(raw_img, cv2.COLOR_BGR2RGB))
    plt.title("Imagen original")
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.imshow(depth, cmap='gray')
    plt.title("Mapa de profundidad")
    plt.axis("off")

    plt.show()
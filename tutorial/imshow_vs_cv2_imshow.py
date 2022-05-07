import cv2
import matplotlib.pyplot as plt

imagem_1 = cv2.imread("./assets/imagem1.jpg")
imagem_2 = cv2.imread("./assets/imagem2.png")

#usando matplotlib imshow
plt.imshow(imagem_1)
plt.title("imshow do matplotlib")
plt.show()

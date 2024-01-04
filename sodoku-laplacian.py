# high pass fillter

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("sodoku.jpg", 0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)

plt.imshow(laplacian, cmap="gray")
plt.title("laplacian"), plt.xticks([]), plt.yticks([])
plt.show()
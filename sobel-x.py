sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
plt.imshow(laplacian, cmap="gray")
plt.title("Sobel x"), plt.xticks([]), plt.yticks([])
plt.show()
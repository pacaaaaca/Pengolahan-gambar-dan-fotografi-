sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
plt.imshow(sobely, cmap="gray")
plt.title("Sobel y"), plt.xticks([]), plt.yticks([])
plt.show()
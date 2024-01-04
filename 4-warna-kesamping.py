import matplotlib.pyplot as plt
import cv2

img = cv2.imread("Gambar 1.png")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

red = rgb_img.copy()
red[:, :, 1] = 0
red[:, :, 2] = 0

green = rgb_img.copy()
green[:, :, 0] = 0
green[:, :, 2] = 0

blue = rgb_img.copy()
blue[:, :, 0] = 0
blue[:, :, 1] = 0

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
ax = axes.ravel()
ax[0].imshow(rgb_img)
ax[0].set_title("Original")
ax[1].imshow(red)
ax[1].set_title("Red Channel")
ax[2].imshow(green)
ax[2].set_title("Green Channel")
ax[3].imshow(blue)
ax[3].set_title("Blue Channel")

fig.tight_layout()
plt.show()
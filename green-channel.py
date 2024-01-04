import matplotlib.pyplot as plt
import cv2

img = cv2.imread("Gambar 1.png")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

green = rgb_img.copy()
green[:, :, 0] = 0
green[:, :, 2] = 0
print('green shape = ', green.shape)

fig, ax = plt.subplots(1, 1, figsize=(6, 6))
ax.imshow(green)
ax.set_title("Green Channel")

plt.show()
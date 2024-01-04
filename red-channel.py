import matplotlib.pyplot as plt
import cv2

img = cv2.imread("Gambar 1.png")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

red = rgb_img.copy()
red[:, :, 1] = 0
red[:, :, 2] = 0
print('red shape = ', red.shape)

fig, ax = plt.subplots(1, 1, figsize=(6, 6))
ax.imshow(red)
ax.set_title("Red Channel")

plt.show()
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("Gambar 1.png")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
r = rgb_img[:,:,0]
g = rgb_img[:,:,1]
b = rgb_img[:,:,2]

red = rgb_img.copy()
red[:,:,1]=0
red[:,:,2]=0
print('red shape = ',red.shape)

green = rgb_img.copy()
green[:,:,0]=0
green[:,:,2]=0
print('green shape = ',green.shape)

blue = rgb_img.copy()
blue[:,:,0]=0
blue[:,:,1]=0
print('blue shape = ',blue.shape)

fig, axes = plt.subplots(2, 2, figsize=(6, 6))
ax = axes.ravel()
ax[0].imshow(rgb_img)
ax[0].set_title("original")
ax[1].imshow(red)
ax[1].set_title("red chanel")
ax[2].imshow(green)
ax[2].set_title("green chanel")
ax[3].imshow(blue)
ax[3].set_title("blue chanel")

fig.tight_layout()
plt.show()
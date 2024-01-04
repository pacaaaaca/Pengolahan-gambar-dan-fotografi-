# konversi BGR dari variable img ke colorspace HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV);

# memisahkan hue, saturation dan value
h, s, v = cv2.split(hsv)

h = img[...,0]  # hue channel
s = img[...,1]  # saturation channel
v = img[...,2]  # value channel

# menampilkan band hue
cv2_imshow (v)
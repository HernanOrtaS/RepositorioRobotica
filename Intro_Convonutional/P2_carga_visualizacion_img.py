
from keras.api.utils import load_img

XY = 500
largo, alto = XY, XY

file = './imgs/hollow.png'
img = load_img(file, target_size = (largo, alto),
               color_mode = "grayscale")

print(img.size)
print(img.mode)

#op 2
import matplotlib.pyplot as plt
plt.imshow(img, cmap = "gray")
plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()

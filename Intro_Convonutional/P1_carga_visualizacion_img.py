
from keras.api.utils import load_img

largo, alto = 1000, 1000

file = './imgs/kirby.jpg'
img = load_img(file, target_size = (largo, alto))

print(img.size)
print(img.mode)

#op 1
img.show()

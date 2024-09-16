from keras.src.utils import img_to_array
from keras.api.utils import load_img

XY = 500
largo, alto = XY, XY

file = './imgs/hollow.png'
img = load_img(file, target_size = (largo, alto),
               color_mode = "grayscale")

print(img.size)
print(img.mode)

#op 2
imagen_en_array = img_to_array(img)
print(imagen_en_array.shape)

for i in imagen_en_array:
    for j in i:
        print(str(j[0]) + ",", end="")
    print()


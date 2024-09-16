## https://en.wikipedia.org/wiki/Kernel_(image_processing)

from keras.api.utils import load_img, img_to_array, array_to_img, save_img #alternative 2
import matplotlib.pyplot as plt

largo, alto = 480, 480
fotos = ['foto_core', 'foto_hernan', 'foto_moises']

nombre_Kernels =[
    '1_IDENTITY',
    '2_RIDGE',
    '3_EDGE-DETECTION',
    '4_SHARPEN',
    '5_BLUR',
    '6_GAUSIAN-BLUR_3x3',
    '7_GAUSIAN-BLUR_5x5',
    '8_UNSHARP-MASKING_5x5'
]

lista_Kernels = [
    [  #IDENTITY
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
],
    [  #EDGE DETECTION
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
],
    [  #EDGE DETECTION
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
],
    [  #SHARPEN
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
],
    [  #BLUR
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
],
    [  #GAUSIAN BLUR 3x3
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
],
    [  #GAUSIAN BLUR 5x5
    [1, 4, 6, 4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, 36, 24, 6],
    [4, 16, 24, 16, 4],
    [1, 4, 6, 4, 1]
],
    [  #UNSHARP MASKING 5x5
    [1, 4, 6, 4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, -476, 24, 6],
    [4, 16, 24, 16, 4],
    [1, 4, 6, 4, 1]
]
]

for i in range(len(fotos)): #el ciclo selecciona cada una de las fotos
    img_original = load_img('fotos/' + fotos[i] + '.png', target_size=(largo, alto)
                            , color_mode="grayscale")

    img_a_convolucinar = img_to_array(img_original)  # filas, columnas, canales de colores

      # nueva imagen

    for j in range(len(lista_Kernels)): #el ciclo ejecuta cada uno de los kernels

        img_convolucionada = [] #limpia la imagen en cada ciclo

        if j == 0:
            borde = 1

        if j == 6:
            borde = 2

        for filas in range(borde, alto - borde):  # ignora los pixeles de la primera y ultima fila
            new_fila = []
            for columnas in range(borde, largo - borde):  # ignora los pixeles de la primera y ultima columna

                pixelConvulucionado = 0
                for f_kernel in range(len(lista_Kernels[j])):  # 0 1 2
                    for c_kernel in range(len(lista_Kernels[j])):  # 0 1 2

                        pixelConvulucionado += (lista_Kernels[j][f_kernel][c_kernel]
                                                * img_a_convolucinar[filas + (f_kernel - borde)][columnas + (c_kernel - borde)])

                if j == 4:
                    pixelConvulucionado = pixelConvulucionado * (1 / 9)

                if j == 5:
                    pixelConvulucionado = pixelConvulucionado * (1 / 16)

                if j == 6:
                    pixelConvulucionado = pixelConvulucionado * (1 / 256)

                if j == 7:
                    pixelConvulucionado = pixelConvulucionado * (-1 / 256)

                new_fila.append(pixelConvulucionado)

            img_convolucionada.append(new_fila)

        img = array_to_img(img_convolucionada)
        #print(img.size)

        plt.figure(figsize=(15, 5))

        plt.subplot(1, 2, 1)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img_original, cmap='gray')

        plt.subplot(1, 2, 2)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img, cmap='gray')

        # Guarda la foto de cada integrante procesada con cada kernel
        save_img('fotos_procesadas/' + fotos[i] + '_' + nombre_Kernels[j] + '.jpg', img_convolucionada)

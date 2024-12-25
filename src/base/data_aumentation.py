from cv2 import getRotationMatrix2D, warpAffine
from numpy import ndarray

def rotate_imagem(image: ndarray) -> list[ndarray]:

    rotate_images = []

    rotate_images.append(image)

    # Realiza as rotações de 90, 180 e 270 graus
    for ang in [90, 180, 270]:
        

        height, width = image.shape[:2]

        # Calcula o centro da imagem
        centro = (width / 2, height / 2)

        # Realiza a rotação da imagem
        rotation_matrix = getRotationMatrix2D(centro, ang, 1.0)
        imagem_rotacionada = warpAffine(image, rotation_matrix, (height, width))

        rotate_images.append(imagem_rotacionada)

    return rotate_images
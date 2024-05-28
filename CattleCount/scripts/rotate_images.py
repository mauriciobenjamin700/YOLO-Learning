from cv2 import getRotationMatrix2D, warpAffine, cvtColor, COLOR_BGR2RGB, imread
from typing import List, Union, Tuple
from numpy import ndarray
from os.path import exists, basename, join, dirname, abspath, exists
from glob import glob
from matplotlib.pyplot import imsave

def rotacoes_imagem(imagem) -> List[ndarray]:

    imagens_rotacionadas = []

    imagens_rotacionadas.append(imagem)

    # Realiza as rotações de 90, 180 e 270 graus
    for angulo in [90, 180, 270]:
        

        altura, largura = imagem.shape[:2]

        # Calcula o centro da imagem
        centro = (largura / 2, altura / 2)

        # Realiza a rotação da imagem
        matriz_rotacao = getRotationMatrix2D(centro, angulo, 1.0)
        imagem_rotacionada = warpAffine(imagem, matriz_rotacao, (largura, altura))

        imagens_rotacionadas.append(imagem_rotacionada)

    return imagens_rotacionadas

def Image(filename:str="image.jpg")-> Union[ndarray, None]:
    """
    Recebe o caminho para uma imagem e retorna:
    - Uma imagem em formato ndarray formatada para RGB com base no item passado, em caso de sucesso
    - None, em caso de falha ao carregar a imagem
    """
    
    file = imread(filename)
    
    if file is not None:
        if file.shape[2] == 4: #se for RGBA vamos dercartar o canal A para economizar memória
            file = file[:,:,:3]
        file = cvtColor(file,COLOR_BGR2RGB)
        
    return file

def Folder(foldername:str="images")->Tuple[List[ndarray],List[str]] | None:
    """
    Recebe o caminho para uma pasta contendo imagens e retorna:
    - Uma tupla, onde o primeiro elemento é uma lista com todas as imagens carregadas como matrizes numpy em formato RGB, e o segundo elemento são os nomes de cada imagem.
    - None, caso não exista a pasta selecionada.
    - Uma tupla, contendo duas listas vazias, caso a pasta exista mas não possuí imagens.
    """
    dataset = None
    
    if exists(foldername):
        
        images = []
        labels = []
        
        extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.tiff', '*.tif']
        
        files = []
            
        for e in extensions:
            files.extend(glob(join(foldername,e)))
            #files.extend(glob(join(foldername,e.upper())))

        for file in files:
            images.append(Image(file))
            labels.append(basename(file))
            
        dataset = (images,labels)
        
    return dataset

def Save(input_folder : str = "images", output_folder : str = "data"):
    ROOT = dirname(dirname(abspath(__file__)))
    IMAGES = join(ROOT, input_folder)
    OUTPUT = join(ROOT, output_folder)
    
    images, labels = Folder(IMAGES)
    
    if exists(OUTPUT):
    
        for id, item in enumerate(images,0):
            to_save = rotacoes_imagem(item)
            
            for idx,g in enumerate(["0.jpg", "90.jpg", "180.jpg", "270.jpg"],0):
                imsave(join(OUTPUT,labels[id]+g), to_save[idx])
                
        print("terminei de rotacionar")
              
    else:
        print("Não achei onde salvar")

if __name__ == '__main__':
    Save()
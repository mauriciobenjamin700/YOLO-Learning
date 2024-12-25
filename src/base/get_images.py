from cv2 import (
    cvtColor, 
    COLOR_BGR2RGB, 
    imread
)
from glob import glob
from numpy import ndarray
from os.path import exists, basename, join


def Image(filename:str="image.jpg")-> ndarray | None:
    """
    Recebe o caminho para uma imagem e retorna:
    - Uma imagem em formato ndarray formatada para RGB com base no item passado, em caso de sucesso
    - None, em caso de falha ao carregar a imagem
    """
    
    file = imread(filename)
    
    if file is not None:
        if file.shape[2] == 4: #se for RGBA vamos descartar o canal A para economizar memória
            file = file[:,:,:3]
        file = cvtColor(file,COLOR_BGR2RGB)
        
    return file

def Folder(foldername:str="images")->tuple[list[ndarray],list[str]] | None:
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
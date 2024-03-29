import numpy as np
from skimage import io
import matplotlib.pyplot as plt
import scr.modulo_tela as modulo_tela
import os

def trata_imagem(caminho: str) -> np.ndarray:
    imagem = io.imread(caminho)
    
    if len(imagem.shape) > 2:  
            imagem_cinza = np.dot(imagem[..., :3], [0.2989, 0.5870, 0.1140])
    else:
        imagem_cinza = imagem

    return imagem_cinza


def avalia_pic(imagem_cinza:np.ndarray)->np:
    imagem = io.imread(caminho)
    print("Está é a imagem:", imagem)
    
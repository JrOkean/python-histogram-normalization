import log
import scr.modulo_tela as modulo_tela
import modulo_avalia_pic
import modulo_normaliza

def main():
    imagem_selecionada = modulo_tela.tela()
    
    if imagem_selecionada:
        modulo_avalia_pic.avalia_pic(imagem_selecionada)
        pass
    else:
        pass
    
    return 0 

if __name__ == "__main__":
    main()
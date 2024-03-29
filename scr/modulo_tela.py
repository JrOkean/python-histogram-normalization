import os
import tkinter as tk
from tkinter import filedialog

def selecionar_arquivo():
    caminho_arquivo = filedialog.askopenfilename()
    if os.path.isfile(caminho_arquivo):
        lbl_arquivo_selecionado.config(text=f"Arquivo selecionado: {caminho_arquivo}")
    else:
        lbl_arquivo_selecionado.config(text="Caminho do arquivo inválido. Tente novamente.")

# Criar janela
janela = tk.Tk()
janela.title("Selecionar Arquivo")

# Adicionar rótulo para instrução
lbl_instrucao = tk.Label(janela, text="Clique no botão abaixo para selecionar o arquivo:")
lbl_instrucao.pack()

# Adicionar botão para selecionar arquivo
btn_selecionar = tk.Button(janela, text="Selecionar Arquivo", command=selecionar_arquivo)
btn_selecionar.pack()

# Adicionar rótulo para exibir o caminho do arquivo selecionado
lbl_arquivo_selecionado = tk.Label(janela, text="")
lbl_arquivo_selecionado.pack()

# Adicionar ícone para sinalizar onde colocar a imagem (opcional)
# Exemplo de como adicionar um ícone de uma câmera
icone_camera = tk.PhotoImage(file="icone_camera.png")  # Substitua "icone_camera.png" pelo caminho do seu ícone
lbl_icone = tk.Label(janela, image=icone_camera)
lbl_icone.pack()

# Executar loop principal da janela
janela.mainloop()
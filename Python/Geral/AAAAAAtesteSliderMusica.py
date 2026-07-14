'''import tkinter as tk

# Função acionada pelo clique do botão
def alternar_imagem():
    global imagem_atual
    
    # Condição IF para alternar a imagem
    if imagem_atual == img1:
        botao.config(image=img2)
        imagem_atual = img2
    else:
        botao.config(image=img1)
        imagem_atual = img1

# Configuração da Janela Principal
janela = tk.Tk()
janela.geometry("300x300")

# Carregando as imagens
img1 = tk.PhotoImage(file="musicas/pause.png")
img2 = tk.PhotoImage(file="musicas/play.png")

# Definindo a imagem inicial
imagem_atual = img1

# Criando o botão com a imagem inicial
botao = tk.Button(janela, image=img1, command=alternar_imagem)
botao.pack(pady=50)

janela.mainloop()'''

import pygame
import tkinter as tk

def alterar_tempo():
    # Converte o valor do slider (segundos) e define a nova posição da música
    campoEntrada = float(campoEntrada)
    pygame.mixer.music.set_pos(float(campoEntrada))
    labeldetempo.config(text=f"{pygame.mixer.music.set_pos(float(campoEntrada))}")

# Inicializa o Pygame e o mixer
pygame.init()


# Carrega a sua música (substitua pelo caminho do seu arquivo)
pygame.mixer.music.load("musicas/VIRA_VIRA.mp3")
pygame.mixer.music.play()


root = tk.Tk()
root.title("Player de Música")
root.geometry("350x150")
campoEntrada = tk.Entry(root, text="").pack()

botaoEntrada = tk.Button(root, text="IR", command=alterar_tempo).pack()

labeldetempo = tk.Label(root, text=f"tempo: {pygame.mixer.music.get_pos()}")
labeldetempo.pack(side="top")


# Obtém a duração da música em segundos (aproximada, dependendo do formato)
# Nota: get_length() pode retornar um valor estimado em certos formatos de áudio
tamanho_musica = pygame.mixer.music.get_pos()


# Cria o campo de controle (Slider)
'''slider_tempo = tk.Scale(
    root, 
    from_=0, 
    to=tamanho_musica if tamanho_musica > 0 else 100, 
    orient=tk.HORIZONTAL, 
    label="Tempo (Segundos)", 
    command=alterar_tempo
)
slider_tempo.pack(pady=20, fill=tk.X, padx=20)'''

root.mainloop()
pygame.quit()
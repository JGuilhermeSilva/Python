import tkinter as tk

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

janela.mainloop()
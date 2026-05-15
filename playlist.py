#programa que cria playlist com interface grafica
import pygame
import tkinter as tk

pygame.mixer.init()

playlist = [
    "musicas/boto_ou_nao.mp3",
    "musicas/Garagem.mp3",
    "musicas/HomemComH.mp3",
    "musicas/JulietaTa.mp3",
    "musicas/VIRA_VIRA.mp3"
]

#indice da musica atual
indice = 0

#funcao para dar play(tocar):
def play_music():
    global indice
    pygame.mixer.music.load(playlist[indice]) #carrega a musica
    pygame.mixer.music.play()
    rotulo_status.config(text=f"{playlist[indice]}") #reproduz a musica
    #rotulo_status.config(text=f"Tocando: {playlist[indice]}")

#pausar musica
def pause_music():
    pygame.mixer.music.pause()
    rotulo_status.config(text="Música pausada")

#tirar musica da pausa
def unpause_music():
    pygame.mixer.music.unpause()
    rotulo_status.config(text=f"Continuando: {playlist[indice]}")

#funcao para parar de tocar musica
def stop_music():
    pygame.mixer.music.stop()
    rotulo_status.config(text="Musica parada")

#pula para a proxima musica
def next_music():
    global indice
    indice = (indice + 1)%len(playlist)
    play_music()

#Voltar para a musica anterior
def prev_music():
    global indice
    indice = (indice - 1)%len(playlist)
    play_music()
'''    if indice!=playlist[0]:
        indice = (indice - 1)%len(playlist)
    else:
        indice = playlist[-1]
    '''


#Iniciando interface grafica
janela = tk.Tk()
janela.title("Tocador de musica")
janela.geometry("600x200")
janela.config(bg="green")

botaoAnterior = tk.Button(janela, text="Voltar musica", command=prev_music, width=10)
botaoAnterior.pack(side='left', padx=5)

botaoPlay = tk.Button(janela, text="Play", command=play_music, width=10)
botaoPlay.pack(side='left', padx=5)

botaoPause = tk.Button(janela, text="Pause", command=pause_music, width=10)
botaoPause.pack(side='left', padx=5)

botaoDespausar = tk.Button(janela, text="Continuar", command=unpause_music, width=10)
botaoDespausar.pack(side='left', padx=5)

botaoParar = tk.Button(janela, text="Parar de tocar", command=stop_music, width=10)
botaoParar.pack(side='left', padx=5)

botaoAdiantar = tk.Button(janela, text="Pular musica", command=next_music, width=10)
botaoAdiantar.pack(side='left', padx=5)

#Rotulo para mostrar o status da musica
rotulo_status = tk.Label(janela, text="Nenhuma musica tocando", font=('Arial', 12))
rotulo_status.pack(side='left')

#play_music()
#input()

janela.mainloop()

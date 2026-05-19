#programa que cria playlist com interface grafica
import pygame
import tkinter as tk
import webbrowser

pygame.mixer.init()

#informa o caminho no HD das musicas da playlist
playlist = [
    "musicas/boto_ou_nao.mp3",
    "musicas/Garagem.mp3",
    "musicas/HomemComH.mp3",
    "musicas/JulietaTa.mp3",
    "musicas/VIRA_VIRA.mp3"
]


#funcao para dar play(tocar):
#indice da musica atual
indice = 0
def play_music():
    global indice
    pygame.mixer.music.load(playlist[indice]) #carrega a musica
    pygame.mixer.music.play() #reproduz a musica
    rotulo_status.config(text=f"{playlist[indice]}") #informa qual musica está tocando
    botaoPlayAndPause.config(image=imagePause)

#variavel que informa se a musica está pausada ou nao
pausado = False
#Funcao para pausar e despausar musica
def pauseUnpause():
    global pausado
    
    if not pausado: #se pausado(False)==False-->True, então:
        pygame.mixer.music.pause() #pausa a musica
        rotulo_status.config(text="Música pausada")

        #verifica se a musica está pausada e muda imagem para que o usuario dê play novamente
        botaoPlayAndPause.config(image=imageContinuar)
        pausado = True #diz que pausado é True--> retorna: se o usuario pausou a musica
        #o icone do do botao deve ser o de continuar
        
    else:
        pygame.mixer.music.unpause() #despausa a musica
        rotulo_status.config(text=f"Continuando: {playlist[indice]}")
        botaoPlayAndPause.config(text="Pausar ||")
        #verifica se a musica está tocando e muda imagem
        botaoPlayAndPause.config(image=imagePause)
        
        pausado = False#diz que pausado é False--> retorna: se a musica está tocando
        #o icone do do botao deve ser o de pausar

        
'''#pausar musica
def pause_music():
    pygame.mixer.music.pause()
    rotulo_status.config(text="Música pausada")

#tirar musica da pausa
def unpause_music():
    pygame.mixer.music.unpause()
    rotulo_status.config(text=f"Continuando: {playlist[indice]}")'''

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


#Iniciando interface grafica
janela = tk.Tk()
janela.title("Tocador de musica")
janela.geometry("900x700")
radio_fundo = tk.PhotoImage(file="musicas/radio_fundo.png").subsample(2,2)
label_fundo = tk.Label(janela, image=radio_fundo)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)


imageVoltar = tk.PhotoImage(file="musicas/voltar.png").subsample(12, 12)
botaoAnterior = tk.Button(janela, text="Voltar musica", image=imageVoltar, command=prev_music)
botaoAnterior.pack(side='left', padx=5)

imagePlay = tk.PhotoImage(file="musicas/play.png").subsample(12, 12)
botaoPlay = tk.Button(janela, text="Play", image=imagePlay,command=play_music)
botaoPlay.pack(side='left', padx=5)

####################################################################
#Imagens que serão usadas na funcao pauseUnpause, para inserir no botao a imagem de play e pause
imagePause = tk.PhotoImage(file="musicas/pause.png").subsample(12,12)
imageContinuar = tk.PhotoImage(file="musicas/play_pause.png").subsample(12,12)

botaoPlayAndPause = tk.Button(janela, text="Pausar ||", image=imagePause, command=pauseUnpause)
botaoPlayAndPause.pack(side='left', padx=5)

#desativei este botao pois anexei as 2 funcoes em uma só
'''botaoDespausar = tk.Button(janela, text="Continuar", command=pauseUnpause, width=10)
botaoDespausar.pack(side='left', padx=5)'''
#######################################################################
imageParar = tk.PhotoImage(file="musicas/parar.png").subsample(12, 12)
botaoParar = tk.Button(janela, text="Parar de tocar", image=imageParar, command=stop_music)
botaoParar.pack(side='left', padx=5)

imageProximo = tk.PhotoImage(file="musicas/proximo.png").subsample(12, 12)
botaoAdiantar = tk.Button(janela, text="Pular musica", image=imageProximo, command=next_music)
botaoAdiantar.pack(side='left', padx=5)

def abrir_site():
    '''pygame.mixer.music.load("interferencia.mp3")
    pygame.mixer.music.play()'''
    webbrowser.open_new_tab("https://radiosaovivo.net/cenecista-picui/")
    rotulo_status.config(text="Tocando FM de Picuí - ao vivo")

imageFM = tk.PhotoImage(file="musicas/fm.png").subsample(12, 12)
botaoFM = tk.Button(janela, text="FM", image=imageFM ,command=abrir_site)
botaoFM.pack(side='left', padx=5)

#Rotulo para mostrar o status da musica
rotulo_status = tk.Label(janela, text="Nenhuma musica tocando",bg="green",  font=('Arial', 12))
rotulo_status.pack(side='left')

#play_music()
#input()

janela.mainloop()

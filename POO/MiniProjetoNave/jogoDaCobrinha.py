# importando as bibliotecas nesessaria: para criar o jogo da cobrinha
import pygame
import time
import random
# inicializando o pygame
pygame.init()
# definindo as coras no formato RGB
banco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
# Definindo o tamanho da tela
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")
# definindo o relogio para controla os FPS
clock = pygame.time.Clock()
# definindo o tamanho do bloco da cobra
tamanho_bloco = 20
# definindo a fonte do texto
fonte = pygame.font.SysFont(None, 36)
# funçao para mostra mensagem na tela.
def mensagem(msg, cor, posicao):
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, posicao)
# funçao principal do jogo
def jogo():
    x = largura / 2
    y = altura / 2
    # movimento inicial (parada)
    x_mudar = 0
    y_mudar = 0
    # corpo da cobra ( lista de blocos)
    cobra = []
    comprimento_cobra = 1
    # posiçao inicial da comida da cobrinha(aleatorio)
    comida_x = round(round.randrange(0, largura - tamanho_bloco)/20.0) * 20.0
    comida_y = round(round.randrange(0, altura - tamanho_bloco)/20.0) * 20.0
    # pontuaçao inicial
    pontos = 0
    # variavel de controle do jogo
    fim_jogo = False
    # loop principal do jogo
    while not fim_jogo:
    # captura de eventos(como fechar a jane ou aperta uma tela)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
    # captura teclas precionadas
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_mudar = -tamanho_bloco
                    y_mudar = 0

                elif evento.key == pygame.K_RIGHT:
                    x_mudar = tamanho_bloco
                    y_mudar = 0

                elif evento.key == pygame.K_UP:
                    y_mudar = -tamanho_bloco
                    x_mudar = 0

                elif evento.key == pygame.K_DOWN:
                    y_mudar = tamanho_bloco
                    x_mudar = 0
# importando as bibliotecas nesessaria: para criar o jogo da cobrinha
import pygame
import time
import random


# inicializando o pygame
pygame.init()

# definindo as coras no formato RGB
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Definindo o tamanho da tela
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

#SONS:
som_batida = pygame.mixer.Sound('POO/MiniProjetoNave/som_explosao.mp3')
som_comida = pygame.mixer.Sound('POO/MiniProjetoNave/pou-eating.mp3')
game_over = pygame.mixer.Sound('POO/MiniProjetoNave/game_over.mp3')
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
    comida_x = round(random.randrange(0, largura - tamanho_bloco)/20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco)/20.0) * 20.0



    # pontuaçao inicial
    pontos = 0

    # variavel de controle do jogo
    fim_jogo = False

    # loop principal do jogo
    while not fim_jogo:
        # captura de eventos(como fechar a janela ou apertar uma tela)
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

        #atualizar a posicao da cobra
        x += x_mudar
        y += y_mudar

        #verifica se a cobra bate na parede da janela
        if x >= largura or x < 0 or y >= altura or y < 0:
            som_batida.play()
            fim_jogo = True
        #limpa a tela (preto)
        tela.fill(preto)

        #desenhar a comida
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        #atualizar o  corpo da cobra
        cabeca_cobra = []
        cabeca_cobra.append(x)
        cabeca_cobra.append(y)
        cobra.append(cabeca_cobra)

        #manter o tamanho correto da cobra
        if len(cobra) > comprimento_cobra:
            del cobra[0]
        
        #verificar a colisao da cobra com ela mesmo
        for bloco in cobra[:-1]:
            if bloco == cabeca_cobra:
                fim_jogo = True

            
        #desenha a cobra (quadrados verdes)
        for bloco in cobra:
            pygame.draw.rect(tela, verde, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

        #verifica se  a cobra comeu a comida
        if x == comida_x and y == comida_y:
            som_comida.play()
            #gerar nova posicao
            comida_x = round(random.randrange(0, largura-tamanho_bloco)/20.0) * 20
            comida_y = round(random.randrange(0, altura-tamanho_bloco)/20.0) * 20
            comprimento_cobra+= 1
            pontos += 10
        #exibir pontos
        mensagem(f"Pontos: {pontos}", branco, (10, 10))

        #atualiza a tela
        pygame.display.update()
        #controlar os FPS (velocidade do jogo aumentar conforme pontos)
        clock.tick(10 + pontos // 500)

    #mensagem de fim de jogo
    tela.fill(preto)
    game_over.play()
    mensagem("Game Over!", vermelho, (largura/2 - 80, altura/2))
    pygame.display.update()
    time.sleep(2)
        

jogo()
pygame.quit()


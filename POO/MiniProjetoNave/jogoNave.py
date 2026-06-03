#importando as bibliotecas necessarias
import pygame
import random
import sys

#inicializar o pygame
pygame.init()

#definir tamanho da tela
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Nave")

#definir as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

#Defimir a fonte para o texto
fonte = pygame.font.SysFont(None, 36)

#CLasse da Nave
class Nave:
    def __init__(self):
        self.x = largura // 2 #eixo x
        self.y = altura - 50 #eixo y
        self.velocidade = 5
        self.vidas = 3
    
    def desenhar(self):
        #desenhar nave com um retangulo azul
        pygame.draw.rect(tela, AZUL, (self.x, self.y, 40, 20))

    def mover(self, teclas):
        #mover para a esquerda se a seta esquerda for pressionada
        if teclas[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velocidade 
        #mover para a direita se a seta direita for pressionada
        if teclas[pygame.K_RIGHT] and self.x < largura - 40:
            self.x += self.velocidade
    
#Classe dos inimigos
class Inimigo:
    def __init__(self, velocidade):
        self.x = random.randint(0, largura-40)
        self.y = -20
        self.velocidade = velocidade
    
    def desenhar(self):
        #desenho do inimigo  como retangulo vermelho
        pygame.draw.rect(tela, VERMELHO, (self.x, self.y, 40, 20))

    def mover(self):
        #move o inimigo para baixo
        self.y += self.velocidade

#classe dos tiros
class Tiro:
    def __init__(self, x, y):
        self.x = x + 15
        self.y = y
        self.velocidade = 7

    def desenhar(self):
        #desenhao o tiro com um pequeno retangulo na cor branca
        pygame.draw.rect(tela, BRANCO, (self.x, self.y, 10, 20))

    def mover(self):
        #move o tiro pra cima
        self.y -= self.velocidade

#funcao principal do jogo
def jogo():
    nave =  Nave()
    inimigos = []
    tiros =  []
    pontos = 0
    nivel = 1
    velocidade_inimigo = 2

    clock = pygame.time.Clock()

    #loop principal do jogo
    while True:
        #captura eventos (como fechar a janela ou apertar teclas)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #se apertar espaço vai disparar um tiro
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    tiros.append(Tiro(nave.x, nave.y))
        
        #captura teclas pressionadas
        teclas = pygame.key.get_pressed()
        nave.mover(teclas) # move a nave

        #criar novos inimigos aleatorios
        if random.randint(1, 30) == 1:
            inimigos.append(Inimigo(velocidade_inimigo))

        #limpar a tela(preto)
        tela.fill(PRETO)

        #desenha a nave
        nave.desenhar()

        #move e desenha inimigo
        for inimigo in inimigos[:]:
            inimigo.mover()
            inimigo.desenhar()

            #verifica colisao com a nave
            if (nave.x < inimigo.x + 40 and nave.x + 40 > inimigo.x and nave.y < inimigo.y + 20 and nave.y + 20 > inimigo.y):
                inimigos.remove(inimigo)
                nave.vidas -= 1
                if nave.vidas == 0: #se a vida chegou a zero informar que o jogador perdeu
                    texto = fonte.render("Se fudeu!", True, BRANCO) #mostrar o texto na tela
                    tela.blit(texto, (largura//2 - 80, altura//2 )) #alinhar o texto
                    pygame.display.update()
                    pygame.time.wait(2000) #2 segundos
                    return
                
            #remover os inimigos que sairam da tela
            if inimigo.y > altura:
                inimigos.remove(inimigo)
                pontos += 10
        
        #move e desenha tiros
        for tiro in tiros[:]:
            tiro.mover()
            tiro.desenhar()

            #remover tiro se sair da tela
            if tiro.y < 0:
                tiros.remove(tiro)
            
            #verificar a colisao do tiro com o inimigo
            for inimigo in inimigos[:]:
                if (tiro.x < inimigo.x + 40 and tiro.x + 10 > inimigo.x and tiro.y < inimigo.y + 20 and tiro.y + 20 > inimigo.y):
                    inimigos.remove(inimigo)
                    if tiro in tiros:
                        tiros.remove(tiro)
                    pontos += 20

        #aumenta nivel e velocidade gradualmente        
        if pontos >= nivel * 100:
            nivel += 1
            velocidade_inimigo += 1

        #exibe pontos, nivel e vidas nas telas
        texto_pontos = fonte.render(f"Pontos: {pontos}", True, BRANCO)
        texto_nivel = fonte.render(f"Nível: {nivel}", True, BRANCO)
        texto_vidas = fonte.render(f"Vidas: {nave.vidas}", True, BRANCO)
        tela.blit(texto_pontos, (10, 10))
        tela.blit(texto_nivel, (10, 40))
        tela.blit(texto_vidas, (10, 70))

        #atualiza a tela
        pygame.display.update()

        #controla frames por segundo(fps)
        clock.tick(60)

jogo()

from random import randint
from time import sleep

lista = []
jogos = []

tentativas = int(input("Quantas tentativas? "))
contarJogos =0
while tentativas > contarJogos:
    cont=0
    while True:
        num = randint(1 ,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont>=6:
            break
    lista.sort()        
    jogos.append(lista[:])
    lista.clear()        
    contarJogos+=1      
        
        
contador = 0
for linha in range(0, len(jogos)):
    contador+=1
    print (f"Jogo {contador}: {jogos[linha]}:")
    sleep(1)
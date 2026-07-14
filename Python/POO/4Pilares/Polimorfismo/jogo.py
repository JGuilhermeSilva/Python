class Jogo:
    def jogar(self):
        print ("Está jogando")

class Futebol(Jogo):
    def jogar(self):
        print ("Está jogando Futebol, olha a topada")

class Videogame(Jogo):
    def jogar(self):
        print ("Está jogando Videogame, cuidado com os zoi")

class Volei(Jogo):
    def jogar(self):
        print ("Está jogando volei, ó a lapada")

class Beachtenis(Jogo):
    def jogar(self):
        print ("Está jogando beachtenis")

class Tenis(Jogo):
    def jogar(self):
        print ("Está jogando Tenis, ói a bolinha")

class Sinuca(Jogo):
    def jogar(self):
        print ("Está jogando Sinuca apostando o aposento")

class FreeFire(Jogo):
    def jogar(self):
        print ("Está jogando Frifas, ó o caba lá o caba lá")

jogos = [Futebol(), Videogame(), Volei(), Beachtenis(), Tenis(), Sinuca(), FreeFire()]
for jogo in jogos:
    jogo.jogar()
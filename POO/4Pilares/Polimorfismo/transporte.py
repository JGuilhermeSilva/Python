#classe pai
class Transporte:
    def mover(self):
        print("Transporte em movimento.")

class Onibus(Transporte):
    def mover(self):
        print("O onibus está em movimento e lotado")

class Bicicleta(Transporte):
    def mover(self):
        print("A bike está em movimento e sem freio")

class Van(Transporte):
    def mover(self):
        print("A van está em movimento e cheia de menino zuando")

veiculos = [Onibus(), Bicicleta(), Van()]
for transporte in veiculos:
    transporte.mover()
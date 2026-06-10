#criando classes abstratas
from abc import ABC, abstractmethod

#criando classe abstrata Eletrodomestico
class Eletrodomestico(ABC):
    @abstractmethod
    def ligar(self):
        #Metodo abstrato: cada elemento liga de forma diferente:
        pass

class Geladeira(Eletrodomestico):
    def ligar(self):
        print("A geladeira ligou e começou a gelar")

class Fogao(Eletrodomestico):
    def ligar(self):
        print("Fogão ligou as bocas, cuida em fazer o café")

class Microondas(Eletrodomestico):
    def ligar(self):
        print("Microondas ligou, coloque uma colher dentro")

class AirFryer(Eletrodomestico):
    def ligar(self):
        print("AirFryer ligou, cuida em assar frango")

class Televisao(Eletrodomestico):
    def ligar(self):
        print("TV ligada e passando novela da globe")


listaEletrodomesticos = [Geladeira(), Fogao(), Microondas(), AirFryer(), Televisao()]
for item in listaEletrodomesticos:
    item.ligar()
    print("")
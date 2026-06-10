from abc import ABC, abstractmethod

#classe abstrata Entrega
class Entrega(ABC):
    @abstractmethod
    def realizar_entrega(self):
        pass

class Mototaxi(Entrega):
    def realizar_entrega(self):
        print("O mototaxi chegou na porta e tá gritando 'O LANCHEE, O LANCHEE!!!'")

class Correio(Entrega):
    def realizar_entrega(self):
        print("5 dias pra chegar da china, e 30 mais dias pra chegar na minha casa")

class Drone(Entrega):
    def realizar_entrega(self):
        print("Já chegou o disco voador")

class Transportadora(Entrega):
    def realizar_entrega(self):
        print("Chegou o pc da Pichau")

tiposDeEntrega = [Mototaxi(), Correio(), Drone(), Transportadora()]
for tipo in tiposDeEntrega:
    tipo.realizar_entrega()
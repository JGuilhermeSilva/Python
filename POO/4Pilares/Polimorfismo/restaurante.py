class Restaurante:
    def servir_comida(self):
        print("Servindo comida")

class Pizzaria(Restaurante):
    def servir_comida(self):
        print("Servindo Pizza de Frango com 3 asas")

class Lanchonete(Restaurante):
    def servir_comida(self):
        print("Servindo o dogão de sempre")

class Padaria(Restaurante):
    def servir_comida(self):
        print("Servindo pão de ontem")

class Churrascaria(Restaurante):
    def servir_comida(self):
        print("Servindo carne de boi de morte matada")

class Espetinho(Restaurante):
    def servir_comida(self):
        print("Servindo espeto de gato")

class Hamburgueria(Restaurante):
    def servir_comida(self):
        print("Servindo Hamburguer de vento")

estabelecimentos = [Pizzaria(), Lanchonete(), Padaria(), Churrascaria(), Espetinho(), Hamburgueria()]
for local in estabelecimentos:
    local.servir_comida()

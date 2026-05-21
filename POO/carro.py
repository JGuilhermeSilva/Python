#definicao de classe carro
class carro:
    def __init__(self, marca, modelo, ano, cor, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.preco = preco
    #metodo do carro: informacoes
    def mostrarInformacoes(self):
        print(f"O carro da: {self.marca}, do modelo: {self.modelo}, do ano: {self.ano}, cor: {self.cor}, tem o preço de: R${self.preco:.2f}")

carro1 = carro("Fiat", "Uno", 2010, "Prata", 22000.00)
carro2 = carro("Nissan", "Versa", 2013, "Cinza", 35000.00)

carro1.mostrarInformacoes()
carro2.mostrarInformacoes()
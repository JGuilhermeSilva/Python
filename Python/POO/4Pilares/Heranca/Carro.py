#criando a classe pai (SuperClasse)
class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def apresentar(self):
        return f"Marca: {self.marca}, ano:{self.ano}"

class Carro(Veiculo):
    def __init__(self, marca, ano, modelo, preco, portas):
        super().__init__(marca, ano)
        self.modelo = modelo
        self.preco = preco
        self.portas = portas

    def detalhes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, ano:{self.ano} tem o valor fipe de R${self.preco:.2f} e possui {self.portas} Portas"
    

class Moto(Veiculo):
    def __init__(self, marca, ano, cilindradas, tipo):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas
        self.tipo = tipo

    def detalhes(self):
        return f"Marca: {self.marca}, ano: {self.ano}, cilindradas: {self.cilindradas}cc, Tipo: {self.tipo}"  

concessionaria1 = Veiculo('Chevrolet', 2002)   
print(concessionaria1.apresentar())

print("")

carro1 = Carro('Fiat', 2011, 'Uno', 22000.00, 4)
print(carro1.detalhes())

print("")

moto1 = Moto('Honda', 2015, 150, 'Urbana')
print(moto1.detalhes())

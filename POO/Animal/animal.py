#definindo classe animal
class animal:
    def __init__(self, nome, especie, idade, raca):
        #criando os atributos(caracteristicas)
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.raca = raca

    def mostrarInformacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Especie: {self.especie}")
        print(f"Idade: {self.idade}")
        print(f"Raça: {self.raca}")

    def emitir_som(self):
        if self.especie.lower() == 'cachorro':
            print(f"{self.nome} está latindo: Au Au")
        elif self.especie.lower() == 'gato':
            print(f"{self.nome} está miando: Miaau")
        elif self.especie.lower() == 'papagaio':
            print(f"{self.nome} está falando coisas de {self.especie}: Louro quer biscoito")
        print("")


#criando objetos
bicho1 = animal('Menina', 'gato', 1, 'Felina')
bicho2 = animal('Louro', 'papagaio', 40, 'Ave')
bicho3 = animal('Dique', 'Cachorro', 10, 'Vira-Lata')

#chamando os metodos
bicho1.mostrarInformacoes()
bicho1.emitir_som()

bicho2.mostrarInformacoes()
bicho2.emitir_som()

bicho3.mostrarInformacoes()
bicho3.emitir_som()


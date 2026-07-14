class Boletim:
    def __init__(self, nome):
        self.nome = nome
        self.__nota = 0

    def definir_nota(self, valor):
        if 10 >= valor >=0:
            self.__nota = valor
        else:
            print('Nota invalida')

    def situacao(self):
        if self.__nota >= 7:
            print (f'{self.nome} foiAprovado com nota: {self.__nota}')
        elif self.__nota >= 4 and self.__nota < 7:
            print (f'{self.nome} ficou em recuperacao com nota: {self.__nota}')
        else:
            print (f'{self.nome} foi reprovado com nota: {self.__nota}')


aluno1 = Boletim("Guilherme")
aluno1.definir_nota(6)
aluno1.situacao()
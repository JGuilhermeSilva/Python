class Pessoa():
    def __init__(self, altura, idade):
        self.altura = altura
        self.idade = idade



class Aluno():
    def __init__(self, altura, idade):
        self.altura = altura
        self.idade = idade

    @classmethod
    def construir_aluno_pessoa(cls, pessoa):
        return cls(pessoa.altura, pessoa.idade)

    def estudar(self):
        print("Estou estudando")


joao = Pessoa(1.85, 18)
mariaAluna = Aluno(1.68, 18)
mariaAluna.estudar()

# Construindo classe Aluno recebendo uma instancia da classe pessoa
joaoAluno = Aluno.construir_aluno_pessoa(joao)
joaoAluno.estudar()
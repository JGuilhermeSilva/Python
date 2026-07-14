#definição da classe aluno

class aluno:
    def __init__(self, nome, idade):
        #iniciar os atributos do aluno
        self.nome = nome
        self.idade = idade

    #inicando o metodo
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade}")
        
aluno1 = aluno("José", 20)
aluno2 = aluno("Guilherme", 23)

aluno1.apresentar()
aluno2.apresentar()

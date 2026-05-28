#criando a classe pessoa(conceitos de herança)
class Pessoa: #classe pai/superclasse
    def __init__(self, nome, idade, cpf=None, cor=None, peso=None, altura=None, sexo=None):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.cor = cor
        self.peso = peso
        self.altura = altura
        self.sexo = sexo

    def apresentar(self):
        return f"Sou {self.nome}, tenho {self.idade} anos\nmeu cpf é: {self.cpf}, minha cor é: {self.cor}\nPeso: {self.peso:.2f}, altura: {self.altura}, sexo: {self.sexo}"

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, serie, turma):
        super().__init__(nome, idade) #aqui acontece a herança
        self.curso = curso
        self.serie = serie
        self.turma = turma
    
    def apresentar(self):
        return f"Sou {self.nome}, tenho {self.idade} estou no curso: {self.curso}, {self.serie}° serie, turma {self.turma}"
    
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, salario):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.salario = salario

    def apresentar(self):
        return f"Sou {self.nome}, tenho {self.idade} anos e leciono a disciplina de {self.disciplina} e ganho R${self.salario} mensal"
    

pessoa1 = Pessoa('Guilherme', 23, '7000000000', 'parda', 54.00, 175, 'Masculino')
print(pessoa1.apresentar())

aluno1 = Aluno('Guilherme', 23, 'Informatica', 3, 'G1')
print(aluno1.apresentar())

professor1 = Professor('Girafales', 43, 'Programacao', 2000)
print(professor1.apresentar())
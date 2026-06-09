#importar recursos para criar classes abstratas
from abc import ABC, abstractmethod

#classe abstrata funcionario
class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome #nome do funcionario entra aqui

    @abstractmethod
    def calcular_salario(self):
        #metodo abstrato: calcula salario diferente para cada tipo de funcionario diferente
        pass


class Gerente(Funcionario):
    def calcular_salario(self):
        #salario fixo para gerente = 5000
        return 5000
    
class Estagiario(Funcionario):
    def calcular_salario(self):
        return 1200

class Vendedor(Funcionario):
    def __init__(self, nome, vendas):
        super().__init__(nome)
        self.vendas = vendas
    
    #salario fixo + comissao de 10% sobre as vendas
    def calcular_salario(self):
        salario_fixo = 2000
        return salario_fixo + (self.vendas * 0.1)
    
def sistema_funcionarios():
    funcionarios = [Gerente('Guilherme'), Estagiario("Renivaldo"), Vendedor("José", 10000)]
        
    #exibir os salarios
    for func in funcionarios:
        print(f"{func.nome} recebe: R${func.calcular_salario():.2f}")

sistema_funcionarios()
            



'''gerente = Gerente('Guilherme')
estagiario = Estagiario('Renivaldo')
vendedor = Vendedor('José', 2000)

print(f"Salario do gerente = {gerente.calcular_salario():.2f}")
print(f"Salario do estagiario = {estagiario.calcular_salario():.2f}")
print(f"Salario do vendedor = {vendedor.calcular_salario():.2f}")'''
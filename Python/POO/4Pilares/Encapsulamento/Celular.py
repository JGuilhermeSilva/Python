#definido a classe Celular
class Celular:
    def __init__(self, modelo, senha):
        #criando os atributos(caracteristicas)
        self.modelo = modelo
        #atributo privado
        self.__senha = senha

    #funcao para acesar atributo privado
    def desbloquear(self, tentativa):
        if tentativa == self.__senha:
            print(f"Modelo: {self.modelo} desbloqueado com sucesso")
        else:
            print(f"Senha Incorreta")

#criando um objeto celular
celular1 = Celular('Poco X6 Pro', '1234')
celular1.desbloquear('40028922')
celular1.desbloquear('1234')


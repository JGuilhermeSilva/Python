#a classe carteira representa o dinheiro guardado

class Carteira:
    def __init__(self):
        self.__dinheiro = 0 #atributo privado: dinheiro

    #Método publico
    def adicionarDinheiro(self, valor):
        self.__dinheiro += valor

    def retirarDinheiro(self, valor):
        if self.__dinheiro>=valor:
            self.__dinheiro -= valor
        else:
            print("Saldo Insuficiente pra gastar! Vá trabalhar")

    def abrirCarteira(self):
        print(f"Valor na carteira: R${self.__dinheiro:.2f}")


carteira1 = Carteira()
carteira1.adicionarDinheiro(500)
carteira1.retirarDinheiro(50)
carteira1.abrirCarteira()
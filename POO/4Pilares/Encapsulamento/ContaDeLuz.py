class ContaDeLuz:
    def __init__(self, valor):
        self.__valor = valor

    def pagar(self, valor_pago):
        if valor_pago >= self.__valor:
            print("Conta paga")
            self.__valor = 0 
        else:
            print("Saldo Insuficiente para pagar a conta")

    def mostrarSaldo(self):
        print(f"Valor restante: R${self.__valor:.2f}")





conta1 = ContaDeLuz(100)
conta1.pagar(110)
conta1.mostrarSaldo()


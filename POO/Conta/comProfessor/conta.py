class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print(f"O usuario tentou sacar R${valor}")
            print("Saldo atual da conta insuficiente para saque")
    
    def depositar(self, valor):
        self.saldo += valor

    def mostrarSaldo(self):
        print(f"O saldo de {self.titular} é de R${self.saldo:.2f} ")

cliente1 = ContaBancaria('Guilherme', 1000)
cliente1.mostrarSaldo()

cliente1.sacar(1500)

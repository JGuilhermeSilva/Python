'''class cliente:
    def __init__(self, nome, endereco, pedido, valorPedido,formaPagamento):
        self.nome = nome
        self.endereco = endereco
        self. pedido = pedido
        self.valorPedido = float(valorPedido)
        self.formaPagamento = formaPagamento

    def entrega(self):
        print (f"Cliente: {self.nome}")
        print (f"Endereço: {self.endereco}")
        print (f"Pedido: {self.pedido}")
        print (f"Valor total do pedido: {self.valorPedido:.2f}")
        print (f"Forma de pagamento: {self.formaPagamento}")
        print('*-' * 30)

cliente1 = cliente('Guilherme', 'Sitio Timbauba', '2 x XBacon + Refri', 55.00, 'PIX')
cliente2 = cliente('Lindomara', 'Frei Martinho', '2 x Sanduiche Natural + Suco', 32.00, 'Cartão')

cliente1.entrega()
cliente2.entrega()
'''
'''
class cliente:
    def __init__(self):
        self.lista = {}
        self.continua = ''
        while self.continua.lower() != 'n':
            self.nome = str(input("Insira o nome: "))
            self.endereco = str(input("Endereço: "))
            self.pedido = str(input("Qual o seu pedido: "))
            self.valorPedido = float(input("valorPedido: "))
            self.formaPagamento = str(input("Forma de pagamento: "))
            self.continua = str(input("\nContinuar? S / N? "))


    def entrega(self):
        print ("\nComanda:")
        print (f"Cliente: {self.nome}")
        print (f"Endereço: {self.endereco}")
        print (f"Pedido: {self.pedido}")
        print (f"Valor total do pedido: {self.valorPedido:.2f}")
        print (f"Forma de pagamento: {self.formaPagamento}")
        print('*-' * 30)
    
cliente1 = cliente()
cliente1.entrega()
'''

class cliente:
    def __init__(self):
        self.lista = {}
        self.continua = ''
        while self.continua.lower() != 'n':
            self.nome = str(input("Insira o nome: "))
            self.endereco = str(input("Endereço: "))
            self.pedido = str(input("Qual o seu pedido: "))
            self.valorPedido = float(input("valorPedido: "))
            self.formaPagamento = str(input("Forma de pagamento: "))
            self.continua = str(input("\nContinuar? S / N? "))
            self.lista.update({
                "nome": self.nome,
                "endereco": self.endereco,
                "pedido": self.pedido,
                "valorPedido": self.valorPedido,
                "formaPagamento": self.formaPagamento
            })
        for linha, coluna in self.lista.items():
            print(f"{linha} : {coluna}")


    def entrega(self):
        print ("\nComanda:")
        print("Teste:", self.lista)
        print (f"Cliente: {self.nome}")
        print (f"Endereço: {self.endereco}")
        print (f"Pedido: {self.pedido}")
        print (f"Valor total do pedido: {self.valorPedido:.2f}")
        print (f"Forma de pagamento: {self.formaPagamento}")
        print('*-' * 30)
    
cliente1 = cliente()
cliente1.entrega()
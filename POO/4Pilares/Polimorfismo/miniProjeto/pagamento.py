#classe pai :pagamento

class pagamento:
    def pagar(self, valor):
        print(f"Pagamento genérico de R${valor:.2f}")

class dinheiro(pagamento):
    def pagar(self, valor):
        desconto = valor * 0.1 #desconto de 10% no dinheiro em especie
        valor_final = valor-desconto
        print(f"Pagamento de R${valor:.2f}")
        print(f"Desconto de R${desconto:.2f} aplicado")
        print(f"Valor final: R${valor_final:.2f}")

class cartao(pagamento):
    def pagar(self, valor, parcelas = 1):
        if parcelas>1:
            valor_parcela = valor/parcelas
            print(f"Pagamento de R${valor:.2f} no cartão {parcelas}X de R${valor_parcela:.2f}")
        else:
            print(f"Pagamento de R${valor:.2f} pago no cartão à vista")

class pix(pagamento):
    def pagar(self, valor):
        print(f"Pagamento de R${valor} via pix")
        print(f"Confirmação instantânea recebida")
#funcao para simular compra
def realizarCompra(metodo_pagamento, valor, parcelas = 1):
    if isinstance(metodo_pagamento, cartao):
        metodo_pagamento.pagar(valor, parcelas)
    else:
        metodo_pagamento.pagar(valor)

#testando polimorfismo com funcionalidades extras
compra1 = dinheiro()
compra2 = cartao()
compra3 = pix()

realizarCompra(compra1, 100)
print('')
realizarCompra(compra2, 300, 3)
print('')
realizarCompra(compra3, 75)
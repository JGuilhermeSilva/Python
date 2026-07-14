class Produto:
    def __init__(self, nome, preco, quantidade, marca, categoria):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.marca = marca
        self.categoria = categoria

    
    #metodo para aplicar desconto de 10% do valor do produto
    def aplicarDesconto(self):
        self.preco -= self.preco*0.10


produto1 = Produto(8, 5, 'Carioca', 'Cereais')
produto1.aplicarDesconto()

print(f"Produto: {produto1.nome}, Preço final: R${produto1.preco:.2f}")

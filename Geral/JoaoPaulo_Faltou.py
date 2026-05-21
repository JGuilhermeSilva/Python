'''valorCompra = float(input("Insira o valor da compra: "))
valorPago = float(input("Insira o valor que o cliente tem: "))
troco = valorPago - valorCompra
print(f"O troco da compra é: {troco:.2f}")'''

'''idade = int(input("Insira a idade do aluno: "))

if idade >= 18:
    print("NAO pode pegar onibus")
else:
    print("Pode usar o onibus")
'''

'''qntHamburgueres = int(input("Digite quantos hamburgueres vc quer: "))

qtdSucos = int(input("Quantos copos de suco de alcerola? "))

precoHamb = 12.99
precoSuco = 5.00
total = (qntHamburgueres*precoHamb)+(qtdSucos*precoSuco)
print(f"Total de {qntHamburgueres} hamburgueres + {qtdSucos} Sucos = {total:.2f}")'''

lista = ['arroz', 'batata', 'salsicha', 'cuscuz', 'manga', 'feijao', 'sorvete']

estoque = ["arroz", "salsicha", "feijao"]

for item in lista:
    if item in estoque:
        print(f"-{item} já está no estoque. Nao precisa comprar")
    else:
        print(f"-{item} precisa ser comprado")
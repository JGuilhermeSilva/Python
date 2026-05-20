'''valorCompra = float(input("Insira qual o valor da compra: "))
valorCliente = float(input("Insira quanto o cliente pagou: "))
troco = valorCliente - valorCompra

print(f"O troco da compra é {troco:.2f}")'''
#--------------------------------------------------------------#

'''nota1 = float(input("Insira a nota 1: "))
nota2 = float(input("Insira a nota 2: "))
nota3 = float(input("Insira a nota 3: "))

media = (nota1+nota2+nota3)/3

if media>=6:
    print("Aprovado")
elif media>=4 and media<6:
    print("Recuperacao")
else:
    print("Reprovado")'''

'''reais = float(input("Insira o valor em R$"))
dolar = 5.20
conversao = reais / dolar

print(f"R${reais:.2f} dolares em reais é: R${conversao:.2f}")'''

'''preco1 = 7
preco2 = 6

print(f"O preco 1(R${preco1}) é maior que preco 2(R${preco2})? {preco1>preco2}")
print("O preco maior é:", max(preco1, preco2))'''

numero = float(input("Insira o número: "))

if numero==0:
    print("Numero é zero")
elif numero>0:
    print("Numero positivo")
else:
    print("numero negativo")
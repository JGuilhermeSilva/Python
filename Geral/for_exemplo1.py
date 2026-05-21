#lista = ["Maça", "Banana", "Uva", "Goiaba"]

#for item in lista:
#   print (item);
'''
lista_vendas = [1000, 3000, 500, 1200]
total = 0
for venda in lista_vendas:
    total = venda+total
    if venda>=1100:
        comissao = (venda*0.1) #10% comissao
        print("comissao: ", comissao)
print("soma total: das vendas sem comissao: ", sum(lista_vendas)) 
#print(total)
#teste2 = "abc"
#print(len(teste2))

lista2 = ["Guilherme", 2002, "Lindomara", 2004]
print(lista2)

for item in lista2:
    print(item)'''
listaWhile = ["Guilherme", 2002, "Lindomara", 2004]
contador1 = 0
while (contador1<len(listaWhile)):
    print(listaWhile[contador1])
    contador1+=1
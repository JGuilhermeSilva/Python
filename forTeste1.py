lista = [1500, 1200, 450, 780, 5000]

#print(sum(lista))
#print(lista[0])
cont = 0
for venda in lista:
    cont +=1;
    if venda>=1000:
        comissao = venda*0.1
        print('Comissão da venda n° ', cont, f"é de:  {comissao:.2f}")
for i in range(1, 11, 2):
    print(i)
'''c2 = 0
while (c2<4):
    print("Ola mundo")
    c2+=1
'''
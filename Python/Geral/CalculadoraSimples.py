num1 = float(input("numero 1: "))
num2 = float(input("numero 2: "))
escolha = str(input("Qual operacao voce quer? "))
if (escolha=="soma" or escolha=="+"):
    print("O resultado é: ", num1+num2)

elif (escolha=="subtracao" or escolha=="-"):
    print("O resultado é: ", num1-num2)

elif (escolha=="multiplicacao" or escolha=="*"):
    print("O resultado é: ", num1*num2)

elif (escolha=="divisao" or escolha=="/"):
    print("O resultado é: ", num1/num2)

else:
    "Nao entendi, recomece o programa"
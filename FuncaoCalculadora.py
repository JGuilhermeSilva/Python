'''def saudacao(nome, sobrenome):
    print(f"Olá {nome} {sobrenome} como vai?")

saudacao(nome="Guilherme", sobrenome="Silva")
'''
num1 = int(input("Insira o numero1: "))
num2 = int(input("Insira o numero2: "))
escolha = str(input("Qual operacao voce quer? "))

def calculadora(num1, num2, escolha):
    if (escolha=="soma" or escolha=="+"):
        soma = num1 + num2
        print(f"\nSoma de {num1}+{num2} = {soma}\n")

    elif (escolha=="subtracao" or escolha=="-"):
        subtracao = num1-num2
        print(f"Subtracao de {num1}-{num2} = {subtracao}\n")

    elif (escolha=="multiplicacao" or escolha=="*"):
        multuplicacao = num1 * num2
        print(f"Multiplicacao de {num1}x{num2} = {multuplicacao}\n")

    elif (escolha=="divisao" or escolha=="/"):
        if num2 != 0:
            divisao = num1/num2
            print(f"Divisão de {num1}/{num2} = {divisao}\n")
        else:
            print("ERRO: Não é possivel dividir por 0!!!")
    
    else:
        print("Nao entendi, recomece o programa")

    


calculadora(num1, num2, escolha)
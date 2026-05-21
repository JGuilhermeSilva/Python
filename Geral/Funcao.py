'''def calcularMedia(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    print(f"Sua média é: {media:.2}")

nota1 = float(input("Insira a nota 1: "))
nota2 = float(input("Insira a nota 2: "))
nota3 = float(input("Insira a nota 3: "))

calcularMedia(nota1, nota2, nota3)'''

def verificaIdade(idade):
    if idade>=18:
        print("O usuário é maior de idade!!")
    else:
        print("O usuário é menor de idade!!")

idade = int(input("Insira a idade do usuario: "))

verificaIdade(idade)
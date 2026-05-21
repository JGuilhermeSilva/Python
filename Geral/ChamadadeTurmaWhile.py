qtd_alunos = 0
lista = []
while (qtd_alunos<5):
    nomeAluno = str(input("Insira seu nome: "))
    lista.append(nomeAluno)
    qtd_alunos+=1

print("Chamada concluida")
print('Alunos presentes na sala: ', lista)
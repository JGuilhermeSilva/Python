'''nome = str(input("Insira o nome da pessoa: ")).lower()
anoNascimento = str(input(f"Insira ano de nascimento de {nome}: "))
nomeFinal = nome
for n in nomeFinal:
    if n == 'a':
        nomeFinal = nomeFinal.replace('a', '@')
    if n == 'o':
        nomeFinal = nomeFinal.replace('o', '0')
    if n == 'e':
        nomeFinal = nomeFinal.replace('e', '3')

#repete a primeira letra do nome se essa for 'a', 'e' ou 'o'
if nome[0] == 'a' or nome[0] == 'e' or nome[0] == 'o':    
    nomeFinal = nome[0] + nomeFinal

#muda a primeira letra da senha para maiusculo
if nomeFinal[0] not in ['@', '0', '3']:
    nomeFinal = nomeFinal.replace(nomeFinal[0], (nomeFinal[0]).upper(), 1) 

#pega os 2 ultimos caracteres do ano de nascimento e adicona no final da senha
nomeFinal += anoNascimento[-2] + anoNascimento[-1]

#adiciona o caractere '!' no final da senha   
nomeFinal += '!' 
    
print(f"Nome: {nome}, Ano Nascimento: {anoNascimento}")
print(f"A senha da pessoa é {nomeFinal}")'''

#melhorado por IA(+ funcao de deixar primeira letra do segundo nome maiusculo)
nome = str(input("Insira o nome da pessoa: ")).lower()
anoNascimento = str(input(f"Insira ano de nascimento de {nome}: "))
nomeFinal = nome
# 1. Trata a letra após o espaço PRIMEIRO (enquanto ainda são letras)
lista_letras = list(nome)
for i, letra in enumerate(lista_letras):
    if letra == " " and i + 1 < len(lista_letras):
        lista_letras[i + 1] = lista_letras[i + 1].upper()
nome_com_espaco_maiusculo = "".join(lista_letras)

# 2. Faz as substituições com base no nome já tratado
nomeFinal = nome_com_espaco_maiusculo
for n in nomeFinal:
    if n == 'a':
        nomeFinal = nomeFinal.replace('a', '@')
    if n == 'o':
        nomeFinal = nomeFinal.replace('o', '0')
    if n == 'e':
        nomeFinal = nomeFinal.replace('e', '3')

# Repete a primeira letra do nome se essa for 'a', 'e' ou 'o'
if nome[0] in ['a', 'e', 'o']:    
    nomeFinal = nome[0] + nomeFinal

# Muda a primeira letra da senha para maiúscula (Correção do bug com 'and')
if nomeFinal[0] not in ['@', '0', '3']:
    nomeFinal = nomeFinal.replace(nomeFinal[0], nomeFinal[0].upper(), 1) 

# Pega os 2 últimos caracteres do ano de nascimento
nomeFinal += anoNascimento[-2:]

# Adiciona o caractere '!' no final da senha   
nomeFinal += '!' 
    
print(f"\nNome: {nome}, Ano Nascimento: {anoNascimento}")
print(f"A senha da pessoa é: {nomeFinal}")
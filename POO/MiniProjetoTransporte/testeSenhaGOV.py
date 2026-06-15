nome = str(input("Insira o nome da pessoa: "))
anoNascimento = str(input(f"Insira ano de nascimento de {nome}: "))
nomeFinal = nome
for n in nome:
    if n.lower() == 'a':
        nomeFinal = nomeFinal.replace('a', '@')
    if n.lower() == 'o':
        nomeFinal = nomeFinal.replace('o', '0')
    if n.lower() == 'e':
        nomeFinal = nomeFinal.replace('e', '3', 0)
    
#muda a primeira letra do nome para maiusculo
if nomeFinal[0] != '@' or nomeFinal[0] != '0' or nomeFinal[0] != '3':
    nomeFinal = nomeFinal.replace(nomeFinal[0], (nomeFinal[0]).upper(), 1) 

#pega os 2 ultimos caracteres do ano de nascimento e adicona no final da senha
nomeFinal += anoNascimento[-2] + anoNascimento[-1]

#adiciona o caractere '!' no final do nome    
nomeFinal += '!' 
    
print(f"Nome: {nome}, Ano Nascimento: {anoNascimento}")
print(f"A senha da pessoa é {nomeFinal}")
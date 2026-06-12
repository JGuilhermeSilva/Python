nome = str(input("Insira o nome da pessoa: "))
anoNascimento = int(input(f"Insira ano de nascimento de {nome}: "))
nomeFinal = nome
for n in nome:
    if n.lower() == 'a':
        nomeFinal = nomeFinal.replace('a', '@')
    if n.lower() == 'o':
        nomeFinal = nomeFinal.replace('o', '0')
    
    #muda a primeira letra do nome para maiusculo
    if nomeFinal[0] != '@' or nomeFinal[0] != '0':
        #muda a primeira letra para maiusculo
        nomeFinal = nomeFinal.replace(nomeFinal[0], (nomeFinal[0]).upper()) 
    




print(f"O nome da pessoa é: {nome}")
print(f"A senha da pessoa é {nomeFinal}")
alunos = [
    ["Guilherme", "Informatica"],
    ["Lindomara", "Estetica"],
    ["Rafinha", "Contabilidade"],
    ["Chagas", "Fisica"],
    ["Renivaldo", "Portugues"]
]

print(alunos)
print("-*" * 30)
print()

#imprime as linhas
'''
for linha in alunos:
    print (linha)
'''

#imprime apenas as colunas:
for linha in alunos:
    for coluna in linha:
        print(coluna)
#matriz 2x3 (2 linhas, 3 colunas)
matriz = [
    [1, 2, 3], #primeira linha
    [4, 5, 6], #segunda linha
    [7, 8, 9] # terceira linha
]
#matriz[1][1] = 10


print(matriz)
'''for c, v in enumerate(matriz):
    print(f"encontrei na posicao {c} o valor de {v}")
'''
#percorre linha na matriz
for linha in matriz:
    #percorre cada coluna
    for elemento in linha:
        print(elemento)
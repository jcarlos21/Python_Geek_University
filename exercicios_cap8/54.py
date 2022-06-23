"""
Questão 54
"""
import random


def GeraMatriz(linha, coluna):
    matriz = []
    laco = 0
    while laco < linha:
        matriz.append([])
        laco += 1
    for a in range(0, linha):
        for b in range(0, coluna):
            matriz[a].append([])
    return matriz


def PreencheMatriz(x):
    for a in range(0, len(x)):
        for b in range(0, len(x[0])):
            x[a][b] = random.randint(0, 99)
    return x


def SomaTodosElementos(x):
    soma = 0
    for a in range(0, len(x)):
        for b in range(0, len(x[0])):
            soma += x[a][b]
    return soma


linhas = colunas = int(input('Entre com o número de linhas e colunas para a matriz quadrática: '))
A = PreencheMatriz(GeraMatriz(linhas, colunas))
for i in range(0, linhas):
    for j in range(0, colunas):
        print(f'{A[i][j]:^3}', end='')
    print()

print(f'\nA soma de todos os elemento da matriz digitada é: {SomaTodosElementos(A)}')

"""
Questão 58
"""
import random
from typing import List, Any


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
            x[a][b] = random.randint(0, 4)
    return x


def ProdutoMatriz(x, y):
    matriz = GeraMatriz(len(x), len(y[0]))
    soma = 0
    # n = 0
    for a in range(0, len(x)):
        for b in range(0, len(y[0])):
            for c in range(0, len(y[0])):
                soma += x[a][c] * y[c][b]
                # n += 1  # forma que consegui fazer desta vez. Se trocar o 'c' pelo 'n' em x[a][c] dá certo tbm.
            matriz[a][b] = soma
            soma = 0
            # n = 0  # Acontece que 'n' faz o mesmo papel do 'c' no for mais interno.
    return matriz


linhas = colunas = int(input('Entre com o número de linhas e colunas para a matriz quadrática: '))
A = PreencheMatriz(GeraMatriz(linhas, colunas))
B = PreencheMatriz(GeraMatriz(linhas, colunas))
for i in range(0, linhas):
    for j in range(0, colunas):
        print(f'{A[i][j]:^3}', end='')
    print()
print()
for i in range(0, linhas):
    for j in range(0, colunas):
        print(f'{B[i][j]:^3}', end='')
    print()

C = ProdutoMatriz(A, B)
print(f'\nO produto das duas matrizes é: {C}\n')
for i in range(0, linhas):
    for j in range(0, colunas):
        print(f'{C[i][j]:^3}', end='')
    print()

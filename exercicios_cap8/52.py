"""
Questão 52
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


def MatrizTransposta(x):
    matrizT = GeraMatriz(len(x), len(x[0]))
    for a in range(0, len(x)):
        for b in range(0, len(x[0])):
            matrizT[a][b] = x[b][a]
    return matrizT


linhas = colunas = int(input('Entre com o número de linhas e colunas para a matriz quadrática: '))
A = PreencheMatriz(GeraMatriz(linhas, colunas))
for i in range(0, linhas):
    for j in range(0, colunas):
        print(f'{A[i][j]:^3}', end='')
    print()

print('\nA transposta de matriz acima é:')
B = MatrizTransposta(A)
for i in range(0, linhas):
    for j in range(0, colunas):
        print(f'{B[i][j]:^3}', end='')
    print()

"""
Questão 55
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


def SomaDiagonalPrincipalSecundaria(x):
    somaDP = somaDS = 0
    b = 0
    for a in range(len(x)-1, -1, -1):
        somaDS += x[a][b]
        b += 1
    for a in range(0, len(x)):
        for b in range(0, len(x[0])):
            if b == a:
                somaDP += x[a][b]
    return somaDP, somaDS


linhas = colunas = int(input('Entre com o número de linhas e colunas para a matriz quadrática: '))
A = PreencheMatriz(GeraMatriz(linhas, colunas))
for i in range(0, linhas):
    for j in range(0, colunas):
        print(f'{A[i][j]:^3}', end='')
    print()

somaP, somaS = SomaDiagonalPrincipalSecundaria(A)
print(f'\nA soma dos elementos das diagonais principal e secundaria é: {somaP + somaS} ')

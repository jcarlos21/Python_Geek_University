"""
Questão 51
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


def SomaDiagonalSecundaria(x):
    soma = 0
    b = 0
    for a in range(len(x)-1, -1, -1):
        soma += x[a][b]
        b += 1
    return soma


linhas = colunas = int(input('Entre com o número de linhas e colunas para a matriz quadrática: '))
# print()
A = PreencheMatriz(GeraMatriz(linhas, colunas))
for i in range(0, linhas):
    for j in range(0, colunas):
        print(f'{A[i][j]:^3}', end='')
    print()
print(f'\nA soma dos elementos da diagonal secundária é: {SomaDiagonalSecundaria(A)}')



